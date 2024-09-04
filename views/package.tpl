% include('header.tpl', title=pack.name)

<div class="package">
	<div class="package__heading box">
		<h2>{{pack.name}} {{meta.get('version')}}</h2>
		<p>{{meta.get('description')}}</p>
	</div>

	<div class="package__readme">
		<%
		import mistune
		import os
		
		content = "No readme"
		try:
			readme_path = os.path.join("packages", pack.name, "data", meta.get('readme'))
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
% if 'homepage' in meta:
		<p><a href="{{meta.get('homepage')}}">Homepage</a></p>
% end
% if 'source' in meta:
		<p><a href="{{meta.get('source')}}">Source code</a></p>
% end
		<p><a href="/package/{{pack.name}}/browse">Documentation</a></p>
		<p>License: <a href="/package/{{pack.name}}/browse/LICENSE">{{meta.get('license')}}</a></p>
		<p>Download count: {{pack.download_count}}</p>
		<%
		import datetime
		from dateutil import relativedelta
		import os.path
		
		path = os.path.join("packages", meta.get('name'), "data", "box.json")
		lastupdated = "No uploads yet."

		if os.path.isfile(path):
			diff = relativedelta.relativedelta(
				datetime.datetime.now(),
				datetime.datetime.fromtimestamp(int(os.path.getmtime(path)))
			)
			
			if diff.years == 1:
				lastupdated = "Last year"
			elif diff.years > 1:
				lastupdated = f"{diff.years} years ago"
			elif diff.months == 1:
				lastupdated = "Last month"
			elif diff.months > 1:
				lastupdated = f"{diff.months} months ago"
			elif diff.days == 1:
				lastupdated = "Yesterday"
			elif diff.days > 1:
				lastupdated = f"{diff.days} days ago"
			elif diff.hours == 1:
				lastupdated = f"An hour ago"
			elif diff.hours > 1:
				lastupdated = f"{diff.hours} hours ago"
			elif diff.minutes > 5:
				lastupdated = f"{diff.minutes} minutes ago"
			else:
				lastupdated = "Just now"
		end
		%>
		<p>Last updated: {{lastupdated}}</p>
		
		<hr>
		
		<p>To add this package to your project run:</p>
		<code><pre>umbox install {{pack.name}}</pre></code>
		
		<p>Or download as a <a href="/api/package/{{pack.name}}/download/box.tar">tar</a>.</p>
		
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
