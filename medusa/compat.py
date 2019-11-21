# -*- coding: utf-8 -*-

import pathlib

try:
    from os import fspath  # noqa
    OLD_PYTHON = False
except ImportError:
    OLD_PYTHON = True


def _fspath(path):
    '''https://www.python.org/dev/peps/pep-0519/#os'''
    if isinstance(path, (str, bytes)):
        return path

    # Work from the object's type to match method resolution of other magic
    # methods.
    path_type = type(path)
    try:
        path = path_type.__fspath__(path)
    except AttributeError:
        # Added for Python 3.5 support.
        if isinstance(path, pathlib.Path):
            return str(path)
        elif hasattr(path_type, '__fspath__'):
            raise
    else:
        if isinstance(path, (str, bytes)):
            return path
        else:
            raise TypeError("expected __fspath__() to return str or bytes, "
                            "not " + type(path).__name__)

    raise TypeError("expected str, bytes, pathlib.Path or os.PathLike object, not " + path_type.__name__)


if OLD_PYTHON:
    fspath = _fspath
