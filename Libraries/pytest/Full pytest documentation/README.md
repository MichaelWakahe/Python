# Full Pytest Documentation

Examples are derived from [Pytest documentation](https://docs.pytest.org/en/latest/contents.html)

To find out what kind of builtin pytest fixtures exist, use the command:
```pytest --fixtures```

To run pytest, you have the option to specify files and directories. If you don’t specify any files
or directories, pytest will look for tests in the current working directory and subdirectories. It
looks for files starting with `test_` or ending with `_test`.