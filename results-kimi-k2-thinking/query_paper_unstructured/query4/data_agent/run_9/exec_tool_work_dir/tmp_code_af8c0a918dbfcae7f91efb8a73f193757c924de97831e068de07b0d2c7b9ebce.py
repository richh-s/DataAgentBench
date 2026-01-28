code = """import json
import re

result_path = var_functions.query_db:30
with open(result_path, 'r') as f:
    papers = json.load(f)

papers_2016 = []

for paper in papers:
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '') if filename else 'Unknown'
    text = paper.get('text', '')
    
    text_upper = text.upper()
    is_2016 = '2016' in text_upper or 'CHI 2016' in text_upper
    
    text_lower = text.lower()
    domain_score = text_lower.count('physical activity')
    
    if is_2016 and domain_score > 0:
        papers_2016.append({
            'title': title,
            'filename': filename,
            'domain_score': domain_score
        })

for paper in papers_2016:
    print('Title:', paper['title'])

result = json.dumps(papers_2016)
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:6': [], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.list_db:14': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json'}

exec(code, env_args)
