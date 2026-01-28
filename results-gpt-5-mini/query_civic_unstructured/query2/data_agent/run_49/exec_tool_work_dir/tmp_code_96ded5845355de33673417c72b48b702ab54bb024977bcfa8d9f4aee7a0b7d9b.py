code = """import json
# Load the query results from storage keys
with open(var_call_hJ83xpCVHpFAd4XwO7rMoVWU, 'r') as f:
    funding_records = json.load(f)
with open(var_call_9yffPogOE7cNYUhKB0gTXbfX, 'r') as f:
    civic_docs_records = json.load(f)

# Normalize funding records and convert Amount to int
for r in funding_records:
    try:
        r['Amount'] = int(r['Amount'])
    except:
        try:
            r['Amount'] = int(float(r['Amount']))
        except:
            r['Amount'] = 0

# Define park-related keywords
keywords = ['park', 'playground', 'walkway', 'benches', 'shade structure', 'south walkway', 'playground', 'benches and arbors']

matched = []

for fr in funding_records:
    pname = fr['Project_Name']
    pname_l = pname.lower()
    if any(k in pname_l for k in keywords):
        # search in civic docs
        found = False
        for doc in civic_docs_records:
            text = doc.get('text','')
            text_l = text.lower()
            idx = text_l.find(pname_l)
            if idx != -1:
                window = text_l[max(0, idx-500): idx+500]
                if ('completed' in window or 'construction was completed' in window) and '2022' in window:
                    found = True
                    break
            else:
                # also search for shorter forms: if 'park' in pname, search for the main identifier words
                # e.g., if 'bluffs park' in pname, search for that
                # try searching for first 5 words of pname
                tokens = pname_l.split()
                for L in range(5,0,-1):
                    substr = ' '.join(tokens[:L])
                    if len(substr) < 4:
                        continue
                    idx2 = text_l.find(substr)
                    if idx2 != -1:
                        window = text_l[max(0, idx2-500): idx2+500]
                        if ('completed' in window or 'construction was completed' in window) and '2022' in window:
                            found = True
                            break
                if found:
                    break
        if found:
            matched.append({'Project_Name': pname, 'Amount': fr['Amount']})

# Compute total
total = sum(m['Amount'] for m in matched)

# Prepare result
result = {'total_funding': total, 'matched_projects': matched}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_tHgFkoya8kc8QzYHZ1skTygj': ['civic_docs'], 'var_call_4jBKp2LxJkXA76gvD4sYmt3W': ['Funding'], 'var_call_hJ83xpCVHpFAd4XwO7rMoVWU': 'file_storage/call_hJ83xpCVHpFAd4XwO7rMoVWU.json', 'var_call_9yffPogOE7cNYUhKB0gTXbfX': 'file_storage/call_9yffPogOE7cNYUhKB0gTXbfX.json'}

exec(code, env_args)
