code = """import json
import re
from collections import defaultdict

# Read the data from files
citations_file = var_functions.query_db:16
paper_docs_file = var_functions.query_db:6

# Load citations data
if isinstance(citations_file, str) and citations_file.endswith('.json'):
    with open(citations_file, 'r') as f:
        citations_data = json.load(f)
else:
    citations_data = citations_file

# Load paper documents data
if isinstance(paper_docs_file, str) and paper_docs_file.endswith('.json'):
    with open(paper_docs_file, 'r') as f:
        paper_docs_data = json.load(f)
else:
    paper_docs_data = paper_docs_file

# Debug: Check what data looks like
print('Number of citation records:', len(citations_data))
print('Number of paper documents:', len(paper_docs_data))

# Create citation mapping
title_to_total_citations = defaultdict(int)
for citation in citations_data:
    title = citation.get('title', '')
    count = int(citation.get('citation_count', 0))
    if title:
        title_to_total_citations[title] += count

# Debug: Show some citation titles
print('\nSample citation titles:')
for i, citation in enumerate(citations_data[:10]):
    print(f"  {i+1}. {citation.get('title')} ({citation.get('citation_year')}) - {citation.get('citation_count')} citations")

# Analyze paper documents
papers_info = []
year_distribution = defaultdict(int)
domain_keywords = defaultdict(int)

for doc in paper_docs_data:
    filename = doc.get('filename', '')
    text = doc.get('text', '')
    
    if not filename or not text:
        continue
    
    # Extract title
    title = filename.replace('.txt', '').strip()
    
    # Extract year
    year = None
    text_start = text[:1500]  # Look in first 1500 chars
    
    # Try multiple year patterns
    patterns = [
        r"\b(20\d{2})\b",  # Full year: 2016
        r"\b'(\d{2})\b",   # Venue year: '16
        r"\b(\d{4})\b",    # Any 4-digit year
    ]
    
    for pattern in patterns:
        matches = re.findall(pattern, text_start)
        if matches:
            for match in matches:
                if isinstance(match, tuple):
                    year_str = match[0]
                else:
                    year_str = match
                
                try:
                    if len(year_str) == 4 and year_str.startswith('20'):
                        year = int(year_str)
                        break
                    elif len(year_str) == 2:
                        year = int('20' + year_str)
                        break
                except:
                    continue
            if year:
                break
    
    # Check for physical activity keywords
    text_lower = text.lower()
    physical_activity_terms = [
        'physical activity', 'physical fitness', 'exercise', 'fitness', 
        'workout', 'sports', 'walking', 'running', 'cycling'
    ]
    
    found_terms = []
    for term in physical_activity_terms:
        if term in text_lower:
            found_terms.append(term)
            domain_keywords[term] += 1
    
    has_physical_activity = len(found_terms) > 0
    
    if year:
        year_distribution[year] += 1
    
    if has_physical_activity:
        papers_info.append({
            'title': title,
            'year': year,
            'found_terms': found_terms
        })

print('\nYear distribution of all papers:')
for yr in sorted(year_distribution.keys()):
    print(f"  {yr}: {year_distribution[yr]} papers")

print('\nPhysical activity keyword frequency:')
for term, count in sorted(domain_keywords.items(), key=lambda x: x[1], reverse=True):
    print(f"  '{term}': {count} papers")

print('\nPhysical activity papers found:')
for paper in papers_info[:20]:
    print(f"  {paper['year']} - {paper['title'][:80]}...")
    print(f"    Keywords: {paper['found_terms']}")

# Now filter for 2016 papers with physical activity
papers_2016_physical_activity = [
    p for p in papers_info 
    if p['year'] == 2016
]

print(f"\nFound {len(papers_2016_physical_activity)} papers from 2016 related to physical activity")

# Add citation counts
total_results = []
for paper in papers_2016_physical_activity:
    title = paper['title']
    total_citations = title_to_total_citations.get(title, 0)
    total_results.append({
        'title': title,
        'total_citation_count': total_citations
    })

# Sort by citation count
total_results.sort(key=lambda x: x['total_citation_count'], reverse=True)

print('__RESULT__:')
print(json.dumps(total_results))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}, {'id': '6', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '95', 'citation_year': '2015'}, {'id': '7', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '14', 'citation_year': '2016'}, {'id': '8', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '12', 'citation_year': '2012'}, {'id': '9', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '76', 'citation_year': '2013'}, {'id': '10', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '55', 'citation_year': '2014'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:14': [], 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json'}

exec(code, env_args)
