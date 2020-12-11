import pytest
from hello import addthis

def test_addthis():
    assert 3 == addthis(1,2)

def test_addthis_wrong_type():
    with pytest.raises(ValueError) as excinfo:
        addthis("one",2)
    assert "invalid literal" in str(excinfo.value)