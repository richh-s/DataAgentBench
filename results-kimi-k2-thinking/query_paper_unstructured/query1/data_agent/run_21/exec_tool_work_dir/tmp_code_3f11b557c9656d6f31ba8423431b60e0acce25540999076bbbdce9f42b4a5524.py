code = """import json

# Load the filtered food papers from MongoDB
with open('/tmp/tmp_result_28.json', 'r') as f:
    food_papers = json.load(f)

# Load all citations from SQLite (using a smaller sample to check structure)
# We need to load the full citations data
import os
# Try to find the full citations file
citations_file = '/tmp/tmp_result_12.json'
if not os.path.exists(citations_file):
    citations_file = '/tmp/tmp_result_20.json'

with open(citations_file, 'r') as f:
    citations = json.load(f)

print('Food papers found: ' + str(len(food_papers)))
print('Total citations records: ' + str(len(citations)))

# Extract titles from food papers
food_titles = []
for paper in food_papers:
    filename = paper['filename']
    title = filename.replace('.txt', '')
    food_titles.append(title)

print('Food paper titles: ' + str(food_titles[:10]))

# Build a map of all citation records by title
citation_map = {}
for citation in citations:
    title = citation['title']
    if title not in citation_map:
        citation_map[title] = []
    citation_map[title].append({
        'citation_count': int(citation['citation_count']),
        'citation_year': int(citation['citation_year'])
    })

print('Unique papers with citations: ' + str(len(citation_map)))

# Find food papers in citations and sum their citations
total_citations = 0
matched_food_papers = []

for food_title in food_titles:
    if food_title in citation_map:
        paper_citations = citation_map[food_title]
        paper_total = sum(c['citation_count'] for c in paper_citations)
        total_citations += paper_total
        matched_food_papers.append({
            'title': food_title,
            'citation_records': len(paper_citations),
            'total_citations': paper_total
        })
        print('Matched: ' + food_title + ' with ' + str(paper_total) + ' citations')

print('Total citations for food papers: ' + str(total_citations))
print('Number of food papers with citation data: ' + str(len(matched_food_papers)))

result = {
    'total_citations': total_citations,
    'food_papers_matched': len(matched_food_papers),
    'food_papers': matched_food_papers
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:6': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}, {'id': '6', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '95', 'citation_year': '2015'}, {'id': '7', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '14', 'citation_year': '2016'}, {'id': '8', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '12', 'citation_year': '2012'}, {'id': '9', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '76', 'citation_year': '2013'}, {'id': '10', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '55', 'citation_year': '2014'}], 'var_functions.list_db:10': ['paper_docs'], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json'}

exec(code, env_args)
