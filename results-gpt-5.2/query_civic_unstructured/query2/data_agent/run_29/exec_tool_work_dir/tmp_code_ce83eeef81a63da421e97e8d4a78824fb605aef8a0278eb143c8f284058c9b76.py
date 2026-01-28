code = """import json, re, pandas as pd

def load_json_maybe(path_or_obj):
    if isinstance(path_or_obj, str) and path_or_obj.endswith('.json'):
        with open(path_or_obj, 'r', encoding='utf-8') as f:
            return json.load(f)
    return path_or_obj

docs = load_json_maybe(var_call_ZDgWY667UVItAA7xwUug9yEp)
fund = load_json_maybe(var_call_ijXcqP4PgqQoWbsuEISz7Brt)

park_projects_completed_2022 = set()

for d in docs:
    lines = [ln.rstrip() for ln in (d.get('text','') or '').splitlines()]
    for i, ln in enumerate(lines):
        if re.search(r'construction\s+was\s+completed', ln, flags=re.I) and '2022' in ln:
            # find nearest previous non-bullet line as project name
            j=i-1
            while j>=0:
                prev = lines[j].strip()
                if prev and not prev.startswith('(') and ':' not in prev and len(prev)<=120:
                    proj = prev
                    break
                j-=1
            else:
                continue
            if re.search(r'\b(park|playground|skate|bluffs)\b', proj, flags=re.I):
                park_projects_completed_2022.add(proj)

fund_df = pd.DataFrame(fund)
fund_df['total_amount'] = pd.to_numeric(fund_df['total_amount'], errors='coerce').fillna(0).astype(int)
matched = fund_df[fund_df['Project_Name'].isin(sorted(park_projects_completed_2022))]

total = int(matched['total_amount'].sum())

print('__RESULT__:')
print(json.dumps({'projects': sorted(park_projects_completed_2022), 'total_funding_usd': total}))"""

env_args = {'var_call_UofbwvMTW9eL8ESjJ7gV8qC2': ['Funding'], 'var_call_BTYCgoMO7sRs5ron6p1T0tv6': ['civic_docs'], 'var_call_Bj4yPTTHhPADOYlzfQxBnD8h': 'file_storage/call_Bj4yPTTHhPADOYlzfQxBnD8h.json', 'var_call_ijXcqP4PgqQoWbsuEISz7Brt': 'file_storage/call_ijXcqP4PgqQoWbsuEISz7Brt.json', 'var_call_NyHUPX899qUjNuhaOSB6OKnM': {'park_related_completed_2022_projects': [], 'total_funding_usd': 0}, 'var_call_ZxUhaAI37K4GBm8xBBT0DT9b': 'file_storage/call_ZxUhaAI37K4GBm8xBBT0DT9b.json', 'var_call_3bsur2ta9hzW4Gt1UYiJ1C3X': {'identified_completed_2022_lines': [], 'park_related_completed_2022_projects': [], 'matched_funding_rows': [], 'total_funding_usd': 0}, 'var_call_ZDgWY667UVItAA7xwUug9yEp': 'file_storage/call_ZDgWY667UVItAA7xwUug9yEp.json', 'var_call_IlHWmDeGRq93m4LWLFxHCtGc': {'projects': [], 'total_funding_usd': 0}, 'var_call_R1FBCXcfWiwJ3xSoX5zKauOV': [{'filename': 'malibucity_agenda_03222023-2060.txt', 'prev_line': 'Bluffs Park Shade Structure', 'line': '(cid:190) Updates: Construction was completed November 2022. Notice of completion'}, {'filename': 'malibucity_agenda_03222023-2060.txt', 'prev_line': '(cid:190) Updates:', 'line': '(cid:131) Construction was completed, November 2022'}, {'filename': 'malibucity_agenda_03222023-2060.txt', 'prev_line': '(cid:190) Updates:', 'line': '(cid:131) Construction was completed, November 2022'}, {'filename': 'malibucity_agenda__01262022-1835.txt', 'prev_line': 'the past several months to complete the engineering work, and the final', 'line': 'draft plans are expected to be completed in early 2022. The Planning'}, {'filename': 'malibucity_agenda__01262022-1835.txt', 'prev_line': '(cid:131) The City has hired a consultant to design this project. The design has', 'line': 'started and is anticipated to be completed by the Spring of 2022.'}, {'filename': 'malibucity_agenda__03232022-1869.txt', 'prev_line': 'the past several months to complete the engineering work, and the final', 'line': 'draft plans are expected to be completed in early 2022. The Planning'}, {'filename': 'malibucity_agenda__03232022-1869.txt', 'prev_line': '(cid:131) The project design has begun and preliminary design should be', 'line': 'completed by Spring 2022.'}, {'filename': 'malibucity_agenda__06222022-1919.txt', 'prev_line': 'the past several months to complete the engineering work, and the final', 'line': 'draft plans are expected to be completed in Spring 2022. The Planning'}, {'filename': 'malibucity_agenda__06282023-2116.txt', 'prev_line': '(cid:190) Updates:', 'line': '(cid:131) Construction was completed November 2022.'}, {'filename': 'malibucity_agenda__06282023-2116.txt', 'prev_line': '(cid:190) Updates:', 'line': '(cid:131) Construction was completed, November 2022'}, {'filename': 'malibucity_agenda__06282023-2116.txt', 'prev_line': '(cid:190) Updates:', 'line': '(cid:131) Construction was completed November 2022'}, {'filename': 'malibucity_agenda__07272022-1939.txt', 'prev_line': 'the past several months to complete the engineering work, and the final', 'line': 'draft plans are expected to be completed in Spring 2022. The Planning'}, {'filename': 'malibucity_agenda__11102022-1995.txt', 'prev_line': 'the past several months to complete the engineering work, and the final', 'line': 'draft plans are expected to be completed in Winter 2022/23. The'}]}

exec(code, env_args)
