code = """import json
import re

citation_path = locals()['var_functions.query_db:0']
mongodb_path = locals()['var_functions.query_db:2']

with open(citation_path, 'r') as f:
    citations = json.load(f)

with open(mongodb_path, 'r') as f:
    papers = json.load(f)

# Debug: Look at first few papers to understand structure
print('First paper filenames:')
for i in range(min(5, len(papers))):
    filename = papers[i].get('filename', '')
    print('  ' + filename[:200] + '...' if len(filename) > 200 else filename)

print('\nFirst citation titles:')
for i in range(min(5, len(citations))):
    print('  ' + citations[i].get('title', '')[:100])

# Debug: Check for empirical papers and years
empirical_papers = []
for paper in papers:
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    text = paper.get('text', '')
    
    if 'empirical' in text.lower():
        # Extract year more carefully
        year_match = re.search(r'\b(201[0-9]|202[0-9])\b', text)
        year = year_match.group(1) if year_match else 'not found'
        
        empirical_papers.append({'title': title, 'year': int(year) if year != 'not found' else None})
        
        # Debug first few
        if len(empirical_papers) <= 5:
            print('\nEmpirical paper debug:')
            print('Title: ' + title[:100])
            print('Year: ' + str(year))
            print('---')

# Filter empirical papers after 2016
empirical_after_2016 = [p for p in empirical_papers if p['year'] and p['year'] > 2016]

print('\nEmpirical papers after 2016: ' + str(len(empirical_after_2016)))

# Debug: Check if titles match
empirical_titles = set(p['title'] for p in empirical_after_2016)
citation_titles = set(c['title'] for c in citations)

# Find intersection
matching_titles = empirical_titles & citation_titles
print('Matching titles between empirical papers and citations: ' + str(len(matching_titles)))

if len(matching_titles) > 0:
    print('Some matching examples:')
    for title in list(matching_titles)[:5]:
        print('  ' + title[:80])
else:
    # Show some empirical titles and citation titles separately
    print('\nFirst 3 empirical titles:')
    for title in list(empirical_titles)[:3]:
        print('  ' + title[:80])
    print('\nFirst 3 citation titles:')
    for title in list(citation_titles)[:3]:
        print('  ' + title[:80])

# Generate full results
full_results = []
for paper in empirical_after_2016:
    title = paper['title']
    if title in citation_titles:
        # Find the citation
        citations_count = 0
        for c in citations:
            if c['title'] == title:
                citations_count = int(c['total_citations'])
                break
        
        full_results.append({
            'title': title,
            'year': paper['year'],
            'total_citations': citations_count
        })

full_results.sort(key=lambda x: x['total_citations'], reverse=True)

results_json = json.dumps(full_results, indent=2)
print('__RESULT__:')
print(results_json)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:10': [], 'var_functions.execute_python:14': []}

exec(code, env_args)
