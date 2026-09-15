import re
from pathlib import Path


def test_redundant_jump_removal(compile_script):
    source = Path(__file__).parent / "fixtures/optimizer/Branch.psc"
    result, output = compile_script(source, game="fallout4", optimize=True)
    assert result.returncode == 0, result.stdout + result.stderr
    assert (output / "Branch.pex").is_file()
    assembly = (output / "Branch.pas").read_text().lower()
    code = re.search(r"\.code\s+(.*?)\.endcode", assembly, re.S)
    assert code, assembly
    instructions = re.sub(r";[^\n]*", "", code[1])
    assert re.fullmatch(
        r"\s*jumpf\s+condition\s+(\w+)\s+return\s+1\s+\1:\s+return\s+2\s*",
        instructions,
    ), instructions
