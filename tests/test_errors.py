from pathlib import Path

import pytest


@pytest.mark.parametrize("parallel", [False, True], ids=["serial", "parallel"])
@pytest.mark.parametrize(
    "script,game,diagnostic",
    [
        ("Bad", "skyrim", "Unresolved identifier 'missingValue'"),
        ("NoHeader", "fallout4", "Unable to find script name"),
    ],
)
def test_compile_error_exits_normally(compile_script, parallel, script, game, diagnostic):
    source = Path(__file__).parent / f"fixtures/errors/{script}.psc"
    result, output = compile_script(source, game=game, parallel=parallel)
    assert diagnostic in result.stdout + result.stderr
    assert result.returncode == 0xFFFFFFFF, result.stdout + result.stderr
    assert not (output / f"{script}.pex").exists()
