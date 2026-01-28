code = """import json, re

# Access variables safely
available = locals()
citations_key = None
papers_key = None

for key in available:
    if 'query_db:22' in key:
        citations_key = key
    if 'query_db:23' in key:
        papers_key = key

if citations_key and papers_key:
    citations_path = available[citations_key]
    papers_path = available[papers_key]
    
    # Read files
    citations_data = json.load(open(citations_path)) if isinstance(citations_path, str) else []
    papers_data = json.load(open(papers_path)) if isinstance(papers_path, str) else []
    
    # Build citation lookup
    cites = {}
    for item in citations_data:
        title = item.get('title', '').lower().strip()
        count = int(item.get('citation_count', 0))
        cites[title] = count
    
    # Process CHI papers
    total = 0
    chi_papers = 0
    
    for paper in papers_data:
        fname = paper.get('filename', '')
        if not fname:
            continue
            
        if 'chi' in fname.lower():
            title = fname.replace('.txt', '').lower().strip()
            if title in cites:
                total += cites[title]
                chi_papers += 1
    
    result = {'total_2020_citations': total, 'chi_papers_cited': chi_papers}
else:
    result = {'error': 'Variables not found'}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.list_db:1': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:15': 'file_storage/functions.query_db:15.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:23': 'file_storage/functions.query_db:23.json', 'var_functions.execute_python:26': {'available_variables': ['var_functions.query_db:4', 'var_functions.query_db:5', 'var_functions.query_db:10', 'var_functions.query_db:11', 'var_functions.query_db:14', 'var_functions.query_db:15', 'var_functions.query_db:20', 'var_functions.query_db:22', 'var_functions.query_db:23'], 'all_locals': ['var_functions.list_db:0', 'var_functions.list_db:1', 'var_functions.query_db:4', 'var_functions.query_db:5', 'var_functions.query_db:10', 'var_functions.query_db:11', 'var_functions.query_db:14', 'var_functions.query_db:15', 'var_functions.query_db:20', 'var_functions.query_db:22', 'var_functions.query_db:23', '__builtins__', 'json', 'available_vars']}}

exec(code, env_args)
