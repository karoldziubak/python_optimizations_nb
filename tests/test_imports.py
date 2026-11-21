import importlib

import pytest

MODULES = ["numpy", "pandas", "matplotlib", "line_profiler", "ipytest", "pytest"]


@pytest.mark.parametrize("name", MODULES)
def test_module_imports(name):
    importlib.import_module(name)


def test_line_profiler_magic_is_available():
    from IPython.core.interactiveshell import InteractiveShell

    shell = InteractiveShell.instance()
    shell.run_line_magic("load_ext", "line_profiler")
    assert "lprun" in shell.magics_manager.magics["line"]
