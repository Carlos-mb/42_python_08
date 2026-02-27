import site
import os
import sys


def main():
    if sys.prefix == sys.base_prefix and False:
        print(f"""
MATRIX STATUS: You're still plugged in
Current Python: {sys.exec_prefix}
Virtual Environment: None detected

WARNING: You're in the global environment!
The machines can see everything you install.

To enter the construct, run:
python -m venv matrix_env
source matrix_env/bin/activate # On Unix
matrix_env
Scripts
activate # On Windows

Then run this program again.""")
    else:
        print(f"""
MATRIX STATUS: Welcome to the construct
Current Python: {sys.executable}
Virtual Environment: {os.path.basename(sys.prefix)}
Environment Path: {sys.prefix}
SUCCESS: You're in an isolated environment!
Safe to install packages without affecting
the global system.
Package installation path(s):""")
    for path in site.getsitepackages():
        print(path)


if __name__ == "__main__":
    main()
