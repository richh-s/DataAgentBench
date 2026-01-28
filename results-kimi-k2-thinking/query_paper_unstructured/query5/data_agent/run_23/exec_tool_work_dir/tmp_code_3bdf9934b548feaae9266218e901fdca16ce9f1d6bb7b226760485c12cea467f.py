code = """import json
import re

# Access stored results
citations_result = var_query_db_5
paper_result = var_query_db_9

print('Types:', type(citations_result), type(paper_result))
print('Counts:', len(citations_result), len(paper_result))

# Build citations dictionary for fast lookup
citations_by_title = {}
for c in citations_result:
    citations_by_title[c['title']] = int(c['citation_count'])

print('Citations dict size:', len(citations_by_title))

# Find CHI papers
chi_titles = []
for doc in paper_result:
    text = doc['text']
    if 'CHI' in text:
        title = doc['filename'].replace('.txt', '')
        chi_titles.append(title)

print('CHI papers found:', len(chi_titles))

# Match with citations
total = 0
matches = 0
for title in chi_titles:
    if title in citations_by_title:
        total += citations_by_title[title]
        matches += 1

print('Matches found:', matches)
print('Total citations:', total)

output = {'total_citations': total, 'papers_matched': matches}
print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_functions.list_db:0': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:2': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json'}

exec(code, env_args)
