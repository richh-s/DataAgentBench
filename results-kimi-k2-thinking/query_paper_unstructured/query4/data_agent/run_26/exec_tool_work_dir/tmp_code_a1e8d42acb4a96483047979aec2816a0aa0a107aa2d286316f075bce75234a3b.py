code = """import json
import re

# Let's read the query result
with open('var_functions.query_db:22.json', 'r') as f:
    papers = json.load(f)

print('Total papers found:', len(papers))

# Function to extract year from a paper's text
def extract_year(text):
    # Look for venue + year patterns
    patterns = ['CHI', 'CSCW', 'DIS', 'TEI', 'IUI', 'WWW', 'UbiComp', 'Ubicomp', 'PervasiveHealth', 'ICHI', 'JMIR', 'AMIA']
    for pattern in patterns:
        match = re.search(pattern + r'\s*\'?.?\s*(\d{4})', text, re.IGNORECASE)
        if match:
            year = int(match.group(1))
            if 2010 <= year <= 2025:
                return year
    
    # Look for year in first 500 chars as fallback
    general_match = re.search(r'\b(20\d{2})\b', text[:1000])
    if general_match:
        year = int(general_match.group(1))
        if 2010 <= year <= 2025:
            return year
    
    return None

# Function to check if paper mentions physical activity
def mentions_physical_activity(text):
    patterns = ['physical activity', 'fitness', 'exercise', 'workout']
    text_lower = text.lower()
    for pattern in patterns:
        if pattern in text_lower:
            return True
    return False

# Analyze papers
papers_2016_physical_activity = []
for paper in papers:
    text = paper.get('text', '')
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '') if filename else 'Unknown'
    
    year = extract_year(text)
    is_physical_activity = mentions_physical_activity(text)
    
    if year == 2016 and is_physical_activity:
        papers_2016_physical_activity.append({
            'title': title,
            'year': year,
            'filename': filename
        })

print('Papers from 2016 in physical activity domain:', len(papers_2016_physical_activity))
for p in papers_2016_physical_activity:
    print('  -', p['title'])

with open('papers_2016.json', 'w') as f:
    json.dump(papers_2016_physical_activity, f)

print('__RESULT__:')
print(json.dumps({'count': len(papers_2016_physical_activity), 'papers': papers_2016_physical_activity}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:12': [{'total_records': '1405'}], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json'}

exec(code, env_args)
