code = """import json
import re
from collections import Counter

path_papers = locals()['var_function-call-11974208795470481837']
with open(path_papers, 'r') as f:
    papers = json.load(f)

stats = []
years = []
has_empirical_count = 0

for p in papers:
    text = p['text']
    
    # Same extraction logic
    year = None
    m = re.search(r'Copyright.*?20(\d{2})', text, re.IGNORECASE)
    if m: year = int("20" + m.group(1))
    
    if not year:
        header = text[:500]
        m_conf = re.search(r"(?:CHI|UbiComp|CSCW|DIS|IUI).*?'(\d{2})", header, re.IGNORECASE)
        if m_conf: year = int("20" + m_conf.group(1))
            
    if not year:
        m_year = re.search(r'\b(20\d{2})\b', text[:1000])
        if m_year: year = int(m_year.group(1))
            
    if not year:
        m_end = re.search(r'Copyright.*?20(\d{2})', text[-2000:], re.IGNORECASE)
        if m_end: year = int("20" + m_end.group(1))

    has_emp = 'empirical' in text.lower()
    
    stats.append({"y": year, "e": has_emp})
    if year: years.append(year)
    if has_emp: has_empirical_count += 1

print("__RESULT__:")
print(f"Years found: {Counter(years)}")
print(f"Papers with 'empirical': {has_empirical_count}")
print(f"Sample stats: {stats[:10]}")"""

env_args = {'var_function-call-3735696705524140447': 'file_storage/function-call-3735696705524140447.json', 'var_function-call-8426954921484076460': ['paper_docs'], 'var_function-call-8432852988790509735': [{'COUNT(*)': '1405'}], 'var_function-call-15575652384849502838': [], 'var_function-call-76014379587843141': 'file_storage/function-call-76014379587843141.json', 'var_function-call-15302473096394275436': 'file_storage/function-call-15302473096394275436.json', 'var_function-call-13901182043948570327': [], 'var_function-call-4571711046377204237': {'years_preview': [2015, None, None, None, None], 'total_papers': 5, 'empirical_in_first_20': 2}, 'var_function-call-11974208795470481837': 'file_storage/function-call-11974208795470481837.json', 'var_function-call-11808156953399460104': []}

exec(code, env_args)
