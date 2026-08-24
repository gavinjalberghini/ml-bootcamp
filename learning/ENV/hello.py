# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""ENV: prove that uv can run this file from its in-file script header."""
import sys

print('hello from uv')
print(f'python {sys.version}')
print(f'executable {sys.executable}')
