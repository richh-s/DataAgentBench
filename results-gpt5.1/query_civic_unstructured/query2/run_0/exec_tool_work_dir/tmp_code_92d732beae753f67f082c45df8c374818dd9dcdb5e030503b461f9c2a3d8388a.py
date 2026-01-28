code = """import re, json, pandas as pd
from pathlib import Path

# Load full civic docs
path_civic = Path(var_call_ozGFs2YWIogZavsxSzAQcEfP)
import json as jsonlib
with path_civic.open() as f:
    civic_docs = jsonlib.load(f)

# Very rough project extraction: split on double newlines and keep lines that look like project titles
project_patterns = [
    re.compile(r"park", re.I),
]

projects = []
for doc in civic_docs:
    text = doc.get('text','')
    # crude split
    lines = [l.strip() for l in text.split('\n') if l.strip()]
    for i, line in enumerate(lines):
        if any(p.search(line) for p in project_patterns):
            # look for status and dates in nearby lines
            window = '\n'.join(lines[max(0,i-5):i+10])
            status = None
            for s in ['completed','design','not started']:
                if re.search(r"\b"+s+r"\b", window, re.I):
                    status = s
                    break
            # end time: simple search for 'Construction was completed, <Month> 2022' etc
            et_match = re.search(r"completed[^\n]*?(20\d{2}[^\n]*)", window, re.I)
            et = et_match.group(1).strip() if et_match else ''
            st = ''
            topic = 'park'
            projects.append({'Project_Name': line, 'status': status, 'st': st, 'et': et, 'topic': topic})

# Filter park projects completed in 2022
park_completed_2022 = [p for p in projects if p['status']=='completed' and '2022' in p.get('et','')]

# Now load funding table
funding = var_call_bMy6q8Z1OwqBl8K2WIP50ND6

# Turn into DataFrame
fund_df = pd.DataFrame(funding)
fund_df['Amount'] = fund_df['Amount'].astype(int)

# Try to match projects by name using simple containment (since title lines should contain official names)
matched_amounts = []
for p in park_completed_2022:
    name = p['Project_Name']
    # find rows where Project_Name is substring of or contained in
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
