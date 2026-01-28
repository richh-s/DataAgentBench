code = """import json, re, pandas as pd

cd = var_call_rrITK0lUpo5usLSikqQouxYp
if isinstance(cd, str):
    with open(cd, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = cd

ft = var_call_PSEZSqWmIRPvYkhDRIsKOJ2Z
if isinstance(ft, str):
    with open(ft, 'r') as f:
        funding_totals = json.load(f)
else:
    funding_totals = ft

fund_df = pd.DataFrame(funding_totals)
if not fund_df.empty:
    fund_df['total_amount'] = pd.to_numeric(fund_df['total_amount'])

# Extract disaster projects and their start indications from disaster sections

disaster_projects = {}  # name -> set(start_strings)

for doc in civic_docs:
    text = doc.get('text', '') or ''
    low = text.lower()
    idx = low.find('disaster recovery projects')
    if idx == -1:
        continue
    sec = text[idx:]
    lines = [ln.strip() for ln in sec.splitlines()]

    for i, ln in enumerate(lines):
        if not ln or len(ln) > 140:
            continue
        lnl = ln.lower()
        if lnl in [
            'disaster recovery projects (design)',
            'disaster recovery projects (construction)',
            'disaster recovery projects (not started)',
            'disaster recovery projects'
        ]:
            continue
        if 'updates' in lnl or 'project schedule' in lnl or 'project description' in lnl:
            continue
        if ln.startswith('(') or ln.startswith('cid:'):
            continue
        if re.match(r'^(to:|prepared by:|approved by:|date prepared:|meeting date:|subject:|recommended action:|discussion:)$', lnl):
            continue
        if re.match(r'^[\-\u2022\*]', ln):
            continue
        if re.search(r'[A-Za-z]', ln) and (ln[0].isalpha() or ln[0].isdigit()):
            if len(ln.split()) < 2 and '(' not in ln:
                continue

            window_lines = lines[i:i+18]
            window = '\n'.join(window_lines)
            starts = set()

            for m in re.finditer(r'(Begin Construction|Start(?: Date)?|Begin)\s*:\s*([^\n]+)', window, flags=re.IGNORECASE):
                starts.add(m.group(2).strip())

            for wln in window_lines:
                if '202' in wln and ':' in wln:
                    rhs = wln.split(':', 1)[1].strip()
                    if rhs:
                        starts.add(rhs)

            if starts:
                disaster_projects.setdefault(ln, set()).update(starts)

projects_2022 = [name for name, starts in disaster_projects.items() if any('2022' in s for s in starts)]

sel_fund = fund_df[fund_df['Project_Name'].isin(projects_2022)].copy() if not fund_df.empty else pd.DataFrame(columns=['Project_Name','total_amount'])

result = {
    'total_funding': int(sel_fund['total_amount'].sum()) if not sel_fund.empty else 0,
    'project_count': int(sel_fund.shape[0]),
    'projects': sel_fund.sort_values('total_amount', ascending=False).to_dict(orient='records')
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_RvZ50pS5WKtMq9Ygsv93soeX': ['Funding'], 'var_call_lstHaO2T1fNcM1AkXqdQUIcQ': ['civic_docs'], 'var_call_rrITK0lUpo5usLSikqQouxYp': 'file_storage/call_rrITK0lUpo5usLSikqQouxYp.json', 'var_call_PSEZSqWmIRPvYkhDRIsKOJ2Z': 'file_storage/call_PSEZSqWmIRPvYkhDRIsKOJ2Z.json'}

exec(code, env_args)
