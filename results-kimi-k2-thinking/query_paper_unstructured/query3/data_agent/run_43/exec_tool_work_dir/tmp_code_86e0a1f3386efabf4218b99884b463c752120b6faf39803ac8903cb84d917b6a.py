code = """import json
import pandas as pd
import re

# Read papers data from file
papers_file = var_functions.query_db:32
with open(papers_file, 'r') as f:
    papers_list = json.load(f)

# Read citations data from file
citations_file = var_functions.query_db:36
with open(citations_file, 'r') as f:
    citations_list = json.load(f)

# Process papers: extract title, year, and contribution
df_papers = pd.DataFrame(papers_list)
df_papers['title'] = df_papers['filename'].str.replace('.txt', '', regex=False)

# Extract year from text
def extract_year(text):
    years = re.findall(r'\b(20[12]\d|202[0-5])\b', str(text))
    return int(years[0]) if years else None

df_papers['year'] = df_papers['text'].apply(extract_year)

# Extract contribution types
def extract_contribution(text):
    text_lower = str(text).lower()
    contributions = []
    if 'empirical' in text_lower:
        contributions.append('empirical')
    if 'artifact' in text_lower or 'system' in text_lower:
        contributions.append('artifact')
    if 'theoretical' in text_lower or 'theory' in text_lower:
        contributions.append('theoretical')
    if 'survey' in text_lower:
        contributions.append('survey')
    if 'methodological' in text_lower or 'method' in text_lower:
        contributions.append('methodological')
    return ','.join(contributions) if contributions else None

df_papers['contribution'] = df_papers['text'].apply(extract_contribution)

# Filter for papers after 2016 with empirical contribution
df_papers_filtered = df_papers[
    (df_papers['year'] > 2016) &
    (df_papers['contribution'].str.contains('empirical', na=False))
]

# Process citations
df_citations = pd.DataFrame(citations_list)
df_citations['total_citations'] = pd.to_numeric(df_citations['total_citations'])

# Merge papers with citations
df_merged = pd.merge(df_papers_filtered, df_citations, on='title', how='inner')

# Prepare results with title and total citation count
result = df_merged[['title', 'total_citations']].to_dict('records')

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:16': ['var_functions.list_db:0', 'var_functions.query_db:2', '__builtins__', 'json'], 'var_functions.execute_python:20': [], 'var_functions.list_db:22': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:24': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}, {'id': '6', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '95', 'citation_year': '2015'}, {'id': '7', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '14', 'citation_year': '2016'}, {'id': '8', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '12', 'citation_year': '2012'}, {'id': '9', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '76', 'citation_year': '2013'}, {'id': '10', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '55', 'citation_year': '2014'}], 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json'}

exec(code, env_args)
