# Python Performance Optimizations

A collection of examples, tricks and comparisons of code optimization techniques in Python. I focus on both speed, readability and memory consumption.

## Table of Contents
- [Python Performance Optimizations](#python-performance-optimizations)
  - [Table of Contents](#table-of-contents)
  - [🔧 Usage](#-usage)
    - [Get repo and create virtual environment](#get-repo-and-create-virtual-environment)
    - [Activate virtual environment](#activate-virtual-environment)
    - [Install requirements](#install-requirements)
  - [📝 Notebooks](#-notebooks)

## 🔧 Usage

### Get repo and create virtual environment
```bash
git clone https://github.com/karoldziubak/python_optimizations_nb.git
cd python_optimizations_nb
python -m venv .venv
```
### Activate virtual environment
For Unix/MacOs:
```bash
source .venv/bin/activate
```
For Windows:
```bash
.venv\Scripts\activate
```
### Install requirements
```bash
pip install -r requirements.txt
```
Run notebook

## 📝 Notebooks
Check out the following notebooks:
- `examples/basics.ipynb` for basic Python optimizations with built-in functions showing performance gains with `%timeit`,
- `examples/line_profiler.ipynb` for line-by-line profiling using `line_profiler` with case study based on optimization with `numpy` and `pandas` vectorization,
- `examples/loops.ipynb` for loop optimizations with `collections.Counter`, `itertools`, list comprehensions, maps and `numpy`.