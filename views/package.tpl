% include('header.tpl', title=name)

<div class="package">
	<div class="package__heading box">
		<h2>{{name}} {{meta.get('version')}}</h2>
		<p>{{meta.get('description')}}</p>
	</div>

	<div class="package__readme">
		<%
		import mistune
		import os
		
		content = "No readme"
		try:
			readme_path = os.path.join("packages", name, "data", meta.get('readme'))
			with open(readme_path) as f:
				content = f.read()
			end
		except:
			pass
		end

		html = mistune.html(content)
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
		
		<p>Or download as a <a href="/api/package/{{name}}/download/pak.tar">tar</a>.</p>
		
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
		
		<h3>Last updated</h3>
		<%
		import datetime
		import os.path
		
		path = os.path.join("packages", meta.get('name'), "pak.json")
		lastupdated = "No uploads yet."

		if os.path.isfile(path):
			lastupdated = datetime.datetime.fromtimestamp(
				int(os.path.getmtime(path))
			).isoformat()
		end
		%>
		<p>{{lastupdated}}</p>
	</div>
</div>

% include('footer.tpl')