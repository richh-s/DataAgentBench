code = """import json
import re

# Read the full paper_docs data
paper_docs_file = var_functions.query_db:2
with open(paper_docs_file, 'r') as f:
    paper_docs = json.load(f)

# Extract information from each paper
papers_info = []

for doc in paper_docs:
    filename = doc['filename']
    text = doc['text']
    
    # Extract title from filename
    title = filename.replace('.txt', '')
    
    # Extract year - look for patterns like '2016' in the text
    # Common patterns: year in conference headers, copyright lines, etc.
    year_match = re.search(r'(?:19|20)\d{2}', text)
    year = int(year_match.group()) if year_match else None
    
    # Extract domain - look for keywords related to domains
    # The text should mention the domain
    domains = []
    text_lower = text.lower()
    
    # Check for physical activity domain
    if 'physical activity' in text_lower or 'fitness' in text_lower or 'exercise' in text_lower:
        domains.append('physical activity')
    
    # Check for other domains mentioned in the hints
    if 'food' in text_lower or 'diet' in text_lower or 'eating' in text_lower:
        domains.append('food')
    if 'sleep' in text_lower:
        domains.append('sleep')
    if 'mental' in text_lower or 'anxiety' in text_lower or 'depression' in text_lower:
        domains.append('mental')
    if 'finances' in text_lower or 'financial' in text_lower:
        domains.append('finances')
    if 'productivity' in text_lower:
        domains.append('productivity')
    if 'screen time' in text_lower:
        domains.append('screen time')
    if 'social' in text_lower:
        domains.append('social interactions')
    if 'location' in text_lower:
        domains.append('location')
    if 'chronic' in text_lower:
        domains.append('chronic')
    if 'diabetes' in text_lower:
        domains.append('diabetes')
    if 'health behavior' in text_lower:
        domains.append('health_behavior')
    
    papers_info.append({
        'title': title,
        'year': year,
        'domains': domains,
        'filename': filename
    })

# Filter papers from 2016 with physical activity domain
papers_2016_physical = [p for p in papers_info if p['year'] == 2016 and 'physical activity' in p['domains']]

print('__RESULT__:')
print(json.dumps(papers_2016_physical, indent=2))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
