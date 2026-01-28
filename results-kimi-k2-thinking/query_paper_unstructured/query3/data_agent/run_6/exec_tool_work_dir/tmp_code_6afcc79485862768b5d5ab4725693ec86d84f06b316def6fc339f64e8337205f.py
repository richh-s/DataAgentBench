code = """import json
import re

# Load the data
papers_data_file = var_functions.query_db:38
citations_data_file = var_functions.query_db:36

with open(papers_data_file, 'r') as f:
    papers_data = json.load(f)

with open(citations_data_file, 'r') as f:
    citations_data = json.load(f)

# Create citation lookup
citation_lookup = {item['title']: int(item['total_citations']) for item in citations_data}

# Process papers
result = []

for doc in papers_data:
    filename = doc['filename']
    text = doc['text']
    
    # Extract title
    title = filename.replace('.txt', '')
    
    # Extract year
    year = None
    patterns = [
        r'(CHI|Ubicomp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH|UbiComp)\s+(\d{4})',
        r'Copyright\s+.*\s+(\d{4})'
    ]
    
    for pattern in patterns:
        match = re.search(pattern, text)
        if match:
            if 'Copyright' in pattern:
                year = int(match.group(1))
            else:
                year = int(match.group(2))
            break
    
    # Check if empirical and after 2016
    if year and year > 2016 and title in citation_lookup:
        result.append({
            'title': title,
            'total_citations': citation_lookup[title]
        })

# Sort by citations
result.sort(key=lambda x: x['total_citations'], reverse=True)

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:8': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json'}

exec(code, env_args)
