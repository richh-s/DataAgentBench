code = """import json

# Load the large repo list
with open(locals()['var_function-call-14703408072722114376'], 'r') as f:
    target_repos_data = json.load(f)

target_repos = set(r['repo_name'] for r in target_repos_data)

# Load the commits aggregation result
# The previous tool output provided the list directly in the text, but also said it is stored under a key.
# If it is stored as a list, I can access it.
# If the previous output was just a print and not a file path for a large result, 
# it might be directly in the variable as a list (since it wasn't "too large").
# Let's check the type of var_function-call-10248769871995382432.

commits_data = locals()['var_function-call-10248769871995382432']

# If it's a string (file path), load it. If it's a list, use it.
if isinstance(commits_data, str) and not isinstance(commits_data, list):
    # It might be a file path if the system decided to store it, even if small?
    # Or it might be the list itself if the system stores the direct return value.
    # The tool output said "The result is stored under key...". 
    # Usually, if it's a file path, the text says "The result is too large...".
    # Here it didn't say that. It printed the result. 
    # So the variable likely holds the list directly.
    # But to be safe, I'll handle both.
    try:
        if commits_data.endswith('.json'):
             with open(commits_data, 'r') as f:
                commits_data = json.load(f)
    except:
        pass # It's likely the list or a string representation

if isinstance(commits_data, str):
    # It might be a string representation of the list if not a file path
    # But query_db returns a list of dicts usually.
    pass

# Filter and sum
total_commits = 0
matched_repos = []

# Ensure commits_data is a list of dicts
if isinstance(commits_data, list):
    for entry in commits_data:
        r_name = entry['repo_name']
        cnt = int(entry['cnt'])
        if r_name in target_repos:
            total_commits += cnt
            matched_repos.append(r_name)

print("__RESULT__:")
print(json.dumps({"total_commits": total_commits, "matched_repos": matched_repos}))"""

env_args = {'var_function-call-14703408072722114376': 'file_storage/function-call-14703408072722114376.json', 'var_function-call-5935493478175422404': 114972, 'var_function-call-10248769871995382432': [{'repo_name': 'facebook/react', 'cnt': '104'}, {'repo_name': 'tensorflow/tensorflow', 'cnt': '114'}, {'repo_name': 'twbs/bootstrap', 'cnt': '251'}, {'repo_name': 'Microsoft/vscode', 'cnt': '171'}, {'repo_name': 'apple/swift', 'cnt': '963'}, {'repo_name': 'torvalds/linux', 'cnt': '13413'}]}

exec(code, env_args)
