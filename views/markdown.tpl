% include('header.tpl', title=title)

<%
import mistune

html = ""
try:
        with open(filepath, 'r') as f:
                md = f.read()
        end
        html = mistune.html(md)
except:
        html = "<h1>404</h2><h2>File not found</h2>"
end

%>

{{!html}}

% include('footer.tpl')