code = """import json
import re

# Load the large JSON results from files
with open(var_call_q8DyybWfMpgsfa01DbrQnpKd, 'r', encoding='utf-8') as f:
    docs = json.load(f)
with open(var_call_PrAYnPh4GhBEfVs4pC5iOKej, 'r', encoding='utf-8') as f:
    citations = json.load(f)

# Build citation mapping: title -> total_citations (int)
cit_map = {}
for rec in citations:
    title = rec.get('title')
    tc = rec.get('total_citations')
    try:
        cit_map[title] = int(tc)
    except:
        try:
            cit_map[title] = int(float(tc))
        except:
            cit_map[title] = 0

results = []
for d in docs:
    filename = d.get('filename','')
    text = d.get('text','')
    if not filename:
        continue
    # derive title from filename (remove .txt)
    title = filename[:-4] if filename.lower().endswith('.txt') else filename
    # confirm empirical is present
    if not re.search(r'\bempirical\b', text, re.I):
        continue
    # find first year-like occurrence
    years = re.findall(r'20\d{2}', text)
    year = None
    if years:
        # pick the first plausible year
        for y in years:
            yi = int(y)
            if 1900 < yi < 2100:
                year = yi
                break
    # if no year found, skip
    if year is None:
        continue
    # filter published after 2016
    if year <= 2016:
        continue
    total_citations = cit_map.get(title, 0)
    results.append({'title': title, 'year': year, 'total_citations': total_citations})

# sort results by title for determinism
results = sorted(results, key=lambda x: x['title'].lower())

# Prepare JSON serializable output but only include title and total_citations per user query
out = [{'title': r['title'], 'total_citations': r['total_citations']} for r in results]

print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_lcOE6rX7jJrlR6ln0WbMfTOW': ['paper_docs'], 'var_call_FFjFWfoyaD6lbJrW5FgOxcmd': ['Citations', 'sqlite_sequence'], 'var_call_q8DyybWfMpgsfa01DbrQnpKd': 'file_storage/call_q8DyybWfMpgsfa01DbrQnpKd.json', 'var_call_PrAYnPh4GhBEfVs4pC5iOKej': 'file_storage/call_PrAYnPh4GhBEfVs4pC5iOKej.json'}

exec(code, env_args)
