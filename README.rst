==========
catplotlib
==========


.. image:: https://img.shields.io/pypi/v/catplotlib.svg
        :target: https://pypi.python.org/pypi/catplotlib


Matplotlib, but for cats.


* Free software: MIT license
* Documentation: https://catplotlib.readthedocs.io. Just kidding. There are no docs.


Features
--------

* Just one.::

        import catplotlib.catplot as clt
        clt.plot()


Making a Release
----------------

1. Bump the version in ``catplotlib/__init__.py`` and ``setup.py``
2. Update the changelog, link the versions.
3. Commit and tag with version number
4. Build a source dist with ``python setup.py clean && rm dist/* && python setup.py sdist``
5. Test upload to PyPI test with ``twine upload --repository-url https://test.pypi.org/legacy/ dist/*``
6. Create a temporary environment ``mktmpenv`` and test install with ``pip install --index-url https://test.pypi.org/simple/ catplotlib``
7. If everything looks good, upload for real with ``twine upload dist/*``