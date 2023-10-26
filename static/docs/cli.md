# PAK CLI

PAK offers a CLI tool written in python.

## Install instructions

First download the sources:

```
git clone https://git.sr.ht/~mrms/pak
cd pak
```

Now install it using python's `setuptools`:

```
python -m pip install -r requirements.txt
python setup.py install --user
```

PAK will now be available using `python -m pak`.

## Creating a new package

A package is any project that uses PAK, even if it is not a library and is not
meant to be published. You can create a new package using the `init` command.
The command lets you choose between two presets: `tophat` and `umka`.

The `init` command will add a sample `pak.json` with all the run scripts setup
and download the required dependencies.

## Running a package

If the package has a run script defined (see `run`, `run_posix` and
`run_windows` in [`pak.json` reference](pakjson.md)), running `pak run args`
will execute the run script and pass the excess flags to it.

## Managing dependencies

One of main PAK features is dependency management. You can add dependencies
either using the `pak install` command or by manually adding them to `pak.json`.

To make sure all dependencies are installed and up-to-date, run `pak update`.

If you do not need a dependency anymore, run `pak remove <dependency>` or remove
it from `pak.json`.

To search for dependencies you can either use the web UI, or the `pak search`
command.

## Making builds

PAK offers a build functionality. It works in the following way:

1. run the `pre_build` command of the package
2. put all the files and directories inside `include` into `pak.tar`
3. run the `post_build` command of the package

You can launch a build using `pak build`. If everything went correctly, will
see `pak.tar` in your directory.

## Publishing a package

Firs you need to register for a package using `pak register`. This will return
a token. You need to save the token or else you won't be able to access the
package.

For a package to be valid, you need to upload `pak.json` and `pak.tar` files.
You can upload them like this:

```
pak upload -t &lt;token&gt; pak.json
pak uplaod -t &lt;token&gt; pak.tar
```

## Automatic builds

If you use SourceHut, you can use the
[CI script](https://git.sr.ht/~mrms/paks/tree/master/item/scripts/srht-build.yml)
to make automatic builds of your packages.