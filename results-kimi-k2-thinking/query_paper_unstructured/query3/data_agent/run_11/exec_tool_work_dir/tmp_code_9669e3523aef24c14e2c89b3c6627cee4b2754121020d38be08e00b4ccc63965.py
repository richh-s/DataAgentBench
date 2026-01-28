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

# Process all papers
paper_info = []
for paper in papers:
    title = paper['filename'].replace('.txt', '')
    text = paper['text']
    
    # Find all years in the text
    year_matches = re.findall(r'20\d{2}', text)
    year = None
    if year_matches:
        # Use the most recent year (highest number)
        year = max(int(y) for y in year_matches)
    
    # Check for empirical contribution - more comprehensive pattern
    has_empirical = re.search(r'(?i)\b(survey|questionnaire|interview|field study|field research|user study|empirical|observation|data collection|experiment|case study|participants|study\s+of|investigation|evaluation|assessment|we\s+conducted|we\s+studied|we\s+interviewed|data\s+was\s+collected|participants\s+were|methodology|methods|results|findings)\b', text)
    
    contribution = []
    if has_empirical:
        contribution.append('empirical')
    
    paper_info.append({'title': title, 'year': year, 'contribution': contribution})

# Filter papers
empirical_after_2016 = [p for p in paper_info if 'empirical' in p['contribution'] and p['year'] and p['year'] > 2016]

print('\nTotal papers processed: ' + str(len(paper_info)))
print('Empirical papers after 2016: ' + str(len(empirical_after_2016)))

# Load citations
citations_file = locals()['var_functions.query_db:12']
with open(citations_file, 'r') as f:
    citations = json.load(f)

print('\nTotal citation records: ' + str(len(citations)))

# Build citation dictionary
citation_dict = {}
for citation in citations:
    title = citation['title']
    count = int(citation['citation_count'])
    citation_dict[title] = citation_dict.get(title, 0) + count

print('Unique papers with citations: ' + str(len(citation_dict)))

# Join paper info with citation data
result = []
for paper in empirical_after_2016:
    title = paper['title']
    if title in citation_dict:
        result.append({
            'title': title,
            'year': paper['year'],
            'total_citation_count': citation_dict[title]
        })

# Sort by citation count
result.sort(key=lambda x: x['total_citation_count'], reverse=True)

print('\nFinal result count: ' + str(len(result)))

# Output the result
output = json.dumps(result)
print('---PRINT FORMAT---')
print('__RESULT__:')
print(output)"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.list_db:2': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:20': [], 'var_functions.execute_python:26': []}

exec(code, env_args)
