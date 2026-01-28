code = """import json
import re

# Load data from storage-provided file paths
with open(var_call_aZURe3TkzDmxJKgkobkFzbj7, 'r', encoding='utf-8') as f:
    docs = json.load(f)
with open(var_call_HbYVb9be9FWKtOodjttq4c7I, 'r', encoding='utf-8') as f:
    citations = json.load(f)

# Build citation totals map
cit_map = {}
for c in citations:
    title = c.get('title')
    # Some citation totals may be strings; convert safely
    try:
        tot = int(c.get('total_citations'))
    except Exception:
        try:
            tot = int(float(c.get('total_citations')))
        except Exception:
            tot = None
    cit_map[title] = tot

results = []
for d in docs:
    filename = d.get('filename','')
    if filename.lower().endswith('.txt'):
        title = filename[:-4]
    else:
        title = filename
    text = d.get('text','')
    header = text[:1000]
    # Determine if publication year is 2016 by checking header area for '2016'
    year = None
    if re.search(r'\b2016\b', header):
        year = 2016
    else:
        # look for common phrases anywhere in text
        if re.search(r'\b(©|Copyright)\W+2016', text, re.I) or re.search(r'\bCHI\W*2016', text, re.I) or re.search(r'Proceedings of .*2016', text, re.I):
            year = 2016
    # Only include if year==2016 and domain mention 'physical activity' in full text
    if year == 2016 and re.search(r'physical activity', text, re.I):
        total_citations = cit_map.get(title)
        # If citation total is None, try matching stripped title keys
        if total_citations is None:
            total_citations = cit_map.get(title.strip())
        # fallback to 0 if still None
        if total_citations is None:
            total_citations = 0
        results.append({"title": title, "total_citations": total_citations})

# Remove duplicates (if any) and sort by title
seen = set()
uniq = []
for r in results:
    if r['title'] not in seen:
        seen.add(r['title'])
        uniq.append(r)
uniq = sorted(uniq, key=lambda x: x['title'])

import json
print("__RESULT__:")
print(json.dumps(uniq))"""

env_args = {'var_call_wQdnI6hks6T5yZhIQVRwTx5I': ['paper_docs'], 'var_call_4boCUXjDl1lUc9qc07KOWzez': ['Citations', 'sqlite_sequence'], 'var_call_aZURe3TkzDmxJKgkobkFzbj7': 'file_storage/call_aZURe3TkzDmxJKgkobkFzbj7.json', 'var_call_HbYVb9be9FWKtOodjttq4c7I': 'file_storage/call_HbYVb9be9FWKtOodjttq4c7I.json'}

exec(code, env_args)
