code = """import json
import re
from collections import defaultdict

# Get the file paths from the storage
citations_file = var_functions.query_db:5
paper_docs_file = var_functions.query_db:6

# Read the citations data
if isinstance(citations_file, str):
    with open(citations_file, 'r') as f:
        citations_data = json.load(f)
else:
    citations_data = citations_file

# Read the paper documents data
if isinstance(paper_docs_file, str):
    with open(paper_docs_file, 'r') as f:
        paper_docs_data = json.load(f)
else:
    paper_docs_data = paper_docs_file

# Process papers to extract metadata
papers = []

for doc in paper_docs_data:
    # Extract title from filename
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    
    # Extract text
    text = doc.get('text', '')
    
    # Extract year - look for patterns like '2015', "'15", or 'UBICOMP '15'
    year = None
    year_patterns = [
        r"\b(20\d{2})\b",  # Full year like 2015
        r"\b'?(\d{2})\b",  # Two digit year like '15 or 15
        r"\d{4}\s*,\s*\w+\s*\d{1,2}-\d{1,2}",  # Pattern like 2015, September 7-11
    ]
    
    for pattern in year_patterns:
        matches = re.findall(pattern, text[:500])  # Search in first 500 chars
        if matches:
            if isinstance(matches[0], tuple):
                year_str = matches[0][0] if matches[0][0] else matches[0][1]
            else:
                year_str = matches[0]
            
            if len(year_str) == 4 and year_str.startswith('20'):
                year = int(year_str)
                break
            elif len(year_str) == 2:
                # Convert two-digit year to four-digit
                if int(year_str) < 50:  # Assuming 2000s
                    year = int('20' + year_str)
                else:
                    year = int('19' + year_str)
                break
    
    # Extract domain - look for 'physical activity' (case-insensitive)
    # Also check for similar patterns
    domain = None
    if re.search(r'physical\s+activity', text, re.IGNORECASE):
        domain = 'physical activity'
    elif re.search(r'physical\s+fitness', text, re.IGNORECASE):
        domain = 'physical activity'
    elif re.search(r'exercise', text, re.IGNORECASE):
        domain = 'physical activity'
    elif re.search(r'fitness', text, re.IGNORECASE):
        domain = 'physical activity'
    
    # Extract venue - look for common HCI venues
    venue = None
    venue_patterns = [
        r"CHI\s*'\d{2}", r"UBICOMP\s*'\d{2}", r"CSCW\s*'\d{2}", r"DIS\s*'\d{2}",
        r"PervasiveHealth", r"WWW", r"IUI", r"OzCHI", r"TEI", r"AH"
    ]
    
    for pattern in venue_patterns:
        match = re.search(pattern, text[:500])
        if match:
            venue = match.group(0)
            break
    
    # Extract source/publisher
    source = None
    if 'ACM' in text[:500]:
        source = 'ACM'
    elif 'IEEE' in text[:500]:
        source = 'IEEE'
    elif 'PubMed' in text[:500]:
        source = 'PubMed'
    
    papers.append({
        'title': title,
        'year': year,
        'domain': domain,
        'venue': venue,
        'source': source
    })

# Filter for papers from 2016 in physical activity domain
papers_2016_physical_activity = [
    p for p in papers 
    if p['year'] == 2016 and p['domain'] == 'physical activity'
]

# Create a mapping from title to citation counts per year
title_to_citations = defaultdict(int)
for citation in citations_data:
    title = citation.get('title', '')
    count = int(citation.get('citation_count', 0))
    title_to_citations[title] += count

# Combine paper info with total citations
results = []
for paper in papers_2016_physical_activity:
    title = paper['title']
    total_citations = title_to_citations.get(title, 0)
    results.append({
        'title': title,
        'total_citation_count': total_citations
    })

# Sort by citation count (descending)
results.sort(key=lambda x: x['total_citation_count'], reverse=True)

print('__RESULT__:')
print(json.dumps(results))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}, {'id': '6', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '95', 'citation_year': '2015'}, {'id': '7', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '14', 'citation_year': '2016'}, {'id': '8', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '12', 'citation_year': '2012'}, {'id': '9', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '76', 'citation_year': '2013'}, {'id': '10', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '55', 'citation_year': '2014'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
