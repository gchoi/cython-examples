# cython-examples

## Setting Up Development Environment

Before you start, make sure you have [Just Command Runner](https://github.com/casey/just) installed.

* macOS: `brew install just`
* Debian/Ubuntu: `sudo apt install just`
* Windows: `choco install just`

```bash
$ git clone https://github.com/gchoi/cython-examples.git
$ cd cython-examples
$ just venv
```

## Jupyter Notebooks

Run with Jupyter Notebooks:

* [Example-1.ipynb](./Example-1.ipynb) - Sum of squares
* [Example-2.ipynb](./Example-2.ipynb) - Monte Carlo simulation to calculate PI
* [Example-3.ipynb](./Example-3.ipynb) - Image processing (sharpen filter for high resolution image)

## Running Python Examples

### Build Cython extensions

```bash
$ just build
```

Running the command above will build the Cython extensions and generate the `.so` files in [cython_mods] folder.

### Run Standard Python Examples

```bash
$ just run-example-python-1   # Sum of squares
$ just run-example-python-2   # Monte Carlo simulation to calculate PI
$ just run-example-python-3   # Image processing (sharpen filter for high resolution image)
```

### Run Cython Examples

```bash
$ just run-example-cython-1   # Sum of squares
$ just run-example-cython-2   # Monte Carlo simulation to calculate PI
$ just run-example-cython-3   # Image processing (sharpen filter for high resolution image)
```

## Results Comparison

|                              | Standard Python (sec) | Cython (sec) | Speed Improvement       |
|------------------------------|-----------------------|--------------|-------------------------|
| Example 1 - Sum of Squares   | 20.4330076250         | 0.0000009170 | 22,282,451 times faster |
| Example 2 - Monte Carlo PI   | 27.96932              | 1.33899      | 21 times faster         |
| Example 3 - Image Processing | 2.86349               | 0.14742      | 20 times faster         |