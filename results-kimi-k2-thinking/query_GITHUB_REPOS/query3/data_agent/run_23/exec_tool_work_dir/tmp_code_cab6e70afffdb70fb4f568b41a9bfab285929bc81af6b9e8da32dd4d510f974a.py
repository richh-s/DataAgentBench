code = """import json

# First, load just a small sample to test
file_path = locals()['var_functions.query_db:8']
with open(file_path, 'r') as f:
    repos_data = json.load(f)

# Let's work with a manageable subset first
repo_names = [repo['repo_name'] for repo in repos_data[:100]]  # Just 100 for testing
print(f"Testing with {len(repo_names)} repositories")

# Build query string differently to avoid the * issue
query_parts = ["SELECT COUNT(*) as commit_count FROM commits WHERE repo_name IN ("]

# Add repo names with proper escaping
for i, name in enumerate(repo_names):
    if i > 0:
        query_parts.append(", ")
    escaped_name = name.replace("'", "''")
    query_parts.append("'" + escaped_name + "'")

query_parts.append(") AND message IS NOT NULL AND LENGTH(message) < 1000")
query_parts.append("AND LOWER(message) NOT LIKE 'merge%' AND LOWER(message) NOT LIKE 'update%' AND LOWER(message) NOT LIKE 'test%'")

query = "".join(query_parts)
print("Query constructed successfully")

result = {
    'test_query': query,
    'repo_count': len(repo_names)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': 'file_storage/functions.execute_python:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:10': 'file_storage/functions.execute_python:10.json', 'var_functions.execute_python:18': 'file_storage/functions.execute_python:18.json', 'var_functions.query_db:20': [{'repo_name': 'jitsi/jipopro'}, {'repo_name': 'NuGet/json-ld.net'}, {'repo_name': 'virtualcoinclub/common'}, {'repo_name': 'pydev/jmx_exporter'}, {'repo_name': 'eskatos/qi4j-dev-scripts'}], 'var_functions.execute_python:22': 'file_storage/functions.execute_python:22.json', 'var_functions.execute_python:26': {'all_repos_count': 114972, 'sample_repos': ['jitsi/jipopro', 'NuGet/json-ld.net', 'virtualcoinclub/common', 'pydev/jmx_exporter', 'eskatos/qi4j-dev-scripts', 'doximity/docker-redis', 'raghavkarol/dotfiles', 'Microsoft/TypeScript', 'romelperez/conky-command', 'NorthernMan54/homebridge-wssensor']}}

exec(code, env_args)
