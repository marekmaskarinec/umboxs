# Home

> **NOTE:** We are experiencing a DB outage, accessing packages is not possible
> right now. Downloading and updating packages should work, but other
> functionality is limited.

UmBox is a package manager for [Umka](https://github.com/vtereshkov/umka-lang).
It can manage dependencies for Umka libraries and programs and help with
automating builds. The source code can be found
[here](https://sr.ht/~mrms/umbox). You can get support on the Umka [Discord
server](https://discord.gg/PcT7cn59h9).

Logo credit: Jakub Víta

## Getting started

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
umbox init umka
umbox run</code></pre>
  </div>

  <div class="code">
    <p>Download the installer <a href="/dl/umbox_install.exe">here</a> and run it.</p>
<pre><code>mkdir my_box
cd my_box
umbox init umka
umbox run</code></pre>
  </div>

  <div class="code">
    <p>Download the portable ZIP <a href="/dl/umbox_portable.zip">here</a> and extract it to directory of your liking.</p>
<pre><code>mkdir my_box
cd my_box
path/to/umbox init umka
path/to/umbox run</code></pre>
  </div>
</div>

Now you can continue by reading the [documentation](/docs/user/guides/02-getting-started.md).

## Features

- CLI tool
- Web UI with documentation browser
- custom build and run scripts
