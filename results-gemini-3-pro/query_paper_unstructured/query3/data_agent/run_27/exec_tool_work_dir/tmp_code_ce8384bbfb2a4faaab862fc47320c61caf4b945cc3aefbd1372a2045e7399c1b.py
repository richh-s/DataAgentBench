code = """import json
import re

# Load citations
path_cit = locals()['var_function-call-76014379587843141']
with open(path_cit, 'r') as f:
    citations_list = json.load(f)

# Map title -> count
cit_map = {}
for item in citations_list:
    t = item['title']
    c = int(item['total_citations'])
    cit_map[t] = c

# Load papers
path_papers = locals()['var_function-call-11974208795470481837']
with open(path_papers, 'r') as f:
    papers = json.load(f)

results = []
debug_info = []

for p in papers:
    title = p['filename'].replace('.txt', '')
    text = p['text']
    
    # Year extraction strategy
    year = None
    
    # 1. Look for Copyright 20xx
    m = re.search(r'Copyright.*?20(\d{2})', text, re.IGNORECASE)
    if m:
        year = int("20" + m.group(1))
    
    # 2. Look for conference header patterns in first 500 chars
    if not year:
        header = text[:500]
        # Match "CHI '19" or "UbiComp '18"
        m_conf = re.search(r"(?:CHI|UbiComp|CSCW|DIS|IUI).*?'(\d{2})", header, re.IGNORECASE)
        if m_conf:
            year = int("20" + m_conf.group(1))
            
    # 3. Look for any 20xx in first 1000 chars
    if not year:
        m_year = re.search(r'\b(20\d{2})\b', text[:1000])
        if m_year:
            year = int(m_year.group(1))
            
    # 4. Look for Copyright at the end
    if not year:
        m_end = re.search(r'Copyright.*?20(\d{2})', text[-2000:], re.IGNORECASE)
        if m_end:
            year = int("20" + m_end.group(1))

    # Store for debug
    if year and year > 2016:
        # Check contribution
        is_empirical = False
        if 'empirical' in text.lower():
            is_empirical = True
        
        if is_empirical:
            count = cit_map.get(title, 0)
            results.append({
                "title": title,
                "total_citation_count": count
            })
    
    if not year:
        debug_info.append(title)

# Sort by count desc
results.sort(key=lambda x: x['total_citation_count'], reverse=True)

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-3735696705524140447': 'file_storage/function-call-3735696705524140447.json', 'var_function-call-8426954921484076460': ['paper_docs'], 'var_function-call-8432852988790509735': [{'COUNT(*)': '1405'}], 'var_function-call-15575652384849502838': [], 'var_function-call-76014379587843141': 'file_storage/function-call-76014379587843141.json', 'var_function-call-15302473096394275436': 'file_storage/function-call-15302473096394275436.json', 'var_function-call-13901182043948570327': [], 'var_function-call-4571711046377204237': {'years_preview': [2015, None, None, None, None], 'total_papers': 5, 'empirical_in_first_20': 2}, 'var_function-call-11974208795470481837': 'file_storage/function-call-11974208795470481837.json'}

exec(code, env_args)
