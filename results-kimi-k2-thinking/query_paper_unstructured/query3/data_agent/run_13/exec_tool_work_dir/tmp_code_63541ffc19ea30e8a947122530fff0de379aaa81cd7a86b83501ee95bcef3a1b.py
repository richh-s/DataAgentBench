code = """import json
import re
import sqlite3

# Load the papers from the file stored in the variable
papers_file = locals()['var_functions.query_db:46']
print('Loading papers from file:', papers_file)

with open(papers_file, 'r') as f:
    papers = json.load(f)

print('Total papers loaded:', len(papers))

# Extract paper metadata
paper_metadata = []
for paper in papers:
    title = paper['filename'].replace('.txt', '')
    text = paper['text'].lower()
    
    # Extract year from text - handle formats like '15 and 2015
    year = None
    # Look for year patterns
    year_matches = re.findall(r"(?:\b|')((?:20)?1[5-9]|20[12]\d)\b", paper['text'])
    years = []
    for match in year_matches:
        if match:
            if len(match) == 2:  # '15 format
                y = int('20' + match)
                if 2010 <= y <= 2030:
                    years.append(y)
            elif len(match) == 4:  # 2015 format
                y = int(match)
                if 2010 <= y <= 2030:
                    years.append(y)
    
    if years:
        year = max(years)
    
    # Determine if paper is empirical
    is_empirical = 'empirical' in text
    
    paper_metadata.append({
        'title': title,
        'year': year,
        'is_empirical': is_empirical
    })

# Create DataFrame
import pandas as pd
df_papers = pd.DataFrame(paper_metadata)

print('\nPaper statistics:')
print('Papers by year:', df_papers['year'].value_counts().sort_index().to_dict())
print('Total empirical papers:', df_papers['is_empirical'].sum())

# Filter for empirical papers after 2016
empirical_papers_2017plus = df_papers[
    (df_papers['is_empirical'] == True) & 
    (df_papers['year'] > 2016)
].copy()

print('\nEmpirical papers after 2016:', len(empirical_papers_2017plus))

# Get titles to match with citations
titles_for_citations = empirical_papers_2017plus['title'].tolist()

# Create result structure
result = {
    'empirical_papers_count': len(titles_for_citations),
    'titles': titles_for_citations[:10]  # First 10 for debugging
}

print('\nSample titles:', titles_for_citations[:5])

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:6': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:16': [{'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': 2018}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': 2019}], 'var_functions.execute_python:22': [], 'var_functions.execute_python:32': [], 'var_functions.execute_python:42': [], 'var_functions.execute_python:44': {'total_papers': 5, 'sample_filename': 'A Lived Informatics Model of Personal Informatics.txt', 'sample_text_start': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Hu"}, 'var_functions.query_db:46': 'file_storage/functions.query_db:46.json'}

exec(code, env_args)
