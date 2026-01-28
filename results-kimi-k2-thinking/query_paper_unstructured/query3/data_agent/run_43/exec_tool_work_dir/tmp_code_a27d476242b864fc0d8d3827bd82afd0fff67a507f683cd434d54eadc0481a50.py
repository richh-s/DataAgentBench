code = """import json
import pandas as pd
import re

# Get the citations data
citations_data = var_functions.query_db:24

# Get the papers file path and read it
papers_file_path = var_functions.query_db:2

# Read the papers data from file
with open(papers_file_path, 'r') as f:
    papers_data = json.load(f)

# Create DataFrame for papers
df_papers = pd.DataFrame(papers_data)

# Extract title from filename (remove .txt extension)
df_papers['title'] = df_papers['filename'].str.replace('.txt', '', regex=False)

# Extract year from text
def extract_year(text):
    years = re.findall(r'\b(20[12]\d|202[0-5])\b', str(text))
    if years:
        return int(years[0])
    return None

df_papers['year'] = df_papers['text'].apply(extract_year)

# Extract contribution type
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

# Filter papers after 2016 with empirical contribution
df_filtered = df_papers[
    (df_papers['year'] > 2016) &
    (df_papers['contribution'].str.contains('empirical', na=False))
]

# Create DataFrame for citations
df_citations = pd.DataFrame(citations_data)

# Merge papers with citations
df_merged = pd.merge(df_filtered, df_citations, on='title', how='inner')

# Calculate total citation count for each paper
df_total_citations = df_merged.groupby('title')['citation_count'].sum().reset_index()

# Get year and contribution info
df_final = pd.merge(df_total_citations, df_filtered[['title', 'year', 'contribution']], on='title',
how='left')

result = df_final.to_dict('records')
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:16': ['var_functions.list_db:0', 'var_functions.query_db:2', '__builtins__', 'json'], 'var_functions.execute_python:20': [], 'var_functions.list_db:22': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:24': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}, {'id': '6', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '95', 'citation_year': '2015'}, {'id': '7', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '14', 'citation_year': '2016'}, {'id': '8', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '12', 'citation_year': '2012'}, {'id': '9', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '76', 'citation_year': '2013'}, {'id': '10', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '55', 'citation_year': '2014'}]}

exec(code, env_args)
