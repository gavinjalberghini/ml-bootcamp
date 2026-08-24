"""Small gh helpers shared by mentor scripts."""
from __future__ import annotations

import json
import subprocess


def run_gh(args: list[str], input_obj=None, check: bool = False):
    cmd = ['gh', *args]
    payload = None if input_obj is None else json.dumps(input_obj)
    result = subprocess.run(cmd, text=True, capture_output=True, input=payload)
    if check and result.returncode != 0:
        raise SystemExit(result.stderr or result.stdout or f'gh {" ".join(args)} failed')
    return result


def gh_json(args: list[str], input_obj=None):
    result = run_gh(['api', *args], input_obj=input_obj)
    if result.returncode != 0:
        return None, (result.stderr or result.stdout).strip()
    text = result.stdout.strip()
    if not text:
        return {}, None
    try:
        return json.loads(text), None
    except json.JSONDecodeError:
        return text, None


def gh_ok(args: list[str]) -> bool:
    return run_gh(args).returncode == 0
