code = """import json
import re

# Get the MongoDB papers data
papers_data = []
try:
    # The variable containing papers with empirical keyword
    mongo_raw = locals()['var_functions.query_db:38']
    if isinstance(mongo_raw, str) and mongo_raw.endswith('.json'):
        with open(mongo_raw, 'r') as f:
            papers_data = json.load(f)
    else:
        papers_data = mongo_raw
except:
    pass

# Get the citation data
citations_data = []
try:
    cit_raw = locals()['var_functions.query_db:36']
    if isinstance(cit_raw, str) and cit_raw.endswith('.json'):
        with open(cit_raw, 'r') as f:
            citations_data = json.load(f)
    else:
        citations_data = cit_raw
except:
    pass

if not papers_data or not citations_data:
    # Try other variable names
    for name in locals().keys():
        if 'query_db' in name and '38' in name:
            papers_data = locals()[name]
            if isinstance(papers_data, str):
                with open(papers_data, 'r') as f:
                    papers_data = json.load(f)
        if 'query_db' in name and '36' in name:
            citations_data = locals()[name]
            if isinstance(citations_data, str):
                with open(citations_data, 'r') as f:
                    citations_data = json.load(f)

print(f"Papers: {len(papers_data)}, Citations: {len(citations_data)}")

# Create citation lookup
citation_dict = {}
for item in citations_data:
    citation_dict[item['title']] = int(item['total_citations'])

# Process papers
results = []

for paper in papers_data:
    filename = paper['filename']
    text = paper['text']
    title = filename.replace('.txt', '')
    
    # Extract year
    year = None
    match = re.search(r'(CHI|Ubicomp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH|UbiComp)\s+(\d{4})', text)
    if match:
        year = int(match.group(2))
    
    if year and year > 2016 and title in citation_dict:
        results.append({
            'title': title,
            'total_citations': citation_dict[title]
        })

results.sort(key=lambda x: x['total_citations'], reverse=True)

print('__RESULT__:')
print(json.dumps(results))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:8': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json'}

exec(code, env_args)
