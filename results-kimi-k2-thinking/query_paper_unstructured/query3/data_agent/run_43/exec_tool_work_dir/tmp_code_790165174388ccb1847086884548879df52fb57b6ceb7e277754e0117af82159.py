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

# Process papers systematically
papers_processed = []
for idx, doc in enumerate(papers_raw):
    title = doc['filename'].replace('.txt', '')
    text = doc['text']
    
    # Extract year - look for 4-digit years around 2010-2025
    year_pattern = r'\b(20[12]\d|202[0-5])\b'
    years_found = re.findall(year_pattern, text)
    year = None
    if years_found:
        # Take the first year found (usually the publication year)
        year = int(years_found[0])
    
    # Check for empirical in the full text
    text_lower = text.lower()
    has_empirical = 'empirical' in text_lower
    
    papers_processed.append({
        'title': title,
        'year': year,
        'has_empirical': has_empirical,
        'text_preview': text[:200]  # First 200 chars for debugging
    })

# Create DataFrame
df_papers = pd.DataFrame(papers_processed)

print('='*60)
print('PAPER ANALYSIS REPORT')
print('='*60)
print(f'Total papers loaded: {len(df_papers)}')
print(f'Papers with year extracted: {df_papers["year"].notna().sum()}')
print(f'Papers with "empirical" mention: {df_papers["has_empirical"].sum()}')
print(f'Year range: {df_papers["year"].min()} to {df_papers["year"].max()}')

# Distribution by year
print('\nPapers by year (all):')
year_counts = df_papers.groupby('year').size().sort_index()
for year, count in year_counts.items():
    if pd.notna(year) and year >= 2010:
        print(f'  {year}: {count} papers')

# Check empirical papers by year
print('\nEmpirical papers by year:')
empirical_by_year = df_papers[df_papers['has_empirical']].groupby('year').size().sort_index()
for year, count in empirical_by_year.items():
    if pd.notna(year) and year >= 2010:
        print(f'  {year}: {count} empirical papers')

# Filter for papers after 2016 with empirical contribution
filtered_papers = df_papers[
    (df_papers['year'] > 2016) & 
    (df_papers['has_empirical'] == True)
]

print(f'\n{'='*60}')
print(f'FILTERED RESULTS: Empirical papers after 2016')
print(f'{'='*60}')
print(f'Count: {len(filtered_papers)}')

if len(filtered_papers) > 0:
    print('\nList of papers:')
    for _, row in filtered_papers.iterrows():
        print(f"  {row['year']}: {row['title']}")
else:
    print('\nNo empirical papers after 2016 found')
    print('\nChecking papers with year > 2016:')
    recent_papers = df_papers[df_papers['year'] > 2016]
    print(f'  Total recent papers: {len(recent_papers)}')
    print('\nChecking empirical papers (any year):')
    empirical_any = df_papers[df_papers['has_empirical']]
    print(f'  Total empirical papers: {len(empirical_any)}')

# Check citations data
print(f'\n{'='*60}')
print('CITATIONS DATA OVERVIEW')
print(f'{'='*60}')
print(f'Total citation records: {len(citations_raw)}')
if citations_raw:
    print(f'First few titles in citations:')
    for i, rec in enumerate(citations_raw[:5]):
        print(f"  {i+1}. {rec.get('title', 'N/A')}: {rec.get('total_citations', 'N/A')} citations")

# Try to match papers with citations
if len(filtered_papers) > 0:
    df_citations = pd.DataFrame(citations_raw)
    df_citations['total_citations'] = pd.to_numeric(df_citations['total_citations'])
    
    # Check for matching titles
    paper_titles = set(filtered_papers['title'])
    citation_titles = set(df_citations['title'])
    
    print(f'\nMatching analysis:')
    print(f'  Paper titles to match: {len(paper_titles)}')
    print(f'  Citation titles available: {len(citation_titles)}')
    print(f'  Overlap: {len(paper_titles & citation_titles)}')
    
    if len(paper_titles & citation_titles) == 0:
        print('\nNo matching titles found. Sample comparison:')
        print('  Sample paper titles:')
        for title in list(paper_titles)[:3]:
            print(f"    - {title}")
        print('  Sample citation titles:')
        for title in list(citation_titles)[:3]:
            print(f"    - {title}")

# Final merged results
final_results = []
if len(filtered_papers) > 0 and citations_raw:
    merged_df = pd.merge(filtered_papers, df_citations, on='title', how='inner')
    final_results = merged_df[['title', 'total_citations']].to_dict('records')

print(f'\n{'='*60}')
print(f'FINAL RESULTS')
print(f'{'='*60}')
print(f'Papers with both empirical contribution and citation data: {len(final_results)}')

print('__RESULT__:')
print(json.dumps(final_results))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:16': ['var_functions.list_db:0', 'var_functions.query_db:2', '__builtins__', 'json'], 'var_functions.execute_python:20': [], 'var_functions.list_db:22': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:24': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}, {'id': '6', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '95', 'citation_year': '2015'}, {'id': '7', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '14', 'citation_year': '2016'}, {'id': '8', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '12', 'citation_year': '2012'}, {'id': '9', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '76', 'citation_year': '2013'}, {'id': '10', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '55', 'citation_year': '2014'}], 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.execute_python:48': ['var_functions.list_db:0', 'var_functions.query_db:2', 'var_functions.execute_python:16', 'var_functions.execute_python:20', 'var_functions.list_db:22', 'var_functions.query_db:24', 'var_functions.query_db:30', 'var_functions.query_db:32', 'var_functions.query_db:36', '__builtins__', 'json'], 'var_functions.execute_python:50': ['var_functions.list_db:0', 'var_functions.query_db:2', 'var_functions.execute_python:16', 'var_functions.execute_python:20', 'var_functions.list_db:22', 'var_functions.query_db:24', 'var_functions.query_db:30', 'var_functions.query_db:32', 'var_functions.query_db:36', 'var_functions.execute_python:48', '__builtins__', 'json'], 'var_functions.execute_python:54': {'var_functions.query_db:2': {'type': "<class 'str'>", 'is_str': True, 'is_list': False, 'value': 'file_storage/functions.query_db:2.json'}, 'var_functions.query_db:24': {'type': "<class 'list'>", 'is_str': False, 'is_list': True, 'length': 10}, 'var_functions.query_db:30': {'type': "<class 'str'>", 'is_str': True, 'is_list': False, 'value': 'file_storage/functions.query_db:30.json'}, 'var_functions.query_db:32': {'type': "<class 'str'>", 'is_str': True, 'is_list': False, 'value': 'file_storage/functions.query_db:32.json'}, 'var_functions.query_db:36': {'type': "<class 'str'>", 'is_str': True, 'is_list': False, 'value': 'file_storage/functions.query_db:36.json'}}, 'var_functions.execute_python:58': [], 'var_functions.execute_python:62': [], 'var_functions.execute_python:70': [], 'var_functions.execute_python:84': []}

exec(code, env_args)
