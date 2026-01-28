code = """import json, re

def load_json_maybe_path(obj):
    if isinstance(obj, str) and obj.endswith('.json'):
        with open(obj, 'r', encoding='utf-8') as f:
            return json.load(f)
    return obj

docs = load_json_maybe_path(var_call_aogXkumn6FWeJlS4Tns9KpMW)

# extract Capital Improvement Projects (Completed) section projects from these docs
results = []
for d in docs:
    text = d.get('text','')
    m = re.search(r'Capital Improvement Projects \(Completed\)(.*?)(?:Disaster Projects|Disaster Recovery Projects|$)', text, flags=re.S|re.I)
    if not m:
        continue
    sec = m.group(1)
    # project names are lines with no bullets followed by blank line
    lines = [ln.strip() for ln in sec.splitlines() if ln.strip()]
    for i, ln in enumerate(lines):
        if 'Updates:' in ln or ln.startswith('(cid') or ln.lower().startswith('page'):
            continue
        # if next line contains 'Updates:' then this is a project name
        if i+1 < len(lines) and lines[i+1].startswith('(cid'):
            continue
        if i+1 < len(lines) and lines[i+1].lower().startswith('updates'):
            results.append({'filename': d['filename'], 'Project_Name': ln, 'updates': lines[i+1]})

print('__RESULT__:')
print(json.dumps(results))"""

env_args = {'var_call_Vtkar1isgHg5NYjEr20jrsBI': 'file_storage/call_Vtkar1isgHg5NYjEr20jrsBI.json', 'var_call_z3Uc0TUUYnFKnmYOips0lfcE': 'file_storage/call_z3Uc0TUUYnFKnmYOips0lfcE.json', 'var_call_MP61JIGkf4luApqBahtYpPyH': {'ok': True}, 'var_call_QeB5hBLZIONgJpDbKQ2OwKNo': {'n_2022_docs': 5, 'n_park_completed_mentions': 5, 'sample_filenames': ['malibucity_agenda__01262022-1835.txt', 'malibucity_agenda__03232022-1869.txt', 'malibucity_agenda__06222022-1919.txt', 'malibucity_agenda__07272022-1939.txt', 'malibucity_agenda__11102022-1995.txt']}, 'var_call_aogXkumn6FWeJlS4Tns9KpMW': 'file_storage/call_aogXkumn6FWeJlS4Tns9KpMW.json'}

exec(code, env_args)
