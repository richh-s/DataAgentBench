code = """import json
import os
import re

# Load food-related papers file
food_papers_file = locals()['var_functions.query_db:18']
print('File path:', food_papers_file)

with open(food_papers_file, 'r') as f:
    food_papers = json.load(f)

print('Total food papers loaded:', len(food_papers))

# Extract titles (remove .txt extension)
food_titles = []
for paper in food_papers:
    filename = paper['filename']
    title = filename.replace('.txt', '')
    food_titles.append(title)

print('Sample food titles:', food_titles[:5])

# Load citations data
citations_file = locals()['var_functions.query_db:16']
print('Citations file path:', citations_file)

with open(citations_file, 'r') as f:
    citations = json.load(f)

print('Total citations records:', len(citations))

# Convert to dict for easy lookup
citation_dict = {}
for item in citations:
    title = item['title']
    total_citations = int(item['total_citations'])
    citation_dict[title] = total_citations

# Find matching food papers and sum citations
food_citation_total = 0
matching_papers = []

for food_title in food_titles:
    if food_title in citation_dict:
        cit_count = citation_dict[food_title]
        food_citation_total += cit_count
        matching_papers.append((food_title, cit_count))

print('Found', len(matching_papers), 'matching papers')
print('Total citations:', food_citation_total)

# Sort by citation count
top_papers = sorted(matching_papers, key=lambda x: x[1], reverse=True)
print('
Top cited papers:')
for title, count in top_papers[:10]:
    print(count, ':', title)

result = {
    'total_citations': food_citation_total,
    'papers_count': len(matching_papers)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:14': [{'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing'}, {'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing'}, {'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies'}, {'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies'}, {'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies'}, {'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies'}, {'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies'}, {'title': 'Sundroid: Solar Radiation Awareness with Smartphones'}, {'title': 'Sundroid: Solar Radiation Awareness with Smartphones'}, {'title': 'Sundroid: Solar Radiation Awareness with Smartphones'}], 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json'}

exec(code, env_args)
