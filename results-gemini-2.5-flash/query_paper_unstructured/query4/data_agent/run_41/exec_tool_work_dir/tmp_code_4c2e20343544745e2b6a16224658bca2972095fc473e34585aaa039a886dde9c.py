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
    # More robust year extraction: look for 4-digit numbers that are likely years
    # Prioritize years appearing early in the document or associated with publication keywords
    year_matches = re.findall(r'(?:CHI|UbiComp|CSCW|Copyright)?\s*(\b(19|20)\d{2}\b)', text, re.IGNORECASE)
    if year_matches:
        for match in year_matches:
            potential_year = int(match[0])
            if 1990 <= potential_year <= 2024: # Assuming a reasonable range for publication years
                year = potential_year
                break # Take the first reasonable year found

    domain = None
    if 'physical activity' in text.lower():
        domain = 'physical activity'

    if year == 2016 and domain == 'physical activity':
        papers_data.append({'title': title, 'year': year, 'domain': domain})

filtered_papers_df = pd.DataFrame(papers_data)
print('__RESULT__:')
print(filtered_papers_df.to_json(orient='records'))"""

env_args = {'var_function-call-3869615726933000262': ['paper_docs'], 'var_function-call-4813969159932217082': 'file_storage/function-call-4813969159932217082.json', 'var_function-call-14316110536064693623': [], 'var_function-call-15112818109314081286': [], 'var_function-call-15130475667034523207': [{'title': 'A Lived Informatics Model of Personal Informatics', 'year': None, 'domain': 'physical activity'}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'year': None, 'domain': 'physical activity'}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': None, 'domain': 'physical activity'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': None, 'domain': 'physical activity'}], 'var_function-call-8875254147032335027': []}

exec(code, env_args)
