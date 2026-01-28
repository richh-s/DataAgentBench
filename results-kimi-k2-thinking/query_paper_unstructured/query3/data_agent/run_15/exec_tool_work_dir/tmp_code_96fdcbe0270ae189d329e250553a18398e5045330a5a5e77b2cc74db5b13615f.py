code = """import json
import re

# Load the papers data from the file
papers_file = var_functions.query_db:8
with open(papers_file, 'r') as f:
    papers_data = json.load(f)

# Parse paper information from text
parsed_papers = []

for paper in papers_data:
    text = paper.get('text', '')
    filename = paper.get('filename', '')
    
    # Extract title from filename
    title = filename.replace('.txt', '') if filename else ''
    
    # Extract year - look for 4-digit year patterns commonly found in citations
    year_match = re.search(r'(?:\'|\")(\d{2}),\s*(20\d{2})', text)
    if not year_match:
        # Try alternative patterns
        year_match = re.search(r'(20\d{2})', text)
    
    year = None
    if year_match:
        try:
            year = int(year_match.group(1)) if len(year_match.group(1)) == 4 else int('20' + year_match.group(1))
            if year < 2000 or year > 2025:  # Validate reasonable year range
                year = None
        except:
            year = None
    
    # Extract contribution type - look for empirical, artifact, theoretical, survey, methodological
    contribution = None
    text_lower = text.lower()
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
    
    # Extract venue
    venue = None
    if 'CHI' in text or 'chi' in filename.lower():
        venue = 'CHI'
    elif 'Ubicomp' in text or 'ubicomp' in text or 'UbiComp' in text:
        venue = 'Ubicomp'
    elif 'CSCW' in text:
        venue = 'CSCW'
    elif 'DIS' in text:
        venue = 'DIS'
    elif 'PervasiveHealth' in text:
        venue = 'PervasiveHealth'
    elif 'WWW' in text:
        venue = 'WWW'
    elif 'IUI' in text:
        venue = 'IUI'
    elif 'OzCHI' in text:
        venue = 'OzCHI'
    elif 'TEI' in text:
        venue = 'TEI'
    elif 'AH' in text:
        venue = 'AH'
    
    # Extract source/publisher
    source = None
    if 'ACM' in text:
        source = 'ACM'
    elif 'IEEE' in text:
        source = 'IEEE'
    elif 'PubMed' in text:
        source = 'PubMed'
    
    # Extract domain
    domains = []
    if 'food' in text_lower:
        domains.append('food')
    if 'physical activity' in text_lower or 'fitness' in text_lower:
        domains.append('physical activity')
    if 'sleep' in text_lower:
        domains.append('sleep')
    if 'mental' in text_lower or 'psychology' in text_lower:
        domains.append('mental')
    if 'finances' in text_lower or 'financial' in text_lower:
        domains.append('finances')
    if 'productivity' in text_lower:
        domains.append('productivity')
    if 'screen time' in text_lower:
        domains.append('screen time')
    if 'social interaction' in text_lower:
        domains.append('social interactions')
    if 'location' in text_lower:
        domains.append('location')
    if 'diabetes' in text_lower:
        domains.append('diabetes')
    if 'chronic' in text_lower:
        domains.append('chronic')
    
    domain = ','.join(domains) if domains else None
    
    parsed_papers.append({
        'title': title,
        'year': year,
        'venue': venue,
        'source': source,
        'domain': domain,
        'contribution': contribution,
        'original_filename': filename
    })

# Filter papers with empirical contribution published after 2016
empirical_papers_after_2016 = [
    p for p in parsed_papers 
    if p['contribution'] == 'empirical' and p['year'] and p['year'] > 2016
]

print('Total papers parsed:', len(parsed_papers))
print('Empirical papers after 2016:', len(empirical_papers_after_2016))
print('Sample empirical papers:', empirical_papers_after_2016[:3])

# Save the filtered papers for next step
result = {
    'all_papers': parsed_papers,
    'empirical_papers_after_2016': empirical_papers_after_2016
}

import json as js
print('__RESULT__:')
print(js.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
