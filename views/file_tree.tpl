%import os
<span>{{os.path.basename(dir)}}/</span>
<ul>
%for f in os.scandir(os.path.join(base_dir, dir)):
    %if os.path.isfile(os.path.join(base_dir, dir, f.name)):
        <li>
            %_, ext = os.path.splitext(f.name)
            %if ext in wl:
                <a href="{{os.path.join(prefix, dir, f.name)}}">
                    {{f.name}}
                </a>
            %end
        </li>
    %else:
        <li>
            %include('file_tree.tpl', prefix=prefix, wl=wl, base_dir=base_dir, dir=os.path.join(dir, f.name))
        </li>
    %end
%end
</ul>