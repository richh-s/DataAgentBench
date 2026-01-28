code = """import json
import re

# Get the data from the variables
papers_data = var_functions.query_db:38
citations_data = var_functions.query_db:36

# Process MongoDB papers
empirical_papers_after_2016 = []

for doc in papers_data:
    filename = doc['filename']
    text = doc['text']
    
    # Extract title
    title = filename.replace('.txt', '')
    
    # Extract year from text
    year = None
    match = re.search(r'(CHI|Ubicomp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH|UbiComp)\s+(\d{4})', text)
    if match:
        year = int(match.group(2))
    else:
        # Try other patterns
        year_match = re.search(r'Copyright\s+.*\s+(\d{4})', text)
        if year_match:
            year = int(year_match.group(1))
    
    # Check if published after 2016
    if year and year > 2016:
        # Check if we have citation data for this title
        citations = None
        for cit in citations_data:
            if cit['title'] == title:
                citations = int(cit['total_citations'])
                break
        
        if citations is not None:
            empirical_papers_after_2016.append({
                'title': title,
                'year': year,
                'total_citations': citations
            })

# Sort by citations descending
empirical_papers_after_2016.sort(key=lambda x: x['total_citations'], reverse=True)

# Create result with just title and total_citations
result = []
for paper in empirical_papers_after_2016:
    result.append({
        'title': paper['title'],
        'total_citations': paper['total_citations']
    })

# Print in required format
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:8': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json'}

exec(code, env_args)
