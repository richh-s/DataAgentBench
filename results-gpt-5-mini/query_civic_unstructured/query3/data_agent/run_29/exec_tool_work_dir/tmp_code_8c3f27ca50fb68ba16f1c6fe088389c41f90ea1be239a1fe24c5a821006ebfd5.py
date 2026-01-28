code = """import json

path_civic = var_call_jzhQseUHxKXVBNdaUVsP8c9e
path_funding = var_call_Utur5J9BLQ3n16jKLtshjCae

with open(path_funding, 'r') as f:
    funding = json.load(f)
with open(path_civic, 'r') as f:
    civic_docs = json.load(f)

# combine texts without escape sequences
sep = '---DOC---'
combined_texts = sep.join([d.get('text','') for d in civic_docs])
combined_lower = combined_texts.lower()

def clean_name(n):
    if not n:
        return n
    if '(' in n:
        return n.split('(')[0].strip()
    return n.strip()

def map_status(snippet):
    s = snippet.lower()
    if 'awaiting' in s and 'fema' in s:
        return 'awaiting FEMA approval'
    if 'under construction' in s or 'begin construction' in s or 'construction was' in s or 'begin construction:' in s:
        return 'under construction'
    if 'complete design' in s or 'design phase' in s or 'design plans' in s or 'preliminary design' in s:
        return 'design'
    if 'completed' in s or 'notice of completion' in s or 'complete construction' in s:
        return 'completed'
    if 'not started' in s or ('identified' in s and 'not' in s):
        return 'not started'
    return None

results = []
seen = set()

for rec in funding:
    pname = rec.get('Project_Name','')
    pname_clean = clean_name(pname)
    lname = pname.lower()
    selected = False
    status = None

    if 'fema' in lname or 'emergency' in lname:
        selected = True
        pos = combined_lower.find(pname_clean.lower())
        if pos != -1:
            start = max(0, pos-200)
            end = min(len(combined_lower), pos+500)
            snippet = combined_texts[start:end]
            status = map_status(snippet)
    else:
        if pname_clean and pname_clean.lower() in combined_lower:
            start_pos = combined_lower.find(pname_clean.lower())
            while start_pos != -1:
                start = max(0, start_pos-300)
                end = min(len(combined_lower), start_pos+300)
                window = combined_lower[start:end]
                if 'fema' in window or 'emergency' in window or 'caloes' in window:
                    selected = True
                    snippet = combined_texts[start:end]
                    status = map_status(snippet)
                    break
                start_pos = combined_lower.find(pname_clean.lower(), start_pos+1)

    if selected and pname not in seen:
        seen.add(pname)
        try:
            amt_v = int(rec.get('Amount'))
        except:
            try:
                amt_v = int(float(rec.get('Amount')))
            except:
                amt_v = None
        results.append({'Project_Name': pname, 'Funding_Source': rec.get('Funding_Source'), 'Amount': amt_v, 'Status': status})

print('__RESULT__:')
print(json.dumps(results))"""

env_args = {'var_call_jzhQseUHxKXVBNdaUVsP8c9e': 'file_storage/call_jzhQseUHxKXVBNdaUVsP8c9e.json', 'var_call_Utur5J9BLQ3n16jKLtshjCae': 'file_storage/call_Utur5J9BLQ3n16jKLtshjCae.json', 'var_call_Sd1f9jZeO7nq1ZQwOV8tkZ9m': {'var_call_jzhQseUHxKXVBNdaUVsP8c9e': 'str', 'var_call_Utur5J9BLQ3n16jKLtshjCae': 'str'}}

exec(code, env_args)
