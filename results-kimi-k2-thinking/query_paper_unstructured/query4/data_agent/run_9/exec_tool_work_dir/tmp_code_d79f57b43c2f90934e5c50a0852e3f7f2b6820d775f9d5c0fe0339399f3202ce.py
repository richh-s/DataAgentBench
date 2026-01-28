code = """import json
import re

# Read all papers from the query result
result_path = var_functions.query_db:30
with open(result_path, 'r') as f:
    papers = json.load(f)

print(f"Total papers in database: {len(papers)}")

# Filter papers from 2016 in physical activity domain
papers_2016 = []

for paper in papers:
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '') if filename else 'Unknown'
    text = paper.get('text', '')
    
    # Check if paper is from 2016
    text_upper = text.upper()
    year_patterns = [
        '2016', 'CHI 2016', 'UBICOMP 2016', 'CSCW 2016', 
        'DIS 2016', 'PERVASIVEHEALTH 2016', 'WWW 2016', 
        'IUI 2016', 'OZCHI 2016', 'TEI 2016', 'AH 2016'
    ]
    
    is_2016 = any(pattern in text_upper for pattern in year_patterns)
    
    # Check if paper is in physical activity domain
    text_lower = text.lower()
    domain_keywords = ['physical activity', 'fitness', 'exercise', 'sedentary behavior']
    domain_score = sum(text_lower.count(keyword) for keyword in domain_keywords)
    
    if is_2016 and domain_score > 0:
        papers_2016.append({
            'title': title,
            'filename': filename,
            'domain_score': domain_score
        })

print(f"Found {len(papers_2016)} papers from 2016 in physical activity domain")
for paper in papers_2016:
    print(f"  - {paper['title']} (domain score: {paper['domain_score']})")

# Return the filtered papers for the next step
result = json.dumps(papers_2016)
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:6': [], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.list_db:14': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json'}

exec(code, env_args)
