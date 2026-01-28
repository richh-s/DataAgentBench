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
    # Extract title from filename
    title = paper['filename'].replace('.txt', '')
    
    # Extract year from the text - look for publication year patterns
    text = paper['text']
    
    # Look for year patterns (2010-2029)
    year_match = re.search(r'(?<!\d)(20(1[0-9]|[2-9]\d))(?!\d)', text)
    year = int(year_match.group()) if year_match else None
    
    # Determine contribution type - check for empirical indicators
    contribution = []
    
    # Check for empirical keywords
    if re.search(r'(?i)\b(survey|questionnaire|interview|field study|field research|user study|empirical|observation|data collection|experiment|case study|participants|study|investigation|evaluation|assessment)\b', text):
        contribution.append('empirical')
    
    paper_info.append({
        'title': title,
        'year': year,
        'contribution': contribution,
    })

# Filter for empirical papers after 2016
empirical_after_2016 = [p for p in paper_info if 'empirical' in p['contribution'] and p['year'] and p['year'] > 2016]

print('Total papers processed: ' + str(len(paper_info)))
print('Empirical papers after 2016: ' + str(len(empirical_after_2016)))

# Load citation data
citations_file = locals()['var_functions.query_db:12']
print('Loading citations from file: ' + str(citations_file))

with open(citations_file, 'r') as f:
    citations = json.load(f)

print('Loaded ' + str(len(citations)) + ' citation records')

# Create a dictionary to store total citations per title  
citation_dict = {}
for citation in citations:
    title = citation['title']
    count = int(citation['citation_count'])
    if title in citation_dict:
        citation_dict[title] += count
    else:
        citation_dict[title] = count

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

# Sort by citation count descending
result.sort(key=lambda x: x['total_citation_count'], reverse=True)

print('Final result count: ' + str(len(result)))

if result:
    print('\nTop papers:')
    for p in result[:10]:
        print(p['title'] + ' (' + str(p['year']) + ') - ' + str(p['total_citation_count']) + ' citations')
else:
    print('\nNo matching papers found')

# Output final result
output = json.dumps(result)
print('\n---PRINT FORMAT---')
print('__RESULT__:')
print(output)"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.list_db:2': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:20': []}

exec(code, env_args)
