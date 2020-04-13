# Awesome PKG

We're going to test hosting a python package on GitHub today.

## Steps

[This](https://dev.to/rf_schubert/how-to-create-a-pip-package-and-host-on-private-github-repo-58pa) link seems promising.
I'm going to set up the basic package structure:

```
pkg_name/
    pkg_name/
        __init__.py
    setup.py
```

Admittedly I have _never_ written a `setup.py` file before.

I've also added a simple module/method to test with:

```python
# apkg.py
def main():
    print('Hey this is pretty awesome')

```

So far seems easy enough. Time to create another project/venv and see if I can install it.

Running `pip install git+ssh://git@github.com/erik-farmer/awesome_pkg.git` worked like a charm.

Test file:
```python
from awesome_pkg.apkg import main
main()
>>> Hey this is pretty awesome
```

Success!!! But now I need to look into versioning...

## Versions!
