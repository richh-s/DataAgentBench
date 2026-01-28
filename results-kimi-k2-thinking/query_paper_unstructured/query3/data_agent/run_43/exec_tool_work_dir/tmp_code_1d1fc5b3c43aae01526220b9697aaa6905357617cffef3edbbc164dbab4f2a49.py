code = """import json
import re

# Load papers data
papers_file_path = locals()['var_functions.query_db:32']
with open(papers_file_path, 'r') as f:
    papers_raw = json.load(f)

# Quick analysis
print('Total papers loaded:', len(papers_raw))

# Sample a few papers
print('\nFirst 5 papers:')
for i, doc in enumerate(papers_raw[:5]):
    title = doc['filename'].replace('.txt', '')
    text_sample = doc['text'][:200]  # First 200 chars
    print(f"{i+1}. {title}")
    print(f"   Sample: {text_sample[:100]}...")
    # Check for year and empirical
    year_match = re.search(r'\b(20[12]\d|202[0-5])\b', doc['text'])
    year = year_match.group(1) if year_match else 'No year'
    has_empirical = 'empirical' in doc['text'].lower()
    print(f"   Year: {year}, Has 'empirical': {has_empirical}")
    print()

# Count empirical papers
empirical_count = sum(1 for doc in papers_raw if 'empirical' in doc['text'].lower())
print('Total papers with "empirical":', empirical_count)

# Count papers by year
from collections import Counter
year_counter = Counter()
for doc in papers_raw:
    year_match = re.search(r'\b(20[12]\d|202[0-5])\b', doc['text'])
    if year_match:
        year_counter[int(year_match.group(1))] += 1

print('\nPapers by year:')
for year in sorted(year_counter.keys()):
    print(f"  {year}: {year_counter[year]}")

# Check papers after 2017 specifically
papers_after_2016 = []
for doc in papers_raw:
    year_match = re.search(r'\b(20[12]\d|202[0-5])\b', doc['text'])
    if year_match:
        year = int(year_match.group(1))
        if year > 2016 and 'empirical' in doc['text'].lower():
            papers_after_2016.append({
                'title': doc['filename'].replace('.txt', ''),
                'year': year
            })

print('\nEmpirical papers after 2016 found:', len(papers_after_2016))
for paper in papers_after_2016[:10]:
    print(f"  {paper['year']}: {paper['title']}")

print('__RESULT__:')
print(json.dumps({
    'total_papers': len(papers_raw),
    'empirical_papers': empirical_count,
    'empirical_after_2016': len(papers_after_2016)
}))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:16': ['var_functions.list_db:0', 'var_functions.query_db:2', '__builtins__', 'json'], 'var_functions.execute_python:20': [], 'var_functions.list_db:22': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:24': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}, {'id': '6', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '95', 'citation_year': '2015'}, {'id': '7', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '14', 'citation_year': '2016'}, {'id': '8', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '12', 'citation_year': '2012'}, {'id': '9', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '76', 'citation_year': '2013'}, {'id': '10', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '55', 'citation_year': '2014'}], 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.execute_python:48': ['var_functions.list_db:0', 'var_functions.query_db:2', 'var_functions.execute_python:16', 'var_functions.execute_python:20', 'var_functions.list_db:22', 'var_functions.query_db:24', 'var_functions.query_db:30', 'var_functions.query_db:32', 'var_functions.query_db:36', '__builtins__', 'json'], 'var_functions.execute_python:50': ['var_functions.list_db:0', 'var_functions.query_db:2', 'var_functions.execute_python:16', 'var_functions.execute_python:20', 'var_functions.list_db:22', 'var_functions.query_db:24', 'var_functions.query_db:30', 'var_functions.query_db:32', 'var_functions.query_db:36', 'var_functions.execute_python:48', '__builtins__', 'json'], 'var_functions.execute_python:54': {'var_functions.query_db:2': {'type': "<class 'str'>", 'is_str': True, 'is_list': False, 'value': 'file_storage/functions.query_db:2.json'}, 'var_functions.query_db:24': {'type': "<class 'list'>", 'is_str': False, 'is_list': True, 'length': 10}, 'var_functions.query_db:30': {'type': "<class 'str'>", 'is_str': True, 'is_list': False, 'value': 'file_storage/functions.query_db:30.json'}, 'var_functions.query_db:32': {'type': "<class 'str'>", 'is_str': True, 'is_list': False, 'value': 'file_storage/functions.query_db:32.json'}, 'var_functions.query_db:36': {'type': "<class 'str'>", 'is_str': True, 'is_list': False, 'value': 'file_storage/functions.query_db:36.json'}}, 'var_functions.execute_python:58': [], 'var_functions.execute_python:62': [], 'var_functions.execute_python:70': []}

exec(code, env_args)
