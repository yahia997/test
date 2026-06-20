import subprocess

# phase 2 builds on phase 1
# student now needs solution.py that:
#   - still prints Hello, World!
#   - also accepts a name argument: python solution.py Ahmed → Hello, Ahmed!

def run_solution(args=[]):
    return subprocess.run(
        ["python", "solution.py"] + args,
        capture_output=True,
        text=True,
        timeout=5
    )

# ── phase 1 tests still must pass ────────────────────────

def test_default_output_still_works():
    result = run_solution()
    assert result.stdout.strip() == "Hello, World!", \
        f"Expected 'Hello, World!' but got '{result.stdout.strip()}'"

def test_exit_code_is_zero():
    result = run_solution()
    assert result.returncode == 0

def test_no_stderr():
    result = run_solution()
    assert result.stderr == ""

# ── phase 2 new requirements ──────────────────────────────

def test_custom_name():
    result = run_solution(["Ahmed"])
    assert result.stdout.strip() == "Hello, Ahmed!", \
        f"Expected 'Hello, Ahmed!' but got '{result.stdout.strip()}'"

def test_another_name():
    result = run_solution(["Yahya"])
    assert result.stdout.strip() == "Hello, Yahya!", \
        f"Expected 'Hello, Yahya!' but got '{result.stdout.strip()}'"

def test_custom_name_exit_code():
    result = run_solution(["Ahmed"])
    assert result.returncode == 0