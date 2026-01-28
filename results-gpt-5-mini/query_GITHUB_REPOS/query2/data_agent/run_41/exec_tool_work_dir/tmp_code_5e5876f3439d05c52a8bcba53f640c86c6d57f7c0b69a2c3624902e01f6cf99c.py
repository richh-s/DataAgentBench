code = """import json, re, pandas as pd

# Load data from storage file paths
with open(var_call_BCGLrbbjh7RqmJqyLFMhEK5V, 'r', encoding='utf-8') as f:
    contents = json.load(f)
with open(var_call_r0GhkdFN7UoM6SndNGW5fOTK, 'r', encoding='utf-8') as f:
    languages = json.load(f)

# Build set of repositories that mention Swift in language_description
swift_repos = set()
for rec in languages:
    ld = rec.get('language_description') or ''
    if 'swift' in ld.lower():
        swift_repos.add(rec.get('repo_name'))

# Parse contents records for non-binary Swift files and extract copy counts
rows = []
for rec in contents:
    desc = (rec.get('repo_data_description') or '').lower()
    path = rec.get('sample_path') or ''
    if '.swift' not in path.lower():
        continue
    if 'non-binary' not in desc and 'non binary' not in desc:
        continue
    # find number before 'times' or 'time'
    m = re.search(r'(\d+)\s+times', desc)
    if not m:
        m = re.search(r'(\d+)\s+time\b', desc)
    if not m:
        # try patterns like 'copied 12 times' or 'appearing 8 times' already caught
        continue
    copies = int(m.group(1))
    rows.append({
        'id': rec.get('id'),
        'sample_repo_name': rec.get('sample_repo_name'),
        'sample_path': rec.get('sample_path'),
        'copies': copies,
        'repo_data_description': rec.get('repo_data_description')
    })

if not rows:
    result = {'error': 'No non-binary Swift files with copy counts found in contents.'}
else:
    df = pd.DataFrame(rows)
    # Keep unique by id (should already be unique)
    df = df.drop_duplicates(subset=['id'])
    # Filter to repositories that are Swift according to languages table
    df_swift = df[df['sample_repo_name'].isin(swift_repos)].copy()
    if df_swift.empty:
        # If none match, fallback to overall max
        top = df.sort_values('copies', ascending=False).iloc[0].to_dict()
        result = {
            'note': 'No matching repository in metadata languages table identified as Swift; returning overall top file',
            'repo_name': top['sample_repo_name'],
            'file_id': top['id'],
            'sample_path': top['sample_path'],
            'copies': int(top['copies'])
        }
    else:
        top = df_swift.sort_values('copies', ascending=False).iloc[0].to_dict()
        result = {
            'repo_name': top['sample_repo_name'],
            'file_id': top['id'],
            'sample_path': top['sample_path'],
            'copies': int(top['copies'])
        }

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_BCGLrbbjh7RqmJqyLFMhEK5V': 'file_storage/call_BCGLrbbjh7RqmJqyLFMhEK5V.json', 'var_call_r0GhkdFN7UoM6SndNGW5fOTK': 'file_storage/call_r0GhkdFN7UoM6SndNGW5fOTK.json'}

exec(code, env_args)
