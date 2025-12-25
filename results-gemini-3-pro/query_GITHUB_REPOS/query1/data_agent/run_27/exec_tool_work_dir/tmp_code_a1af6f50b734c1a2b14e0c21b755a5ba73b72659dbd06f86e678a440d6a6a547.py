code = """import json

# Load languages
with open(locals()['var_function-call-10580302241464987080'], 'r') as f:
    langs = json.load(f)

# Identify non-Python repos
non_python_repos = set()
for item in langs:
    desc = item.get('language_description', '')
    if 'Python' not in desc:
        non_python_repos.add(item['repo_name'])

# Load README files info
with open(locals()['var_function-call-7473736151300254069'], 'r') as f:
    readmes = json.load(f)

# Filter READMEs for non-Python repos
# We want to count repos (denominator) and then check content (numerator)
# One repo might have multiple READMEs? "path = 'README.md'" usually implies one per repo root.
# But `files` table has `ref`? The provided output doesn't show `ref`. 
# The query was `SELECT repo_name, id FROM files`.
# If multiple refs, we might have duplicates. 
# We should probably consider unique repo_names.
# But if a repo has a README, we count it.
# Let's see if we have duplicates per repo.

repo_readme_map = {} # repo_name -> set of blob_ids
target_blob_ids = set()

for item in readmes:
    repo = item['repo_name']
    blob_id = item['id']
    if repo in non_python_repos:
        if repo not in repo_readme_map:
            repo_readme_map[repo] = set()
        repo_readme_map[repo].add(blob_id)
        target_blob_ids.add(blob_id)

# Calculate stats
num_non_python_repos_with_readme = len(repo_readme_map)
num_blobs_to_fetch = len(target_blob_ids)

print(f"Non-Python repos with README: {num_non_python_repos_with_readme}")
print(f"Unique Blob IDs to fetch: {num_blobs_to_fetch}")

# Prepare output
result = {
    "num_repos": num_non_python_repos_with_readme,
    "num_blobs": num_blobs_to_fetch,
    "sample_blobs": list(target_blob_ids)[:10]
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-10580302241464987080': 'file_storage/function-call-10580302241464987080.json', 'var_function-call-7473736151300254069': 'file_storage/function-call-7473736151300254069.json'}

exec(code, env_args)
