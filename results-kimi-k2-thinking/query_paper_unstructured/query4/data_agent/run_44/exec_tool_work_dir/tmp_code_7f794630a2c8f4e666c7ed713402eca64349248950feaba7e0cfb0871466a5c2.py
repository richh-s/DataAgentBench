code = """import json
import re

# Try to get the file path from storage
paper_docs_file = locals()['var_functions.query_db:2']

# Read the paper documents
with open(paper_docs_file, 'r') as f:
    paper_docs = json.load(f)

# Alternative: if the above doesn't work, we need a different approach
# For now, let's try processing what's available
papers_info = []

for doc in paper_docs:
    filename = doc['filename']
    text = doc.get('text', '')
    
    # Extract title from filename
    title = filename.replace('.txt', '')
    
    # Extract year - look for 4-digit year patterns
    year_match = re.search(r'(?:19|20)\d{2}', text)
    year = int(year_match.group()) if year_match else None
    
    # Extract domain information
    domains = []
    text_lower = text.lower()
    
    # Check for physical activity related keywords
    activity_keywords = ['physical activity', 'fitness', 'exercise', 'activity tracking', 
                        'workout', 'steps', 'walking', 'running', 'fitness tracker']
    
    for keyword in activity_keywords:
        if keyword in text_lower:
            domains.append('physical activity')
            break
    
    papers_info.append({
        'title': title,
        'year': year,
        'domains': domains,
        'filename': filename
    })

# Filter papers from 2016 in physical activity domain
papers_2016_physical = [p for p in papers_info if p['year'] == 2016 and 'physical activity' in p['domains']]

print('__RESULT__:')
print(json.dumps(papers_2016_physical, indent=2))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
