code = """import json

# Load repository names
file_path = locals()['var_functions.query_db:8']
with open(file_path, 'r') as f:
    repos_data = json.load(f)

# Extract just the repository names
repo_names = [repo['repo_name'] for repo in repos_data]
print(f"Total repositories to check: {len(repo_names)}")

# Build the query string for DuckDB
# Use proper escaping for repo names
escaped_repos = []
for name in repo_names:
    # Escape single quotes by doubling them
    escaped = name.replace("'", "''")
    escaped_repos.append(f"'{escaped}'")

# Create the IN clause
in_clause = ', '.join(escaped_repos)

# Build the complete query
query = f"""
SELECT COUNT(*) as commit_count
FROM commits
WHERE repo_name IN ({in_clause})
AND message IS NOT NULL 
AND LENGTH(message) < 1000
AND LOWER(message) NOT LIKE 'merge%'
AND LOWER(message) NOT LIKE 'update%'
AND LOWER(message) NOT LIKE 'test%'
"""

print("Query built successfully")
print(f"Query length: {len(query)} characters")

# Store the query for execution
result = {
    'query': query,
    'repo_count': len(repo_names),
    'query_length': len(query)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': 'file_storage/functions.execute_python:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:10': 'file_storage/functions.execute_python:10.json', 'var_functions.execute_python:18': 'file_storage/functions.execute_python:18.json', 'var_functions.query_db:20': [{'repo_name': 'jitsi/jipopro'}, {'repo_name': 'NuGet/json-ld.net'}, {'repo_name': 'virtualcoinclub/common'}, {'repo_name': 'pydev/jmx_exporter'}, {'repo_name': 'eskatos/qi4j-dev-scripts'}], 'var_functions.execute_python:22': 'file_storage/functions.execute_python:22.json', 'var_functions.execute_python:26': {'all_repos_count': 114972, 'sample_repos': ['jitsi/jipopro', 'NuGet/json-ld.net', 'virtualcoinclub/common', 'pydev/jmx_exporter', 'eskatos/qi4j-dev-scripts', 'doximity/docker-redis', 'raghavkarol/dotfiles', 'Microsoft/TypeScript', 'romelperez/conky-command', 'NorthernMan54/homebridge-wssensor']}}

exec(code, env_args)
