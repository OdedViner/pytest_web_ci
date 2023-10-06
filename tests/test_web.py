import pytest
import logging


log = logging.getLogger(__name__)

from framework.pytest_customization import tier1, tier2, tier3


@tier1
def test_web1(project_factory):
    # project_factory()
    # helper.run_command("pwd")
    log.info("tier1")


@tier2
def test_web2():
    log.info("tier2")


@tier3
def test_web3():
    log.info("tier3")
