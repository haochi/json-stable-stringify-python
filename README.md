# json-stable-stringify-python

[![CircleCI](https://circleci.com/gh/haochi/json-stable-stringify-python.svg?style=shield)](https://circleci.com/gh/haochi/json-stable-stringify-python)

Basically a Python port of [substack's json-stable-stringify](https://github.com/substack/json-stable-stringify) with just the default options.

## Installation

```bash
pip install json_stable_stringify_python
```

## Usage

```python
>>> import json_stable_stringify_python as json_stable
>>> json_stable.stringify({'z': 1, 'a': 2})
'{"a":2,"z":1}'
```
