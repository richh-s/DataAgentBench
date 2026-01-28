code = """import json
import re

# Load the data
citations_file = locals()['var_functions.query_db:6']
papers_file = locals()['var_functions.query_db:16']

with open(citations_file, 'r') as f:
    citations_data = json.load(f)

with open(papers_file, 'r') as f:
    papers_data = json.load(f)

# Clean and normalize citations
citations_dict = {}
for cit in citations_data:
    title = cit['title'].strip().lower()
    count = int(cit['citation_count'])
    if title in citations_dict:
        citations_dict[title] += count
    else:
        citations_dict[title] = count

# Extract domains from papers - look for domain keywords
food_papers = []
domain_keywords = ["food", "physical activity", "sleep", "mental", "finances", "productivity", "screen time", "social interactions", "location", "chronic", "diabetes", "health_behavior"]

for paper in papers_data:
    text = paper['text'].lower()
    filename = paper['filename'].replace('.txt', '').lower()
    title = filename
    
    # Check if paper is in food domain
    if 'food' in text:
        food_papers.append(title)

# Get total citations for food papers
total_citations = 0
food_paper_citations = {}

for paper_title in food_papers:
    if paper_title in citations_dict:
        total_citations += citations_dict[paper_title]
        food_paper_citations[paper_title] = citations_dict[paper_title]

result = {
    'food_papers_found': len(food_papers),
    'total_citations_for_food_papers': total_citations,
    'food_papers': food_paper_citations
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}, {'id': '6', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '95', 'citation_year': '2015'}, {'id': '7', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '14', 'citation_year': '2016'}, {'id': '8', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '12', 'citation_year': '2012'}, {'id': '9', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '76', 'citation_year': '2013'}, {'id': '10', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '55', 'citation_year': '2014'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:14': {'citations_loaded': 1405, 'papers_loaded': 5}, 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:18': {'citations_file': 'file_storage/functions.query_db:6.json', 'papers_file': 'file_storage/functions.query_db:16.json', 'locals_keys': ['var_functions.query_db:0', 'var_functions.query_db:2', 'var_functions.query_db:6', 'var_functions.query_db:8', 'var_functions.execute_python:14', 'var_functions.query_db:16', '__builtins__', 'json', 'os', 'citations_key', 'papers_key', 'citations_file_path', 'papers_file_path']}, 'var_functions.execute_python:20': {'citations_loaded': 1405, 'papers_loaded': 5}}

exec(code, env_args)
