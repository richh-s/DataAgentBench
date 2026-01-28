code = """import json
import re

# Read the MongoDB data from the file
with open('var_functions.query_db:2', 'r') as f:
    papers_data = json.load(f)

# Extract paper information from the documents
papers = []
for doc in papers_data:
    filename = doc.get('filename', '')
    text = doc.get('text', '')
    
    # Extract title from filename (remove .txt extension)
    title = filename.replace('.txt', '') if filename else ''
    
    # Extract year from text - look for 4-digit years around 2015-2025
    year_match = re.search(r'(20(?:1[5-9]|2[0-5]))', text)
    year = int(year_match.group(1)) if year_match else None
    
    # Extract contribution type - look for empirical, artifact, theoretical, survey, methodological
    contribution = None
    text_lower = text.lower()
    
    # Check for contribution types
    if 'empirical' in text_lower:
        contribution = 'empirical'
    elif 'artifact' in text_lower:
        contribution = 'artifact'
    elif 'theoretical' in text_lower:
        contribution = 'theoretical'
    elif 'survey' in text_lower:
        contribution = 'survey'
    elif 'methodological' in text_lower:
        contribution = 'methodological'
    
    papers.append({
        'title': title,
        'year': year,
        'contribution': contribution
    })

# Filter papers with empirical contribution published after 2016
empirical_papers_after_2016 = [
    p for p in papers 
    if p['contribution'] == 'empirical' and p['year'] and p['year'] > 2016
]

print('__RESULT__:')
print(json.dumps({
    'empirical_papers_after_2016': empirical_papers_after_2016,
    'total_empirical_papers': len(empirical_papers_after_2016)
}))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
