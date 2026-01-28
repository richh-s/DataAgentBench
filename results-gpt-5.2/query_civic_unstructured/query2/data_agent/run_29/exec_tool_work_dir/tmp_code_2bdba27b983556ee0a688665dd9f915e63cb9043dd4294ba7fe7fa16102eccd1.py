code = """import json, re

def load_json_maybe(path_or_obj):
    if isinstance(path_or_obj, str) and path_or_obj.endswith('.json'):
        with open(path_or_obj, 'r', encoding='utf-8') as f:
            return json.load(f)
    return path_or_obj

docs = load_json_maybe(var_call_ZDgWY667UVItAA7xwUug9yEp)

# find lines with 'completed' and 2022, plus preceding non-empty line as candidate project
hits = []
for d in docs:
    lines = [ln.rstrip() for ln in (d.get('text','') or '').splitlines()]
    for i, ln in enumerate(lines):
        if re.search(r'completed', ln, flags=re.I) and '2022' in ln:
            # find prev non-empty
            j=i-1
            while j>=0 and not lines[j].strip():
                j-=1
            prev = lines[j].strip() if j>=0 else None
            hits.append({'filename': d.get('filename'), 'prev_line': prev, 'line': ln.strip()})

print('__RESULT__:')
print(json.dumps(hits[:50]))"""

env_args = {'var_call_UofbwvMTW9eL8ESjJ7gV8qC2': ['Funding'], 'var_call_BTYCgoMO7sRs5ron6p1T0tv6': ['civic_docs'], 'var_call_Bj4yPTTHhPADOYlzfQxBnD8h': 'file_storage/call_Bj4yPTTHhPADOYlzfQxBnD8h.json', 'var_call_ijXcqP4PgqQoWbsuEISz7Brt': 'file_storage/call_ijXcqP4PgqQoWbsuEISz7Brt.json', 'var_call_NyHUPX899qUjNuhaOSB6OKnM': {'park_related_completed_2022_projects': [], 'total_funding_usd': 0}, 'var_call_ZxUhaAI37K4GBm8xBBT0DT9b': 'file_storage/call_ZxUhaAI37K4GBm8xBBT0DT9b.json', 'var_call_3bsur2ta9hzW4Gt1UYiJ1C3X': {'identified_completed_2022_lines': [], 'park_related_completed_2022_projects': [], 'matched_funding_rows': [], 'total_funding_usd': 0}, 'var_call_ZDgWY667UVItAA7xwUug9yEp': 'file_storage/call_ZDgWY667UVItAA7xwUug9yEp.json', 'var_call_IlHWmDeGRq93m4LWLFxHCtGc': {'projects': [], 'total_funding_usd': 0}}

exec(code, env_args)
