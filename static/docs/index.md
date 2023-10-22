
# PAK documentation index

  * [`pak.json` file](pakjson.md)
  
## Registering a new package
  
First run the `register` command with the package's name:

```
pak register <name>
```

Then **save** the returned token. You will need the token to upload content to
the package.

## Uploading files to a package

For a package to be valid, you need to upload `pak.json` and `pak.zip` files.
You can upload them like this:

<code><pre>
pak upload -t &lt;token&gt; pak.json
pak uplaod -t &lt;token&gt; pak.zip
</pre></code>

## Build process

PAK offers a build functionality. It works in the following way:

1. run the `pre_build` commands of the dependencies in the order they are included
2. run the `pre_build` command of the package
3. put all the files and directories inside `include` into `pak.zip`
4. run the `post_build` commands of the dependencies in the order they are included
5. run the `port_build` command of the package