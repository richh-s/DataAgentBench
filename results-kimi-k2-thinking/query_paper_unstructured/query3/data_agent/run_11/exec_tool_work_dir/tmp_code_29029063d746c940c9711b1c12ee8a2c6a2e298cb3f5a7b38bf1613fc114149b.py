code = """import json
import re

# Load the paper documents from storage
papers_file = locals()['var_functions.query_db:5']
with open(papers_file, 'r') as f:
    papers = json.load(f)

print('Total papers loaded: ' + str(len(papers)))

# Sample paper to understand the format
first_paper = papers[0]
print('\nFirst paper filename: ' + first_paper['filename'])
print('First paper title: ' + first_paper['filename'].replace('.txt', ''))

# Check text for year patterns
sample_text = first_paper['text'][:500]
print('\nSample text (first 500 chars):')
print(sample_text)

# Check for year patterns in the sample
year_matches = re.findall(r'20\d{2}', first_paper['text'])
print('\nAll year matches in first paper: ' + str(year_matches))

# Process more papers and check for empirical indicators
paper_info = []
for i, paper in enumerate(papers[:50]):  # Process first 50 papers
    title = paper['filename'].replace('.txt', '')
    text = paper['text']
    
    # Find all years
    year_matches = re.findall(r'20\d{2}', text)
    year = None
    if year_matches:
        # Use the most recent year (highest number)
        year = max(int(y) for y in year_matches)
    
    # Check for empirical contribution
    has_empirical = re.search(r'(?i)\b(survey|questionnaire|interview|field study|field research|user study|empirical|observation|data collection|experiment|case study|participants|study\s+of|investigation|evaluation|assessment|we\s+conducted|we\s+studied|we\s+interviewed|data\s+was\s+collected|participants\s+were)\b', text)
    
    if has_empirical:
        contribution = ['empirical']
    else:
        contribution = []
    
    paper_info.append({'title': title, 'year': year, 'contribution': contribution, 'year_matches': year_matches})
    
    if i < 10:  # Print first 10 for debugging
        print(f"Paper {i+1}: {title[:50]} - Year: {year} - Years found: {year_matches} - Empirical: {len(contribution) > 0}")

# Filter papers
all_years = [p['year'] for p in paper_info if p['year']]
print('\nYear distribution:')
for yr in sorted(set(all_years)):
    count = len([p for p in paper_info if p['year'] == yr])
    print(f'{yr}: {count} papers')

empirical_papers = [p for p in paper_info if 'empirical' in p['contribution']]
print('\nTotal empirical papers (in sample): ' + str(len(empirical_papers)))

empirical_after_2016 = [p for p in paper_info if 'empirical' in p['contribution'] and p['year'] and p['year'] > 2016]
print('Empirical papers after 2016 (in sample): ' + str(len(empirical_after_2016)))

# Load citations and check format
citations_file = locals()['var_functions.query_db:12']
with open(citations_file, 'r') as f:
    citations = json.load(f)

print('\nCitation records: ' + str(len(citations)))
print('First citation: ' + str(citations[0]))

# Get unique citation titles
citation_titles = set(c['title'] for c in citations)
print('Unique citation titles: ' + str(len(citation_titles)))

# Check for matches
paper_titles = set(p['title'] for p in paper_info)
matches = paper_titles.intersection(citation_titles)
print('\nMatching titles (in sample): ' + str(len(matches)))

if matches:
    print('Sample matches:')
    for title in list(matches)[:5]:
        print('  - ' + title)

# Output debug info
out_result = json.dumps({
    'sample_papers': paper_info[:10],
    'empirical_after_2016_sample': empirical_after_2016[:10] if empirical_after_2016 else [],
    'matching_titles_sample': list(matches)[:10] if matches else [],
    'total_citations': len(citations),
    'unique_citation_titles': len(citation_titles)
})

print('\n---PRINT FORMAT---')
print('__RESULT__:')
print(out_result)"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.list_db:2': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:20': [], 'var_functions.execute_python:26': []}

exec(code, env_args)
