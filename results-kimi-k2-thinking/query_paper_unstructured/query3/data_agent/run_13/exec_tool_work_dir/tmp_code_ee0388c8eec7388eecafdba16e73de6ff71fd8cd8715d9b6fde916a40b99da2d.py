code = """import json
import pandas as pd
import re
import os

# Load all paper documents from the stored file
papers_file = var_functions.query_db:8
papers = json.load(open(papers_file))

paper_list = []
for paper in papers:
    title = paper['filename'].replace('.txt', '')
    text = paper['text'].lower()
    
    # Extract year - look for various patterns
    year = None
    # Pattern 1: "'15" format with conference names
    pattern1 = re.findall(r"(?:ubicomp|chi|cscw|dis|tei|iui|www|hci| pervasivehealth|ozchi|ah|ieee|acm)\s*'?(\d{2})[\s,]", text, re.IGNORECASE)
    if pattern1:
        years = [int('20' + y) for y in pattern1 if int(y) < 30]  # 2000s
        if years:
            year = max(years)
    
    # Pattern 2: Full year like 2015, 2016, etc.
    if not year:
        pattern2 = re.findall(r"\b(201[5-9]|202[0-9])\b", text)
        if pattern2:
            year = max([int(y) for y in pattern2])
    
    # Check for empirical contribution
    is_empirical = 'empirical' in text
    
    paper_list.append({
        'title': title,
        'year': year,
        'is_empirical': is_empirical,
        'text_len': len(text)
    })

df = pd.DataFrame(paper_list)
print('Total papers:', len(df))
print('Year distribution:', df['year'].value_counts().sort_index().to_dict())
print('Empirical papers:', df['is_empirical'].sum())

# Filter empirical papers after 2016
filtered = df[(df['is_empirical'] == True) & (df['year'] > 2016)]
print('\nEmpirical papers after 2016:', len(filtered))

result = filtered[['title', 'year']].to_dict('records')
print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:6': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:16': [{'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': 2018}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': 2019}], 'var_functions.execute_python:22': []}

exec(code, env_args)
