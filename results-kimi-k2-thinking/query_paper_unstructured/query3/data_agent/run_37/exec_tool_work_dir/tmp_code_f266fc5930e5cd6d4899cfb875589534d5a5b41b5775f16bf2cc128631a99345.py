code = """import json
import re

# Read the MongoDB query results from the file
result_file = var_functions.query_db:2

# Load the full result
with open(result_file, 'r') as f:
    papers = json.load(f)

# Extract relevant information from each paper
paper_info = []

for paper in papers:
    filename = paper.get('filename', '')
    text = paper.get('text', '')
    
    # Extract title from filename (remove .txt extension)
    title = filename[:-4] if filename.endswith('.txt') else filename
    
    # Extract year from text - look for 4-digit years starting with 20
    year = None
    year_match = re.search(r'\\b(20\\d{2})\\b', text[:2000])
    if year_match:
        year = int(year_match.group(1))
    
    # Check for empirical contribution in first 3000 characters
    has_empirical = False
    text_to_search = text[:3000].lower()
    
    # Look for contribution and empirical together
    contrib_patterns = [
        r'contribution[^\\n]*empirical',
        r'empirical[^\\n]*contribution',
        r'empirical study',
        r'empirical research',
        r'empirical investigation'
    ]
    
    for pattern in contrib_patterns:
        if re.search(pattern, text_to_search):
            has_empirical = True
            break
    
    # Check for empirical in context of this paper's work
    if not has_empirical and 'empirical' in text_to_search:
        # Look for first-person or possessive indicators
        context_patterns = [
            r'we conducted[^\\n]*empirical',
            r'our empirical',
            r'this empirical',
            r'an empirical study',
            r'empirical data',
            r'empirical results'
        ]
        for pattern in context_patterns:
            if re.search(pattern, text_to_search):
                has_empirical = True
                break
    
    # Only include papers with valid data
    if title and year and has_empirical:
        paper_info.append({
            'title': title,
            'year': year,
            'has_empirical': has_empirical
        })

# Filter for papers published after 2016
filtered = [p for p in paper_info if p['year'] > 2016]
print('__RESULT__:')
print(json.dumps({
    'extracted_count': len(paper_info),
    'filtered_count': len(filtered),
    'sample_filtered': filtered[:3]
}))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
