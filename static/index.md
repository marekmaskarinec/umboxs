
# Home

PAK is a package manager for [Umka](https://github.com/vtereshkov/umka-lang).
It can manage dependencies for Umka libraries and programs and help with
automating builds.

Logo credit: Jakub Víta

## Getting started

```sh
# Clone the PAK source
git clone https://git.sr.ht/~mrms/pak
cd pak
# Install pak
sudo python setup.py install
# Make a new project directory
mkdir mypak
cd mypak
# Setup a tophat project
python -m pak init tophat
# Run the project!
python -m pak run
```

Now you can continue by reading the [documentation](/static/docs/index.md).

## Features

  * dependency management
  * Web UI
  * custom build and run scripts
  
## Roadmap

  * make available through PIP
  * CI scripts for GitHub projects
  * rewrite cli tool in Umka
  * add `pre_build_inject` and `post_build_inject`
  * documentation browser
  * multiple build targets
  * better registration handling
  * rewrite server in Umka
  
## Not planned

  * version management