### Hangman

## Install

`Hangman` was designed as a module and to be run as a "binary".

What does that mean?  You can't do the following:

```
$ python hangman/__init__.py
```

Instead, it's intended to be installed using [`setuptools`], which will conveniently put it in your `PATH`.  This allows for running this as you would any other binary on your system:

```
$ hangman
```

My suggestion would be to install this globally, because I'm the author of this amazing piece of software, but perhaps you 'd rather install it in a [Python virtual environment].

To install globally:

```
$ git clone https://github.com/btoll/hangman
$ cd hangman
$ python setup.py install
$ hangman
```

To install in a Python virtual environment (assumes you have `virtualenv`):

```
$ git clone https://github.com/btoll/hangman
$ cd hangman
$ virtualenv balls
$ . balls/bin/activate
(balls) $ python setup.py install
(balls) $ hangman
```

[`setuptools`]: https://pythonhosted.org/an_example_pypi_project/setuptools.html
[Python virtual environment]: https://www.benjamintoll.com/2021/04/01/on-virtualenv/
![ScreenShot](https://raw.github.com/btoll/i/master/hangman/hangman1.png)
![ScreenShot](https://raw.github.com/btoll/i/master/hangman/hangman2.png)

