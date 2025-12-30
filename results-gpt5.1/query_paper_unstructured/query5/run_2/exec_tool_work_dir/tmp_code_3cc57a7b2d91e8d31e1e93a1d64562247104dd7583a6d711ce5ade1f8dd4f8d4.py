code = """import re, json
from pathlib import Path

# Load full results
with open(var_call_zjT0pr1o9tJemhyia5x82ZAH, 'r') as f:
    chi_docs = json.load(f)
with open(var_call_uwTKwK79j5njrBw1yj00jROd, 'r') as f:
    citations = json.load(f)

# Helper to guess venue and year from text
venue_pattern = re.compile(r"CHI\s+'?\d{2}", re.IGNORECASE)
year_pattern = re.compile(r"(19|20)\d{2}")

chi_titles = set()
for doc in chi_docs:
    text = doc.get('text','')
    if venue_pattern.search(text):
        # very rough year extraction: first year in text
        m = year_pattern.search(text)
        year = int(m.group(0)) if m else None
        if year is not None:
            # consider CHI papers (venue already implied by CHI pattern), any year
            title = doc.get('filename','').replace('.txt','')
            if title:
                chi_titles.add(title)

# Sum citation counts in 2020 for those titles
chi_titles_lower = {t.lower() for t in chi_titles}

total_citations = 0
for rec in citations:
    title = rec['title']
    if title.lower() in chi_titles_lower:
        try:
            c = int(rec['citation_count'])
        except Exception:
            c = 0
        total_citations += c

import json as _json
result = total_citations
print("__RESULT__:")
print(_json.dumps(result))"""

env_args = {'var_call_zjT0pr1o9tJemhyia5x82ZAH': 'file_storage/call_zjT0pr1o9tJemhyia5x82ZAH.json', 'var_call_uwTKwK79j5njrBw1yj00jROd': 'file_storage/call_uwTKwK79j5njrBw1yj00jROd.json'}

exec(code, env_args)
