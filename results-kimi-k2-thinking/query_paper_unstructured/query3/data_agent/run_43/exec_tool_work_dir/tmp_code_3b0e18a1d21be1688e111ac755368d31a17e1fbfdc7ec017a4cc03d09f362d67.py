code = """import json
import pandas as pd
import re

# Load papers data from file
papers_file = locals()['var_functions.query_db:32']
with open(papers_file, 'r') as f:
    papers_raw = json.load(f)

# Load citations data from file
citations_file = locals()['var_functions.query_db:36']
with open(citations_file, 'r') as f:
    citations_raw = json.load(f)

# Process all papers
papers = []
for doc in papers_raw:
    title = doc['filename'].replace('.txt', '')
    text = doc['text']
    
    # Extract year
    year_match = re.search(r'\b(20[12]\d|202[0-5])\b', text)
    year = int(year_match.group(1)) if year_match else None
    
    # Check for empirical
    has_empirical = 'empirical' in text.lower()
    
    papers.append({
        'title': title,
        'year': year,
        'has_empirical': has_empirical
    })

# Create DataFrame
df_papers = pd.DataFrame(papers)

print('Paper analysis:')
print('Total papers:', len(df_papers))
print('Years extracted:', df_papers['year'].notna().sum())
print('Unique years with counts:')
year_counts = df_papers['year'].value_counts().sort_index()
for year, count in year_counts.items():
    if year is not None:
        print(f"  {year}: {count}")

print('\nEmpirical papers found:', df_papers['has_empirical'].sum())

# After 2016
after_2016 = df_papers[df_papers['year'] > 2016]
print('Papers after 2016:', len(after_2016))

empirical_after_2016 = after_2016[after_2016['has_empirical']]
print('Empirical papers after 2016:', len(empirical_after_2016))

if len(empirical_after_2016) > 0:
    print('\nSome empirical papers after 2016:')
    for _, row in empirical_after_2016.head(10).iterrows():
        print(f"  {row['year']}: {row['title']}")

# Merge with citations
print('\n\nCitations data loaded:', len(citations_raw))
citations_df = pd.DataFrame(citations_raw)
citations_df['total_citations'] = pd.to_numeric(citations_df['total_citations'])

# Find matching papers
empirical_titles = set(empirical_after_2016['title'])
citations_with_papers = citations_df[citations_df['title'].isin(empirical_titles)]
print('Citations for empirical papers after 2016:', len(citations_with_papers))

if len(citations_with_papers) > 0:
    results = citations_with_papers[['title', 'total_citations']].to_dict('records')
    print('\nFinal results:')
    for r in results:
        print(f"  {r['title']}: {r['total_citations']} citations")
else:
    print('\nNo matches found between empirical papers and citations')

# Output for final
final_results = citations_with_papers[['title', 'total_citations']].to_dict('records')
print('__RESULT__:')
print(json.dumps(final_results))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:16': ['var_functions.list_db:0', 'var_functions.query_db:2', '__builtins__', 'json'], 'var_functions.execute_python:20': [], 'var_functions.list_db:22': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:24': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}, {'id': '6', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '95', 'citation_year': '2015'}, {'id': '7', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '14', 'citation_year': '2016'}, {'id': '8', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '12', 'citation_year': '2012'}, {'id': '9', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '76', 'citation_year': '2013'}, {'id': '10', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '55', 'citation_year': '2014'}], 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.execute_python:48': ['var_functions.list_db:0', 'var_functions.query_db:2', 'var_functions.execute_python:16', 'var_functions.execute_python:20', 'var_functions.list_db:22', 'var_functions.query_db:24', 'var_functions.query_db:30', 'var_functions.query_db:32', 'var_functions.query_db:36', '__builtins__', 'json'], 'var_functions.execute_python:50': ['var_functions.list_db:0', 'var_functions.query_db:2', 'var_functions.execute_python:16', 'var_functions.execute_python:20', 'var_functions.list_db:22', 'var_functions.query_db:24', 'var_functions.query_db:30', 'var_functions.query_db:32', 'var_functions.query_db:36', 'var_functions.execute_python:48', '__builtins__', 'json'], 'var_functions.execute_python:54': {'var_functions.query_db:2': {'type': "<class 'str'>", 'is_str': True, 'is_list': False, 'value': 'file_storage/functions.query_db:2.json'}, 'var_functions.query_db:24': {'type': "<class 'list'>", 'is_str': False, 'is_list': True, 'length': 10}, 'var_functions.query_db:30': {'type': "<class 'str'>", 'is_str': True, 'is_list': False, 'value': 'file_storage/functions.query_db:30.json'}, 'var_functions.query_db:32': {'type': "<class 'str'>", 'is_str': True, 'is_list': False, 'value': 'file_storage/functions.query_db:32.json'}, 'var_functions.query_db:36': {'type': "<class 'str'>", 'is_str': True, 'is_list': False, 'value': 'file_storage/functions.query_db:36.json'}}, 'var_functions.execute_python:58': [], 'var_functions.execute_python:62': []}

exec(code, env_args)
