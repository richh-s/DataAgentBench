code = """import json

# Read the Swift repositories from the previous query
swift_repos_file = '/tmp/tmp_result_func___query_db___0.json'
with open(swift_repos_file, 'r') as f:
    swift_repos_data = json.load(f)

swift_repos = [repo['repo_name'] for repo in swift_repos_data]

print(f"Found {len(swift_repos)} Swift repositories")
print(f"First 10: {swift_repos[:10]}")

# Store for later use
with open('/tmp/swift_repos.json', 'w') as f:
    json.dump(swift_repos, f)

print('__RESULT__:')
print('{"count": '+str(len(swift_repos))+', "sample_repos": '+json.dumps(swift_repos[:10])+'}')"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['commits', 'contents', 'files'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json'}

exec(code, env_args)
