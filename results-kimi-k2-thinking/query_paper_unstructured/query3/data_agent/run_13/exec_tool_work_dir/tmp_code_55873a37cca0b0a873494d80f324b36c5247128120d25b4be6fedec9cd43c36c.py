code = """import json
import pandas as pd
import re
import os

# Load paper data from MongoDB query
paper_data_file = locals()['var_functions.query_db:8']

with open(paper_data_file, 'r') as f:
    papers = json.load(f)

print(f"Total papers loaded: {len(papers)}")

# Extract metadata from each paper
paper_metadata = []
for paper in papers:
    title = paper['filename'].replace('.txt', '')
    text = paper['text']
    
    # Extract year - look for conference years and publication years
    year = None
    # Patterns to match: '15, 2015, 2020, etc.
    year_patterns = re.findall(r"(?:'|\b)(\d{2})\b|(?:\b)(201\d|202\d)\b", text)
    years_found = []
    
    for pattern in year_patterns:
        if pattern[0]:  # '15 format
            year_num = int('20' + pattern[0])
            if 2010 <= year_num <= 2030:
                years_found.append(year_num)
        elif pattern[1]:  # 2015 or 2020 format
            year_num = int(pattern[1])
            if 2010 <= year_num <= 2030:
                years_found.append(year_num)
    
    if years_found:
        year = max(years_found)  # Most recent year is likely publication year
    
    # Check if paper has empirical contribution
    has_empirical = 'empirical' in text.lower()
    
    paper_metadata.append({
        'title': title,
        'year': year,
        'has_empirical': has_empirical
    })

# Create DataFrame
df_papers = pd.DataFrame(paper_metadata)
print(f"Papers by year: {df_papers['year'].value_counts().sort_index().to_dict()}")
print(f"Papers with 'empirical': {df_papers['has_empirical'].sum()}")

# Filter for empirical papers published after 2016
empirical_papers_after_2016 = df_papers[
    (df_papers['has_empirical'] == True) & 
    (df_papers['year'] > 2016)
]

print(f"\nEmpirical papers after 2016: {len(empirical_papers_after_2016)}")
if len(empirical_papers_after_2016) > 0:
    print("Titles:")
    for title in empirical_papers_after_2016['title'].tolist():
        print(f"  - {title}")

# Prepare result for next step
result = empirical_papers_after_2016[['title', 'year']].to_dict('records')
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:6': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:16': [{'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': 2018}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': 2019}]}

exec(code, env_args)
