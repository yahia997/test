import subprocess

def test_hello_world():
    result = subprocess.run(
        ["python", "solution.py"],
        capture_output=True,
        text=True
    )
    assert result.stdout.strip() == "Hello, World!"