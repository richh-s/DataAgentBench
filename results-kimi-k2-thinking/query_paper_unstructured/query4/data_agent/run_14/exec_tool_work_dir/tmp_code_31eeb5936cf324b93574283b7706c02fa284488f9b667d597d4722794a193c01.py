code = """import json

# Get the full MongoDB data
mongo_result_path = locals()['var_functions.query_db:2']
with open(mongo_result_path, 'r') as f:
    papers = json.load(f)

print('Analyzing papers to extract metadata...')

papers_metadata = []

for paper in papers:
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    text = paper.get('text', '')
    
    # Extract year from text (look for patterns like 2016, 2015, etc.)
    # Look for patterns near conference/journal names
    year = None
    text_lines = text.split('\n')
    for line in text_lines[:20]:  # Check first 20 lines for year
        line_upper = line.upper()
        if '2016' in line_upper and ('CONF' in line_upper or 'JOURNAL' in line_upper or 'PROCEEDINGS' in line_upper):
            year = 2016
            break
        elif '2015' in line_upper and ('CONF' in line_upper or 'JOURNAL' in line_upper or 'PROCEEDINGS' in line_upper):
            year = 2015
            break
        elif '2014' in line_upper and ('CONF' in line_upper or 'JOURNAL' in line_upper or 'PROCEEDINGS' in line_upper):
            year = 2014
            break
        elif '2017' in line_upper and ('CONF' in line_upper or 'JOURNAL' in line_upper or 'PROCEEDINGS' in line_upper):
            year = 2017
            break
    
    # Extract domain from text - check for 'physical activity' or related domains
    text_lower = text.lower()
    domain = []
    if 'physical activity' in text_lower or 'fitness' in text_lower or 'exercise' in text_lower:
        domain.append('physical activity')
    if 'food' in text_lower or 'diet' in text_lower or 'nutrition' in text_lower:
        domain.append('food')
    if 'sleep' in text_lower:
        domain.append('sleep')
    if 'finances' in text_lower or 'financial' in text_lower:
        domain.append('finances')
    if 'mental health' in text_lower or 'stress' in text_lower:
        domain.append('mental')
    
    # Extract venue (common venues mentioned in the prompt)
    venue = []
    if 'chi' in text_lower:
        venue.append('CHI')
    if 'ubicomp' in text_lower or 'ubicomp' in text_lower:
        venue.append('Ubicomp')
    if 'cscw' in text_lower:
        venue.append('CSCW')
    if 'dis' in text_lower:
        venue.append('DIS')
    if 'pervasivehealth' in text_lower:
        venue.append('PervasiveHealth')
    if 'www' in text_lower and 'http' not in text_lower:
        venue.append('WWW')
    if 'iui' in text_lower:
        venue.append('IUI')
    
    # Extract source/publisher
    source = []
    if 'acm' in text_lower:
        source.append('ACM')
    if 'ieee' in text_lower:
        source.append('IEEE')
    if 'pubmed' in text_lower:
        source.append('PubMed')
    
    # Extract contribution type
    contribution = []
    if 'empirical' in text_lower or 'study' in text_lower or 'survey' in text_lower:
        contribution.append('empirical')
    if 'artifact' in text_lower or 'prototype' in text_lower or 'system' in text_lower:
        contribution.append('artifact')
    if 'theoretical' in text_lower or 'model' in text_lower:
        contribution.append('theoretical')
    if 'methodological' in text_lower:
        contribution.append('methodological')
    
    papers_metadata.append({
        'title': title,
        'year': year,
        'domain': domain,
        'venue': venue,
        'source': source,
        'contribution': contribution
    })

# Filter papers from 2016 with 'physical activity' domain
papers_2016_physical_activity = []
for paper in papers_metadata:
    if paper['year'] == 2016 and 'physical activity' in paper['domain']:
        papers_2016_physical_activity.append(paper)

print('Found papers for 2016 physical activity domain:', len(papers_2016_physical_activity))
for paper in papers_2016_physical_activity:
    print('  - ' + paper['title'])

# Store results
result = {
    'all_papers': papers_metadata,
    'papers_2016_physical_activity': papers_2016_physical_activity
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:10': {'paper_count': 5, 'sample_keys': ['_id', 'filename', 'text'], 'sample_filename': 'A Lived Informatics Model of Personal Informatics.txt'}}

exec(code, env_args)
