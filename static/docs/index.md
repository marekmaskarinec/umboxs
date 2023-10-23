
# PAK documentation index

  * [`pak.json` file](pakjson.md)
  
## Creating a new package

You can create a new package like this:

```
pak init
```

Then you can tweak the created `pak.json` to your liking.

## Publishing a package

Firs you need to register for a package using `pak register`. This will return
a token. You need to save the token or else you won't be able to access the
package.

For a package to be valid, you need to upload `pak.json` and `pak.tar` files.
You can upload them like this:

<code><pre>
pak upload -t &lt;token&gt; pak.json
pak uplaod -t &lt;token&gt; pak.tar
</pre></code>

## Build process

PAK offers a build functionality. It works in the following way:

1. run the `pre_build` command of the package
2. put all the files and directories inside `include` into `pak.tar`
3. run the `post_build` commands of the dependencies in the order they are included