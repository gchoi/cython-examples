# cython-examples

> **Reference**: [Run Your Python Code up to 80x Faster Using the Cython Library](https://towardsdatascience.com/run-your-python-code-up-to-80x-faster-using-the-cython-library/?utm_campaign=tds%20variable&utm_medium=email&_hsenc=p2ANqtz-_c5HiWe-kqVA-fHMGhC8qvQy6IF3FiCTd_zzW5n8kEk-FH-iQiY9EM9QptohU9-t6R-A0Fc-uNf1q8oM53Gne8lIVmlA&_hsmi=373735563&utm_source=newsletter)

## Setting Up Development Environment

---

Before you start, make sure you have [Just Command Runner](https://github.com/casey/just) installed.

```bash
$ git clone https://github.com/gchoi/cython-examples.git
$ cd cython-examples
$ just venv
```

## Jupyter Notebooks

---

Run with Jupyter Notebooks:

* [cython-example-1](notebooks/cython-example-1.ipynb)
* [cython-example-2](notebooks/cython-example-2.ipynb)
* [cython-example-3](notebooks/cython-example-3.ipynb)

## Running Python Examples

---

### Build Cython extensions

```bash
$ just build
```

Running the command above will build the Cython extensions and generate the `.so` files in [cython_mods] folder.

### Run Python Examples

```bash
$ just run-example-1   # Sum of squares
$ just run-example-2   # Monte Carlo simulation to calculate PI
$ just run-example-3   # Image processing (sharpen filter for high resolution image)
```
