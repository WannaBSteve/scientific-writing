from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "audit_prose.py"
SPEC = importlib.util.spec_from_file_location("audit_prose", SCRIPT)
assert SPEC and SPEC.loader
AUDIT = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = AUDIT
SPEC.loader.exec_module(AUDIT)


class AuditProseTests(unittest.TestCase):
    def test_clean_fixture_has_no_findings(self) -> None:
        text = (ROOT / "tests" / "fixtures" / "clean.md").read_text(encoding="utf-8")
        self.assertEqual(AUDIT.audit_text(text), [])

    def test_problematic_fixture_exercises_core_rules(self) -> None:
        text = (ROOT / "tests" / "fixtures" / "problematic.tex").read_text(
            encoding="utf-8"
        )
        codes = {finding.code for finding in AUDIT.audit_text(text)}
        self.assertTrue({"STYLE001", "STYLE003", "FLOW001", "FLOW002"} <= codes)
        self.assertTrue({"CITE001", "REF001", "REF002", "EQ001"} <= codes)

    def test_json_cli_is_machine_readable(self) -> None:
        result = subprocess.run(
            [
                sys.executable,
                str(SCRIPT),
                "--format",
                "json",
                str(ROOT / "tests" / "fixtures" / "problematic.tex"),
            ],
            check=True,
            capture_output=True,
            text=True,
        )
        payload = json.loads(result.stdout)
        self.assertEqual(len(payload), 1)
        self.assertGreater(len(payload[0]["findings"]), 0)

    def test_fail_on_warning_sets_exit_status(self) -> None:
        result = subprocess.run(
            [
                sys.executable,
                str(SCRIPT),
                "--fail-on",
                "warning",
                str(ROOT / "tests" / "fixtures" / "problematic.tex"),
            ],
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 1)


if __name__ == "__main__":
    unittest.main()
