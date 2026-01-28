code = """import json
import re

# Read the paper documents file
paper_docs_file = locals()['var_functions.query_db:6']
with open(paper_docs_file, 'r') as f:
    paper_docs = json.load(f)

# Extract paper information
papers = []
for doc in paper_docs:
    filename = doc['filename']
    text = doc['text']
    
    # Extract title from filename (remove .txt extension)
    title = filename.replace('.txt', '')
    
    # Extract year from text - look for patterns like '2017', 'CHI 2017', etc.
    # Common patterns: year in header, in copyright, or in references
    year_match = re.search(r'(19|20)\d{2}', text)
    year = int(year_match.group()) if year_match else None
    
    # Check if paper has 'empirical' contribution by searching the text
    has_empirical = 'empirical' in text.lower()
    
    papers.append({
        'title': title,
        'year': year,
        'has_empirical': has_empirical,
        'text_preview': text[:500]  # Just for debugging
    })

# Filter papers with empirical contribution and published after 2016
empirical_papers = [p for p in papers if p['has_empirical'] and p['year'] and p['year'] > 2016]

print('__RESULT__:')
print(json.dumps({
    'total_papers': len(papers),
    'empirical_papers_count': len(empirical_papers),
    'empirical_papers': empirical_papers[:10]  # First 10 for preview
}, indent=2))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
