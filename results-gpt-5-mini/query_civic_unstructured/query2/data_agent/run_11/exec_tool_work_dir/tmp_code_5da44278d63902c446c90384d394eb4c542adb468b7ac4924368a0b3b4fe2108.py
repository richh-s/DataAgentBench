code = """import json, re

# Load data from storage variables (file paths)
with open(var_call_FA7KkPgziK2Q90TPgVoTXk32, 'r', encoding='utf-8') as f:
    funding = json.load(f)
with open(var_call_mka5UEs3QWagkOJUBTVZMduK, 'r', encoding='utf-8') as f:
    docs = json.load(f)

# Normalize funding entries: ensure Amount is int and Project_Name exists
for r in funding:
    # Convert Amount to int
    try:
        r['Amount'] = int(r.get('Amount') if r.get('Amount') is not None else 0)
    except:
        # remove commas or other characters
        amt = str(r.get('Amount','0')).replace(',','').strip()
        try:
            r['Amount'] = int(amt)
        except:
            r['Amount'] = 0
    r['Project_Name_norm'] = str(r.get('Project_Name','')).strip()

# Identify park-related funding records by keywords in the Project_Name
park_keywords = ['park', 'playground', 'walkway', 'bench', 'benches', 'shade structure', 'play area']
park_funding = [r for r in funding if any(kw in r['Project_Name_norm'].lower() for kw in park_keywords)]

# For each park funding record, search civic documents for completion in 2022
matched_projects = []
patterns = [r'completed[^\n]{0,120}2022', r'construction was completed[^\n]{0,120}2022', r'complete construction[^\n]{0,120}2022', r'complete[^\n]{0,120}2022']

for rec in park_funding:
    pname = rec['Project_Name_norm']
    pname_lower = pname.lower()
    found_completion = False
    for doc in docs:
        text = doc.get('text','')
        text_lower = text.lower()
        if pname_lower in text_lower:
            # If project name mentioned, check for any completion pattern near mention
            # Find index of mention
            idx = text_lower.find(pname_lower)
            start = max(0, idx-200)
            end = min(len(text_lower), idx+400)
            context = text_lower[start:end]
            for pat in patterns:
                if re.search(pat, context, flags=re.IGNORECASE):
                    found_completion = True
                    break
            if not found_completion:
                # As fallback, search the whole doc for completion with 2022
                for pat in patterns:
                    if re.search(pat, text_lower, flags=re.IGNORECASE):
                        found_completion = True
                        break
        if found_completion:
            break
    if found_completion:
        matched_projects.append({'Project_Name': rec['Project_Name_norm'], 'Amount': rec['Amount']})

# Additionally, some park projects might be referred in doc with slightly different names.
# We'll also try to match by keywords within docs indicating a park project was completed in 2022,
# then map by checking funding table for projects that share a common token with the doc heading.
# Find doc lines that mention 'park' and 'completed' with 2022
for doc in docs:
    text_lower = doc.get('text','').lower()
    if 'park' in text_lower and re.search(r'completed[^\n]{0,120}2022', text_lower, flags=re.IGNORECASE):
        # extract lines mentioning 'park' and nearby words to identify project names
        lines = doc.get('text','').splitlines()
        for i,line in enumerate(lines):
            if 'park' in line.lower():
                # try to extract potential project name from this line (strip bullets/markers)
                candidate = line.strip().strip('\ufeff').strip('•').strip()
                # remove leading numbering or cid markers
                candidate = re.sub(r'^\W+','',candidate)
                if len(candidate) > 3:
                    # find funding records that contain significant words from candidate
                    for rec in funding:
                        if rec['Project_Name_norm'].lower() in candidate.lower() or candidate.lower() in rec['Project_Name_norm'].lower():
                            # check not already included
                            if not any(d['Project_Name']==rec['Project_Name_norm'] for d in matched_projects):
                                # verify funding rec is park-related
                                if any(kw in rec['Project_Name_norm'].lower() for kw in park_keywords):
                                    # ensure doc indeed has completion 2022 near this line
                                    start = max(0, i-3)
                                    end = min(len(lines), i+3)
                                    context = '\n'.join(lines[start:end]).lower()
                                    if re.search(r'completed[^\n]{0,120}2022', context, flags=re.IGNORECASE) or re.search(r'construction was completed[^\n]{0,120}2022', context, flags=re.IGNORECASE):
                                        matched_projects.append({'Project_Name': rec['Project_Name_norm'], 'Amount': rec['Amount']})

# Remove duplicates
unique = {}
for p in matched_projects:
    unique[p['Project_Name']] = unique.get(p['Project_Name'], 0) + p['Amount']

matching_list = [{'Project_Name': k, 'Amount': v} for k,v in unique.items()]
total_funding = sum(v for v in unique.values())

result = {'total_funding': total_funding, 'matched_projects': matching_list, 'matched_count': len(matching_list)}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_FA7KkPgziK2Q90TPgVoTXk32': 'file_storage/call_FA7KkPgziK2Q90TPgVoTXk32.json', 'var_call_mka5UEs3QWagkOJUBTVZMduK': 'file_storage/call_mka5UEs3QWagkOJUBTVZMduK.json'}

exec(code, env_args)
