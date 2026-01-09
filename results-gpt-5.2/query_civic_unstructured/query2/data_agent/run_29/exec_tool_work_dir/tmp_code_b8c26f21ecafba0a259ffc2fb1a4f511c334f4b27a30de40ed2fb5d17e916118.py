code = """import json, re, pandas as pd

def load_json_maybe(path_or_obj):
    if isinstance(path_or_obj, str) and path_or_obj.endswith('.json'):
        with open(path_or_obj, 'r', encoding='utf-8') as f:
            return json.load(f)
    return path_or_obj

docs = load_json_maybe(var_call_ZDgWY667UVItAA7xwUug9yEp)
fund = load_json_maybe(var_call_ijXcqP4PgqQoWbsuEISz7Brt)

park_completed_2022 = set()

for d in docs:
    lines = [ln.strip() for ln in (d.get('text','') or '').splitlines()]
    current = None
    for ln in lines:
        if not ln:
            continue
        # detect project names as standalone lines (common in status reports)
        if (len(ln) <= 120 and ':' not in ln and not re.search(r'\b(Updates|Project Schedule|Estimated Schedule|Project Description)\b', ln, flags=re.I)
            and re.search(r'[A-Za-z]', ln) and len(ln.split())>=2
            and not re.match(r'^(Public Works|Agenda|To:|Prepared by:|Approved by:|Date prepared:|Meeting date:|Subject:|RECOMMENDED ACTION|DISCUSSION|Capital Improvement Projects|Disaster Recovery Projects|Page\s+\d+|Agenda Item)', ln, flags=re.I)):
            current = ln
        if current and re.search(r'construction\s+was\s+completed', ln, flags=re.I) and '2022' in ln:
            if re.search(r'\b(park|playground|skate|bluffs)\b', current, flags=re.I):
                park_completed_2022.add(current)

fund_df = pd.DataFrame(fund)
fund_df['total_amount'] = pd.to_numeric(fund_df['total_amount'], errors='coerce').fillna(0).astype(int)

total = int(fund_df[fund_df['Project_Name'].isin(sorted(park_completed_2022))]['total_amount'].sum())

print('__RESULT__:')
print(json.dumps({'projects': sorted(park_completed_2022), 'total_funding_usd': total}))"""

env_args = {'var_call_UofbwvMTW9eL8ESjJ7gV8qC2': ['Funding'], 'var_call_BTYCgoMO7sRs5ron6p1T0tv6': ['civic_docs'], 'var_call_Bj4yPTTHhPADOYlzfQxBnD8h': 'file_storage/call_Bj4yPTTHhPADOYlzfQxBnD8h.json', 'var_call_ijXcqP4PgqQoWbsuEISz7Brt': 'file_storage/call_ijXcqP4PgqQoWbsuEISz7Brt.json', 'var_call_NyHUPX899qUjNuhaOSB6OKnM': {'park_related_completed_2022_projects': [], 'total_funding_usd': 0}, 'var_call_ZxUhaAI37K4GBm8xBBT0DT9b': 'file_storage/call_ZxUhaAI37K4GBm8xBBT0DT9b.json', 'var_call_3bsur2ta9hzW4Gt1UYiJ1C3X': {'identified_completed_2022_lines': [], 'park_related_completed_2022_projects': [], 'matched_funding_rows': [], 'total_funding_usd': 0}, 'var_call_ZDgWY667UVItAA7xwUug9yEp': 'file_storage/call_ZDgWY667UVItAA7xwUug9yEp.json'}

exec(code, env_args)
