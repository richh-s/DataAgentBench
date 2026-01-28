code = """import json
import re
import pandas as pd

# Load previous tool results from storage keys
# var_call_bDmjKL2mUDkPM33K0c25w6W9 and var_call_OyigBIL4uZrPfKo6Hs2TN8za

with open(var_call_bDmjKL2mUDkPM33K0c25w6W9, 'r', encoding='utf-8') as f:
    papers = json.load(f)

with open(var_call_OyigBIL4uZrPfKo6Hs2TN8za, 'r', encoding='utf-8') as f:
    citations = json.load(f)

# Build citation lookup
cit_lookup = {rec['title']: int(rec['total_citations']) for rec in citations}

results = []

def extract_year(text):
    # find first 4-digit year between 1990 and 2026
    m = re.search(r"\b(?:19|20)\d{2}\b", text)
    if m:
        try:
            y = int(m.group(0))
            return y
        except:
            return None
    return None

for doc in papers:
    filename = doc.get('filename','')
    title = filename[:-4] if filename.lower().endswith('.txt') else filename
    text = doc.get('text','')
    year = extract_year(text)
    if year is None:
        # try searching first 500 chars only
        year = extract_year(text[:500])
    # contribution: check if 'empirical' occurs in text or title
    contrib = False
    if re.search(r'\bempirical\b', text, re.IGNORECASE) or re.search(r'\bempirical\b', title, re.IGNORECASE):
        contrib = True
    # filter: empirical and published after 2016
    if contrib and year and year > 2016:
        total_cit = cit_lookup.get(title, 0)
        results.append({'title': title, 'total_citations': int(total_cit), 'year': int(year)})

# Sort results by total_citations descending
results = sorted(results, key=lambda x: x['total_citations'], reverse=True)

# Only include title and total_citations in final output
final = [{'title': r['title'], 'total_citations': r['total_citations']} for r in results]

print("__RESULT__:")
print(json.dumps(final))"""

env_args = {'var_call_VMIGlUcjCoFrPe8dJqzLW9cd': ['paper_docs'], 'var_call_bDmjKL2mUDkPM33K0c25w6W9': 'file_storage/call_bDmjKL2mUDkPM33K0c25w6W9.json', 'var_call_MiEHW1T3i4DAX06o7EI0sEOP': ['Citations', 'sqlite_sequence'], 'var_call_OyigBIL4uZrPfKo6Hs2TN8za': 'file_storage/call_OyigBIL4uZrPfKo6Hs2TN8za.json'}

exec(code, env_args)
