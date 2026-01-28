code = """import json
# load repo in-clause from earlier
path = var_call_AUL5MSdQI6iDOfhO8Khnfil0
with open(path, 'r') as f:
    repos = json.load(f)
# Load commits messages
commits_path = var_call_CxeBb2Vj3MuU0dUQeFFdtYwr
with open(commits_path, 'r') as f:
    commits = json.load(f)

# Filter commits to those whose repo_name is in repos
repos_set = set(repos)
filtered = [c for c in commits if c['repo_name'] in repos_set and c.get('message')]

# Further filter: message length < 1000, and not start with 'merge', 'update', or 'test' (case-insensitive)
import re
out = []
for c in filtered:
    msg = c['message'].lstrip()
    if len(msg) < 1000:
        first_word = re.match(r"^(\w+)", msg, re.IGNORECASE)
        if first_word:
            fw = first_word.group(1).lower()
            if fw in ('merge','update','test'):
                continue
        out.append(c)

count = len(out)
print('__RESULT__:')
print(json.dumps(count))"""

env_args = {'var_call_YBeocKWRxOxzvPgZ8i7fI1aQ': 'file_storage/call_YBeocKWRxOxzvPgZ8i7fI1aQ.json', 'var_call_TvoXgW0CKJm579O4NIyP6Kis': 'file_storage/call_TvoXgW0CKJm579O4NIyP6Kis.json', 'var_call_AUL5MSdQI6iDOfhO8Khnfil0': 'file_storage/call_AUL5MSdQI6iDOfhO8Khnfil0.json', 'var_call_t2cps1GWHaysbvhEKMJXSPzg': 'file_storage/call_t2cps1GWHaysbvhEKMJXSPzg.json', 'var_call_CxeBb2Vj3MuU0dUQeFFdtYwr': 'file_storage/call_CxeBb2Vj3MuU0dUQeFFdtYwr.json'}

exec(code, env_args)
