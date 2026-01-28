code = """import json
import re

# Load the data
citation_path = locals()['var_functions.query_db:0']
mongodb_path = locals()['var_functions.query_db:2']

with open(citation_path, 'r') as f:
    citations = json.load(f)

with open(mongodb_path, 'r') as f:
    papers = json.load(f)

# Step 1: Find all empirical papers
empirical_papers = []
for paper in papers:
    text = paper.get('text', '').lower()
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    
    if 'empirical' in text and title:
        empirical_papers.append(title)

print('Total empirical papers found: ' + str(len(empirical_papers)))
print('First 10 empirical papers:')
for i, title in enumerate(empirical_papers[:10]):
    print('  ' + str(i+1) + '. ' + title[:100])

# Step 2: Find dates in papers
papers_with_years = []
for paper in papers:
    text = paper.get('text', '')
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    
    years = re.findall(r'\b(20[0-9]{2})\b', text)
    year = int(years[0]) if years else 0
    
    has_empirical = 'empirical' in text.lower()
    
    if year > 2016:
        papers_with_years.append({
            'title': title,
            'year': year,
            'empirical': has_empirical
        })

papers_with_years.sort(key=lambda x: x['year'], reverse=True)

print('\nPapers after 2016: ' + str(len(papers_with_years)))
print('Post-2016 empirical papers: ' + str(len([p for p in papers_with_years if p['empirical']])))

# Step 3: Check citation titles
citation_titles = [c['title'] for c in citations]
print('\nFirst 10 citation titles:')
for i, title in enumerate(citation_titles[:10]):
    print('  ' + str(i+1) + '. ' + title[:100])

# Step 4: Manual matching on exact titles
empirical_after_2016 = [p for p in papers_with_years if p['empirical']]
emp_titles_set = set(p['title'] for p in empirical_after_2016)
citation_titles_set = set(citation_titles)

exact_matches = emp_titles_set & citation_titles_set
print('\nExact title matches: ' + str(len(exact_matches)))

# Step 5: Try to find ANY matches using flexible matching
matches_found = []
for emp_title in emp_titles_set:
    for cit_title in citation_titles_set:
        # Normalize both titles for comparison
        norm_emp = re.sub(r'\W+', ' ', emp_title.lower()).strip()
        norm_cit = re.sub(r'\W+', ' ', cit_title.lower()).strip()
        
        # Check if they match
        if norm_emp == norm_cit or norm_emp in norm_cit or norm_cit in norm_emp:
            matches_found.append(emp_title)
            
            # Get citation details
            for c in citations:
                if c['title'] == cit_title:
                    matches_found.append([
                        emp_title,
                        cit_title,
                        int(c['total_citations'])
                    ])
            break

print('\nFlexible matches found: ' + str(len(matches_found)))

# Prepare final output
final_output = []
for match in matches_found:
    if len(match) == 3:  # Should be [emp_title, cit_title, citations]
        # Extract year for this title
        for paper in papers_with_years:
            if paper['title'] == match[0]:
                final_output.append({
                    'title': match[0],
                    'year': paper['year'],
                    'total_citations': match[2]
                })
                break

final_output.sort(key=lambda x: x['total_citations'], reverse=True)

print('\nFinal results count: ' + str(len(final_output)))
print('__RESULT__:')
print(json.dumps(final_output, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:10': [], 'var_functions.execute_python:14': [], 'var_functions.execute_python:20': [], 'var_functions.execute_python:22': [], 'var_functions.execute_python:26': [], 'var_functions.execute_python:34': [], 'var_functions.execute_python:38': []}

exec(code, env_args)
