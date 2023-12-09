# Installing Packages

This guide will show how to add packages to your project.

## Adding a package

This can be done in two ways. The first is to add the package's name to the `dependencies` array
in your `pak.json` and then run `pak update`. The same can be done using the install command.

```
pak install <package_name>
```

## Removing a package

Similarly to adding a package, removing it can also be done in two ways. Either by removing it from the dependency
list and then running `pak update`, or using the remove command.

```
pak remove <package_name>
```

## Updating packages

Packages can be automatically updated using the update command.

```
pak update
```
