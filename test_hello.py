import pytest
from click.testing import CliRunner
from hello import addthis
from hellocli import calladdthis

def test_addthis():
    assert 3 == addthis(1,2)

def test_addthis_wrong_type():
    with pytest.raises(ValueError) as excinfo:
        addthis("one",2)
    assert "invalid literal" in str(excinfo.value)

def test_cli():
  runner = CliRunner()
  result = runner.invoke(calladdthis, ['--x', '1', '--y', '1'])
  assert result.exit_code == 0
  assert '2' in result.output