# Local Server

While developing UmBox, it is required to have a local instance of the UmBox
server running. Setting this up is pretty simple. First, clone the repository
and install all the requirements.

```
git clone https://github.com/marekmaskarinec/umboxs
cd umboxs
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Then, download [test_data.zip](https://mrms.cz/dl/umbox/text_data.zip) and
extract it into the root of the cloned server. This archive contains the data
for three testing boxes `box1`, `box2`, `box3`. You can obviously add more if
you need.

After setting up the server directory, you can run the server like this:

```
./run
```

This will run the server in debug mode at
[http://localhost:4832](http://localhost:4832).
