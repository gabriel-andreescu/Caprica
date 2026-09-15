import re
from pathlib import Path


def test_parent_and_self_struct_members(compile_script):
    source = Path(__file__).parent / "fixtures/struct_members/StructMembers.psc"
    result, output = compile_script(source, game="fallout4")
    assert result.returncode == 0, result.stdout + result.stderr
    assert (output / "StructMembers.pex").is_file()
    assembly = (output / "StructMembers.pas").read_text().lower()

    def body(name):
        match = re.search(rf"\.function {name}\b(.*?)\.endfunction", assembly, re.S)
        assert match, f"Missing function: {name}\n{assembly}"
        return match[1]

    get_member = r"\bstructget\s+\S+\s+\S+\s+(\w+)"
    set_member = r"\bstructset\s+\S+\s+(\w+)"
    assert set(re.findall(get_member, body("read"))) == {"parent", "self"}
    assert set(re.findall(set_member, body("write"))) == {"parent", "self"}
    assert set(re.findall(get_member, body("increment"))) == {"parent", "self"}
    assert set(re.findall(set_member, body("increment"))) == {"parent", "self"}
    assert re.search(r"\bcallparent\s+getvalue\b", body("inherited"))
    assert re.search(r"\bcallmethod\s+getvalue\s+self\b", body("current"))
