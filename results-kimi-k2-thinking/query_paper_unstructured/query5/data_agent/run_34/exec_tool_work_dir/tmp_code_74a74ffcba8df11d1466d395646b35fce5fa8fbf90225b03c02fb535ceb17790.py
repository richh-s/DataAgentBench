code = """import json
import re

chi_papers_data = locals()['var_functions.query_db:2']
chi_papers = []

for doc in chi_papers_data:
    filename = doc['filename']
    text = doc['text']
    title = filename.replace('.txt', '')
    
    chi_patterns = [r'CHI\s*\'?\d{2}', r'CHI\s*20\d{2}', r'CHI\s+Conference', r'Proceedings of the.*?CHI', r'ACM.*?CHI', r'CHI\s*\d{4}\s*Conference']
    
    is_chi = False
    for pattern in chi_patterns:
        if re.search(pattern, text, re.IGNORECASE):
            is_chi = True
            break
    
    if is_chi:
        chi_papers.append(title)

print('__RESULT__:')
print(json.dumps(chi_papers))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json'}

exec(code, env_args)
