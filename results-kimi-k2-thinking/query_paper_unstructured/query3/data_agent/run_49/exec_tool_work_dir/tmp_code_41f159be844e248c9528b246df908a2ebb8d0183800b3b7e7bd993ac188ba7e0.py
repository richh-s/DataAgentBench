code = """import json
import re

# Get the file path
file_path_key = 'var_functions.query_db:2'
file_path = locals().get(file_path_key, '')

if not file_path:
    print('__RESULT__:')
    print(json.dumps({'error': 'File path not found'}))
else:
    # Read the file
    with open(file_path, 'r') as f:
        papers_data = json.load(f)
    
    # Extract papers with empirical contribution and year > 2016
    empirical_papers = []
    
    for paper in papers_data:
        filename = paper.get('filename', '')
        text = paper.get('text', '')
        
        # Extract title
        title = filename.replace('.txt', '')
        
        # Extract year from text
        year_match = re.search(r'(19|20)\d{2}', text)
        year = int(year_match.group()) if year_match else None
        
        # Check if paper mentions empirical contribution
        if year and year > 2016:
            # Check if text contains mention of empirical work
            if re.search(r'empirical', text, re.IGNORECASE):
                empirical_papers.append({
                    'title': title,
                    'year': year,
                    'filename': filename
                })
    
    result = {
        'count': len(empirical_papers),
        'papers': empirical_papers
    }
    
    print('__RESULT__:')
    print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
