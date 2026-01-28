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
    # Broader search for 4-digit years in the first 500 characters
    first_part_text = text[:500]
    year_matches = re.findall(r'\b(19|20)\d{2}\b', first_part_text)
    if year_matches:
        # Assuming the first valid 4-digit number is the publication year
        for ym in year_matches:
            potential_year = int(ym)
            if 1950 <= potential_year <= 2025: # Reasonable range for publication years
                year = potential_year
                break
    else:
        # Also check for 'YY pattern, e.g., '16 for 2016
        year_match_short = re.search(r"\'(\d{2})", first_part_text)
        if year_match_short:
            short_year = int(year_match_short.group(1))
            if short_year > 50: # Assume 19xx for >50
                year = 1900 + short_year
            else: # Assume 20xx for <=50
                year = 2000 + short_year

    domain = 'physical activity' if 'physical activity' in text.lower() else None

    if year == 2016 and domain == 'physical activity':
        papers_data.append({'title': title, 'year': year, 'domain': domain})

filtered_papers_df = pd.DataFrame(papers_data)
print('__RESULT__:')
print(filtered_papers_df.to_json(orient='records'))"""

env_args = {'var_function-call-3869615726933000262': ['paper_docs'], 'var_function-call-4813969159932217082': 'file_storage/function-call-4813969159932217082.json', 'var_function-call-14316110536064693623': []}

exec(code, env_args)
