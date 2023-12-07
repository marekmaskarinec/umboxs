%include('header.tpl')

<div class="docs">
    <div class="docs__tree">
        <ul>
            <li>
                %include('file_tree.tpl', prefix=prefix, base_dir=dir, dir='')
            </li>
        </ul>
    </div>

    <div class="docs__content">
        <%
        import mistune
        import os
        from paks import mmdoc

        _, ext = os.path.splitext(filepath)

        html = ""
        try:
                with open(filepath, 'r') as f:
                        data = f.read()
                end
            if ext == ".md":
                html = mistune.html(data)
            elif ext == ".um":
                html = mistune.html(mmdoc.genMd(filepath, data)) + f"<hr>\n\n<pre><code>{data}</code></pre>"
            elif ext == ".html":
                html = data
            else:
                html = f"<pre><code>{data}</code></pre>"
            end
        except:
                html = "<h1>404</h2><h2>File not found</h2>"
        end

        %>
        {{!html}}
    </div>
</div>

%include('footer.tpl')