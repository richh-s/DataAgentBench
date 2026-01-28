code = """import json, re

# Load data from storage-provided file paths
with open(var_call_1WNMnXzLqRr9u8gix6ncsCDL, 'r') as f:
    funding = json.load(f)
with open(var_call_wWPlT1QfVgACpt3TGPAyJdfb, 'r') as f:
    civic_docs = json.load(f)

# Normalize funding records
for r in funding:
    try:
        r['Amount'] = int(r['Amount'])
    except:
        nums = re.findall(r"\d+", str(r.get('Amount','0')))
        r['Amount'] = int(nums[0]) if nums else 0
    r['Project_Name_lc'] = r['Project_Name'].lower()

# Identify park-related funding records
park_funds = [r for r in funding if 'park' in r['Project_Name_lc']]

matched = []

# For each park-related funding record, check civic docs for completion in 2022
for r in park_funds:
    name_lc = r['Project_Name_lc']
    name_words = [w for w in re.findall(r"[a-z0-9]+", name_lc) if len(w)>3]
    found = False
    for doc in civic_docs:
        text = doc.get('text','').lower()
        if not text:
            continue
        # crude checks: project name phrase appears in doc OR key words from name appear
        if name_lc in text or any(' '.join(name_words[i:i+2]) in text for i in range(len(name_words))):
            if 'completed' in text and '2022' in text:
                matched.append(r)
                found = True
                break
        # fallback: if both words like 'bluffs' and 'park' present
        if all(w in text for w in name_words[:2]) and 'completed' in text and '2022' in text:
            matched.append(r)
            found = True
            break
    # if not found, still check whole corpus: maybe project mentioned in any doc with completed and 2022
    if not found:
        corpus = ' '.join([doc.get('text','').lower() for doc in civic_docs])
        if 'completed' in corpus and '2022' in corpus and any(w in corpus for w in name_words):
            matched.append(r)

# Deduplicate by Project_Name
unique = {}
for r in matched:
    unique[r['Project_Name']] = r
matched_unique = list(unique.values())

total = sum(r['Amount'] for r in matched_unique)

result = {'park_projects_completed_2022': sorted(list(unique.keys())), 'total_funding': total}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_CeyxRynO2d9ptMHB9H0F39vr': ['civic_docs'], 'var_call_1WNMnXzLqRr9u8gix6ncsCDL': 'file_storage/call_1WNMnXzLqRr9u8gix6ncsCDL.json', 'var_call_wWPlT1QfVgACpt3TGPAyJdfb': 'file_storage/call_wWPlT1QfVgACpt3TGPAyJdfb.json'}

exec(code, env_args)
