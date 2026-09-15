# Compiler tests

Requires Python 3.10+ and a built Caprica executable.

```powershell
python -m pip install -r requirements-test.txt
python -m pytest tests --compiler build/Caprica/Release/Caprica.exe
```

The suite compiles self-contained Papyrus fixtures and checks generated assembly.
