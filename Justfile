# Justfile

VENV := ".venv"
PYTHON_VER := "3.14"

# list all tasks
default:
  @just --list

# Install uv
install-uv:
	curl -LsSf https://astral.sh/uv/install.sh | sh

# Set up Python virtual environment
venv: install-uv
    #!/usr/bin/env sh
    if [ "$(uname)" = "Darwin" ] || [ "$(uname)" = "Linux" ]; then
        echo "Installing virtual env on Darwin or Linux..."
        uv venv {{ VENV }} --python {{ PYTHON_VER }}
        . {{ VENV }}/bin/activate && uv sync
    else
        echo "Installing virtual env on Windows..."
        uv venv {{ VENV }} --python {{ PYTHON_VER }}
        {{ VENV }}/Scripts/activate && uv sync
    fi

# Copy module files
copy_modules:
    cp ./cython_mods/sum_of_squares.pyx ./sum_of_squares.pyx
    cp ./cython_mods/monte_carlo.pyx ./monte_carlo.pyx
    cp ./cython_mods/image_processor.pyx ./image_processor.pyx

# Build cpython modules
build: copy_modules
    . {{ VENV }}/bin/activate && \
    uv sync && \
    python setup.py build_ext --inplace
    mv ./sum_of_squares.cpython-314-darwin.so ./cython_mods/sum_of_squares.cpython-314-darwin.so
    mv ./monte_carlo.cpython-314-darwin.so ./cython_mods/monte_carlo.cpython-314-darwin.so
    mv ./image_processor.cpython-314-darwin.so ./cython_mods/image_processor.cpython-314-darwin.so
    just clean-up

# Clean up artifacts
clean-up:
    rm -rf build
    rm -r sum_of_squares.pyx
    rm -r monte_carlo.pyx
    rm -r image_processor.pyx
    rm -r sum_of_squares.c
    rm -r monte_carlo.c
    rm -r image_processor.c

# Run example 1 for Cython
run-example-cython-1:
    . {{ VENV }}/bin/activate && \
    uv sync && \
    uv run Example-Cython-1.py

# Run example 1 for Python
run-example-python-1:
    . {{ VENV }}/bin/activate && \
    uv sync && \
    uv run Example-Python-1.py

# Run example 2 for Cython
run-example-cython-2:
    . {{ VENV }}/bin/activate && \
    uv sync && \
    uv run Example-Cython-2.py

# Run example 2 for Python
run-example-python-2:
    . {{ VENV }}/bin/activate && \
    uv sync && \
    uv run Example-Python-2.py

# Run example 3 for Cython
run-example-cython-3:
    . {{ VENV }}/bin/activate && \
    uv sync && \
    uv run Example-Cython-3.py

# Run example 3 for Python
run-example-python-3:
    . {{ VENV }}/bin/activate && \
    uv sync && \
    uv run Example-Python-3.py