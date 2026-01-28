code = """import json
import re

# Read the file
result_path = var_functions.query_db:14
with open(result_path, 'r') as f:
    papers = json.load(f)

print('Total papers:', len(papers))

papers_2016 = []
for paper in papers:
    text = paper['text']
    filename = paper['filename']
    title = filename.replace('.txt', '')
    
    # Find year
    year_match = re.search(r'20\d{2}', text[:2000])
    if year_match:
        year = int(year_match.group())
        if year == 2016:
            # Check for physical activity
            if 'physical activity' in text.lower():
                papers_2016.append(title)

print('2016 physical activity papers:', len(papers_2016))

for title in papers_2016:
    print(title)

print('__RESULT__:')
print(json.dumps(papers_2016))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:10': [{'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.list_db:12': ['paper_docs'], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)
