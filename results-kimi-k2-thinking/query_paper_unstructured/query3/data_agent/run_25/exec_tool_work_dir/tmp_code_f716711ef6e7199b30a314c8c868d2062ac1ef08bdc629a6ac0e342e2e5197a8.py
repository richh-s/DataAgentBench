code = """import json
import re

# Load data
citation_path = locals()['var_functions.query_db:0']
mongodb_path = locals()['var_functions.query_db:2']

with open(citation_path, 'r') as f:
    citations = json.load(f)

with open(mongodb_path, 'r') as f:
    papers = json.load(f)

# Debug 1: Check year distribution in papers
print('=== YEAR DISTRIBUTION DEBUG ===')
year_counts = {}
for paper in papers:
    text = paper.get('text', '')
    years = re.findall(r'\b(20[0-2][0-9])\b', text)
    if years:
        year = int(years[0])
        year_counts[year] = year_counts.get(year, 0) + 1

for year in sorted(year_counts.keys()):
    print('Year ' + str(year) + ': ' + str(year_counts[year]) + ' papers')

# Debug 2: Check empirical papers by year
print('\n=== EMPIRICAL PAPER DISTRIBUTION ===')
emp_by_year = {}
for paper in papers:
    text = paper.get('text', '')
    years = re.findall(r'\b(20[0-2][0-9])\b', text)
    if years:
        year = int(years[0])
        if 'empirical' in text.lower():
            emp_by_year[year] = emp_by_year.get(year, 0) + 1

for year in sorted(emp_by_year.keys()):
    print('Year ' + str(year) + ': ' + str(emp_by_year[year]) + ' empirical papers')

# Debug 3: Check if there are ANY empirical papers after 2016
emp_after_2016 = []
for paper in papers:
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    text = paper.get('text', '')
    
    years = re.findall(r'\b(20[0-2][0-9])\b', text)
    year = int(years[0]) if years else 0
    
    if year > 2016 and 'empirical' in text.lower():
        emp_after_2016.append(title)

print('\n=== EMPIRICAL PAPERS AFTER 2016 ===')
print('Count: ' + str(len(emp_after_2016)))
if len(emp_after_2016) > 0:
    print('First 5 empirical papers after 2016:')
    for i, title in enumerate(emp_after_2016[:5]):
        print('  ' + str(i+1) + '. ' + title)

# Debug 4: Check citation titles
print('\n=== CITATION TITLES SAMPLE ===')
citation_titles = [c['title'] for c in citations[:10]]
for i, title in enumerate(citation_titles):
    print('  ' + str(i+1) + '. ' + title)

# Debug 5: Check for exact matches
citation_titles_set = set(c['title'] for c in citations)
matches = []
for title in emp_after_2016:
    if title in citation_titles_set:
        matches.append(title)

print('\n=== EXACT MATCHES ===')
print('Exact matches found: ' + str(len(matches)))

# Debug 6: Try normalized matching
norm_citation_map = {}
for c in citations:
    title = c['title']
    norm = re.sub(r'[^a-zA-Z0-9]', '', title.lower())
    norm_citation_map[norm] = title

norm_matches = []
for paper_title in emp_after_2016:
    norm_paper = re.sub(r'[^a-zA-Z0-9]', '', paper_title.lower())
    if norm_paper in norm_citation_map:
        norm_matches.append((paper_title, norm_citation_map[norm_paper]))

print('\n=== NORMALIZED MATCHES ===')
print('Normalized matches: ' + str(len(norm_matches)))

if norm_matches:
    print('First few normalized matches:')
    for i, (paper, cit) in enumerate(norm_matches[:3]):
        print('  Paper: "' + paper + '"')
        print('  Citation: "' + cit + '"')
        print('')

# Generate final results using normalized matches
final_results = []
for paper in papers:
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    text = paper.get('text', '')
    
    years = re.findall(r'\b(20[0-2][0-9])\b', text)
    year = int(years[0]) if years else 0
    
    if year > 2016 and 'empirical' in text.lower():
        norm_title = re.sub(r'[^a-zA-Z0-9]', '', title.lower())
        if norm_title in norm_citation_map:
            # Get actual citation count
            matching_citation = None
            for c in citations:
                if re.sub(r'[^a-zA-Z0-9]', '', c['title'].lower()) == norm_title:
                    matching_citation = c
                    break
            
            if matching_citation:
                final_results.append({
                    'title': title,
                    'year': year,
                    'total_citations': int(matching_citation['total_citations'])
                })

final_results.sort(key=lambda x: x['total_citations'], reverse=True)

print('\n=== FINAL RESULTS ===')
print('Total papers with citations: ' + str(len(final_results)))

if final_results:
    print('Top 5 papers by citations:')
    for i, paper in enumerate(final_results[:5]):
        print('  ' + str(i+1) + '. ' + paper['title'][:100])
        print('     Year: ' + str(paper['year']) + ', Citations: ' + str(paper['total_citations']))
else:
    print('No results found after all matching attempts')

print('\n__RESULT__:')
print(json.dumps(final_results, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:10': [], 'var_functions.execute_python:14': [], 'var_functions.execute_python:20': [], 'var_functions.execute_python:22': [], 'var_functions.execute_python:26': []}

exec(code, env_args)
