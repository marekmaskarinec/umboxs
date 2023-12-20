# Installing Boxes

This guide will show how to add boxes to your project.

## Adding a box

This can be done in two ways. The first is to add the box's name to the `dependencies` array
in your `box.json` and then run `umbox update`. The same can be done using the install command.

```
umbox install <box_name>
```

## Removing a box

Similarly to adding a box, removing it can also be done in two ways. Either by removing it from the dependency
list and then running `umbox update`, or using the remove command.

```
umbox remove <box_name>
```

## Updating boxes

Boxes can be automatically updated using the update command.

```
umbox update
```
