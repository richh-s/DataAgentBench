code = """import json
import re

# Load citations with min year
path_cit = locals()['var_function-call-12413501451811374278']
with open(path_cit, 'r') as f:
    citations_data = json.load(f)

# Map title -> {min_year, total_count}
cit_info = {}
for item in citations_data:
    t = item['title']
    c = int(item['total_citations'])
    y_str = item['first_citation_year']
    y = int(y_str) if y_str else 9999
    cit_info[t] = {"min_year": y, "count": c}

# Load papers
path_papers = locals()['var_function-call-11974208795470481837']
with open(path_papers, 'r') as f:
    papers = json.load(f)

final_results = []

for p in papers:
    title = p['filename'].replace('.txt', '')
    text = p['text']
    
    if title not in cit_info:
        continue
        
    c_data = cit_info[title]
    min_cit_year = c_data['min_year']
    total_count = c_data['count']
    
    # Extract year from text
    text_year = None
    
    # Regex for Conference/Year
    # Try: "CHI '17", "CHI 2017", "Copyright 2017"
    patterns = [
        r"Copyright.*?20(\d{2})",
        r"(?:CHI|UbiComp|CSCW|DIS|IUI).*?'(\d{2})",
        r"(?:CHI|UbiComp|CSCW|DIS|IUI).*?20(\d{2})",
        r"Published.*?20(\d{2})"
    ]
    
    for pat in patterns:
        m = re.search(pat, text, re.IGNORECASE)
        if m:
            text_year = int("20" + m.group(1))
            break
            
    # Fallback: search for 20xx in first 1000
    if not text_year:
        m = re.search(r'\b(20\d{2})\b', text[:1000])
        if m:
            text_year = int(m.group(1))

    # Decision logic
    pub_year = text_year if text_year else min_cit_year
    
    # If using min_cit_year, be conservative?
    # If min_cit_year is 2017, and text_year is None, assume 2017.
    
    if pub_year > 2016:
        # Check empirical
        if 'empirical' in text.lower():
            final_results.append({
                "title": title,
                "total_citation_count": total_count
            })

# Sort by title
final_results.sort(key=lambda x: x['title'])

print("__RESULT__:")
print(json.dumps(final_results))"""

env_args = {'var_function-call-3735696705524140447': 'file_storage/function-call-3735696705524140447.json', 'var_function-call-8426954921484076460': ['paper_docs'], 'var_function-call-8432852988790509735': [{'COUNT(*)': '1405'}], 'var_function-call-15575652384849502838': [], 'var_function-call-76014379587843141': 'file_storage/function-call-76014379587843141.json', 'var_function-call-15302473096394275436': 'file_storage/function-call-15302473096394275436.json', 'var_function-call-13901182043948570327': [], 'var_function-call-4571711046377204237': {'years_preview': [2015, None, None, None, None], 'total_papers': 5, 'empirical_in_first_20': 2}, 'var_function-call-11974208795470481837': 'file_storage/function-call-11974208795470481837.json', 'var_function-call-11808156953399460104': [], 'var_function-call-12413501451811374278': 'file_storage/function-call-12413501451811374278.json'}

exec(code, env_args)
