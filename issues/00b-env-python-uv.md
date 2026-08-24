# [Environment] Python and uv

You need: PA0 done (this repo cloned, `learning/README.md` on a branch).

You will: install Python and uv, then run a script whose dependencies are
declared **in the file**. Every later programming assignment uses that same
pattern. You will not create a project virtualenv and `pip install` into it.

## Steps

1. Install **Python 3.10 or newer** if `python3 --version` is missing or older.
   - Windows: [python.org downloads](https://www.python.org/downloads/) or `winget install Python.Python.3.12`
   - macOS: `brew install python` or the python.org installer
   - Linux: your package manager (`sudo apt install python3` on Debian/Ubuntu)
2. Install **uv**: follow [uv installation](https://docs.astral.sh/uv/getting-started/installation/). Then open a new terminal and run `uv --version`.
3. Optional but used by the README shortcuts: install [Task](https://taskfile.dev/installation/). You can always call `uv run path/to/script.py` instead of `task pa1`.
4. Open `learning/ENV/hello.py`. It already has a [PEP 723](https://peps.python.org/pep-0723/) header:

   ```python
   # /// script
   # requires-python = ">=3.10"
   # dependencies = []
   # ///
   ```

   That header is how uv knows which Python and which packages the file needs.
   Empty `dependencies` means stdlib only.
5. From the repo root run:

   ```bash
   uv run learning/ENV/hello.py
   ```

   You should see `hello from uv` and a Python version of 3.10+. uv will
   download a Python if the system one is too old. There is no `venv` for you
   to activate.
6. Write `learning/ENV/notes.md` with: `uv --version`, the Python version
   `hello.py` printed, and one sentence in your own words on what the
   `# /// script` block is for.
7. Commit `learning/ENV/notes.md` on a branch and open a pull request.

## How later assignments use this

- Each `learning/PA*/…py` file starts with its own `# /// script` block.
- Run it with `uv run learning/PA1/kNN.py …` or `task pa1`. uv reads **that
  file's** header, not `pyproject.toml`.
- Third-party packages (matplotlib in PA2, optional CuPy in PA4) are added
  to that file's `dependencies` list. Do not `pip install` them globally.
- If script A imports script B, A's header must list every third-party
  package A still calls. uv does not inherit B's dependencies.

## How you reuse code after PA1

Do **not** copy `kNN.py` into the next folder. Import the previous
assignment as a module and subclass it:

```python
from load_assignment import import_pa
PA1 = import_pa('PA1')
class ScaledKNN(PA1.KNN):
    ...
```

`learning/load_assignment.py` is provided. The PA6+ skeletons already call
it. If you find a bug in leave-one-out, fix it in PA1; PA6 will pick it up
the next time it runs.

## Acceptance criteria

- `uv run learning/ENV/hello.py` prints a 3.10+ version without activating a venv.
- `learning/ENV/notes.md` exists and answers the prompts in step 6.
- A pull request includes that file.

## References

- [Installing uv](https://docs.astral.sh/uv/getting-started/installation/)
- [Running scripts with uv](https://docs.astral.sh/uv/guides/scripts/)
- [Inline script metadata (PEP 723)](https://docs.astral.sh/uv/guides/scripts/#declaring-script-dependencies)
- [PEP 723](https://peps.python.org/pep-0723/)
