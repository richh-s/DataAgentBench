code = """import json
import re

# Load the paper documents from storage
papers_file = locals()['var_functions.query_db:5']
print('Loading papers from file: ' + str(papers_file))

with open(papers_file, 'r') as f:
    papers = json.load(f)

print('Loaded ' + str(len(papers)) + ' papers')

# Extract structured information from papers
paper_info = []

for paper in papers:
    title = paper['filename'].replace('.txt', '')
    text = paper['text']
    
    # Extract year - look for 4-digit years
    year_match = re.search(r'(?<!\d)(20\d{2})(?!\d)', text)
    year = int(year_match.group()) if year_match else None
    
    # Check for empirical contribution
    contribution = []
    empirical_pattern = r'(?i)\b(survey|questionnaire|interview|field study|field research|user study|empirical|observation|data collection|experiment|case study|participants|study|investigation|evaluation|assessment)\b'
    if re.search(empirical_pattern, text):
        contribution.append('empirical')
    
    paper_info.append({'title': title, 'year': year, 'contribution': contribution})

# Filter papers
empirical_after_2016 = [p for p in paper_info if 'empirical' in p['contribution'] and p['year'] and p['year'] > 2016]

print('Total papers: ' + str(len(paper_info)))
print('Empirical after 2016: ' + str(len(empirical_after_2016)))

# Load citations
citations_file = locals()['var_functions.query_db:12']
with open(citations_file, 'r') as f:
    citations = json.load(f)

# Build citation index
citation_dict = {}
for citation in citations:
    title = citation['title']
    count = int(citation['citation_count'])
    citation_dict[title] = citation_dict.get(title, 0) + count

# Join and collect results
result = []
for paper in empirical_after_2016:
    title = paper['title']
    if title in citation_dict:
        result.append({'title': title, 'year': paper['year'], 'total_citation_count': citation_dict[title]})

# Sort by citations
result.sort(key=lambda x: x['total_citation_count'], reverse=True)

print('Final results: ' + str(len(result)))

# Output
out_result = json.dumps(result)
print('---PRINT FORMAT---')
print('__RESULT__:')
print(out_result)"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.list_db:2': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:20': []}

exec(code, env_args)
