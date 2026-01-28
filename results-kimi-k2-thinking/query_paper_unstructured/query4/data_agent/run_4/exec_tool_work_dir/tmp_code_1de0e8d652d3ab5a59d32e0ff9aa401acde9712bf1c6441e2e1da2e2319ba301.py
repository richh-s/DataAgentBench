code = """import json
import re

# Get the paper documents data from storage
file_path = locals()['var_functions.query_db:8']

# Read and process the data
with open(file_path, 'r') as f:
    paper_docs = json.load(f)

print(f"Total paper documents: {len(paper_docs)}")

# Process papers to extract information
papers_2016_pa = []

for doc in paper_docs:
    text = doc['text']
    filename = doc['filename']
    title = filename.replace('.txt', '')
    
    # Extract year from text
    year = None
    # Look for copyright year first
    copyright_match = re.search(r'Copyright\s*[@©]?\s*(20\d{2})', text)
    if copyright_match:
        year = int(copyright_match.group(1))
    else:
        # Look for 4-digit year patterns
        year_match = re.search(r'\b(20\d{2})\b', text)
        if year_match:
            year = int(year_match.group(1))
    
    # Check if domain includes physical activity
    text_lower = text.lower()
    has_physical_activity = False
    pa_keywords = ['physical activity', 'physical activities', 'fitness', 'exercise', 'workout']
    
    for keyword in pa_keywords:
        if keyword in text_lower:
            has_physical_activity = True
            break
    
    if year == 2016 and has_physical_activity:
        papers_2016_pa.append({
            'title': title,
            'year': year,
            'filename': filename
        })

print(f"Papers from 2016 in physical activity domain: {len(papers_2016_pa)}")

if papers_2016_pa:
    print("Paper titles:")
    for p in papers_2016_pa:
        print(f"  - {p['title']}")

# Prepare results for citation lookup
result = {
    'paper_titles': [p['title'] for p in papers_2016_pa],
    'papers': papers_2016_pa
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
