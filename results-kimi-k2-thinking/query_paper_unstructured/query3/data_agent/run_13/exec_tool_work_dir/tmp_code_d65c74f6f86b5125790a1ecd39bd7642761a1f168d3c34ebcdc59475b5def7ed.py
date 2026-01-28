code = """import json
import re
import pandas as pd

# Load data papers and citations
papers_file = locals()['var_functions.query_db:46']
citations_file = locals()['var_functions.query_db:14']

with open(papers_file, 'r') as f:
    papers = json.load(f)

with open(citations_file, 'r') as f:
    citations = json.load(f)

# Analyze papers
paper_metadata = []
for paper in papers:
    title = paper['filename'].replace('.txt', '')
    text = paper['text']
    
    # Extract year
    year = None
    year_matches = re.findall(r"\b(20[0-9]{2})\b", text)
    if year_matches:
        valid_years = [int(y) for y in year_matches if 2000 <= int(y) <= 2030]
        if valid_years:
            year = max(valid_years)
    
    # Check for empirical
    has_empirical = 'empirical' in text.lower()
    
    paper_metadata.append({'title': title, 'year': year, 'empirical': has_empirical})

# Create DataFrames
df_papers = pd.DataFrame(paper_metadata)
df_citations = pd.DataFrame(citations)

print('Total papers:', len(df_papers))
print('Papers with year:', df_papers['year'].notna().sum())
print('Year range:', df_papers['year'].min(), 'to', df_papers['year'].max())
print('Empirical papers:', df_papers['empirical'].sum())

# Filter empirical papers after 2016
empirical_filtered = df_papers[(df_papers['empirical'] == True) & (df_papers['year'] > 2016)]

titles = empirical_filtered['title'].tolist()
years = empirical_filtered['year'].tolist()

print('Empirical after 2016:', len(titles))
print('Years:', years)

# Match with citations
results = []
for idx, title in enumerate(titles):
    year = years[idx]
    
    # Find citation record
    citation_row = df_citations[df_citations['title'] == title]
    if not citation_row.empty:
        total_citations = int(citation_row.iloc[0]['total_citations'])
        results.append({'title': title, 'year': year, 'total_citations': total_citations})

print('Results with citations:', len(results))

# Prepare output
output_json = json.dumps(results)
print('__RESULT__:')
print(output_json)"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:6': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:16': [{'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': 2018}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': 2019}], 'var_functions.execute_python:22': [], 'var_functions.execute_python:32': [], 'var_functions.execute_python:42': [], 'var_functions.execute_python:44': {'total_papers': 5, 'sample_filename': 'A Lived Informatics Model of Personal Informatics.txt', 'sample_text_start': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Hu"}, 'var_functions.query_db:46': 'file_storage/functions.query_db:46.json', 'var_functions.execute_python:50': [], 'var_functions.execute_python:52': {'total_records': 259, 'unique_titles': 259, 'sample_titles': ['"This Girl is on Fire": Sensemaking in an Online Health Community for Vulvodynia', 'A Family Health App: Engaging Children to Manage Wellness of Adults', 'A Lived Informatics Model of Personal Informatics', 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity', 'A Situated Exploration of Designing for Personal Health Ecosystems Through Data-enabled Design', 'A Spark of Activity: Exploring Informative Art As Visualization for Physical Activity', 'A Stage-based Model of Personal Informatics Systems', 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'Activity Tracking in Vivo']}, 'var_functions.execute_python:56': [], 'var_functions.execute_python:64': {'count': 0, 'titles': []}, 'var_functions.execute_python:72': {'papers': []}}

exec(code, env_args)
