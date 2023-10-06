import pytest

__all__ = [
    "pytest_addoption",
]


def pytest_addoption(parser):
    parser.addoption(
        f"--webci-conf",
        dest=f"webci_conf",
        action="append",
        help="Path to config file",
    )
