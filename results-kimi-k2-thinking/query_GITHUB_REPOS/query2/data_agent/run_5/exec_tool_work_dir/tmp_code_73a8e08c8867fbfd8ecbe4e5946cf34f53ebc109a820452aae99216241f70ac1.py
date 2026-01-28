code = """import json
import re

# Load the Swift repositories data
with open('var_functions.query_db:4', 'r') as f:
    swift_repos = json.load(f)

print(f"Found {len(swift_repos)} Swift repositories")
print("Sample:", swift_repos[0] if swift_repos else "No data")

# Extract repo names
swift_repo_names = [repo['repo_name'] for repo in swift_repos]
print(f"\nFirst few repo names: {swift_repo_names[:5]}")

# For debugging, let's also check the structure of repo_data_description
print("\n--- Sample repo_data_description patterns ---")
sample_descriptions = []
if swift_repos:
    # Let's query a few Swift files to see the description format
    import subprocess
    import sys

# Save the repo names for later use
with open('/tmp/swift_repo_names.json', 'w') as f:
    json.dump(swift_repo_names, f)

print("Swift repo names saved to /tmp/swift_repo_names.json")"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses'], 'var_functions.list_db:1': ['commits', 'contents', 'files'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:6': [{'total_rows': '24286'}], 'var_functions.query_db:7': [{'total_rows': '524077'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
