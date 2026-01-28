code = """import json

# Load the civic docs query result and funding table result from storage variables
with open(var_call_Vv9yG18KzmVPqSRthrZuJ0Ij, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)
with open(var_call_JbnbYUikoZOZIidJW2h5THqW, 'r', encoding='utf-8') as f:
    funding = json.load(f)

# Helper: normalize
def norm(s):
    return s.lower()

# Define park-related keywords to filter funding table and to check in docs
park_keywords = ['park', 'playground', 'walkway', 'shade', 'bluffs', 'point dume', 'legacy park', 'malibu park', 'trancas canyon', 'trancas']

# Build a single string of all civic texts for searching, but also keep per-doc
all_texts = [doc.get('text','') for doc in civic_docs]

matched = []

for rec in funding:
    pname = rec.get('Project_Name','')
    pname_l = norm(pname)
    # Quick filter: project name contains any park keyword
    if any(k in pname_l for k in park_keywords):
        # Search in civic docs for evidence of completion in 2022
        found = False
        for text in all_texts:
            tl = norm(text)
            if pname_l in tl and 'completed' in tl and '2022' in tl:
                found = True
                break
            # Also check proximity: if project short name words appear near 'completed' and '2022'
            # Check if project short tokens each appear within 200 chars of 'completed' and '2022'
            if 'completed' in tl and '2022' in tl:
                # find indices
                try:
                    idx_completed = tl.index('completed')
                    idx_2022 = tl.index('2022')
                except ValueError:
                    idx_completed = -1
                    idx_2022 = -1
                # Check if any token of project name appears within 200 chars of either
                tokens = [t for t in pname_l.split() if len(t)>3]
                for tok in tokens:
                    if tok in tl:
                        idx_tok = tl.index(tok)
                        if (abs(idx_tok - idx_completed) < 300) or (abs(idx_tok - idx_2022) < 300):
                            found = True
                            break
                if found:
                    break
        if found:
            try:
                amt = int(rec.get('Amount') )
            except:
                try:
                    amt = int(float(rec.get('Amount')))
                except:
                    amt = 0
            matched.append({
                'Funding_ID': rec.get('Funding_ID'),
                'Project_Name': rec.get('Project_Name'),
                'Amount': amt
            })

# Sum amounts
total = sum(r['Amount'] for r in matched)

# Prepare output
out = {
    'total_funding_park_projects_completed_in_2022': total,
    'matched_records': matched
}

print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_Vv9yG18KzmVPqSRthrZuJ0Ij': 'file_storage/call_Vv9yG18KzmVPqSRthrZuJ0Ij.json', 'var_call_GWi5yi94rjIbOCAx4Jperl21': ['Funding'], 'var_call_JbnbYUikoZOZIidJW2h5THqW': 'file_storage/call_JbnbYUikoZOZIidJW2h5THqW.json'}

exec(code, env_args)
