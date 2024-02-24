# CLI tool reference

## Flags

### `-h`, `--help`

Show help and exit.

### `-u`, `--url`

Specify URL of the umbox server. Defaults to `https://umbox.tophat2d.dev`

## Modes

### `build`

Builds as `box.tar` file in the current directory. This archive will contain:

- files and directories specified in the `include` field of `box.json`
- the `box.json` file
- the readme specified in `box.json`

### `init [ <init preset> ]`

Creates a new box in the current directory. The box will have the same name
as the directory. Optionally, you can specify a name of a box, which will
be used as a preset.

> **NOTE:** A box can only be used as a preset, if it has the `init.tar` file
> uploaded. If you are a maintainer, see: [03-init-presets](/docs/maintainer/guides/03-init-presets.md)

### `install <box>`

Adds and installs a box. You can specify box sources.

### `remove <box>`

Removes a box. Here, box sources are irrelevant - the box is matched based on
the name.

### `run [ <command> ]`

This mode is used for running commands in an UmBox environment. In this
environment, all of the box directories are in the `PATH`.

If your box has a run field in the `box.json`, UmBox will first run that.
If you pass any argument after the `run`, UmBox will run them as a command.

### `search <query>`

Searches for available boxes on the server and prints the results.

### `update [ -c ]`

Updates all of the dependencies, removing one that are not used anymore.
By default, `update` uses symlinks to save drive space, however in some cases,
this might be undesirable. In these cases, you can pass the `-c` flag.

> **NOTE:** The `-c` flag is experimental. It is recommended to remove the
> entire `umbox/` directory before running with `-c`.

### `register <name>`

Registers a box with the name `name`. It will print out the secret token to the
console.

### `upload <token> <file>`

Uploads a file to the box storage.
