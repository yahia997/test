import subprocess

# phase 1: basic hello world
# student only needs solution.py that prints Hello, World!

def run_solution():
    return subprocess.run(
        ["python", "solution.py"],
        capture_output=True,
        text=True,
        timeout=5
    )

def test_output_is_correct():
    result = run_solution()
    assert result.stdout.strip() == "Hello, World!", \
        f"Expected 'Hello, World!' but got '{result.stdout.strip()}'"

def test_exit_code_is_zero():
    result = run_solution()
    assert result.returncode == 0, \
        f"Expected exit code 0 but got {result.returncode}"

def test_no_stderr():
    result = run_solution()
    assert result.stderr == "", \
        f"Unexpected stderr: {result.stderr}"