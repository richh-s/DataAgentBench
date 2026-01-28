code = """import json
import pandas as pd
import re

# Get the papers data (file path stored in variable)
papers_file = var_functions.query_db_32

# Read the papers data
with open(papers_file, 'r') as f:
    papers_data = json.load(f)

# Get the citations data (actual list from variable)
citations_data = var_functions.query_db_36

# Process papers
papers_df = pd.DataFrame(papers_data)
papers_df['title'] = papers_df['filename'].str.replace('.txt', '', regex=False)

def extract_year(text):
    years = re.findall(r'\b(20[12]\d|202[0-5])\b', str(text))
    return int(years[0]) if years else None

papers_df['year'] = papers_df['text'].apply(extract_year)

def extract_contribution(text):
    text_lower = str(text).lower()
    contributions = []
    if 'empirical' in text_lower: contributions.append('empirical')
    if 'artifact' in text_lower or 'system' in text_lower: contributions.append('artifact')
    if 'theoretical' in text_lower or 'theory' in text_lower: contributions.append('theoretical')
    if 'survey' in text_lower: contributions.append('survey')
    if 'methodological' in text_lower or 'method' in text_lower: contributions.append('methodological')
    return ','.join(contributions) if contributions else None

papers_df['contribution'] = papers_df['text'].apply(extract_contribution)

# Filter for papers after 2016 with empirical contribution
filtered_papers = papers_df[
    (papers_df['year'] > 2016) & 
    (papers_df['contribution'].str.contains('empirical', na=False))
]

# Process citations
citations_df = pd.DataFrame(citations_data)
citations_df['total_citations'] = pd.to_numeric(citations_df['total_citations'])

# Merge papers with citations
merged_df = pd.merge(filtered_papers, citations_df, on='title', how='inner')

# Prepare results
result = merged_df[['title', 'total_citations']].to_dict('records')

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:16': ['var_functions.list_db:0', 'var_functions.query_db:2', '__builtins__', 'json'], 'var_functions.execute_python:20': [], 'var_functions.list_db:22': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:24': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}, {'id': '6', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '95', 'citation_year': '2015'}, {'id': '7', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '14', 'citation_year': '2016'}, {'id': '8', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '12', 'citation_year': '2012'}, {'id': '9', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '76', 'citation_year': '2013'}, {'id': '10', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '55', 'citation_year': '2014'}], 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json'}

exec(code, env_args)
