code = """import json
import re
# Load data from files provided by previous tool calls
with open(var_call_yjzn3iNOn32CLVsLyYyIGQ0r, 'r') as f:
    citations = json.load(f)
with open(var_call_lklYoy79yHZjMo2P1Kctad7P, 'r') as f:
    papers = json.load(f)

# Build citation map for 2020 results (title -> citation_count)
citation_map = {}
for rec in citations:
    title = rec.get('title')
    # citation_count may be string; convert to int safely
    try:
        count = int(rec.get('citation_count', 0))
    except:
        try:
            count = int(float(rec.get('citation_count', 0)))
        except:
            count = 0
    citation_map[title] = count

# Identify CHI papers from paper_docs
chi_titles = set()
for doc in papers:
    filename = doc.get('filename', '')
    title = filename[:-4] if filename.lower().endswith('.txt') else filename
    text = doc.get('text', '')
    # Consider as CHI paper if 'CHI' is found as a word or common CHI indicators
    if re.search(r'\bCHI\b', text, re.IGNORECASE) or "CHI'" in text or "Conference on Human Factors in Computing Systems" in text:
        chi_titles.add(title)

# Now find intersection with citation_map
matched = []
for t, c in citation_map.items():
    if t in chi_titles:
        matched.append({'title': t, 'citation_count': c})

total_citations = sum(x['citation_count'] for x in matched)
num_papers = len(matched)

# Prepare result
result = {
    'total_citations': total_citations,
    'num_papers': num_papers,
    'papers': matched
}

import json
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_zYcIxDalWMaFFKPWswQ1yPH6': ['paper_docs'], 'var_call_uDRemQivcXp5YcsJxLvKZjij': ['Citations', 'sqlite_sequence'], 'var_call_yjzn3iNOn32CLVsLyYyIGQ0r': 'file_storage/call_yjzn3iNOn32CLVsLyYyIGQ0r.json', 'var_call_lklYoy79yHZjMo2P1Kctad7P': 'file_storage/call_lklYoy79yHZjMo2P1Kctad7P.json'}

exec(code, env_args)
