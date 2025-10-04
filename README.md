# celerysee

A minimal tool for watching celery queues.

## Usage

### Django shell
1. Open django shell
    ```
    $ python manage.py shell
    ```
2. Import `celerysee` to watch the queues in your celery app instance.

    ```
    from celerysee import see
    from myproject.celery import app
    see(app)
    ```

## Development

**Getting started**

Clone [source code](https://github.com/raiyankamal/celerysee).

**Running tests**

(wip)

***Making a build***

```
$ pip install build
$ python -m build
```


*** Publish to PyPI ***

```
$ pip install twine
$ twine upload --repository testpypi dist/*
```

*** Check after publishing ***

```
$ pip install --index-url https://test.pypi.org/simple/ celerysee
```