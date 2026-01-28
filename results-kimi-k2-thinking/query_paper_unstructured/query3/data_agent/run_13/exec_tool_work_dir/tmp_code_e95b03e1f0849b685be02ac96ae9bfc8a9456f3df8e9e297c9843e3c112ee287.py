code = """import json
import pandas as pd
import re

# Load paper data
papers_file = var_functions.query_db:8
papers = json.load(open(papers_file))

# Extract metadata
papers_data = []
for p in papers:
    title = p['filename'].replace('.txt', '')
    text = p['text']
    
    # Find year patterns
    year = None
    patterns = re.findall(r"(?:'|\b)(\d{2})\b|(\b201\d|\b202\d)\b", text)
    years = []
    for pat in patterns:
        if pat[0]:
            y = int('20' + pat[0])
            if 2010 <= y <= 2030: years.append(y)
        if pat[1]:
            y = int(pat[1])
            if 2010 <= y <= 2030: years.append(y)
    if years: year = max(years)
    
    # Check empirical
    has_empirical = 'empirical' in text.lower()
    
    papers_data.append({'title': title, 'year': year, 'empirical': has_empirical})

df = pd.DataFrame(papers_data)
print('Total:', len(df))
print('By year:', df['year'].value_counts().sort_index().head().to_dict())
print('Empirical count:', df['empirical'].sum())

empirical_2017plus = df[(df['empirical'] == True) & (df['year'] > 2016)]
print('\nEmpirical after 2016:', len(empirical_2017plus))

result = empirical_2017plus[['title', 'year']].to_dict('records')
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:6': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:16': [{'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': 2018}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': 2019}], 'var_functions.execute_python:22': []}

exec(code, env_args)
