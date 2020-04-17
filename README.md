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
So I've ran `python setup.py bdist --format=zip` on the existing 0.0.1 version, change the main function, bumped the version and re-ran bdist. Pushing everything to github now.

## Attempting to specify the new version.

I made a release on gitHub (0.0.2) and ran `pip install git+ssh://git@github.com/erik-farmer/awesome_pkg.git#release=0.0.2` and it worked with the new code. Im going to make _another_ new release and try to install the 0.0.2 version, then uninstall that, and upgrade.

I pushed the code to master, created a new release and ran the following:

`pip install git+ssh://git@github.com/erik-farmer/awesome_pkg.git#releases=0.0.2`

I ran the previous python code and got the 0.0.2 release print statement.

## However

When I did a `pip uninstall awesome_pkg` it said uninstalling 0.0.3 which I awesome it is getting from the `setup.py` file.

I tried to install the latest with `pip install git+ssh://git@github.com/erik-farmer/awesome_pkg.git#releases=0.0.3` and it still ran the 0.0.2 statement.

This raises a few problems. One of which is that I am not even using the `dist` folder on the project. Time to poke around the internet.

## Resolution
So I didn't make a 0.0.3 dist...
Reran `python setup.py bdist --format=zip` and uploaded to github (no new release) and it picked up the right version.

## However (again)
I've attempted to downgrade and it was still installing 0.0.3
I will consult the internet once again! But this seems like a good stopping point before lunch.

## Back at it...
(a few days later)

Going to try wheel. Deleting all of the old build files and releases on github and start over with wheel. Then I will try to use this tagging scheme: `git+ssh://git@github.com/erik-farmer/awesome_pkg.git@v<version>`
