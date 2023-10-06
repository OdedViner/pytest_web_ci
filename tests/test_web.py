import pytest
import logging

from framework import config
from framework.pytest_customization import tier1, tier2, tier3

log = logging.getLogger(__name__)


@pytest.mark.tier4
def test_web1(project_factory):
    port = config.ENV["port"]
    version = config.ENV["web_version"]
    log.info(f"port123={port}")
    log.info(f"web_version={version}")
    project_factory()
    log.info("tier1")


@tier2
def test_web2():
    log.info("tier2")


@tier3
def test_web3():
    log.info("tier3")
