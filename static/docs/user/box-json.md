# `box.json` File

This file is in the root directory of every box. It specifies metadata about the it.

## Example

```
{
    "name": "awesome_box",
    "version": "v0.1.0",
    "author": "John Doe",
    "license": "MIT",
    "description": "John Doe's awesome box for doing awesome stuff",
    "readme": "README.md",
    "homepage": "https://awesomebox.mrms.cz",
    "source": "https://git.sr.ht/~jdoe/awesome_box",
    "dependencies": ["strings", "umka"],
    "include": ["awesome.um"],
    "run": "umka awesome.um"
}
```

## Options

### `name`

This sets the box's name. It has to match the name specified when
registering the box. If it does not match, it will be changed accordingly.

### `version`

Version of the box.

### `author`

Author of the box.

### `license`

Name of the license.

### `description`

Short description of the box.

### `readme`

Path to the box's readme file.

### `homepage` (optional)

A link to the homepage of the project. This should be a web page.

### `source` (optional)

A link to the sourcecode of the project. It should point directly to a downloadable file or a clonable repository.

### `dependencies`

A list of boxes this box depends on.

### `include`

A list of files or directories that shall be packaged with the build.

### `run` (optional)

A command used before `umbox run` arguments are executed. Supports [platform strings](platform-strings.md).

### `pre_build` (optional)

A command ran before a build. Supports [platform strings](platform-strings.md).

### `post_build` (optional)

A command ran after a build. Supports [platform strings](platform-strings.md).
