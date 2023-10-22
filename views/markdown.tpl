% include('header.tpl', title=title)

<%
import markdown

html = ""
try:
        with open(filepath, 'r') as f:
                md = f.read()
        end
        html = markdown.markdown(md)
except:
        html = "<h1>404</h2><h2>File not found</h2>"
end

%>

{{!html}}

% include('footer.tpl')