code = """import json
from pathlib import Path

# Load data from storage-provided file paths
civic_docs_path = var_call_GTFsELpkrFtLopFqUsIf2Xbg
funding_path = var_call_DCm5L3Mh2rqiovWnbQdaKUgV

with open(civic_docs_path, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)
with open(funding_path, 'r', encoding='utf-8') as f:
    funding = json.load(f)

# Normalize texts
for doc in civic_docs:
    doc['text_lower'] = doc['text'].lower()

# Define park-related keywords for funding project names
park_keywords = ['park', 'playground', 'bluffs', 'walkway', 'point dume', 'trancas canyon', 'legacy park', 'malibu park', 'playground']

# Function to check if project is mentioned as completed in 2022 in civic docs
def is_completed_2022(project_name):
    pname = project_name.lower()
    for doc in civic_docs:
        text = doc['text_lower']
        if pname in text:
            # check nearby for completed and 2022
            # simple heuristic: check within 500 chars of project occurrence for 'complete' and '2022'
            start = 0
            while True:
                idx = text.find(pname, start)
                if idx == -1:
                    break
                window_start = max(0, idx-500)
                window_end = min(len(text), idx+500)
                window = text[window_start:window_end]
                if ('complete' in window or 'construction was completed' in window or 'notice of completion' in window) and '2022' in window:
                    return True
                start = idx + len(pname)
            # fallback: if doc contains phrase 'construction was completed' and '2022' and project name anywhere in doc => True
            if 'construction was completed' in text and '2022' in text:
                return True
            if 'completed' in text and '2022' in text and ('park' in pname or any(k in text for k in ['park', 'playground','bluffs','walkway','point dume','trancas'])):
                return True
    return False

# Find funding records that are park-related and completed in 2022
matched_records = []
for rec in funding:
    pname = rec.get('Project_Name','')
    lname = pname.lower()
    if any(k in lname for k in park_keywords):
        if is_completed_2022(pname):
            # convert amount to int
            try:
                amt = int(rec.get('Amount') or 0)
            except:
                try:
                    amt = int(float(rec.get('Amount')))
                except:
                    amt = 0
            matched_records.append({'Project_Name': pname, 'Amount': amt})

# Compute total
total = sum(r['Amount'] for r in matched_records)

# Prepare output
output = {
    'matched_projects': matched_records,
    'total_funding': total
}

import json
print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_EQKbGbmn6c2rRFIGBDFJoots': ['civic_docs'], 'var_call_mI5na0Wa8XKWa0q021u1lYCF': ['Funding'], 'var_call_GTFsELpkrFtLopFqUsIf2Xbg': 'file_storage/call_GTFsELpkrFtLopFqUsIf2Xbg.json', 'var_call_DCm5L3Mh2rqiovWnbQdaKUgV': 'file_storage/call_DCm5L3Mh2rqiovWnbQdaKUgV.json'}

exec(code, env_args)
