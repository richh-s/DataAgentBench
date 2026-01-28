code = """import json, re
# Load the large query result stored in var_call_x1F7ho40paHqd6gQrRddG274
path = var_call_x1F7ho40paHqd6gQrRddG274
with open(path, 'r') as f:
    records = json.load(f)

# For each record, extract a numeric copies count from repo_data_description
pattern = re.compile(r'(?:repeated|repeated|copied|copied|appears|appearing|duplicated|duplicated|appears|appears)\s+(?:\D*?)?(\d+)\s+times|copied\s+(\d+)|appearing\s+(\d+)|appears\s+(\d+)|duplicated\s+(\d+)|repeated\s+(\d+)', re.IGNORECASE)

def extract_count(s):
    if not s:
        return 1
    m = pattern.search(s)
    if m:
        for grp in m.groups():
            if grp:
                try:
                    return int(grp)
                except:
                    pass
    # fallback: find all numbers and take the largest
    nums = re.findall(r"(\d+)", s)
    if nums:
        return max(int(x) for x in nums)
    return 1

# Compute counts
for r in records:
    r['parsed_copies'] = extract_count(r.get('repo_data_description',''))

# Find max
max_copies = max(r['parsed_copies'] for r in records) if records else 0
max_records = [ { 'id': r['id'], 'parsed_copies': r['parsed_copies'], 'any_repo': r.get('any_repo'), 'any_path': r.get('any_path'), 'repo_data_description': r.get('repo_data_description')} for r in records if r['parsed_copies']==max_copies ]

output = { 'max_copies': max_copies, 'records': max_records }

import json
print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_QCEF4EENSwc1rWuQhx7QQFyS': [], 'var_call_DOqIQ9EmEmqMdjhKYF5xge2C': 'file_storage/call_DOqIQ9EmEmqMdjhKYF5xge2C.json', 'var_call_EdcoI6Abh0pPUAyTtXxAemox': [], 'var_call_x1F7ho40paHqd6gQrRddG274': 'file_storage/call_x1F7ho40paHqd6gQrRddG274.json', 'var_call_RloITwH3ggQel9JoksjJ8ipZ': []}

exec(code, env_args)
