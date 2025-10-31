# CLI tool reference

## Flags

### `-h`, `--help`

Show help and exit.

### `-u`, `--url`

Specify URL of the UmBox server. Defaults to `https://umbox.tophat2d.dev`.
This doesn't affect boxes that have changed their source using [box sources](/docs/spec/box-sources.md).

### `-d`, `--debug`

Run in a debug mode. If activated, full stack traces and other extra info will
be shown.

## Modes

### `build`

Builds as `box.tar` file in the current directory. This archive will contain:

- files and directories specified in the `include` field of `box.json`
- the `box.json` file
- the readme specified in `box.json`

### `init [path] [ -p preset ]`

Creates a new box at path. If path is omitted, the box is created in the
current directory. The box will have the same name as the directory.
Optionally, you can specify a name of a box, which will be used as a preset.

> **NOTE:** A box can only be used as a preset, if it has the `init.tar` file
> uploaded. If you are a maintainer, see: [03-init-presets](/docs/maintainer/03-init-presets.md)

### `install <box>`

Adds a box to `box.json` and runs `umbox update`.

### `remove <box>`

Removes a box. Here, box sources are irrelevant - the box is matched based on
the name.

### `run [ <command>|<args> ]`

If the `run` field in `box.json` is defined, runs it's content with the command
line arguments appended. Otherwise runs the command line arguments as a
command.

This mode is used for running commands in an UmBox environment. In this
environment, all of the box directories are in the `PATH`.

### `search <query>`

Searches for available boxes on the server and prints the results.

### `update [ -c ]`

Updates all of the dependencies, removing ones that are not used anymore.
By default, `update` uses symlinks to save drive space, however in some cases,
this might be undesirable. In these cases, passing the `-c` flag will result
in each instance of a box having its own hard copy.

> **NOTE:** The `-c` flag is experimental. It is recommended to remove the
> entire `umbox/` directory before running with `-c`.

### `register <name>`

Registers a box with the name `name`. It will print out the secret token to the
console.

### `upload <token> <file>`

Uploads a file to the box storage.
