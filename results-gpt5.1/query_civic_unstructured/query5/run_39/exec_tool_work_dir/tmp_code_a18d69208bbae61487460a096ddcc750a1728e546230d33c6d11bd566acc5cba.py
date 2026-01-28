code = """import json, pandas as pd, re

funding = pd.DataFrame(var_call_LJd4H09XkUfEbHSFSvYSR73l)

# Inspect types
for col in funding.columns:
    funding[col] = funding[col].astype(str)

path_docs = var_call_O5EfH7EZdYFhberNDh3qxvUv
with open(path_docs, 'r') as f:
    docs = json.load(f)
texts = ' '.join(d['text'] for d in docs)

mask = funding['Project_Name'].str.contains('(FEMA', case=False, regex=False) | \
       funding['Project_Name'].str.contains('(CalOES', case=False, regex=False) | \
       funding['Project_Name'].str.contains('(CalJPIA', case=False, regex=False)

fund_dis = funding[mask].copy()

def started_2022(name):
    base = re.sub(r"\s*\(.*?\)", "", name).strip()
    pattern = re.escape(base)
    found = False
    for m in re.finditer(pattern, texts):
        window = texts[max(0, m.start()-50): m.end()+50]
        if '2022' in window:
            return True
    return False

fund_dis['started_2022'] = fund_dis['Project_Name'].apply(started_2022)
sub = fund_dis[fund_dis['started_2022']].copy()
sub['Amount'] = sub['Amount'].astype(int)

total = int(sub['Amount'].sum())

result = json.dumps({"total": total})
print("__RESULT__:")
print(result)"""

env_args = {'var_call_O5EfH7EZdYFhberNDh3qxvUv': 'file_storage/call_O5EfH7EZdYFhberNDh3qxvUv.json', 'var_call_LJd4H09XkUfEbHSFSvYSR73l': 'file_storage/call_LJd4H09XkUfEbHSFSvYSR73l.json'}

exec(code, env_args)
