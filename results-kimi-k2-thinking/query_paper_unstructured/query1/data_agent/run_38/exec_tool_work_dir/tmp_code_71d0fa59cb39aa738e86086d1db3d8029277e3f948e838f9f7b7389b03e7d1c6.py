code = """import json
import os

# Load food-related papers
food_papers_file = locals()['var_functions.query_db:18']
with open(food_papers_file, 'r') as f:
    food_papers = json.load(f)

# Extract titles
food_titles = []
for paper in food_papers:
    title = paper['filename'].replace('.txt', '')
    food_titles.append(title)

# Load citations
citations_file = locals()['var_functions.query_db:16']
with open(citations_file, 'r') as f:
    citations = json.load(f)

# Create citation dictionary
citation_dict = {}
for item in citations:
    citation_dict[item['title']] = int(item['total_citations'])

# Match and sum citations for food papers
total_citations = 0
matches = 0
for title in food_titles:
    if title in citation_dict:
        total_citations += citation_dict[title]
        matches += 1

result = {'total_citations': total_citations, 'papers_matched': matches}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:14': [{'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing'}, {'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing'}, {'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies'}, {'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies'}, {'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies'}, {'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies'}, {'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies'}, {'title': 'Sundroid: Solar Radiation Awareness with Smartphones'}, {'title': 'Sundroid: Solar Radiation Awareness with Smartphones'}, {'title': 'Sundroid: Solar Radiation Awareness with Smartphones'}], 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json'}

exec(code, env_args)
