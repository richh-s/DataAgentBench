code = """import json

# Load results from previous tool calls (file paths provided in variables)
path_docs = var_call_dziWdH68wzWWoRRglXmdYLQx
path_fund = var_call_VqvuxlAzlcifj1bcMkrjIDVw

with open(path_fund, 'r', encoding='utf-8') as f:
    funds = json.load(f)
with open(path_docs, 'r', encoding='utf-8') as f:
    docs = json.load(f)

keywords = ['fema', 'emergency']

# Collect from funding table where project name mentions FEMA or emergency
results = []
for rec in funds:
    pname = rec.get('Project_Name','')
    lname = pname.lower()
    if 'fema' in lname or 'emergency' in lname:
        try:
            amt = int(rec.get('Amount'))
        except Exception:
            amt = None
        results.append({'Project_Name': pname, 'Funding_Source': rec.get('Funding_Source'), 'Amount': amt, 'Status': None})

# From documents, find projects mentioned near keywords
for doc in docs:
    text = doc.get('text','')
    lines = text.splitlines()
    for i, line in enumerate(lines):
        low = line.lower()
        if any(k in low for k in keywords):
            # search up to 6 lines above for a title-like line
            title = None
            for j in range(max(0, i-6), i)[::-1]:
                cand = lines[j].strip()
                if not cand:
                    continue
                if len(cand) > 300:
                    continue
                # consider as title if contains common project words
                if any(w in cand.lower() for w in ['project', 'repairs', 'improvements', 'sirens', 'park', 'road', 'bridge', 'drain', 'culvert', 'slope', 'water', 'treatment']):
                    title = cand
                    break
            if not title:
                # fallback to short snippet
                snippet = ' '.join(l.strip() for l in lines[max(0,i-2):i+1] if l.strip())
                title = snippet
            # avoid duplicates
            if not any(r['Project_Name'].lower() == title.lower() for r in results):
                results.append({'Project_Name': title, 'Funding_Source': None, 'Amount': None, 'Status': None})

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_call_jWONQnnlxfAddtKc97l9A619': ['civic_docs'], 'var_call_kS6pRvnaONEfsjsY5YLZIDQR': ['Funding'], 'var_call_dziWdH68wzWWoRRglXmdYLQx': 'file_storage/call_dziWdH68wzWWoRRglXmdYLQx.json', 'var_call_VqvuxlAzlcifj1bcMkrjIDVw': 'file_storage/call_VqvuxlAzlcifj1bcMkrjIDVw.json'}

exec(code, env_args)
