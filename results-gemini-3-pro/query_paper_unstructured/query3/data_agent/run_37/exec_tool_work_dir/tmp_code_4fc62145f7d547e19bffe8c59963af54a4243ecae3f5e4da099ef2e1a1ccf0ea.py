code = """import json
import re

# Load data
with open(locals()['var_function-call-1188879216130437550'], 'r') as f:
    papers = json.load(f)

with open(locals()['var_function-call-6926115911538441459'], 'r') as f:
    citations_data = json.load(f)

# Aggregate citations by title
citation_map = {}
for entry in citations_data:
    title = entry['title']
    count = int(entry['citation_count'])
    if title not in citation_map:
        citation_map[title] = 0
    citation_map[title] += count

# Process papers
filtered_papers = []
for p in papers:
    text = p.get('text', '')
    filename = p.get('filename', '')
    title = filename.replace('.txt', '')
    
    # Extract year
    # Look for 4 digits in the first 1000 characters
    # Common patterns: "CHI 2017", "Copyright 2017", "2017"
    # We take the first 4-digit number that looks like a year (1990-2025)
    header_text = text[:2000]
    years = re.findall(r'\b(20[0-2][0-9])\b', header_text)
    
    pub_year = None
    if years:
        # Heuristic: pick the first one found, assuming header contains the date
        pub_year = int(years[0])
    
    # Check contribution
    # "empirical" in text (case insensitive)
    has_empirical = "empirical" in text.lower()
    
    if pub_year and pub_year > 2016 and has_empirical:
        filtered_papers.append({
            "title": title,
            "year": pub_year,
            "contribution_check": has_empirical
        })

# Join with citations
results = []
for p in filtered_papers:
    t = p['title']
    c_count = citation_map.get(t, 0)
    results.append({
        "title": t,
        "total_citation_count": c_count
    })

print("__RESULT__:")
print(json.dumps(results, indent=2))"""

env_args = {'var_function-call-563988683724796528': 'file_storage/function-call-563988683724796528.json', 'var_function-call-1188879216130437550': 'file_storage/function-call-1188879216130437550.json', 'var_function-call-6926115911538441459': 'file_storage/function-call-6926115911538441459.json'}

exec(code, env_args)
