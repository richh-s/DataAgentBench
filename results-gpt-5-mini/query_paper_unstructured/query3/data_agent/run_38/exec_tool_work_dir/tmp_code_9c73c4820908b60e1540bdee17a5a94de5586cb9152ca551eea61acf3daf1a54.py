code = """import json, re
# Load the MongoDB paper docs result file and the citations SQL result file
with open(var_call_fOnW8mqo8NSGYX1WqxSUjuMe, 'r', encoding='utf-8') as f:
    papers = json.load(f)
with open(var_call_UVBHko1vWYSIdpZ7GDYHfmez, 'r', encoding='utf-8') as f:
    citations = json.load(f)

# Build a mapping from title to total citations (ensure int)
cit_map = {}
for rec in citations:
    title = rec.get('title')
    # Some titles in citations may have surrounding quotes; normalize by stripping
    if isinstance(title, str):
        norm = title.strip()
    else:
        norm = title
    try:
        total = int(rec.get('total_citations') if rec.get('total_citations') is not None else 0)
    except:
        # sometimes numbers come as strings with commas
        s = rec.get('total_citations')
        if isinstance(s, str):
            total = int(re.sub(r"[^0-9]", "", s) or 0)
        else:
            total = 0
    cit_map[norm] = total

results = []

for doc in papers:
    filename = doc.get('filename','')
    # derive title from filename by removing .txt
    title = filename[:-4] if filename.lower().endswith('.txt') else filename
    text = doc.get('text','') or ''
    tl = text.lower()
    # Check contribution contains 'empirical' (substring match anywhere)
    if 'empirical' not in tl:
        continue
    # Extract year: look in first 500 characters for a 4-digit year
    head = text[:1000]
    years = re.findall(r'\b(19|20)\d{2}\b', head)
    # re.findall with groups returns only group1; instead find full matches
    years_full = re.findall(r'\b(?:19|20)\d{2}\b', head)
    year = None
    if years_full:
        try:
            year = int(years_full[0])
        except:
            year = None
    else:
        # fallback: search entire text
        years_full = re.findall(r'\b(?:19|20)\d{2}\b', text)
        if years_full:
            try:
                year = int(years_full[0])
            except:
                year = None
    if year is None:
        continue
    if year <= 2016:
        continue
    # find citation total from cit_map; try several normalizations
    total = None
    # try exact title
    if title in cit_map:
        total = cit_map[title]
    else:
        # try variants: sometimes citations title has quotes around it
        if f'"{title}"' in cit_map:
            total = cit_map[f'"{title}"']
        else:
            # try matching ignoring quotes and extra spaces
            for k in cit_map.keys():
                if k.strip('"') == title:
                    total = cit_map[k]
                    break
    if total is None:
        # If no citation record, assume 0
        total = 0
    results.append({'title': title, 'total_citations': total, 'year': year})

# Prepare final output: list of dicts with title and total citation count
final = [{'title': r['title'], 'total_citations': r['total_citations']} for r in results]

# Optionally sort by total citations descending
final_sorted = sorted(final, key=lambda x: x['total_citations'], reverse=True)

import json
print("__RESULT__:")
print(json.dumps(final_sorted))"""

env_args = {'var_call_fOnW8mqo8NSGYX1WqxSUjuMe': 'file_storage/call_fOnW8mqo8NSGYX1WqxSUjuMe.json', 'var_call_UVBHko1vWYSIdpZ7GDYHfmez': 'file_storage/call_UVBHko1vWYSIdpZ7GDYHfmez.json'}

exec(code, env_args)
