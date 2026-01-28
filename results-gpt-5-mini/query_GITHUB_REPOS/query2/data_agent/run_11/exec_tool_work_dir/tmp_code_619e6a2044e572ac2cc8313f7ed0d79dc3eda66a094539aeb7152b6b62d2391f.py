code = """import json, re
# Load the contents query result (file path stored in var_call_FsKrfGfFhGLHW2nr80mbA8L5)
with open(var_call_FsKrfGfFhGLHW2nr80mbA8L5, 'r') as f:
    contents = json.load(f)
# Load the languages query result
with open(var_call_hOsA8ZfygHPVS7xT3O0P8af5, 'r') as f:
    languages = json.load(f)

# Build a map of repo_name -> language_description
lang_map = {r['repo_name']: r['language_description'] for r in languages}

# Function to determine primary language from language_description
def primary_language(desc):
    # desc examples: "The codebase includes: Ruby (22,438 bytes), Shell (465 bytes)."
    # We'll find all occurrences of <Lang> (number bytes)
    parts = re.findall(r"([A-Za-z#+]+(?: [A-Za-z#+]+)*)\s*\((\d[\d,]*) bytes\)", desc)
    if not parts:
        # fallback: look for 'Swift' presence
        return 'Swift' if 'Swift' in desc else None
    # parts is list of tuples (lang, bytes_str)
    max_lang = None
    max_bytes = -1
    for lang, bstr in parts:
        b = int(bstr.replace(',', ''))
        if b > max_bytes:
            max_bytes = b
            max_lang = lang
    return max_lang

# Parse contents entries for non-binary swift files and extract copies from repo_data_description
entries = []
for e in contents:
    path = e.get('sample_path','') or ''
    if not path.lower().endswith('.swift'):
        continue
    desc = e.get('repo_data_description','') or ''
    if 'non-binary' not in desc.lower():
        continue
    # find pattern like '123 times'
    m = re.search(r"(\d+)\s+times", desc)
    copies = None
    if m:
        copies = int(m.group(1))
    else:
        # try to find 'appearing (\d+)' or 'appears (\d+)' etc
        m2 = re.search(r"appearing (\d+)", desc)
        if not m2:
            m2 = re.search(r"appears (\d+)", desc)
        if not m2:
            m2 = re.search(r"appears \w+ (\d+)", desc)
        if m2:
            copies = int(m2.group(1))
    if copies is None:
        continue
    entries.append({'id': e.get('id'), 'sample_repo_name': e.get('sample_repo_name'), 'sample_path': path, 'copies': copies, 'repo_data_description': desc})

# Find max copies
if not entries:
    result = {'error': 'No matching swift non-binary entries found'}
else:
    max_copies = max(x['copies'] for x in entries)
    max_entries = [x for x in entries if x['copies']==max_copies]
    # For each max entry, determine if its sample_repo_name is Swift primary in languages
    out = []
    for me in max_entries:
        repo = me['sample_repo_name']
        lang_desc = lang_map.get(repo)
        primary = None
        if lang_desc:
            primary = primary_language(lang_desc)
        out.append({'id': me['id'], 'copies': me['copies'], 'sample_repo_name': repo, 'primary_language': primary})
    result = {'max_copies': max_copies, 'entries': out}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_4vuCBzSNbuxurHfRsSXyzmEM': ['languages', 'repos', 'licenses'], 'var_call_60rgap9dLx5wiOp5J5llLZZl': ['commits', 'contents', 'files'], 'var_call_OYcX2oKBHRiVasDVwFh7Lihj': [{'id': '71a17ce92451858f3eb01aa8082551e48bc5550d', 'copies': '1'}, {'id': 'cc41f22d46f21f11c9e716b30cbaeb11f4ef80fc', 'copies': '1'}], 'var_call_FsKrfGfFhGLHW2nr80mbA8L5': 'file_storage/call_FsKrfGfFhGLHW2nr80mbA8L5.json', 'var_call_hOsA8ZfygHPVS7xT3O0P8af5': 'file_storage/call_hOsA8ZfygHPVS7xT3O0P8af5.json'}

exec(code, env_args)
