# 🐶 ES6 Sniffer

ES6 Sniffer is a simple CLI to identify installed Node packages that may contain ES6 features. It cribs heavily from the approach in [`babel-engine-plugin`](https://github.com/SamVerschueren/babel-engine-plugin) but meets the need without adding additional build tools.

## Installation

Simply run:

```bash
pip install pip install git+https://github.com/hancush/python-es6-sniffer
```

## Usage

Basic usage:

```bash
es6-sniffer
```

For options:

```bash
es6-sniffer --help
```

## Development

```bash
pip install pytest
pip install -e .
# Make changes, then test
pytest -sv
```
