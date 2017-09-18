# Voice proxy with Nexmo

Example code for creating a voice proxy or call forwarding application using
Python, Sanic and the Nexmo API.

## Quick start

For more detailed instructions be sure to read the post on our
[blog](https://nexmo.com/blog/). You will need a Nexmo virtual number and an
associated voice application.

```
git clone git@github.com:nexmo-community/voice-proxy-python-example.git
cd voice-proxy-python-example

# requires python 3.5+
# always use a virtualenv
pip install -r requirements.txt

cp example.config .config

python proxy.py
```
