code = """import json

# Load the paper data from MongoDB
mongo_result_path = locals()['var_functions.query_db:2']
with open(mongo_result_path, 'r') as f:
    papers = json.load(f)

papers_metadata = []

for paper in papers:
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    text = paper.get('text', '')
    
    # Initialize default values
    year = None
    domain = []
    venue = []
    source = []
    contribution = []
    
    # Extract year from text
    text_upper = text.upper()
    if '2016' in text_upper:
        year = 2016
    elif '2015' in text_upper:
        year = 2015
    elif '2014' in text_upper:
        year = 2014
    elif '2017' in text_upper:
        year = 2017
    
    # Extract domain
    text_lower = text.lower()
    if 'physical activity' in text_lower or 'fitness' in text_lower:
        domain.append('physical activity')
    if 'food' in text_lower or 'diet' in text_lower:
        domain.append('food')
    if 'sleep' in text_lower:
        domain.append('sleep')
    if 'finances' in text_lower or 'financial' in text_lower:
        domain.append('finances')
    if 'mental health' in text_lower or 'stress' in text_lower:
        domain.append('mental')
    
    # Extract venue
    if 'chi' in text_lower:
        venue.append('CHI')
    if 'ubicomp' in text_lower:
        venue.append('Ubicomp')
    if 'cscw' in text_lower:
        venue.append('CSCW')
    
    # Extract source
    if 'acm' in text_lower:
        source.append('ACM')
    if 'ieee' in text_lower:
        source.append('IEEE')
    
    # Extract contribution
    if 'empirical' in text_lower or 'study' in text_lower or 'survey' in text_lower:
        contribution.append('empirical')
    if 'prototype' in text_lower or 'system' in text_lower or 'artifact' in text_lower:
        contribution.append('artifact')
    if 'model' in text_lower or 'theoretical' in text_lower:
        contribution.append('theoretical')
    
    papers_metadata.append({
        'title': title,
        'year': year,
        'domain': domain,
        'venue': venue,
        'source': source,
        'contribution': contribution
    })

# Filter for 2016 physical activity papers
papers_2016 = []
for p in papers_metadata:
    if p['year'] == 2016 and 'physical activity' in p['domain']:
        papers_2016.append(p)

print('Found total papers:', len(papers_metadata))
print('Papers from 2016 in physical activity domain:', len(papers_2016))

output = {
    'all_papers': papers_metadata,
    'papers_2016_physical_activity': papers_2016
}

print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:10': {'paper_count': 5, 'sample_keys': ['_id', 'filename', 'text'], 'sample_filename': 'A Lived Informatics Model of Personal Informatics.txt'}}

exec(code, env_args)
