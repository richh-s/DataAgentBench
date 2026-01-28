code = """import json
import re

# Load MongoDB data
mongo_path = locals()['var_functions.query_db:2']
print('MongoDB file path:', mongo_path)

with open(mongo_path, 'r') as f:
    all_docs = json.load(f)

print('Total documents:', len(all_docs))

# Process all documents to extract metadata
paper_metadata = []
for doc in all_docs:
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    text = doc.get('text', '')
    
    # Extract year using multiple regex patterns
    year = None
    
    # Pattern 1: Look for 4-digit year (20XX) in the text
    year_match = re.search(r'\b(20\d{2})\b', text)
    if year_match:
        year = int(year_match.group(1))
    
    # Pattern 2: Look for 2-digit year after venue name (e.g., "UbiComp '15")
    if not year:
        venue_match = re.search(r"[A-Za-z]+\s+'(\d{2})\b", text)
        if venue_match:
            year_str = venue_match.group(1)
            # Assume 2000s for HCI conference papers
            year = 2000 + int(year_str)
    
    # Pattern 3: Look for "Proceedings of" with year
    if not year:
        proc_match = re.search(r'Proceedings.*?\b(20\d{2})\b', text, re.IGNORECASE)
        if proc_match:
            year = int(proc_match.group(1))
    
    # Extract domains - check for physical activity and other domains
    text_lower = text.lower()
    domains = []
    
    # Check for physical activity specifically
    if 'physical activity' in text_lower:
        domains.append('physical activity')
    
    # Check for other domains mentioned in the hints
    other_domains = ['sleep', 'food', 'mental', 'finances', 'fitness', 'health']
    for domain in other_domains:
        if domain in text_lower:
            domains.append(domain)
    
    domain_str = ', '.join(domains) if domains else None
    
    paper_metadata.append({
        'title': title,
        'year': year,
        'domains': domains,
        'domain_str': domain_str,
        'has_physical_activity': 'physical activity' in text_lower
    })

# Filter for 2016 papers with physical activity
papers_2016_pa = []
for paper in paper_metadata:
    if paper['year'] == 2016 and paper['has_physical_activity']:
        papers_2016_pa.append(paper)

print('\nPapers from 2016 in physical activity domain:', len(papers_2016_pa))
for p in papers_2016_pa:
    print(f"  - {p['title']} (Year: {p['year']}, Domains: {p['domain_str']})")

# Show distribution of all papers by year
year_counts = {}
for p in paper_metadata:
    y = p['year']
    if y:
        year_counts[y] = year_counts.get(y, 0) + 1

print('\nAll papers by year:')
for y in sorted(year_counts.keys()):
    print(f"  {y}: {year_counts[y]} papers")

result = {
    'total_documents': len(all_docs),
    'papers_with_year': len([p for p in paper_metadata if p['year']]),
    'papers_2016_count': len([p for p in paper_metadata if p['year'] == 2016]),
    'papers_2016_physical_activity': papers_2016_pa
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:6': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}, {'id': '6', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '95', 'citation_year': '2015'}, {'id': '7', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '14', 'citation_year': '2016'}, {'id': '8', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '12', 'citation_year': '2012'}, {'id': '9', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '76', 'citation_year': '2013'}, {'id': '10', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '55', 'citation_year': '2014'}], 'var_functions.execute_python:10': {'all_papers_count': 5, 'filtered_papers': []}, 'var_functions.execute_python:14': {'total_papers': 5, 'papers_2016_count': 0, 'papers_2016_physical_activity': []}, 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.execute_python:22': {'papers_2016_pa_count': 0, 'papers_2016_pa_titles': []}, 'var_functions.execute_python:26': {'count': 0, 'titles': []}, 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json'}

exec(code, env_args)
