# Installing Packages

The main purpose of UmBox is dependency management. Each box specifies its direct
dependencies in the `dependencies` array of `box.json`. Whenever you run
`umbox update`, UmBox will make sure all the required dependencies are installed
to their latest version and that there are no unneeded boxes installed.

This means installing dependencies can be done just by adding the name of the box
to the `dependencies` array and running `umbox update`. Conversely, uninstalling
boxes is done by removing them from the `dependencies` array and running `umbox update`.

Alternatively, UmBox offers a short hand in form of the `install` and `remove` commands,
which edit the `box.json` file and automatically run `umbox update`.
