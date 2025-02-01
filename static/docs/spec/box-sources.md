# Box Sources

When installing a package using `umbox install`, or by adding it to the
dependency list, it is possible to specify, where the box should be sourced.
By default, if you don't specify anything, it is downloaded from the official
server at `umbox.tophat2d.dev`.

## Syntax

```
package_name[@source_type://source]
```

## Source types

Currently there are two source types supported:

- `http` or `https` - download from an UmBox server
  - `source` specifies the URL of the server
- `file` - install from a local (or a remote :] ) `box.tar` file
  - `source` specifies the path to the file

## Dependency shadowing

Let's consider the following scenario:

- Our box depends on `box2` and `logs`
- `box2` also depends on `logs`

UmBox will use the dependency source of the first reference to a box it sees.
In this case, `logs` will be installed from a file, even for `box2`:

```
"dependencies": {
    "logs@file://../logs/box.tar",
    "box2"
}
```

In this case, `logs` will be installed from the source specified by `box2`,
even though we specify a different source ourselves:

```
"dependencies": {
    "box2",
    "logs@file://../logs/box.tar"
}
```

It is a good idea to specify dependencies with custom sources first in the list
to prevent any unexpected behavior.

## Examples

Download from the official server:

```
logs
```

Download from an alternative server:

```
logs@https://umbox.example.com
```

Install from a file using relative path:

```
logs@file://../logs/box.tar
```

Install from a file using absolute path:

```
logs@file:///home/joe/source/logs/box.tar
```
