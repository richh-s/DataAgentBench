code = """import json
import re

# Read the query result file
result_file = 'var_functions.query_db:22.json'
trees = []
with open(result_file, 'r') as f:
    papers = json.load(f)

print('Total papers retrieved:', len(papers))

# Initialize counters and storage
papers_2016_physical_activity = []

# Function to extract year from venue patterns
def extract_year_from_text(text):
    venue_patterns = ['CHI', 'CSCW', 'DIS', 'TEI', 'IUI', 'WWW', 'Ubicomp', 'UbiComp', 'PervasiveHealth', 'ICHI', 'JMIR', 'AMIA', 'HCI International']
    for pattern in venue_patterns:
        match = re.search(pattern + r"[^\d]*\d{4}", text, re.IGNORECASE)
        if match:
            year_match = re.search(r"(20\d{2})", match.group())
            if year_match:
                year = int(year_match.group(1))
                if 2010 <= year <= 2025:
                    return year
    return None

# Check each paper
for paper in papers:
    text = paper.get('text', '')
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '')
    
    # Extract year
    year = extract_year_from_text(text)
    
    # Check if mentions physical activity
    mentions_physical_activity = 'physical activity' in text.lower()
    
    if year == 2016 and mentions_physical_activity:
        papers_2016_physical_activity.append({
            'title': title,
            'year': year
        })

print('Found', len(papers_2016_physical_activity), 'papers from 2016 in physical activity domain')
for p in papers_2016_physical_activity:
    print('  -', p['title'])

# Save to file for next step
with open('papers_2016.json', 'w') as f:
    json.dump(papers_2016_physical_activity, f)

print('__RESULT__:')
print(json.dumps(papers_2016_physical_activity))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:12': [{'total_records': '1405'}], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json'}

exec(code, env_args)
