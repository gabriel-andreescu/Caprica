def test_bare_script_name_with_crlf(compile_script, tmp_path):
    source = tmp_path / "BareHeader.psc"
    source.write_bytes(
        b"Scriptname BareHeader\r\n"
        b"Int Function Answer() Global\r\n"
        b"    Return 42\r\n"
        b"EndFunction\r\n"
    )
    (tmp_path / "ScriptObject.psc").write_bytes(b"Scriptname ScriptObject Native\r\n")

    result, output = compile_script(source, game="fallout4", pcompiler=True)

    assert result.returncode == 0, result.stdout + result.stderr
    assert (output / "BareHeader.pex").is_file()
