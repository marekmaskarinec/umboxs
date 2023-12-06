%import os
<span>{{os.path.basename(dir)}}/</span>
<ul>
%for f in os.scandir(os.path.join(base_dir, dir)):
    %if os.path.isfile(os.path.join(base_dir, dir, f.name)):
        <li>
            <a href="{{os.path.join(prefix, dir, f.name)}}">
                {{f.name}}
            </a>
        </li>
    %else:
        <li>
            %include('file_tree.tpl', prefix=prefix, base_dir=base_dir, dir=os.path.join(dir, f.name))
        </li>
    %end
%end
</ul>