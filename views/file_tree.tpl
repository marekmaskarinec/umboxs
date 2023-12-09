%import os
<span>{{os.path.basename(dir)}}/</span>
<ul>
% fs = [f.name for f in os.scandir(os.path.join(base_dir, dir))]
% fs.sort()
%for f in fs:
    %if os.path.isfile(os.path.join(base_dir, dir, f)):
        <li>
            %_, ext = os.path.splitext(f)
            %if ext in wl:
                <a href="{{os.path.join(prefix, dir, f)}}">
                    {{f}}
                </a>
            %end
        </li>
    %else:
        <li>
            %include('file_tree.tpl', prefix=prefix, wl=wl, base_dir=base_dir, dir=os.path.join(dir, f))
        </li>
    %end
%end
</ul>