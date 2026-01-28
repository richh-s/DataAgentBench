code = """import json, re
# load citations data from storage path
path = var_call_6pF9CiLk8kixPf8GWCy6dT6W
with open(path, 'r', encoding='utf-8') as f:
    citations = json.load(f)

# load mongo docs with 'empirical' (full result path)
mongo_path = var_call_lNdRBtmAjueUf49lJMDLkygD
with open(mongo_path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

# Extract titles and year from docs where 'empirical' appears and year > 2016
matches = {}
year_re = re.compile(r"\b(19|20)\d{2}\b")
for doc in docs:
    text = doc.get('text','')
    if re.search(r'(?i)empirical', text):
        filename = doc.get('filename','')
        title = filename[:-4] if filename.endswith('.txt') else filename
        # find first year in text
        years = year_re.findall(text)
        # year_re.findall returns tuples if group; adjust pattern
        # We'll search for explicit 2017-2026
        m = re.search(r"\b(2017|2018|2019|2020|2021|2022|2023|2024|2025|2026)\b", text)
        if m:
            year = int(m.group(1))
            if year > 2016:
                matches[title] = year

# Now join with citations by title
results = []
for c in citations:
    t = c['title']
    # The titles in citations might include quotes; strip surrounding quotes and whitespace
    t_stripped = t.strip()
    if t_stripped.startswith('"') and t_stripped.endswith('"'):
        t_stripped = t_stripped[1:-1]
    # Check if this title is in matches (exact match)
    if t_stripped in matches:
        results.append({'title': t_stripped, 'year': matches[t_stripped], 'total_citations': c['total_citations']})

# If no exact matches, try fuzzy by checking if citation title is substring of doc title or vice versa
if not results:
    for c in citations:
        t = c['title'].strip()
        if t.startswith('"') and t.endswith('"'):
            t = t[1:-1]
        for doc_title, year in matches.items():
            if t.lower() in doc_title.lower() or doc_title.lower() in t.lower():
                results.append({'title': doc_title, 'year': year, 'total_citations': c['total_citations']})

print('__RESULT__:')
print(json.dumps(results))"""

env_args = {'var_call_O6T9ov9jzG5YdiuSjrbbVoPU': ['paper_docs'], 'var_call_CGhz2TCzvXvH0HGqonLb9qg7': 'file_storage/call_CGhz2TCzvXvH0HGqonLb9qg7.json', 'var_call_YMGpqlZGu0Ru3MTyBeiGGaXL': [], 'var_call_lNdRBtmAjueUf49lJMDLkygD': 'file_storage/call_lNdRBtmAjueUf49lJMDLkygD.json', 'var_call_paHLpoipdY0FxATN0W1kuYUM': ['Citations', 'sqlite_sequence'], 'var_call_LOZUWIdfPemCtSAQhAHcUAdw': 'file_storage/call_LOZUWIdfPemCtSAQhAHcUAdw.json', 'var_call_6pF9CiLk8kixPf8GWCy6dT6W': 'file_storage/call_6pF9CiLk8kixPf8GWCy6dT6W.json'}

exec(code, env_args)
