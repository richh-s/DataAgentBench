code = """import json, re, pandas as pd

def load_json_maybe(path_or_obj):
    if isinstance(path_or_obj, str) and path_or_obj.endswith('.json'):
        with open(path_or_obj, 'r', encoding='utf-8') as f:
            return json.load(f)
    return path_or_obj

docs = load_json_maybe(var_call_Bj4yPTTHhPADOYlzfQxBnD8h)
fund = load_json_maybe(var_call_ijXcqP4PgqQoWbsuEISz7Brt)

# Build set of projects that are park-related AND completed in 2022
park_completed_2022 = set()

# Patterns to extract a project header line (assume line by itself, title case-ish)
# We'll iterate line-by-line and track current project name.
for d in docs:
    text = d.get('text','') or ''
    lines = [ln.strip() for ln in text.splitlines()]
    current_project = None
    for ln in lines:
        if not ln:
            continue
        # identify likely project name line: not too long, not bullet markers, not headings
        if len(ln) <= 90 and not re.match(r'^(\(cid:|Page\s+\d+|Agenda\s+Item|Public\s+Works|Capital\s+Improvement|Disaster\s+Recovery|RECOMMENDED\s+ACTION|DISCUSSION|To:|Prepared by:|Approved by:|Date prepared:|Meeting date:|Subject:)', ln, flags=re.I):
            # project names often contain keywords and no colon
            if ':' not in ln and not re.search(r'\bUpdates\b|\bProject Schedule\b|\bEstimated Schedule\b|\bProject Description\b', ln, flags=re.I):
                # heuristic: contains at least one letter and not all caps long
                if re.search(r'[A-Za-z]', ln) and (len(ln.split())>=2):
                    # accept as project if next lines include Updates/Schedule etc; but we set current and can overwrite
                    current_project = ln
        # Check for completion mention within updates lines
        if current_project:
            if re.search(r'\bcompleted\b', ln, flags=re.I):
                # must mention 2022 somewhere in same line
                if '2022' in ln:
                    # park-related? either project name has park/playground/bluffs etc OR nearby mentions park keyword
                    context = (current_project + ' ' + ln).lower()
                    if any(k in context for k in ['park','playground','bluffs']):
                        park_completed_2022.add(current_project)

# Also catch cases where completion date in separate line e.g. "Construction was completed November 2022." already handled.

# Map funding by project name
fund_df = pd.DataFrame(fund)
if fund_df.empty:
    total = 0
else:
    fund_df['total_amount'] = pd.to_numeric(fund_df['total_amount'], errors='coerce').fillna(0).astype(int)
    total = int(fund_df[fund_df['Project_Name'].isin(sorted(park_completed_2022))]['total_amount'].sum())

out = {
    'park_related_completed_2022_projects': sorted(park_completed_2022),
    'total_funding_usd': total
}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_UofbwvMTW9eL8ESjJ7gV8qC2': ['Funding'], 'var_call_BTYCgoMO7sRs5ron6p1T0tv6': ['civic_docs'], 'var_call_Bj4yPTTHhPADOYlzfQxBnD8h': 'file_storage/call_Bj4yPTTHhPADOYlzfQxBnD8h.json', 'var_call_ijXcqP4PgqQoWbsuEISz7Brt': 'file_storage/call_ijXcqP4PgqQoWbsuEISz7Brt.json'}

exec(code, env_args)
