# Getting Started

This guide will show you how to get started with publishing your own package.
It assumes that you are already familiar with the `user/` section of the
documentation.

Just to recapitulate, you can create a new package like this:

```
mkdir my_package
cd my_package
pak init
```

When you have your package ready, make sure it follows these rules:

- You have chosen some kind of license. It's generally advised against using the GPL, but it's
  not prohibited.
- You have written a proper readme file for your package. This file will be shown on your
  package's main page.
- You have properly set up your package's build.

If you follow these rules, you can continue by registering your package. In your
package directory, run this command:

```
pak register
```

The command will print out a 64-character long token. Save this token somewhere
safe (for example a password manager) and don't share it with anyone. If you've
lost your token, are suspicious that someone might've stolen it or have some
other similar issues, please contact me using my email
[marek@mrms.cz](mailto:marek@mrms.cz).

After successfully registering a package, you can upload files to it. PAK accepts
these files: `pak.json`, `pak.tar` and `init.tar`. The first two are required
for the package to be valid. The last one is optional and is used when your package
is passed as an argument to the `pak init` command.
