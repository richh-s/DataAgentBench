code = """import json, re

# Load query results from storage file paths
with open(var_call_imMVVH4ydlnQiLitue5achAa, 'r') as f:
    funding = json.load(f)
with open(var_call_LsS5gYiobVLdbl1d1c1xS3Ye, 'r') as f:
    civic_docs = json.load(f)

# Normalize funding amounts and records
for r in funding:
    try:
        r['Amount'] = int(r['Amount'])
    except:
        try:
            r['Amount'] = int(float(r['Amount']))
        except:
            r['Amount'] = 0
    r['Project_Name_norm'] = re.sub(r"\(.*?\)", "", r['Project_Name']).strip().lower()

park_keywords = ['park', 'playground', 'walkway', 'shade', 'bench', 'benches', 'bluffs', 'point dume', 'legacy park']

matched = []

civic_texts = [doc.get('text','').lower() for doc in civic_docs]
full_civic = "\n".join(civic_texts)

for r in funding:
    name = r['Project_Name'].lower()
    name_norm = r['Project_Name_norm']
    is_park = any(kw in name for kw in park_keywords) or any(kw in name_norm for kw in park_keywords)
    if not is_park:
        continue
    found_completion = False
    # Try exact name match in civic texts
    for text in civic_texts:
        if name in text or name_norm in text:
            # find all occurrences
            for m in re.finditer(re.escape(name_norm), text):
                idx = m.start()
                start = max(0, idx-200)
                end = min(len(text), idx+500)
                window = text[start:end]
                if ('complete' in window or 'construction was completed' in window or 'notice of completion' in window) and '2022' in window:
                    found_completion = True
                    break
            if found_completion:
                break
    # If not found, try searching for key phrases like 'bluffs park' or 'point dume' shorter tokens
    if not found_completion:
        tokens = name_norm.split()
        # try combos of up to 3 contiguous tokens
        for i in range(len(tokens)):
            for j in range(i+1, min(i+4, len(tokens))+1):
                phrase = ' '.join(tokens[i:j])
                if len(phrase) < 4:
                    continue
                if phrase in full_civic:
                    for m in re.finditer(re.escape(phrase), full_civic):
                        idx = m.start()
                        start = max(0, idx-200)
                        end = min(len(full_civic), idx+500)
                        window = full_civic[start:end]
                        if ('complete' in window or 'construction was completed' in window or 'notice of completion' in window) and '2022' in window:
                            found_completion = True
                            break
                    if found_completion:
                        break
            if found_completion:
                break
    if found_completion:
        matched.append({'Project_Name': r['Project_Name'], 'Amount': r['Amount']})

total = sum(m['Amount'] for m in matched)

result = {'total_funding': total, 'projects': matched}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_NnUo40dHHTLYgcQTqlojtfqg': ['civic_docs'], 'var_call_UjP3tQXtgm9tRd9gDjbiDPvo': ['Funding'], 'var_call_LsS5gYiobVLdbl1d1c1xS3Ye': 'file_storage/call_LsS5gYiobVLdbl1d1c1xS3Ye.json', 'var_call_imMVVH4ydlnQiLitue5achAa': 'file_storage/call_imMVVH4ydlnQiLitue5achAa.json'}

exec(code, env_args)
