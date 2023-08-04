import pytest

tier1 = pytest.mark.run(order=2)
tier2 = pytest.mark.run(order=4)
tier3 = pytest.mark.run(order=1)
