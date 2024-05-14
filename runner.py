import os

os.environ.pop('MOCK_SERVER', None)
os.environ.pop('MOCK_SERVER_PORT', None)

import subprocess
from settings import BASE_URL


arguments = []

if os.environ.get("MOCK_SERVER") == "0":
    arguments = ["-n", "auto"]

test_env = os.environ.copy()
exit_code = subprocess.call(["pytest"] + arguments, env=test_env)

if exit_code == 0:
  print("Pytest execution successful!")
else:
  print(f"Pytest execution failed with exit code: {exit_code}")

