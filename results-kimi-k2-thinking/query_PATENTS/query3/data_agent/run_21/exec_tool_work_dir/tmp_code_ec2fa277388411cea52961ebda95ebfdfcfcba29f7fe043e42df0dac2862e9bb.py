code = """import json
import re

# Access the storage variable properly
storage_key = 'var_functions.query_db:6'
if storage_key in locals():
    file_path = locals()[storage_key]
    if isinstance(file_path, str) and file_path.endswith('.json'):
        with open(file_path, 'r') as f:
            california_patents = json.load(f)
    else:
        california_patents = file_path
else:
    california_patents = []

# Debug info
assignees = []
for patent in california_patents:
    info_str = patent.get('Patents_info', '')
    
    # Look for assignee extraction
    patterns = [
        r'(?:owned by|assigned to|holds|is owned by|is assigned to|is held by)\s+([A-Z][A-Z0-9\s\.\,&\(\)\-]+?)(?:\.|,|\sand\s|\sor\s|\swith\s|\swhich\s|\shas\s)',
        r'by\s+([A-Z][A-Z0-9\s\.\,&\(\)\-]+?)\s+(?:holds|owns|is assigned|has)'
    ]
    
    assignee = None
    for pattern in patterns:
        matches = re.findall(pattern, info_str, re.IGNORECASE)
        if matches:
            assignee = matches[0].strip()
            break
    
    if assignee:
        assignees.append(assignee)

result = {
    'total_patents': len(california_patents),
    'sample_assignees': assignees[:10]
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.list_db:11': ['cpc_definition']}

exec(code, env_args)
