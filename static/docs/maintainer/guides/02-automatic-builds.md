# Automatic Builds

This guide will show you how to automatically update your package's data
after every commit.

## GitHub

Currently, no package uses GitHub's CI, but the approach should be similar
to SourceHut.

## SourceHut

Setting up builds using [builds.sr.ht](https://builds.sr.ht) is very easy.
First, you need to set up a secret for your token on the website. Set it up according to
the image.

![](/static/docs/maintainer/guides/02--secret-setup.png)

After setting up the secret, you have to add a `.build.yml` to your repository root.
This file has already been created and all you need to do to make it works is change a few lines.

```
image: debian/bullseye
packages:
- curl
- mingw-w64
- unzip
secrets:
- <your_secret>
sources:
- <your_package_url>
environment:
    NAME: <your_package_name>
tasks:
- setup: |
    curl https://pak.tophat2d.dev/static/pak_portable.zip -O
    unzip pak_portable.zip
- build: |
    cd $NAME
    ../pak_portable/pak update
    ../pak_portable/pak build
- deploy: |
    cd $NAME
    set +x
    ../pak_portable/pak upload `cat ../.secret` pak.tar
    ../pak_portable/pak upload `cat ../.secret` pak.json
    set -x
```
