code = """import json
import re

# Get stored data - these should be the actual data lists
papers_data = locals()['var_functions.query_db:30']
citations_data = locals()['var_functions.query_db:28']

# Process citations into lookup dictionary
citation_map = {}
for cit in citations_data:
    title = cit.get('title', '')
    total_citations = int(cit.get('total_citations', 0))
    if title:
        citation_map[title] = total_citations

# Process papers and find matches
paper_matches = []
for doc in papers_data:
    filename = doc.get('filename', '')
    text = doc.get('text', '')
    
    # Extract title
    title = filename.replace('.txt', '') if filename else ''
    
    # Find year
    year_match = re.search(r'(20\d{2})', text)
    year = int(year_match.group(1)) if year_match else None
    
    # Check for empirical (exact string match, case-insensitive)
    has_empirical = 'empirical' in text.lower()
    
    # Apply filters
    if has_empirical and year and year > 2016:
        total_citations = citation_map.get(title, 0)
        if total_citations > 0:
            paper_matches.append({
                'title': title,
                'year': year,
                'total_citations': total_citations
            })

# Sort by citations descending
paper_matches_sorted = sorted(paper_matches, key=lambda x: x['total_citations'], reverse=True)

# Format results
results_strings = []
for paper in paper_matches_sorted:
    results_strings.append(paper['title'] + ': ' + str(paper['total_citations']) + ' citations')

print('__RESULT__:')
print(json.dumps(results_strings))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.execute_python:40': ['A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App: 266 citations', 'A Trip to the Moon: Personalized Animated Movies for Self-reflection: 265 citations'], 'var_functions.execute_python:48': ['A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App: 266 citations', 'A Trip to the Moon: Personalized Animated Movies for Self-reflection: 265 citations']}

exec(code, env_args)
