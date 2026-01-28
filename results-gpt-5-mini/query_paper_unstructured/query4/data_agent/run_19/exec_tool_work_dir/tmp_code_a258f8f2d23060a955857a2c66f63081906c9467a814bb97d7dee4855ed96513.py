code = """import json, re
# Load the Mongo query result stored in var_call_7US8qjJdvllDx82xqMMY1siE
path = var_call_7US8qjJdvllDx82xqMMY1siE
with open(path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

results = []
for d in docs:
    filename = d.get('filename','')
    if filename.lower().endswith('.txt'):
        title = filename[:-4]
    else:
        title = filename
    text = d.get('text','') or ''
    text_low = text.lower()
    # confirm domain mention
    domain_match = 'physical activity' in text_low
    # attempt to extract publication year: look for 4-digit years in header (first 400 chars)
    header = text[:800]
    years = re.findall(r"\b(19|20)\d{2}\b", header)
    # The above regex returns only the first two digits captured; instead find full years
    years_full = re.findall(r"\b(?:19|20)\d{2}\b", header)
    pub_year = None
    if years_full:
        # pick the earliest occurrence in header
        pub_year = years_full[0]
    else:
        # fallback: search whole text
        years_full_all = re.findall(r"\b(?:19|20)\d{2}\b", text)
        if years_full_all:
            pub_year = years_full_all[0]
    # mark if contains 2016
    is_2016 = '2016' in text
    if domain_match and is_2016:
        results.append({'title': title, 'extracted_year': pub_year})

# Deduplicate by title
unique = {}
for r in results:
    unique[r['title']] = r
final_list = list(unique.values())

import json
print("__RESULT__:")
print(json.dumps(final_list))"""

env_args = {'var_call_7US8qjJdvllDx82xqMMY1siE': 'file_storage/call_7US8qjJdvllDx82xqMMY1siE.json'}

exec(code, env_args)
