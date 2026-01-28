code = """import json
import pandas as pd
import re

# Read papers data from storage
papers_list = var_query_db_32

# Read citations data from storage  
citations_list = var_query_db_36

# Process papers
papers_df = pd.DataFrame(papers_list)
papers_df['title'] = papers_df['filename'].str.replace('.txt', '')

def get_year(text):
    years = re.findall(r'\b(20[12]\d|202[0-5])\b', str(text))
    return int(years[0]) if years else None

papers_df['year'] = papers_df['text'].apply(get_year)

def get_contrib(text):
    t = str(text).lower()
    c = []
    if 'empirical' in t: c.append('empirical')
    if 'artifact' in t or 'system' in t: c.append('artifact')
    if 'theoretical' in t or 'theory' in t: c.append('theoretical')
    if 'survey' in t: c.append('survey')
    if 'methodological' in t or 'method' in t: c.append('methodological')
    return ','.join(c) if c else None

papers_df['contribution'] = papers_df['text'].apply(get_contrib)

# Filter papers after 2016 with empirical contribution
filtered_papers = papers_df[
    (papers_df['year'] > 2016) &
    (papers_df['contribution'].str.contains('empirical', na=False))
]

# Process citations
citations_df = pd.DataFrame(citations_list)
citations_df['total_citations'] = pd.to_numeric(citations_df['total_citations'])

# Merge results
merged = pd.merge(filtered_papers, citations_df, on='title', how='inner')

# Prepare output
output = merged[['title', 'total_citations']].to_dict('records')
print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:16': ['var_functions.list_db:0', 'var_functions.query_db:2', '__builtins__', 'json'], 'var_functions.execute_python:20': [], 'var_functions.list_db:22': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:24': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}, {'id': '6', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '95', 'citation_year': '2015'}, {'id': '7', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '14', 'citation_year': '2016'}, {'id': '8', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '12', 'citation_year': '2012'}, {'id': '9', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '76', 'citation_year': '2013'}, {'id': '10', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '55', 'citation_year': '2014'}], 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json'}

exec(code, env_args)
