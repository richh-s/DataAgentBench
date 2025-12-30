code = """import re, json
from pathlib import Path

# Load full results
with open(var_call_xMCeFY3h6LYopdhzc8sbFeGM, 'r') as f:
    papers = json.load(f)
with open(var_call_NbFBNQ1NiG9WyGnt8wzo8rvj, 'r') as f:
    citations = json.load(f)

# Helper to extract year from text
year_pattern = re.compile(r"20(\d{2})")

def extract_year(text):
    years = [int(y.group(0)) for y in year_pattern.finditer(text)]
    years = [y for y in years if 2000 <= y <= 2025]
    return min(years) if years else None

results = []

# Build citation map
cit_map = {c['title']: int(c['total_citations']) for c in citations}

for doc in papers:
    text = doc.get('text', '')
    year = extract_year(text)
    if year != 2016:
        continue
    filename = doc.get('filename', '')
    title = filename[:-4] if filename.lower().endswith('.txt') else filename
    # crude domain filter: ensure 'physical activity' mentioned
    if 'physical activity' not in text.lower():
        continue
    total_cit = cit_map.get(title)
    if total_cit is None:
        # try unquoted variant if title has quotes
        alt_title = title.replace('"', '\"')
        total_cit = cit_map.get(alt_title)
    results.append({
        'title': title,
        'total_citations': total_cit if total_cit is not None else 0
    })

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_call_xMCeFY3h6LYopdhzc8sbFeGM': 'file_storage/call_xMCeFY3h6LYopdhzc8sbFeGM.json', 'var_call_NbFBNQ1NiG9WyGnt8wzo8rvj': 'file_storage/call_NbFBNQ1NiG9WyGnt8wzo8rvj.json'}

exec(code, env_args)
