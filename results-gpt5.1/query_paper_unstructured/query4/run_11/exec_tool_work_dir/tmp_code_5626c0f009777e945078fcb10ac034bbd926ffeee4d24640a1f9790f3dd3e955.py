code = """import re, json
from pathlib import Path

# Load full mongo results
path_docs = Path(var_call_7lS5UCudbNb0l6wrqTN0Xo4Q)
with path_docs.open() as f:
    docs = json.load(f)

# Extract title (from filename) and year (search in text)
physical_2016_titles = set()
for d in docs:
    text = d.get('text','')
    years = re.findall(r'20\d{2}', text)
    year = None
    if years:
        # heuristic: use first 4-digit 20xx that is <=2019; then check for 2016 anywhere
        if '2016' in years:
            year = 2016
    if year == 2016:
        title = d.get('filename','').rsplit('.txt',1)[0]
        # require physical activity phrase in text
        if re.search(r'physical activity', text, re.I):
            physical_2016_titles.add(title)

# Load citations aggregated by title
path_cit = Path(var_call_4eIbqkIQduUUdjWLc6iqP0pk)
with path_cit.open() as f:
    cits = json.load(f)

# Build map
cit_map = {c['title']: int(c['total_citations']) for c in cits}

results = []
for t in sorted(physical_2016_titles):
    if t in cit_map:
        results.append({'title': t, 'total_citations': cit_map[t]})

out = json.dumps(results)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_7lS5UCudbNb0l6wrqTN0Xo4Q': 'file_storage/call_7lS5UCudbNb0l6wrqTN0Xo4Q.json', 'var_call_4eIbqkIQduUUdjWLc6iqP0pk': 'file_storage/call_4eIbqkIQduUUdjWLc6iqP0pk.json'}

exec(code, env_args)
