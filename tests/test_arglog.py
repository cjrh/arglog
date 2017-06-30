import os
import sys
import subprocess
import pytest


@pytest.mark.parametrize('levelname', ['DEBUG', 'INFO', 'WARNING'])
def test_known(levelname):
    output = subprocess.check_output([
        sys.executable,
        os.path.join(os.path.dirname(__file__), 'main.py'),
        levelname,
    ])
    assert output == levelname.encode('utf-8')


@pytest.mark.parametrize('levelname', ['DEBUG', 'INFO', 'WARNING'])
def test_unknown(levelname):
    output = subprocess.check_output([
        sys.executable,
        os.path.join(os.path.dirname(__file__), 'main_known.py'),
        levelname,
    ])
    assert output == levelname.encode('utf-8')
