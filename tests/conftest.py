import subprocess
from pathlib import Path

import pytest


def pytest_addoption(parser):
    parser.addoption("--compiler", required=True, help="Path to the Caprica executable")


@pytest.fixture(scope="session")
def compiler(pytestconfig):
    path = Path(pytestconfig.getoption("--compiler")).resolve()
    if not path.is_file():
        raise pytest.UsageError(f"Compiler not found: {path}")
    return path


@pytest.fixture
def compile_script(compiler, tmp_path):
    def compile(source, *, game, pcompiler=False, optimize=False, release=False, final=False, parallel=False):
        result = subprocess.run(
            [
                str(compiler),
                source.name if pcompiler else str(source),
                f"--game={game}",
                f"--import={source.parent}",
                f"--output={tmp_path}",
                "--ignorecwd",
                "--dump-asm",
                *(["--pcompiler"] if pcompiler else []),
                *(["--optimize"] if optimize else []),
                *(["--release"] if release else []),
                *(["--final"] if final else []),
                *(["--parallel-compile"] if parallel else []),
            ],
            cwd=tmp_path,
            capture_output=True,
            text=True,
            timeout=30,
        )
        return result, tmp_path

    return compile
