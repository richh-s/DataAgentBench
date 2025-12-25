code = """import json, re
from collections import defaultdict

path = var_call_XV2z1VhUkMeNTVKGslGoGeIt
with open(path) as f:
    data = json.load(f)

max_copies = -1
best = None

for row in data:
    desc = row.get('repo_data_description','')
    m = re.search(r'copied (\d+) times', desc)
    if not m:
        m = re.search(r'appearing (\d+) times', desc)
    if not m:
        m = re.search(r'duplicated (\d+) times', desc)
    if not m:
        m = re.search(r'repeated (\d+) times', desc)
    if not m:
        m = re.search(r'seen (\d+) times', desc)
    if not m:
        continue
    copies = int(m.group(1))
    if copies > max_copies:
        max_copies = copies
        best = {'id': row['id'], 'sample_repo_name': row['sample_repo_name'], 'copies': copies}

result = best

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_XV2z1VhUkMeNTVKGslGoGeIt': 'file_storage/call_XV2z1VhUkMeNTVKGslGoGeIt.json'}

exec(code, env_args)
