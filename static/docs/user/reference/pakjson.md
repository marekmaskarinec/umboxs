# `pak.json` File

This file is in the root directory of ever PAK package. It specifies metadata about the package.

## Example

```
{
    "name": "awesome_package",
    "version": "v0.1.0",
    "author": "John Doe",
    "license": "MIT",
    "description": "John Doe's awesome package for doing awesome stuff",
    "readme": "README.md",
    "link": "https://git.sr.ht/~jdoe/awesome_package",
    "dependencies": ["coulau", "umka"],
    "include": ["awesome.um"],
    "run": "umka awesome.um"
}
```

## Options

### `name`

This sets the package's name. It has to match the name specified when
registering the package. If it does not match, it will be changed accordingly.

### `version`

Version of the package.

### `author`

Author of the package.

### `license`

Name of the license.

### `description`

Short description of the package.

### `readme`

Path to the package's readme file.

### `link`

Link to the package's homepage or repository.

### `dependencies`

A list of packages this package depends on.

### `include`

A list of files or directories that shall be packaged with the build.

### `run`

A command used when `pak run` is executed.

### `run_posix`

A version of the ran command used on POSIX systems.

### `run_windows`

A version of the ran command used on Windows systems.

### `pre_build`

A command ran before a build.

### `post_build`

A command ran after a build.
