<html lang="en">
<head>
        <title>UmBox</title>
        <link rel="stylesheet" type="text/css" href="/static/style.css" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
				<link rel="icon" type="image/png" href="/static/cat.png" />
% if plausible != None:
	<script defer data-domain="{{plausible}}" src="https://plausible.chamik.eu/js/script.js"></script>
% end
</head>
<body>
<article><div class="article">
<div class="index">
	<img class="no-aa" src="/static/cat.png" />
	<h1>UmBox</h1>
	<p>The <a href="https://github.com/vtereshkov/umka-lang/">Umka</a> package manager</p>
	<ul>
		<li><a href="/docs">Docs</a></li>
		<li><a href="/static/dl.md">Downloads</a></li>
		<li><a href="/all">Browse</a></li>
		<li><a href="https://discord.gg/PcT7cn59h9">Discord</a></li>
	</ul>
	<form action="/search" method="post">
		<input class="box" name="query" type="text" placeholder="Search" />
	</form>

  <a href="#about" class="arrow">▾</a>
</div>

<div class="index-content">
  <h2 id="about">About</h2>

  UmBox is a package manager for <a
  href="https://github.com/vtereshkov/umka-lang">Umka</a>. It can manage
  dependencies for Umka libraries and programs. It features a web UI with an
  automatic API reference generator (using <a
  href="https://github.com/marekmaskarinec/mmdoc">MMDOC</a> syntax) and other useful
  features. The official UmBox repository is hosted here at tophat2d.dev, but it
  is possible to host your own repository if needed.

  Both the <a href="https://github.com/marekmaskarinec/umboxs">server</a> and <a
  href="https://github.com/marekmaskarinec/umbox">CLI</a> parts of UmBox are open
  sourced. You can browse documentation <a href="/docs">here</a>. For technical
  support or discussions about UmBox, join the official Umka <a href="https://discord.gg/PcT7cn59h9">Discord Server</a>.

  <h2>Getting started</h2>

  <style>
  .getting-started {
      display: grid;
      grid-template-columns: 33% 33% 33%;
      grid-gap: 15px;
  }

  .getting-started h3 {
    margin: 0;
  }

  .code {
      align-self: end;
  }

  .code >* {
      margin: 0;
  }
  </style>

  <div class="getting-started">
    <div>
      <h3>Linux</h3>
    </div>
    <div>
      <h3>Windows</h3>
    </div>
    <div>
      <h3>Portable</h3>
    </div>

    <div class="code">
      <pre><code>curl -L https://umbox.tophat2d.dev/dl/setup.sh | sh
  mkdir my_box
  cd my_box
  umbox init -p umka
  umbox run</code></pre>
    </div>

    <div class="code">
      <p>Download the installer <a href="/dl/umbox_install.exe">here</a> and run it.</p>
  <pre><code>mkdir my_box
  cd my_box
  umbox init -p umka
  umbox run</code></pre>
    </div>

    <div class="code">
      <p>Download the portable ZIP <a href="/dl/umbox_portable.zip">here</a> and extract it to directory of your liking.</p>
  <pre><code>mkdir my_box
  cd my_box
  path/to/umbox init -p umka
  path/to/umbox run</code></pre>
    </div>
  </div>

  <p>
  Now you can continue by reading the <a href="/docs/user/02-getting-started.md">documentation</a>.
  </p>

  <p>
  * More information about the install procedure is available
  <a href="/docs/user/01-installation.md">here</a>.
  </p>
<div>

% include('footer.tpl')
