code = """import json
import pandas as pd
import re

# Access the query result correctly
papers_data = locals()['var_functions.query_db:2']

# Check the structure of the data
print('Type of papers_data:', type(papers_data))
if isinstance(papers_data, list) and len(papers_data) > 0:
    print('First item type:', type(papers_data[0]))
    print('First item keys:', papers_data[0].keys() if isinstance(papers_data[0], dict) else 'Not a dict')
    
    # Create DataFrame
df_papers = pd.DataFrame(papers_data)
    
    # Extract title from filename
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
    
    # Filter for papers after 2016 with empirical contribution
    df_filtered = df_papers[
        (df_papers['year'] > 2016) & 
        (df_papers['contribution'].str.contains('empirical', na=False))
    ]
    
    result = df_filtered[['title', 'year', 'contribution']].to_dict('records')
    print('__RESULT__:')
    print(json.dumps(result))
else:
    print('__RESULT__:')
    print(json.dumps([]))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:16': ['var_functions.list_db:0', 'var_functions.query_db:2', '__builtins__', 'json']}

exec(code, env_args)
