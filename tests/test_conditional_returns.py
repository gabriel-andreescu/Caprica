import re
from pathlib import Path

import pytest


@pytest.mark.parametrize("mode", ["normal", "release", "final"])
def test_conditional_return_values(compile_script, mode):
    source = Path(__file__).parent / "fixtures/conditional_returns/ConditionalReturns.psc"
    result, output = compile_script(
        source, game="fallout4", release=mode != "normal", final=mode == "final"
    )
    assert result.returncode == 0, result.stdout + result.stderr
    assert (output / "ConditionalReturns.pex").is_file()
    assembly = (output / "ConditionalReturns.pas").read_text().lower()
    for caller, callee, value_type, retained in [
        ("readdebug", "debugvalue", "int", mode == "normal"),
        ("readbeta", "betavalue", "float", mode != "final"),
    ]:
        body = re.search(rf"\.function {caller}\b(.*?)\.endfunction", assembly, re.S)[1]
        call = re.search(rf"\bcallstatic\s+\S+\s+{callee}\s+(\S+)", body)
        assert bool(call) == retained, body
        if retained:
            operand = re.escape(call[1])
            assert re.search(rf"\.local\s+{operand}\s+{value_type}\b", body)
            assert re.search(rf"\breturn\s+{operand}(?=\s)", body)
    diagnostics = result.stdout + result.stderr
    assert "W1001" in diagnostics
    assert "W1002" in diagnostics
