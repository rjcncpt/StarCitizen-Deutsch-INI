import subprocess
import sys
from pathlib import Path


def run_all_tests():
    """Run all test files in the current directory."""
    test_dir = Path(__file__).parent
    test_files = sorted(test_dir.glob("*_test.py"))

    if not test_files:
        print("No test files found.")
        return 1

    failed, passed = 0, 0
    for test_file in test_files:
        print(f"\n{'='*60}")
        print(f"Running: {test_file.name}")
        print(f"{'='*60}\n")
        result = subprocess.run([sys.executable, str(test_file), "--fail-on-error"])
        if result.returncode != 0:
            failed += 1
        else:
            passed += 1

    print(f"\n{'='*60}")
    print(f"{len(test_files)} Tests completed. Failed: {failed}, Passed: {passed}.")
    print(f"{'='*60}")
    return 1 if failed > 0 else 0


if __name__ == "__main__":
    sys.exit(run_all_tests())
