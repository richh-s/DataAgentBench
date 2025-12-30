code = """import json, pandas as pd

funding = var_call_urFTCKneRrxyFg7X8D3jwQJD
if isinstance(funding, str):
    with open(funding, 'r') as f:
        funding = json.load(f)

fund_df = pd.DataFrame(funding)
fund_df['Amount'] = fund_df['Amount'].astype(int)

mask = fund_df['Project_Name'].str.contains('emergency', case=False, na=False) | fund_df['Project_Name'].str.contains('FEMA', case=False, na=False)
rel_fund = fund_df.loc[mask, ['Project_Name', 'Funding_Source', 'Amount']]

civic = var_call_LLocYwsCtuRkIli6s5Eo0qur
if isinstance(civic, str):
    with open(civic, 'r') as f:
        civic = json.load(f)

texts = [d['text'] for d in civic]

project_status = {}

for text in texts:
    lines = text.split('\n')
    for i, line in enumerate(lines):
        low = line.lower()
        if ('emergency' in low or 'fema' in low) and len(line.strip()) > 0:
            context = '\n'.join(lines[max(0, i-5):min(len(lines, i+6))]).lower()
            status = None
            if 'completed' in context:
                status = 'completed'
            elif 'under construction' in context or 'begin construction' in context or 'construction' in context:
                status = 'design'
            elif 'not started' in context or 'identified' in context:
                status = 'not started'
            pname = line.strip()
            if status:
                project_status.setdefault(pname, set()).add(status)

results = []
for _, row in rel_fund.iterrows():
    pname = row['Project_Name']
    status_found = None
    for ptext, stats in project_status.items():
        if pname.lower() in ptext.lower() or ptext.lower() in pname.lower():
            if 'completed' in stats:
                status_found = 'completed'
            elif 'design' in stats:
                status_found = 'design'
            elif 'not started' in stats:
                status_found = 'not started'
            break
    results.append({
        'Project_Name': pname,
        'Funding_Source': row['Funding_Source'],
        'Amount': int(row['Amount']),
        'Status': status_found if status_found else 'unknown'
    })

out = json.dumps(results)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_urFTCKneRrxyFg7X8D3jwQJD': 'file_storage/call_urFTCKneRrxyFg7X8D3jwQJD.json', 'var_call_LLocYwsCtuRkIli6s5Eo0qur': 'file_storage/call_LLocYwsCtuRkIli6s5Eo0qur.json'}

exec(code, env_args)
