code = """import pandas as pd
import json
import re

file_path = locals()['var_function-call-16910803448492452394']

with open(file_path, 'r') as f:
    papers_data = json.load(f)

extracted_papers = []

for paper in papers_data:
    text = paper['text']
    filename = paper['filename']
    title = filename.replace('.txt', '')

    year = None
    year_match = re.search(r'(?:19|20)\\d{2}', text[:500])
    if year_match:
        year = int(year_match.group(0))
    
    contribution = None
    contribution_match = re.search(r'contribution: (.*?)(?:\\n|\\.|,)', text, re.IGNORECASE)
    if contribution_match:
        contribution = contribution_match.group(1).strip()
    
    is_empirical = False
    if contribution and 'empirical' in contribution.lower():
        is_empirical = True
    elif not contribution:
        # Try to infer empirical if contribution is not explicitly mentioned
        empirical_keywords = ['study', 'experiment', 'participants', 'data collection', 'survey', 'interview']
        if any(keyword in text.lower() for keyword in empirical_keywords):
            is_empirical = True

    if year and year > 2016 and is_empirical:
        extracted_papers.append({
            'title': title,
            'year': year,
            'contribution': 'empirical' # We only care if it's empirical for this query
        })

df_papers = pd.DataFrame(extracted_papers)

print('__RESULT__:')
print(df_papers.to_json(orient='records'))"""

env_args = {'var_function-call-2783535409203713964': ['paper_docs'], 'var_function-call-11985281394751560404': 'file_storage/function-call-11985281394751560404.json', 'var_function-call-1858781425464915204': [], 'var_function-call-16910803448492452394': 'file_storage/function-call-16910803448492452394.json'}

exec(code, env_args)
