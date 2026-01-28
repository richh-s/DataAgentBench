code = """import json
import re
import pandas as pd

# Load papers
with open(locals()['var_function-call-1637746451261953747'], 'r') as f:
    papers_data = json.load(f)

# Load citations
with open(locals()['var_function-call-1625983961919980937'], 'r') as f:
    citations_data = json.load(f)

# Convert citations to dict for easy lookup
# citations_data is a list of dicts: [{"title": "...", "total_citations": 53}, ...]
# Wait, let's verify if total_citations is int or str. The preview showed "53" (string).
citation_map = {}
for item in citations_data:
    try:
        count = int(item['total_citations'])
    except:
        count = 0
    citation_map[item['title']] = count

def get_year(text):
    # Try to find year in first 2000 chars
    header = text[:2000]
    # Look for 20xx
    matches = re.findall(r'\b(20[0-2][0-9])\b', header)
    valid_years = []
    for m in matches:
        y = int(m)
        if 2000 <= y <= 2025:
            valid_years.append(y)
    
    if valid_years:
        # Return the first one, or maybe the most common?
        # Usually the first one is the publication year in the header.
        return valid_years[0]
    
    # Fallback: look for 'YY
    matches_short = re.findall(r"'(\d{2})", header)
    for m in matches_short:
        y = 2000 + int(m)
        if 2000 <= y <= 2025:
            return y
    return None

results = []
for p in papers_data:
    title = p.get('filename', '').replace('.txt', '')
    text = p.get('text', '')
    
    year = get_year(text)
    is_empirical = "empirical" in text.lower()
    
    if year and year > 2016 and is_empirical:
        count = citation_map.get(title, 0)
        results.append({"title": title, "total_citation_count": count})

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-1625983961919980332': 'file_storage/function-call-1625983961919980332.json', 'var_function-call-1625983961919980937': 'file_storage/function-call-1625983961919980937.json', 'var_function-call-603899956623293996': 'file_storage/function-call-603899956623293996.json', 'var_function-call-10661397933404745766': [], 'var_function-call-11800293491939370274': {'count': 5, 'years': [None, None, None, None, None], 'empirical_count': 2, 'gt_2016_count': 0}, 'var_function-call-1637746451261953747': 'file_storage/function-call-1637746451261953747.json'}

exec(code, env_args)
