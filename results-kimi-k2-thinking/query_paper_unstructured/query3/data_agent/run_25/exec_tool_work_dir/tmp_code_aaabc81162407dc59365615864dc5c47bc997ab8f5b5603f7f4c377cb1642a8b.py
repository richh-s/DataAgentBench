code = """import json
import re

# Load data
citation_path = locals()['var_functions.query_db:0']
mongodb_path = locals()['var_functions.query_db:2']

with open(citation_path, 'r') as f:
    citations = json.load(f)

with open(mongodb_path, 'r') as f:
    papers = json.load(f)

# Let's examine the data carefully
print('=== Debug Stage 1: Understanding Data ===')
print('Sample citation record:', citations[0] if citations else 'No citations')
print('Sample paper record:', papers[0] if papers else 'No papers')

# Count empirical papers by year
emp_counts = {}
for paper in papers:
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    text = paper.get('text', '')
    
    # Find years
    years = re.findall(r'\b(20[0-2][0-9])\b', text)
    has_empirical = 'empirical' in text.lower()
    
    if years:
        year = int(years[0])
        if has_empirical:
            emp_counts[year] = emp_counts.get(year, 0) + 1

print('Empirical paper counts by year:', sorted(emp_counts.items()))

# Check intersection between empirical papers after 2016 and citations
emp_titles_after_2016 = []
for paper in papers:
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    text = paper.get('text', '')
    
    # Extract year
    years = re.findall(r'\b(20[0-2][0-9])\b', text)
    year = int(years[0]) if years else 0
    
    has_empirical = 'empirical' in text.lower()
    
    if title and year > 2016 and has_empirical:
        emp_titles_after_2016.append(title)

citation_titles = set(c['title'] for c in citations)
emp_citation_titles = [t for t in emp_titles_after_2016 if t in citation_titles]

print('Total empirical papers after 2016:', len(emp_titles_after_2016))
print('Papers with citations:', len(emp_citation_titles))

# Get actual final results
final_papers = []
for paper in papers:
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    text = paper.get('text', '')
    
    # Extract year
    years = re.findall(r'\b(20[0-2][0-9])\b', text)
    year = int(years[0]) if years else 0
    
    has_empirical = 'empirical' in text.lower()
    
    if title and year > 2016 and has_empirical and title in citation_titles:
        # Find citation count
        citations_count = 0
        for c in citations:
            if c['title'] == title:
                citations_count = int(c['total_citations'])
                break
        final_papers.append({
            'title': title,
            'year': year,
            'total_citations': citations_count
        })

final_papers.sort(key=lambda x: x['total_citations'], reverse=True)

# Output results
print('=== Final Results ===')
print('Count:', len(final_papers))
for i, paper in enumerate(final_papers[:10]):
    print(f"{i+1}. {paper['title']} - {paper['year']} - {paper['total_citations']} citations")

print('__RESULT__:')
print(json.dumps(final_papers, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:10': [], 'var_functions.execute_python:14': [], 'var_functions.execute_python:20': []}

exec(code, env_args)
