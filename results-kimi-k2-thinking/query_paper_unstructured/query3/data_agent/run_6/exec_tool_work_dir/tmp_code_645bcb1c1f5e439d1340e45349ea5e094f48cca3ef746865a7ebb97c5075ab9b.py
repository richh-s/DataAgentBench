code = """import json
import re

# Process the papers from the stored value
papers_var = 'var_functions.query_db:38'
citations_var = 'var_functions.query_db:36'

# Since these are file paths, read them
papers_file = '/tmp/tmpk3cghq9p.json'
citations_file = '/tmp/tmpk0z7xbrf.json'

with open(papers_file, 'r') as f:
    papers_data = json.load(f)

with open(citations_file, 'r') as f:
    citations_data = json.load(f)

# Create citation dictionary
citations_dict = {}
for item in citations_data:
    citations_dict[item['title']] = int(item['total_citations'])

# Process papers
final_result = []

for paper in papers_data:
    filename = paper['filename']
    text = paper['text']
    
    title = filename.replace('.txt', '')
    
    # Find year
    year = None
    y1 = re.search(r'(CHI|Ubicomp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH|UbiComp)\s+(\d{4})', text)
    if y1:
        year = int(y1.group(2))
    else:
        y2 = re.search(r'Copyright[^\d]*(\d{4})', text)
        if y2:
            year = int(y2.group(1))
    
    if year and year > 2016 and title in citations_dict:
        final_result.append({
            'title': title,
            'total_citations': citations_dict[title]
        })

# Sort
def get_citations(p):
    return p['total_citations']

final_result.sort(key=get_citations, reverse=True)

# Output
output = json.dumps(final_result)
print('__RESULT__:')
print(output)"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:8': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json'}

exec(code, env_args)
