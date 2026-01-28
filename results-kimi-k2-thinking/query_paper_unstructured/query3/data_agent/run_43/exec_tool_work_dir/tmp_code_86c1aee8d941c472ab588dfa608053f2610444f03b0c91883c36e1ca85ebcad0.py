code = """import json, pandas as pd, re

# Load data
papers_path = locals()['var_functions.query_db:32']
with open(papers_path, 'r') as f:
    papers_raw = json.load(f)

citations_path = locals()['var_functions.query_db:36']
with open(citations_path, 'r') as f:
    citations_raw = json.load(f)

# Check papers
papers_list = []
for doc in papers_raw:
    title = doc['filename'].replace('.txt', '')
    text = doc['text']
    year_match = re.search(r'\b(20[12]\d|202[0-5])\b', text)
    year = int(year_match.group(1)) if year_match else None
    has_empirical = 'empirical' in text.lower()
    papers_list.append({'title': title, 'year': year, 'empirical': has_empirical})

papers_df = pd.DataFrame(papers_list)

# Check citations
citations_df = pd.DataFrame(citations_raw)

print('Overall statistics:')
print(f'Total papers: {len(papers_df)}')
print(f'Papers with year: {papers_df["year"].notna().sum()}')
print(f'Year range: {papers_df["year"].min()} to {papers_df["year"].max()}')
print(f'Empirical papers: {papers_df["empirical"].sum()}')

print('\nYear distribution (2014-2022):')
for year in range(2014, 2023):
    count = len(papers_df[papers_df['year'] == year])
    emp_count = len(papers_df[(papers_df['year'] == year) & papers_df['empirical']])
    if count > 0:
        print(f'  {year}: {count} papers ({emp_count} empirical)')

print('\nRecent papers (2017-2022):')
recent = papers_df[papers_df['year'] >= 2017]
print(f'Total recent papers: {len(recent)}')
print(f'Recent empirical papers: {len(recent[recent["empirical"]])}')

if len(recent[recent['empirical']]) > 0:
    print('\nRecent empirical papers:')
    for _, row in recent[recent['empirical']].head(10).iterrows():
        print(f'  {row["year"]}: {row["title"]}')

print('\nCitations data:')
print(f'Total citation records: {len(citations_df)}')
if len(citations_df) > 0:
    print(f'Unique titles in citations: {citations_df["title"].nunique()}')
    print('Sample titles:', citations_df["title"].head(5).tolist())

# Check for matching titles (any year, just to see if matching works)
empirical_titles = set(papers_df[papers_df['empirical']]['title'].tolist())
citation_titles = set(citations_df['title'].tolist())
intersection = empirical_titles & citation_titles

print(f'\nMatching titles (any year, empirical): {len(intersection)}')
if len(intersection) > 0:
    print('Sample matches:', list(intersection)[:5])

print('__RESULT__:')
print(json.dumps({
    'total_papers': len(papers_df),
    'empirical_papers': int(papers_df['empirical'].sum()),
    'recent_empirical': int(len(recent[recent['empirical']])),
    'citation_records': len(citations_df),
    'matching_titles': len(intersection)
}))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:16': ['var_functions.list_db:0', 'var_functions.query_db:2', '__builtins__', 'json'], 'var_functions.execute_python:20': [], 'var_functions.list_db:22': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:24': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}, {'id': '6', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '95', 'citation_year': '2015'}, {'id': '7', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '14', 'citation_year': '2016'}, {'id': '8', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '12', 'citation_year': '2012'}, {'id': '9', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '76', 'citation_year': '2013'}, {'id': '10', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '55', 'citation_year': '2014'}], 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.execute_python:48': ['var_functions.list_db:0', 'var_functions.query_db:2', 'var_functions.execute_python:16', 'var_functions.execute_python:20', 'var_functions.list_db:22', 'var_functions.query_db:24', 'var_functions.query_db:30', 'var_functions.query_db:32', 'var_functions.query_db:36', '__builtins__', 'json'], 'var_functions.execute_python:50': ['var_functions.list_db:0', 'var_functions.query_db:2', 'var_functions.execute_python:16', 'var_functions.execute_python:20', 'var_functions.list_db:22', 'var_functions.query_db:24', 'var_functions.query_db:30', 'var_functions.query_db:32', 'var_functions.query_db:36', 'var_functions.execute_python:48', '__builtins__', 'json'], 'var_functions.execute_python:54': {'var_functions.query_db:2': {'type': "<class 'str'>", 'is_str': True, 'is_list': False, 'value': 'file_storage/functions.query_db:2.json'}, 'var_functions.query_db:24': {'type': "<class 'list'>", 'is_str': False, 'is_list': True, 'length': 10}, 'var_functions.query_db:30': {'type': "<class 'str'>", 'is_str': True, 'is_list': False, 'value': 'file_storage/functions.query_db:30.json'}, 'var_functions.query_db:32': {'type': "<class 'str'>", 'is_str': True, 'is_list': False, 'value': 'file_storage/functions.query_db:32.json'}, 'var_functions.query_db:36': {'type': "<class 'str'>", 'is_str': True, 'is_list': False, 'value': 'file_storage/functions.query_db:36.json'}}, 'var_functions.execute_python:58': [], 'var_functions.execute_python:62': [], 'var_functions.execute_python:70': [], 'var_functions.execute_python:84': [], 'var_functions.execute_python:88': []}

exec(code, env_args)
