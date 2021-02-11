import pytest
from click.testing import CliRunner
from es6_sniffer import cli


@pytest.fixture
def runner():
    return CliRunner()


def test_cli(runner):
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    assert not result.exception
    assert result.output == 'Found 0 packages, 0 with engines, 0 without engines\nRecommend transpiling 0 packages\n[]\n'


def test_dummy_node_modules(runner):
    result = runner.invoke(cli.main, '--node-modules=tests/fixtures/node_modules')
    assert result.exit_code == 0
    assert not result.exception

    desired_output = (
        'tests/fixtures/node_modules/es6-package/package.json exceeds max version',
        'tests/fixtures/node_modules/es5-package/package.json includes max version',
        'Found 3 packages, 2 with engines, 1 without engines',
        'Recommend transpiling 1 packages',
        "['tests/fixtures/node_modules/es6-package']",
    )

    for msg in desired_output:
        assert msg in result.output


@pytest.mark.parametrize('engines,expected_value', [
    ({'npm': 'foo'}, None),
    ({'node': ['>=8.10.0']}, '>=8.10.0'),
    ({'node': ['>= 8.10.0']}, '>=8.10.0'),
    ({'node': ['>=8.10.x']}, '>=8.10.0'),
    (['node >= 8.10.0'], '>=8.10.0'),
    ({'node': '^6 || ^7 || ^8 || ^9 || ^10 || ^11 || ^12 || >=13.7'}, '>=6,>=7,>=8,>=9,>=10,>=11,>=12,>=13.7'),
    ({'node': '*'}, '*'),
])
def test_format_version(engines, expected_value):
    output = cli.get_formatted_node_version(engines)
    assert output == expected_value
