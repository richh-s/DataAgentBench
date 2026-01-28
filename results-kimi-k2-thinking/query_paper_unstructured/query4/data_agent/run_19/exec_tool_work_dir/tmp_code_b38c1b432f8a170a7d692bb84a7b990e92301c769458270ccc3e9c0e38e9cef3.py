code = """import json, re

# Load the physical activity papers
mongo_path = locals()['var_functions.query_db:26']
with open(mongo_path, 'r') as f:
    papers = json.load(f)

# Load citation data
citation_path = locals()['var_functions.query_db:6']
with open(citation_path, 'r') as f:
    citation_data = json.load(f)

# Create citation lookup
citation_dict = {item['title']: int(item['total_citations']) for item in citation_data}

# Process papers to verify they're from 2016
result = []

for doc in papers:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '')
    
    # More robust year checking
    year = None
    
    # Look for copyright statement
    copyright_match = re.search(r'Copyright[^\n]{0,100}?(201\d)', text)
    if copyright_match:
        year = int(copyright_match.group(1))
    
    # Look for conference header patterns
    if not year:
        conf_match = re.search(r'(CHI|UbiComp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH|Ubicomp)\s*[-\'"]?\s*(201\d)', text, re.IGNORECASE)
        if conf_match:
            year = int(conf_match.group(2))
    
    # Look for proceedings patterns  
    if not year:
        proc_match = re.search(r'Proceedings[^\n]{0,100}?(201\d)', text)
        if proc_match:
            year = int(proc_match.group(1))
    
    # Only include if year is 2016
    if year == 2016:
        citations = citation_dict.get(title, 0)
        result.append({'title': title, 'total_citations': citations, 'publication_year': year})

# Sort by citations
result.sort(key=lambda x: x['total_citations'], reverse=True)

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:22': [], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json'}

exec(code, env_args)
