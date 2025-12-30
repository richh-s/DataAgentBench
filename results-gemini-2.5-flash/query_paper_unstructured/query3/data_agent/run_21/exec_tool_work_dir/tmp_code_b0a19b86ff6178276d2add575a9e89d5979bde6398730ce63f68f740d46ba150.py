code = """import pandas as pd
import json
import re

# Load the full result from the JSON file
with open(locals()['var_function-call-12322513092794815217'], 'r') as f:
    paper_docs = json.load(f)

papers_data = []
for doc in paper_docs:
    filename = doc['filename']
    title = filename.replace('.txt', '')
    text = doc['text']

    year_match = re.search(r'(?:19|20)\d{2}', text)
    year = int(year_match.group(0)) if year_match else None

    contribution_match = re.search(r'Contribution(?:s)?:(.*)', text, re.IGNORECASE)
    contribution = contribution_match.group(1).strip() if contribution_match else None

    # Check for 'empirical' in contribution, case-insensitive
    is_empirical = 'empirical' in (contribution.lower() if contribution else '') if contribution else False

    papers_data.append({
        'title': title,
        'year': year,
        'contribution': contribution,
        'is_empirical': is_empirical
    })

df_papers = pd.DataFrame(papers_data)

# Filter for 'empirical' contribution and year > 2016
filtered_papers = df_papers[(df_papers['is_empirical'] == True) & (df_papers['year'] > 2016)]

# Select relevant columns and convert to JSON
result = filtered_papers[['title', 'year', 'contribution']].to_json(orient='records')

print('__RESULT__:')
print(result)"""

env_args = {'var_function-call-18399910345816842253': ['paper_docs'], 'var_function-call-12322513092794815217': 'file_storage/function-call-12322513092794815217.json'}

exec(code, env_args)
