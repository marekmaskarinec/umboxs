% include('header.tpl', title=name)

<div class="package">
	<div class="package__heading box">
		<h2>{{name}} {{meta.get('version')}}</h2>
		<p>{{meta.get('description')}}</p>
	</div>

	<div class="package__readme">
		<%
		import markdown
		import os

		readme_path = os.path.join("packages", name, "data", meta.get('readme'))

		content = "No readme"
		try:
			with open(readme_path) as f:
				content = f.read()
			end
		except:
			pass
		end

		html = markdown.markdown(content)
		%>

		<p>README</p>
		<hr>
		{{!html}}
	</div>
	
	<div class="package__info">
		<p><a href="{{meta.get('link')}}">Homepage</a></p>
		<p>License: {{meta.get('license')}}</p>
		
		<hr>
		
		<p>To add this package to your project run:</p>
		<code><pre>pak install {{name}}</pre></code>
		
		<hr>
		
		<h3>Dependencies</h3>
		% if len(meta.get('dependencies')) == 0:
			<p>No dependencies</p>
		% else:
		<ul>
			% for d in meta.get('dependencies'):
				<li><a href="/package/{{d}}">{{d}}</a></li>
			% end
		</ul>
		% end
	</div>
</div>

% include('footer.tpl')