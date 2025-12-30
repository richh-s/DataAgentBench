code = """import json, re, pandas as pd

with open(var_call_GQohpNwzKQfcLQDDg2YyH4le, 'r') as f:
    civic_docs = json.load(f)

funding_records = var_call_wQUbrlN0U1Q5DEkEdeSRiWNL

pattern = r'(FEMA|CalOES|CalJPIA|Disaster|Recovery|Fire)'
DISASTER_PATTERN = re.compile(pattern, re.IGNORECASE)

project_infos = {}
for doc in civic_docs:
    text = doc.get('text', '')
    for line in text.split('\n'):
        line = line.strip()
        if not line:
            continue
        m = re.match(r'20\d{2}.*', line)
        if m:
            pname = m.group(0).strip()
            if pname not in project_infos:
                project_infos[pname] = {'Project_Name': pname}

fund_df = pd.DataFrame(funding_records)
fund_df['Amount'] = fund_df['Amount'].astype(int)

fund_df['is_disaster'] = fund_df['Project_Name'].str.contains(DISASTER_PATTERN)

civic_project_names = list(project_infos.keys())

def started_2022(name):
    if '2022' in name:
        return True
    for cp in civic_project_names:
        if '2022' in cp and cp.split('2022')[-1].strip() and cp.split('2022')[-1].strip() in name:
            return True
    return False

fund_df['started_2022'] = fund_df['Project_Name'].apply(started_2022)

mask = fund_df['is_disaster'] & fund_df['started_2022']
subset = fund_df[mask]

total_funding = int(subset['Amount'].sum())

result = {
    'total_disaster_funding_started_2022': total_funding,
    'matching_projects': subset[['Funding_ID','Project_Name','Amount']].to_dict(orient='records')
}

out = json.dumps(result)
print('__RESULT__:')
print(out)"""

env_args = {'var_call_GQohpNwzKQfcLQDDg2YyH4le': 'file_storage/call_GQohpNwzKQfcLQDDg2YyH4le.json', 'var_call_wQUbrlN0U1Q5DEkEdeSRiWNL': 'file_storage/call_wQUbrlN0U1Q5DEkEdeSRiWNL.json', 'var_call_gbaRxp9EGTyTfTp2agElyMEb': ['civic_docs'], 'var_call_sfQKx7owcYhdd8ofvMSKpKEG': ['Funding']}

exec(code, env_args)
