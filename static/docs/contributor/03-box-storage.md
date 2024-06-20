# Package Storage

Package data is stored in the `packages/` directory in the root of the server.
Each package has it's own directory there which is named same as the package (see `Package.fpath`).

The following files are in the package folder:

- `box.tar` - the uploaded `box.tar`
- `data/` - unarchived data from the `box.tar`
- `box.json` - meta JSON, may contain postprocessing
- `version` - the current version of the package
- `init.tar` (optional) - the init preset

These files can be downloaded or uploaded (if authorized by a token) through the HTTP API.
