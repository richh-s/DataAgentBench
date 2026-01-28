code = """import json
import re

# Get file paths from variables (using direct assignment to avoid syntax issues)
citations_var = var_functions.query_db:22
papers_var = var_functions.query_db:23

# Ensure paths are clean strings
citations_path = str(citations_var).strip("'") if isinstance(citations_var, str) else str(citations_var)
papers_path = str(papers_var).strip("'") if isinstance(papers_var, str) else str(papers_var)

# Load data
citations_data = []
papers_data = []

# Try to load files
try:
    with open(citations_path, 'r') as f:
        citations_data = json.load(f)
except:
    pass

try:
    with open(papers_path, 'r') as f:
        papers_data = json.load(f)
except:
    pass

# Create citation dictionary
citation_counts = {}
for item in citations_data:
    title_key = item.get('title', '').lower().strip()
    count = int(item.get('citation_count', 0))
    citation_counts[title_key] = count

# Find CHI papers with citations
total = 0
chi_count = 0

for paper in papers_data:
    fname = paper.get('filename', '')
    txt = paper.get('text', '')
    
    if not fname or not txt:
        continue
    
    # Check for CHI
    is_chi = False
    if 'chi' in fname.lower():
        is_chi = True
    
    if not is_chi and re.search(r'CHI', txt, re.IGNORECASE):
        is_chi = True
    
    if is_chi:
        title_name = fname.replace('.txt', '')
        key = title_name.lower().strip()
        if key in citation_counts:
            total += citation_counts[key]
            chi_count += 1

result = {'total_citations': total, 'chi_papers_count': chi_count}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.list_db:1': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:15': 'file_storage/functions.query_db:15.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:23': 'file_storage/functions.query_db:23.json', 'var_functions.execute_python:26': {'available_variables': ['var_functions.query_db:4', 'var_functions.query_db:5', 'var_functions.query_db:10', 'var_functions.query_db:11', 'var_functions.query_db:14', 'var_functions.query_db:15', 'var_functions.query_db:20', 'var_functions.query_db:22', 'var_functions.query_db:23'], 'all_locals': ['var_functions.list_db:0', 'var_functions.list_db:1', 'var_functions.query_db:4', 'var_functions.query_db:5', 'var_functions.query_db:10', 'var_functions.query_db:11', 'var_functions.query_db:14', 'var_functions.query_db:15', 'var_functions.query_db:20', 'var_functions.query_db:22', 'var_functions.query_db:23', '__builtins__', 'json', 'available_vars']}}

exec(code, env_args)
