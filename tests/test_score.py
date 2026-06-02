#!/usr/bin/env python3
"""
Unit tests for AI Agent Governance Score.
"""

import unittest
import json
import subprocess
import os
import sys

# Paths (adjust if needed)
SCRIPT_PATH = os.path.join(os.path.dirname(__file__), "..", "governance_score.py")
EXAMPLE_FAILURE = os.path.join(os.path.dirname(__file__), "..", "examples", "aws_trace_failure.json")
EXAMPLE_SUCCESS = os.path.join(os.path.dirname(__file__), "..", "examples", "aws_trace_success.json")

class TestGovernanceScore(unittest.TestCase):

    def test_failure_trace_score(self):
        """Test that failure trace produces a Warning score (50–69)."""
        result = subprocess.run(
            [sys.executable, SCRIPT_PATH, EXAMPLE_FAILURE, "--json"],
            capture_output=True, text=True
        )
        self.assertEqual(result.returncode, 0, f"Script failed: {result.stderr}")
        data = json.loads(result.stdout)
        self.assertIn("governance_score", data)
        # Expect score between 50 and 69 (Warning range)
        self.assertGreaterEqual(data["governance_score"], 50)
        self.assertLess(data["governance_score"], 70)
        self.assertEqual(data["interpretation"], "Warning – risk of silent failure")

    def test_success_trace_score(self):
        """Test that success trace produces a high governance score (>=90)."""
        result = subprocess.run(
            [sys.executable, SCRIPT_PATH, EXAMPLE_SUCCESS, "--json"],
            capture_output=True, text=True
        )
        self.assertEqual(result.returncode, 0, f"Script failed: {result.stderr}")
        data = json.loads(result.stdout)
        self.assertGreaterEqual(data["governance_score"], 90,
                                f"Expected score >=90, got {data['governance_score']}")
        self.assertEqual(data["interpretation"], "Excellent – highly governable")

    def test_verbose_output(self):
        """Test verbose mode produces expected step details."""
        result = subprocess.run(
            [sys.executable, SCRIPT_PATH, EXAMPLE_FAILURE, "--verbose"],
            capture_output=True, text=True
        )
        self.assertEqual(result.returncode, 0)
        self.assertIn("Step‑by‑step details:", result.stdout)
        self.assertIn("Step 1:", result.stdout)

    def test_invalid_trace_file(self):
        """Test that non-existent file returns non-zero exit code."""
        result = subprocess.run(
            [sys.executable, SCRIPT_PATH, "nonexistent.json"],
            capture_output=True, text=True
        )
        self.assertNotEqual(result.returncode, 0)

    def test_empty_trace(self):
        """Test that empty trace is rejected (non-zero exit)."""
        import tempfile
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
            json.dump([], f)
            temp_path = f.name
        try:
            result = subprocess.run(
                [sys.executable, SCRIPT_PATH, temp_path],
                capture_output=True, text=True
            )
            # Script should exit with error because empty trace is invalid
            self.assertNotEqual(result.returncode, 0)
        finally:
            os.unlink(temp_path)

if __name__ == "__main__":
    unittest.main()