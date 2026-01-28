code = """import json
import re

# Load data
with open('var_functions.query_db:30.json', 'r') as f:
    paper_docs = json.load(f)

with open('var_functions.query_db:28.json', 'r') as f:
    citations = json.load(f)

# Extract paper info with better debugging
papers_info = []
empirical_count = 0
year_after_2016_count = 0
both_count = 0

for i, doc in enumerate(paper_docs[:100]):  # Check first 100
    filename = doc['filename']
    text = doc['text']
    title = filename.replace('.txt', '')
    
    year_match = re.search(r'(20\d{2})', text)
    year = int(year_match.group(1)) if year_match else None
    
    has_empirical = 'empirical' in text.lower()
    
    if has_empirical:
        empirical_count += 1
    if year and year > 2016:
        year_after_2016_count += 1
    if has_empirical and year and year > 2016:
        both_count += 1
        print(f"Match {both_count}: {title} (year: {year}, empirical: {has_empirical})")
    
    papers_info.append({
        'title': title,
        'year': year,
        'has_empirical': has_empirical
    })

print(f'\nFirst 100 papers:')
print(f'Empirical: {empirical_count}')
print(f'Year > 2016: {year_after_2016_count}')
print(f'Both: {both_count}')

# Process all papers
all_papers_info = []
for doc in paper_docs:
    filename = doc['filename']
    text = doc['text']
    title = filename.replace('.txt', '')
    year_match = re.search(r'(20\d{2})', text)
    year = int(year_match.group(1)) if year_match else None
    has_empirical = 'empirical' in text.lower()
    
    all_papers_info.append({
        'title': title,
        'year': year,
        'has_empirical': has_empirical
    })

filtered_papers = [p for p in all_papers_info if p['has_empirical'] and p['year'] and p['year'] > 2016]
print(f'\nAll papers: {len(paper_docs)}')
print(f'Filtered (empirical + year > 2016): {len(filtered_papers)}')

# Check citation coverage
citation_titles = set(cit['title'] for cit in citations)
print(f'Papers with citation data: {len(citation_titles)}')

# Match papers with citations
matching_papers = [p for p in filtered_papers if p['title'] in citation_titles]
print(f'Filtered papers with citation data: {len(matching_papers)}')

# Show some examples
print('\nSample filtered papers:')
for p in filtered_papers[:10]:
    has_citations = p['title'] in citation_titles
    print(f"  {p['title']} (year: {p['year']}) - has citations: {has_citations}")"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.execute_python:40': ['A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App: 266 citations', 'A Trip to the Moon: Personalized Animated Movies for Self-reflection: 265 citations']}

exec(code, env_args)
