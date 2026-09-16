import re
from pathlib import Path


def test_local_before_later_outer_declaration(compile_script):
    source = Path(__file__).parent / "fixtures/local_scopes/LocalScopes.psc"
    result, output = compile_script(source, game="skyrim")
    assert result.returncode == 0, result.stdout + result.stderr
    assert (output / "LocalScopes.pex").is_file()
    assembly = (output / "LocalScopes.pas").read_text().lower()
    inner = re.search(r'\bassign\s+(\S+)\s+7\b', assembly)
    outer = re.search(r'\bassign\s+(\S+)\s+"9"', assembly)
    assert inner and outer, assembly
    assert inner[1] != outer[1]
    assert re.search(rf"\breturn\s+{re.escape(inner[1])}(?=\s)", assembly)
    assert re.search(rf"\bcast\s+\S+\s+{re.escape(outer[1])}(?=\s)", assembly)
