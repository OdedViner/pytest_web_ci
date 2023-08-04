import pytest
import logging

from framework import config


log = logging.getLogger(__name__)


@pytest.fixture()
def project_factory(request):
    return project_factory_fixture(request)


def project_factory_fixture(request):
    a = [1]

    def factory(project_name=None):
        a.append(2)
        log.info(a)
        return a

    def finalizer():
        a.append(3)
        log.info(a)

    request.addfinalizer(finalizer)
    return factory
