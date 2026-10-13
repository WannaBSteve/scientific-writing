from __future__ import annotations

import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class RepositoryTests(unittest.TestCase):
    def test_repository_consistency(self) -> None:
        subprocess.run(
            [sys.executable, str(ROOT / "scripts" / "check_repo.py")],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
        )

    def test_eval_assets(self) -> None:
        subprocess.run(
            [sys.executable, str(ROOT / "scripts" / "check_eval_assets.py")],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
        )


if __name__ == "__main__":
    unittest.main()
