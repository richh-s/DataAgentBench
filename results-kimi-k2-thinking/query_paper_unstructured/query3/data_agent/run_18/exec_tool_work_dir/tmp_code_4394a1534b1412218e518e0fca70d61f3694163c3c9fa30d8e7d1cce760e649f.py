code = """import json
import re
import os

# Read the paper data from the file
file_path = '/tmp/tmpld3w_0o1.json'
with open(file_path, 'r') as f:
    papers = json.load(f)

print('Number of papers:', len(papers))

# Function to extract year from text
def extract_year(text):
    year_matches = re.findall(r'\b(20[0-9]{2})\b', text)
    if year_matches:
        return int(year_matches[0])
    return None

# Function to extract contribution type
def extract_contribution(text):
    text_lower = text.lower()
    contributions = []
    
    if 'empirical' in text_lower:
        contributions.append('empirical')
    if 'artifact' in text_lower:
        contributions.append('artifact')
    if 'theoretical' in text_lower:
        contributions.append('theoretical')
    if 'survey' in text_lower:
        contributions.append('survey')
    if 'methodological' in text_lower:
        contributions.append('methodological')
    
    return contributions

# Extract information from each paper
paper_info = []
for paper in papers:
    title = paper['filename'].replace('.txt', '')
    year = extract_year(paper['text'])
    contributions = extract_contribution(paper['text'])
    
    paper_info.append({
        'title': title,
        'year': year,
        'contributions': contributions
    })

# Filter for papers after 2016 with empirical contribution
filtered_papers = [
    p for p in paper_info 
    if p['year'] and p['year'] > 2016 and 'empirical' in p['contributions']
]

print('Total papers:', len(paper_info))
print('Papers after 2016 with empirical contribution:', len(filtered_papers))

# Prepare result
result = {'filtered_papers': filtered_papers}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json'}

exec(code, env_args)
