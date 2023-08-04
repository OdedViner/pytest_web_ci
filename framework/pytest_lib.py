import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--deploy",
        dest="deploy",
        action="store_true",
        default=False,
        help="If provided a test cluster will be deployed on AWS to use for testing",
    )


@pytest.mark.my_marker
def pytest_my_marker():
    print("This is a custom marker.")
