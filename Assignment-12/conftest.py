import sys
import os

# Add project root to path immediately
rootdir = os.path.dirname(os.path.abspath(__file__))
if rootdir not in sys.path:
    sys.path.insert(0, rootdir)

# Also patch it in before any module is collected
def pytest_configure(config):
    if rootdir not in sys.path:
        sys.path.insert(0, rootdir)