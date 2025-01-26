# Getting Started

This article shows how to get started with using UmBox. It assumes you have already installed
the CLI tool according to the [guide](01-installation.md).

To create a new box you can use the `init` command:

```
umbox init hello
```

This will create a box called `hello` in a folder with the same name. If you want
to create a box in your current directory, you can do it the following way:

```
umbox init .
```

This will create a box, which has the same name as the current directory.

Some boxes offer an init preset, which can be used to quickly start working with
that box. For example to start a project based on Umka, you can run the following command:

```
umbox init -p umka .
```

This will initialize your box with the correct dependencies, `box.json` setup and an
example `main.um` file. After intialising, the box is ready to be run.

```
umbox run
```
