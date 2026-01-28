code = """import pandas as pd
import json
import re

file_path = locals()['var_function-call-4813969159932217082']

with open(file_path, 'r') as f:
    mongo_docs = json.load(f)

papers_data = []
for doc in mongo_docs:
    filename = doc['filename']
    text = doc['text']

    title = filename.replace('.txt', '')

    year = None
    # Broader search for 4-digit years throughout the text
    year_matches = re.findall(r'\b(19|20)\d{2}\b', text)
    if year_matches:
        # Prioritize years that appear earlier in the text, assuming it's the publication year
        for ym in year_matches:
            potential_year = int(ym)
            # Filter out years that are clearly not publication years (e.g., in citations)
            if 1950 <= potential_year <= 2024: # Assuming papers are not from the future
                year = potential_year
                break

    domain = None
    if 'physical activity' in text.lower():
        domain = 'physical activity'

    if domain == 'physical activity':
        papers_data.append({'title': title, 'year': year, 'domain': domain})

filtered_papers_df = pd.DataFrame(papers_data)
print('__RESULT__:')
print(filtered_papers_df.to_json(orient='records'))"""

env_args = {'var_function-call-3869615726933000262': ['paper_docs'], 'var_function-call-4813969159932217082': 'file_storage/function-call-4813969159932217082.json', 'var_function-call-14316110536064693623': [], 'var_function-call-15112818109314081286': []}

exec(code, env_args)
