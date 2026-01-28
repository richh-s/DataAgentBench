code = """import json

# Access variables by constructing the variable name
var_name_32 = None
var_name_34 = None

# Find the right variable names
for name in dir():
    if 'query_db' in name and '32' in name:
        var_name_32 = name
    if 'query_db' in name and '34' in name:
        var_name_34 = name

print('Found variable names:', var_name_32, var_name_34)

# Load the data
citations_file_path = globals()[var_name_32]
papers_file_path = globals()[var_name_34]

with open(citations_file_path, 'r') as f:
    citations_data = json.load(f)

with open(papers_file_path, 'r') as f:
    papers_data = json.load(f)

# Find ACM papers
paper_sources = {}
for paper in papers_data:
    filename = paper.get('filename', '')
    title = filename[:-4] if filename.endswith('.txt') else filename
    text = paper.get('text', '')
    
    if 'ACM' in text:
        paper_sources[title] = 'ACM'

# Calculate statistics
acm_citations = []
all_citation_counts = []

for citation in citations_data:
    title = citation.get('title', '')
    count = int(citation.get('citation_count', 0))
    all_citation_counts.append(count)
    
    if title in paper_sources:
        acm_citations.append(count)

total_papers = len(citations_data)
acm_count = len(acm_citations)
avg_acm = sum(acm_citations) / acm_count if acm_count > 0 else 0
avg_all = sum(all_citation_counts) / len(all_citation_counts) if all_citation_counts else 0

result = {
    'total_papers': total_papers,
    'acm_papers': acm_count,
    'avg_acm_citations': round(avg_acm, 2),
    'avg_all_citations': round(avg_all, 2)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.execute_python:28': {'status': 'checking_variables'}, 'var_functions.execute_python:30': {'status': 'variable_check_complete'}, 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.execute_python:40': {'status': 'variable_search_complete'}}

exec(code, env_args)
