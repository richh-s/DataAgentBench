code = """import json
import re

# Load data
citation_path = locals()['var_functions.query_db:0']
mongodb_path = locals()['var_functions.query_db:2']

with open(citation_path, 'r') as f:
    citations = json.load(f)

with open(mongodb_path, 'r') as f:
    papers = json.load(f)

# Get citation titles
citation_titles_set = set(c['title'] for c in citations)

# Get all paper titles and check which ones might be in citations
all_paper_titles = []
empirical_papers_after_2016 = []

for paper in papers:
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    text = paper.get('text', '')
    
    if not title:
        continue
    
    # Find year
    years = re.findall(r'\b(20[0-2][0-9])\b', text)
    year = int(years[0]) if years else 0
    
    has_empirical = 'empirical' in text.lower()
    
    # Collect all titles for comparison
    all_paper_titles.append(title)
    
    # Collect empirical papers after 2016
    if year > 2016 and has_empirical:
        empirical_papers_after_2016.append({
            'title': title,
            'year': year
        })

print('Total papers examined: ' + str(len(all_paper_titles)))
print('Total empirical papers after 2016: ' + str(len(empirical_papers_after_2016)))

# Debug: Find partial matches
print('\n=== Debug: Checking title matches ===')
citation_titles_sample = list(citation_titles_set)[:5]
empirical_titles_sample = [p['title'] for p in empirical_papers_after_2016[:5]]

print('Sample citation titles:')
for title in citation_titles_sample:
    print('  "' + title + '"')

print('\nSample empirical paper titles:')
for title in empirical_titles_sample:
    print('  "' + title + '"')

# Find potential matches using partial matching (case-insensitive)
potential_matches = []
for emp_paper in empirical_papers_after_2016:
    emp_title = emp_paper['title'].lower()
    for citation_title in citation_titles_set:
        if emp_title == citation_title.lower():
            potential_matches.append(emp_paper['title'])
            break

print('\nExact matches (case-insensitive): ' + str(len(potential_matches)))

# Try substring matching (paper title contains citation title or vice versa)
substring_matches = []
for emp_paper in empirical_papers_after_2016:
    emp_title = emp_paper['title'].lower()
    for citation_title in citation_titles_set:
        cit_title_lower = citation_title.lower()
        if emp_title in cit_title_lower or cit_title_lower in emp_title:
            substring_matches.append({
                'paper_title': emp_paper['title'],
                'citation_title': citation_title
            })
            break

print('Substring matches: ' + str(len(substring_matches)))

if substring_matches:
    print('\nFirst few substring matches:')
    for i, match in enumerate(substring_matches[:5]):
        print('  Paper: "' + match['paper_title'] + '"')
        print('  Citation: "' + match['citation_title'] + '"')
        print('')

# Prepare final output
final_results = []

# Use substring matching approach to get actual results
for emp_paper in empirical_papers_after_2016:
    emp_title = emp_paper['title']
    
    # Find matching citation
    for citation in citations:
        cit_title = citation['title']
        # Case-insensitive matching, ignoring spaces and punctuation
        if ''.join(e for e in emp_title.lower() if e.isalnum()) == ''.join(e for e in cit_title.lower() if e.isalnum()):
            final_results.append({
                'title': emp_title,
                'year': emp_paper['year'],
                'total_citations': int(citation['total_citations'])
            })
            break

final_results.sort(key=lambda x: x['total_citations'], reverse=True)

print('\n=== Final Results (' + str(len(final_results)) + ' papers) ===')
for i, paper in enumerate(final_results[:10]):
    print(str(i+1) + '. ' + paper['title'][:80] + '...')
    print('   Year: ' + str(paper['year']) + ', Citations: ' + str(paper['total_citations']))

print('\n__RESULT__:')
print(json.dumps(final_results, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:10': [], 'var_functions.execute_python:14': [], 'var_functions.execute_python:20': [], 'var_functions.execute_python:22': []}

exec(code, env_args)
