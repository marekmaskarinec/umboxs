# Automatic Builds

This guide will show you how to automatically update your box's data
after every commit.

## GitHub

Automatic builds on GitHub can be done using UmBox's composite action. Example:

```
name: UmBox upload

on:
  push:
    branches: [ master ]

  workflow_dispatch:

jobs:
  upload:
    runs-on: ubuntu-20.04

    steps:
      - uses: actions/checkout@v2
      - run: sudo apt install -y mingw-w64
      - uses: marekmaskarinec/umbox@master
        with:
          secret: ${{ secrets.UMBOX }}
```

For this to work, you will need to add your UmBox token as a repository secret.
It is important that your workflow runs on `ubuntu-20.04`. If it runs on a
different system, it may be possible that your box will not be compatible with
others.

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
- <your_box_url>
environment:
    NAME: <your_box_name>
tasks:
- setup: |
    curl https://umbox.tophat2d.dev/static/umbox_portable.zip -O
    unzip umbox_portable.zip
- build: |
    cd $NAME
    ../umbox_portable/umbox update
    ../umbox_portable/umbox build
- deploy: |
    cd $NAME
    set +x
    ../umbox_portable/umbox upload `cat ../.secret` box.json
    set -x
```
