code = """# Read the full paper data from the file
import json

# Access the variable from storage
paper_data = locals()['var_functions.query_db:2']

# If it's a file path (string), read the file
if isinstance(paper_data, str):
    with open(paper_data, 'r') as f:
        paper_docs = json.load(f)
else:
    # Otherwise it's already the data
    paper_docs = paper_data

# Extract paper titles and publication years from the documents
papers_info = []
for doc in paper_docs:
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    
    # Extract year from the text - look for patterns like 'YYYY', 'YYYY.', or venue years
    text = doc.get('text', '')
    year = None
    
    # Try to find 4-digit year patterns
    import re
    year_matches = re.findall(r'(20\d{2})', text)
    if year_matches:
        # Take the earliest year found (most likely publication year)
        year = int(min(year_matches))
    
    # Extract contribution type from text - look for "empirical"
    contribution = ''
    if 'empirical' in text.lower():
        contribution = 'empirical'
    
    papers_info.append({
        'title': title,
        'year': year,
        'contribution': contribution,
        'filename': filename
    })

# Filter papers that are empirical and published after 2016
empirical_papers_after_2016 = [
    paper for paper in papers_info 
    if paper['contribution'] == 'empirical' and paper['year'] and paper['year'] > 2016
]

print('__RESULT__:')
print(json.dumps({
    'total_papers': len(paper_docs),
    'empirical_papers_after_2016_count': len(empirical_papers_after_2016),
    'sample_empirical_papers': empirical_papers_after_2016[:5]
}))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
