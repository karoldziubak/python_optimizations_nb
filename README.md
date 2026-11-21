# Python Performance Optimizations

A collection of examples, tricks and comparisons of code optimization techniques in Python. I focus on both speed, readability and memory consumption.

## Table of Contents
- [Python Performance Optimizations](#python-performance-optimizations)
  - [Table of Contents](#table-of-contents)
  - [🔧 Usage](#-usage)
    - [Get repo and install dependencies](#get-repo-and-install-dependencies)
    - [Run notebooks](#run-notebooks)
    - [Run tests](#run-tests)
  - [📝 Notebooks](#-notebooks)

## 🔧 Usage

The project is managed with [uv](https://docs.astral.sh/uv/) and targets Python 3.14 (pinned in `.python-version`). uv downloads the interpreter if it is missing.

### Get repo and install dependencies
```bash
git clone https://github.com/karoldziubak/python_optimizations_nb.git
cd python_optimizations_nb
uv sync
```
`uv sync` creates `.venv` and installs the exact versions from `uv.lock`.

### Run notebooks
In JupyterLab:
```bash
uv run jupyter lab
```
In VS Code, select the `.venv` interpreter as the notebook kernel.

### Run tests
Import smoke tests:
```bash
uv run pytest tests/
```
Execute every notebook cell (`basics.ipynb` takes a while because of `%timeit`). The `NBMAKE` variable makes failing `%%ipytest` assertions fail the run:
```bash
NBMAKE=1 uv run pytest --nbmake examples/ --nbmake-timeout=3600
```
In PowerShell:
```powershell
$env:NBMAKE = "1"; uv run pytest --nbmake examples/ --nbmake-timeout=3600
```

To add or update dependencies use `uv add <package>` and `uv lock --upgrade`.

## 📝 Notebooks
Check out the following notebooks:
- `examples/basics.ipynb` for basic Python optimizations with built-in functions showing performance gains with `%timeit`,
- `examples/line_profiler.ipynb` for line-by-line profiling using `line_profiler` with case study based on optimization with `numpy` and `pandas` vectorization,
- `examples/loops.ipynb` for loop optimizations with `collections.Counter`, `itertools`, list comprehensions, maps and `numpy`.