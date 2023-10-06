import pytest

__all__ = [
    "pytest_addoption",
]


def pytest_addoption(parser):
    parser.addoption(
        f"--webci-conf",
        dest="webci_conf",
        action="append",
        help="Path to config file",
    )
    parser.addoption(
        f"--web-version",
        dest="web_version",
        help="web version",
    )
    A = 1
