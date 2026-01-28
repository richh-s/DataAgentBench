code = """import json

# Store keys from locals - avoid iterating over changing dict
keys = list(locals().keys())

citations_path = None
papers_path = None

for key in keys:
    if 'query_db:22' in key:
        citations_path = locals()[key]
    if 'query_db:23' in key:
        papers_path = locals()[key]

# Load data
citations_data = json.load(open(citations_path))
papers_data = json.load(open(papers_path))

# Build citation dictionary
citation_dict = {}
for item in citations_data:
    title = item.get('title', '').lower().strip()
    count = int(item.get('citation_count', 0))
    citation_dict[title] = count

# Find CHI papers and sum citations
total_citations = 0
chi_paper_count = 0

def is_chi_paper(paper):
    fname = paper.get('filename', '')
    txt = paper.get('text', '')
    if not fname:
        return False
    if 'chi' in fname.lower():
        return True
    if txt and 'CHI' in txt:
        return True
    return False

for paper in papers_data:
    if is_chi_paper(paper):
        title = paper['filename'].replace('.txt', '').lower().strip()
        if title in citation_dict:
            total_citations += citation_dict[title]
            chi_paper_count += 1

result = {
    'total_citation_count': total_citations,
    'chi_papers_cited': chi_paper_count
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.list_db:1': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:15': 'file_storage/functions.query_db:15.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:23': 'file_storage/functions.query_db:23.json', 'var_functions.execute_python:26': {'available_variables': ['var_functions.query_db:4', 'var_functions.query_db:5', 'var_functions.query_db:10', 'var_functions.query_db:11', 'var_functions.query_db:14', 'var_functions.query_db:15', 'var_functions.query_db:20', 'var_functions.query_db:22', 'var_functions.query_db:23'], 'all_locals': ['var_functions.list_db:0', 'var_functions.list_db:1', 'var_functions.query_db:4', 'var_functions.query_db:5', 'var_functions.query_db:10', 'var_functions.query_db:11', 'var_functions.query_db:14', 'var_functions.query_db:15', 'var_functions.query_db:20', 'var_functions.query_db:22', 'var_functions.query_db:23', '__builtins__', 'json', 'available_vars']}}

exec(code, env_args)
