# Getting Started

This guide will show you how to get started with publishing your own box.
It assumes that you are already familiar with the `user/` section of the
documentation.

Just to recapitulate, you can create a new box like this:

```
mkdir my_box
cd my_box
umbox init
```

When you have your box ready, make sure it follows these rules:

- You have chosen some kind of license. It's generally advised against using the GPL, but it's
  not prohibited.
- You have written a proper readme file for your box. This file will be shown on your
  box's main page.
- You have properly set up your box's build.

If you follow these rules, you can continue by registering your box. In your
directory, run this command:

```
umbox register
```

The command will print out a 64-character long token. Save this token somewhere
safe (for example a password manager) and don't share it with anyone. If you've
lost your token, are suspicious that someone might've stolen it or have some
other similar issues, please contact me using my email
[marek@mrms.cz](mailto:marek@mrms.cz).

After successfully registering a box, you can upload files to it. UmBox accepts
these files: `box.tar` and `init.tar`. The former is required
for the box to be valid. The latter is optional and is used when your box name
is passed as an argument to the `umbox init` command.
