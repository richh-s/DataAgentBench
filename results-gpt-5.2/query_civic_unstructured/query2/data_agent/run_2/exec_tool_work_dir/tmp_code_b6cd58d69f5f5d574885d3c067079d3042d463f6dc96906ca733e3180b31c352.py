code = """import json, re, pandas as pd

def load_json_maybe_path(obj):
    if isinstance(obj, str) and obj.endswith('.json'):
        with open(obj, 'r', encoding='utf-8') as f:
            return json.load(f)
    return obj

docs = load_json_maybe_path(var_call_aogXkumn6FWeJlS4Tns9KpMW)
fund = load_json_maybe_path(var_call_z3Uc0TUUYnFKnmYOips0lfcE)

# Find park-related completed in 2022 by looking for lines like 'Construction was completed ... 2022' under any project with 'Park' in name.
park_completed = set()
for d in docs:
    lines = d.get('text','').splitlines()
    for idx, ln in enumerate(lines):
        if re.search(r'\bPark\b', ln):
            proj = ln.strip()
            window = ' '.join(l.strip() for l in lines[idx:idx+60])
            if re.search(r'Construction was completed[^.]*2022', window, flags=re.I) or re.search(r'completed\s+\w+\s+2022', window, flags=re.I):
                park_completed.add(proj)

fund_df = pd.DataFrame(fund)
fund_df['total_amount'] = pd.to_numeric(fund_df['total_amount'])
eligible = pd.DataFrame({'Project_Name': sorted(park_completed)})
merged = eligible.merge(fund_df, on='Project_Name', how='left')
merged['total_amount'] = merged['total_amount'].fillna(0)

total = int(merged['total_amount'].sum())

print('__RESULT__:')
print(json.dumps({'projects': merged.to_dict(orient='records'), 'total': total}))"""

env_args = {'var_call_Vtkar1isgHg5NYjEr20jrsBI': 'file_storage/call_Vtkar1isgHg5NYjEr20jrsBI.json', 'var_call_z3Uc0TUUYnFKnmYOips0lfcE': 'file_storage/call_z3Uc0TUUYnFKnmYOips0lfcE.json', 'var_call_MP61JIGkf4luApqBahtYpPyH': {'ok': True}, 'var_call_QeB5hBLZIONgJpDbKQ2OwKNo': {'n_2022_docs': 5, 'n_park_completed_mentions': 5, 'sample_filenames': ['malibucity_agenda__01262022-1835.txt', 'malibucity_agenda__03232022-1869.txt', 'malibucity_agenda__06222022-1919.txt', 'malibucity_agenda__07272022-1939.txt', 'malibucity_agenda__11102022-1995.txt']}, 'var_call_aogXkumn6FWeJlS4Tns9KpMW': 'file_storage/call_aogXkumn6FWeJlS4Tns9KpMW.json', 'var_call_j7cMOPCBCSfMLqHy0u076Bha': [{'filename': 'malibucity_agenda__06222022-1919.txt', 'Project_Name': 'Civic Center Way Improvements', 'updates': 'Updates: The contractor completed the project and Council accepted this project as'}, {'filename': 'malibucity_agenda__06222022-1919.txt', 'Project_Name': 'Civic Center Stormwater Diversion Structure', 'updates': 'Updates: The contractor has completed the storm drain improvements on Civic Center'}, {'filename': 'malibucity_agenda__06222022-1919.txt', 'Project_Name': '2021 Annual Street Maintenance', 'updates': 'Updates: This project included resurfacing Malibu Road, Broad Beach Road, Latigo'}]}

exec(code, env_args)
