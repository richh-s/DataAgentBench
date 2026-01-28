code = """import re, json, pandas as pd
from pathlib import Path
import json as jsonlib

path_civic = Path(var_call_ozGFs2YWIogZavsxSzAQcEfP)
with path_civic.open() as f:
    civic_docs = jsonlib.load(f)

# define simple patterns to identify park-related project lines
park_pattern = re.compile('park', re.IGNORECASE)

projects = []
for doc in civic_docs:
    text = doc.get('text', '')
    lines = [l.strip() for l in text.split('\n') if l.strip()]
    for i, line in enumerate(lines):
        if park_pattern.search(line):
            window_lines = lines[max(0, i-5): i+10]
            window = '\n'.join(window_lines)
            status = None
            for s in ['completed', 'design', 'not started']:
                if re.search(r'\b' + s + r'\b', window, re.IGNORECASE):
                    status = s
                    break
            et_match = re.search(r'completed[^\n]*?(20\d{2}[^\n]*)', window, re.IGNORECASE)
            et = et_match.group(1).strip() if et_match else ''
            projects.append({'Project_Name': line, 'status': status, 'st': '', 'et': et, 'topic': 'park'})

park_completed_2022 = [p for p in projects if p.get('status') == 'completed' and '2022' in p.get('et', '')]

funding = var_call_bMy6q8Z1OwqBl8K2WIP50ND6
fund_df = pd.DataFrame(funding)
fund_df['Amount'] = fund_df['Amount'].astype(int)

matched_amounts = []
for p in park_completed_2022:
    name = p['Project_Name']
    mask = fund_df['Project_Name'].str.contains(re.escape(name), case=False, na=False) | fund_df['Project_Name'].apply(lambda x: name.lower() in x.lower())
    sub = fund_df[mask]
    if not sub.empty:
        matched_amounts.extend(sub['Amount'].tolist())

total_funding = int(sum(matched_amounts)) if matched_amounts else 0

result = {'total_funding_park_completed_2022': total_funding}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_ozGFs2YWIogZavsxSzAQcEfP': 'file_storage/call_ozGFs2YWIogZavsxSzAQcEfP.json', 'var_call_bMy6q8Z1OwqBl8K2WIP50ND6': 'file_storage/call_bMy6q8Z1OwqBl8K2WIP50ND6.json'}

exec(code, env_args)
