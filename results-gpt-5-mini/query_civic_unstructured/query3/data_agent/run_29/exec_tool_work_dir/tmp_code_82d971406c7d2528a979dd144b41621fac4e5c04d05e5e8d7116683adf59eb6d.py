code = """import json

# Access storage-provided variables
path_civic = var_call_jzhQseUHxKXVBNdaUVsP8c9e
path_funding = var_call_Utur5J9BLQ3n16jKLtshjCae

with open(path_funding, 'r') as f:
    funding = json.load(f)
with open(path_civic, 'r') as f:
    civic_docs = json.load(f)

# Combine civic texts for searching
combined_texts = "\n---DOC---\n".join([d.get('text','') for d in civic_docs])
combined_lower = combined_texts.lower()

results = []

def clean_name(n):
    if not n:
        return n
    if '(' in n:
        return n.split('(')[0].strip()
    return n.strip()

def extract_status(snippet):
    s = snippet.lower()
    if 'under construction' in s or 'begin construction' in s or 'construction was' in s:
        return 'under construction'
    if 'complete design' in s or 'design phase' in s or 'design plans' in s or 'preliminary design' in s:
        return 'design'
    if 'completed' in s or 'notice of completion' in s or 'complete construction' in s:
        return 'completed'
    if 'not started' in s or 'identified' in s and 'not' in s:
        return 'not started'
    if 'awaiting' in s and 'fema' in s:
        return 'awaiting FEMA approval'
    return None

for rec in funding:
    pname = rec.get('Project_Name','')
    pname_clean = clean_name(pname)
    lname = pname.lower()
    selected = False
    status = None

    if 'fema' in lname or 'emergency' in lname:
        selected = True
        # try to find project name in civic docs
        idx = combined_lower.find(pname_clean.lower())
        if idx != -1:
            snippet = combined_texts[max(0, idx-200): idx+500]
            status = extract_status(snippet)
    else:
        if pname_clean and pname_clean.lower() in combined_lower:
            start_pos = combined_lower.find(pname_clean.lower())
            while start_pos != -1:
                start = max(0, start_pos-300)
                end = min(len(combined_lower), start_pos+300)
                window = combined_lower[start:end]
                if ('fema' in window) or ('emergency' in window) or ('caloes' in window):
                    selected = True
                    snippet = combined_texts[start:end]
                    status = extract_status(snippet)
                    break
                start_pos = combined_lower.find(pname_clean.lower(), start_pos+1)

    if selected:
        amt = rec.get('Amount')
        try:
            amt_v = int(amt)
        except:
            try:
                amt_v = int(float(amt))
            except:
                amt_v = None
        results.append({
            'Project_Name': pname,
            'Funding_Source': rec.get('Funding_Source'),
            'Amount': amt_v,
            'Status': status
        })

# deduplicate by Project_Name
seen = set()
unique_results = []
for r in results:
    if r['Project_Name'] not in seen:
        unique_results.append(r)
        seen.add(r['Project_Name'])

print("__RESULT__:")
print(json.dumps(unique_results))"""

env_args = {'var_call_jzhQseUHxKXVBNdaUVsP8c9e': 'file_storage/call_jzhQseUHxKXVBNdaUVsP8c9e.json', 'var_call_Utur5J9BLQ3n16jKLtshjCae': 'file_storage/call_Utur5J9BLQ3n16jKLtshjCae.json'}

exec(code, env_args)
