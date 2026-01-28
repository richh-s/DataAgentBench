code = """import json
import pandas as pd
import re

# Load papers data
papers_file = locals()['var_functions.query_db:32']
with open(papers_file, 'r') as f:
    papers_raw = json.load(f)

# Load citations data
citations_file = locals()['var_functions.query_db:36']
with open(citations_file, 'r') as f:
    citations_raw = json.load(f)

# Comprehensive analysis
print('=== COMPREHENSIVE DATA ANALYSIS ===')

# Analyze papers
papers_analysis = []
for doc in papers_raw:
    title = doc['filename'].replace('.txt', '')
    text = doc['text']
    
    # Extract year
    year_match = re.search(r'\b(20[12]\d|202[0-5])\b', text)
    year = int(year_match.group(1)) if year_match else None
    
    # Check for empirical
    has_empirical = 'empirical' in text.lower()
    
    papers_analysis.append({
        'title': title,
        'year': year,
        'has_empirical': has_empirical
    })

papers_df = pd.DataFrame(papers_analysis)

print(f'\nPAPERS DATASET:')
print(f'Total papers: {len(papers_df)}')
print(f'Papers with extracted year: {papers_df["year"].notna().sum()}')
print(f'Papers with "empirical": {papers_df["has_empirical"].sum()}')

# Year distribution
print(f'\nYear distribution (2015-2022):')
yearly = papers_df.groupby('year').agg({'title': 'count', 'has_empirical': 'sum'})
for year in range(2015, 2023):
    if year in yearly.index:
        total = yearly.loc[year, 'title']
        empirical = yearly.loc[year, 'has_empirical']
        print(f'  {year}: {total} papers ({empirical} empirical)')

# Check empirical after 2016
empirical_after_2016 = papers_df[(papers_df['year'] > 2016) & papers_df['has_empirical']]
print(f'\nEmpirical papers after 2016: {len(empirical_after_2016)}')

if len(empirical_after_2016) > 0:
    print('\nThese papers are:')
    for _, row in empirical_after_2016.iterrows():
        print(f'  {row["year"]}: {row["title"]}')

# Analyze citations
print(f'\nCITATIONS DATASET:')
print(f'Total records: {len(citations_raw)}')

citations_df = pd.DataFrame(citations_raw)
citations_df['total_citations'] = pd.to_numeric(citations_df['total_citations'])

print(f'Unique titles in citations: {citations_df["title"].nunique()}')
print(f'Citation range: {citations_df["total_citations"].min()} to {citations_df["total_citations"].max()}')

# Check for matches (any year, any contribution)
print(f'\nMATCHING ANALYSIS:')
paper_titles = set(papers_df['title'])
citation_titles = set(citations_df['title'])

exact_matches = paper_titles & citation_titles
print(f'Total papers: {len(paper_titles)}')
print(f'Total cited papers: {len(citation_titles)}')
print(f'Exact title matches: {len(exact_matches)}')

# Check empirical papers specifically
empirical_titles = set(papers_df[papers_df['has_empirical']]['title'])
empirical_matches = empirical_titles & citation_titles
print(f'Empirical papers: {len(empirical_titles)}')
print(f'Empirical papers with citations: {len(empirical_matches)}')

# Check recent empirical papers
recent_empirical_titles = set(empirical_after_2016['title'])
recent_empirical_matches = recent_empirical_titles & citation_titles
print(f'Recent empirical papers (2017+): {len(recent_empirical_titles)}')
print(f'Recent empirical papers with citations: {len(recent_empirical_matches)}')

# Show some matches if any
if len(recent_empirical_matches) > 0:
    print('\nMatching recent empirical papers:')
    matching_titles = list(recent_empirical_matches)[:10]
    for title in matching_titles:
        citation_count = citations_df[citations_df['title'] == title]['total_citations'].iloc[0]
        year = papers_df[papers_df['title'] == title]['year'].iloc[0]
        print(f'  {year}: {title} ({citation_count} citations)')
else:
    print('\nNo matching recent empirical papers found.')
    print('\nSample recent empirical vs citation titles:')
    print('Recent empirical titles (first 3):')
    for title in list(recent_empirical_titles)[:3]:
        print(f'  - {title}')
    print('Citation titles (first 3):')
    for title in list(citation_titles)[:3]:
        print(f'  - {title}')

# Final results
if len(recent_empirical_matches) > 0:
    final_results = []
    for title in recent_empirical_matches:
        citation_count = citations_df[citations_df['title'] == title]['total_citations'].iloc[0]
        final_results.append({'title': title, 'total_citations': int(citation_count)})
else:
    final_results = []

print(f'\n{'='*60}')
print(f'FINAL ANSWER: {len(final_results)} papers found')
print(f'{'='*60}')

print('__RESULT__:')
print(json.dumps(final_results))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:16': ['var_functions.list_db:0', 'var_functions.query_db:2', '__builtins__', 'json'], 'var_functions.execute_python:20': [], 'var_functions.list_db:22': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:24': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}, {'id': '6', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '95', 'citation_year': '2015'}, {'id': '7', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '14', 'citation_year': '2016'}, {'id': '8', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '12', 'citation_year': '2012'}, {'id': '9', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '76', 'citation_year': '2013'}, {'id': '10', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '55', 'citation_year': '2014'}], 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.execute_python:48': ['var_functions.list_db:0', 'var_functions.query_db:2', 'var_functions.execute_python:16', 'var_functions.execute_python:20', 'var_functions.list_db:22', 'var_functions.query_db:24', 'var_functions.query_db:30', 'var_functions.query_db:32', 'var_functions.query_db:36', '__builtins__', 'json'], 'var_functions.execute_python:50': ['var_functions.list_db:0', 'var_functions.query_db:2', 'var_functions.execute_python:16', 'var_functions.execute_python:20', 'var_functions.list_db:22', 'var_functions.query_db:24', 'var_functions.query_db:30', 'var_functions.query_db:32', 'var_functions.query_db:36', 'var_functions.execute_python:48', '__builtins__', 'json'], 'var_functions.execute_python:54': {'var_functions.query_db:2': {'type': "<class 'str'>", 'is_str': True, 'is_list': False, 'value': 'file_storage/functions.query_db:2.json'}, 'var_functions.query_db:24': {'type': "<class 'list'>", 'is_str': False, 'is_list': True, 'length': 10}, 'var_functions.query_db:30': {'type': "<class 'str'>", 'is_str': True, 'is_list': False, 'value': 'file_storage/functions.query_db:30.json'}, 'var_functions.query_db:32': {'type': "<class 'str'>", 'is_str': True, 'is_list': False, 'value': 'file_storage/functions.query_db:32.json'}, 'var_functions.query_db:36': {'type': "<class 'str'>", 'is_str': True, 'is_list': False, 'value': 'file_storage/functions.query_db:36.json'}}, 'var_functions.execute_python:58': [], 'var_functions.execute_python:62': [], 'var_functions.execute_python:70': [], 'var_functions.execute_python:84': [], 'var_functions.execute_python:88': [], 'var_functions.execute_python:92': []}

exec(code, env_args)
