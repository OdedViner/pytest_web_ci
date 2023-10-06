import pytest
import logging


log = logging.getLogger(__name__)

from framework.pytest_customization import tier1, tier2, tier3


@pytest.mark.tier4
def test_web1(project_factory):
    project_factory()
    log.info("tier1")


@tier2
def test_web2():
    log.info("tier2")


@tier3
def test_web3():
    log.info("tier3")
