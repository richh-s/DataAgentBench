code = """import json
import re
import os

# Load package data with MIT license and release status
packages_file = 'file_storage/functions.query_db:8.json'
with open(packages_file, 'r') as f:
    packages = json.load(f)

# Load project package version mappings
projects_file = 'file_storage/functions.query_db:10.json'
with open(projects_file, 'r') as f:
    project_mappings = json.load(f)

print('__RESULT__:')
print(json.dumps({
    'packages_with_mit': len(packages),
    'project_mappings': len(project_mappings)
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:6': 100, 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:12': ['functions.query_db:0.json', 'functions.query_db:10.json', 'functions.query_db:8.json']}

exec(code, env_args)
