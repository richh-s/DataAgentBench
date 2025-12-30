code = """import re, json, pandas as pd
from datetime import datetime

# Load full Mongo results if needed
path = var_call_763ce1c3Mw5B8jFBt9RtCrIq
with open(path, 'r') as f:
    mongo_records = json.load(f)

# Extract year from text (search for patterns like CHI 2018, 2019, etc.)
empirical_papers = []
for doc in mongo_records:
    text = doc.get('text', '') or ''
    # Check contribution contains 'empirical' heuristically: look for 'empirical study' or 'we conducted an empirical'
    if re.search(r'empirical', text, re.I):
        # extract year: look for 20xx near venue keywords or copyright
        years = re.findall(r'20(1[0-9]|2[0-9])', text)
        year = None
        if years:
            # take earliest plausible publication year >= 2000
            year = int(sorted(years)[0][:4]) if len(sorted(years)[0])==4 else int('20'+sorted(years)[0])
        filename = doc.get('filename','')
        title = filename.rsplit('.txt',1)[0]
        empirical_papers.append({'title': title, 'year': year})

# Filter to papers published after 2016
empirical_after_2016 = {p['title'] for p in empirical_papers if p['year'] and p['year']>2016}

# Load citations aggregated by title
path2 = var_call_zB77TMmSmzchUaFYg5XbEP1L
with open(path2, 'r') as f:
    cit_records = json.load(f)

# Build dict of total citations
cit_dict = {r['title']: int(r['total_citations']) for r in cit_records}

results = []
for title in empirical_after_2016:
    if title in cit_dict:
        results.append({'title': title, 'total_citations': cit_dict[title]})

# Sort by title
results_sorted = sorted(results, key=lambda x: x['title'])

out = json.dumps(results_sorted)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_763ce1c3Mw5B8jFBt9RtCrIq': 'file_storage/call_763ce1c3Mw5B8jFBt9RtCrIq.json', 'var_call_zB77TMmSmzchUaFYg5XbEP1L': 'file_storage/call_zB77TMmSmzchUaFYg5XbEP1L.json'}

exec(code, env_args)
