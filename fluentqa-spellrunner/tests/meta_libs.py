import importlib.metadata


def test_print_py_meta():
    print(importlib.metadata)
    metadata = importlib.metadata
    print(metadata.PackageMetadata)
    print(metadata.entry_points())