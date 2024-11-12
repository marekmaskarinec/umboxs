# Platform strings

Platform strings are used in `box.json` to specify different variants of
strings depending on the platform UmBox is run on. This is useful for cross
platform run a build scripts.

A plaftorm string can have two different forms - either a string or an object:

```
python run.py
```

or

```
{
    "windows": ".\umbox\umka\umka.exe main.um",
    "posix": "./umbox/umka/umka main.um"
}
```

You can also use the `unknown` platform as a fallback for unsupported
platforms:

```
{
    "unknown": "echo This platform isn't supported",
    "linux": "./run.sh"
}
```

The supported platforms are:

* `unknown`
* `posix`
* `windows`
* `emscripten`

They are the same as in the `os::Platform` enum (see
[os.um](https://umbox.tophat2d.dev/package/os)).
