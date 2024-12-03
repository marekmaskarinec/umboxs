<html lang="en">
<head>
	<title>{{title}} | UmBox</title>
	<link rel="stylesheet" type="text/css" href="/static/style.css" />
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<link rel="icon" type="image/png" href="/static/cat.png" />
% if plausible != None:
	<script defer data-domain="{{plausible}}" src="https://plausible.chamik.eu/js/script.js"></script>
% end
</head>
<body>
<div class="wrapper">
	<header>
		<div class="nav">
			<a href="/">
				<img class="" src="/static/cat.png" />
			</a>
			<form action="/search" method="post">
				<input class="box" name="query" type="text" placeholder="Search" />
			</form>
			<a href="/all">All packages</a>
			<a href="/docs">Docs</a>
			<a href="/static/dl.md">Downloads</a>
		</div>
	</header>
	<article><div class="article">
