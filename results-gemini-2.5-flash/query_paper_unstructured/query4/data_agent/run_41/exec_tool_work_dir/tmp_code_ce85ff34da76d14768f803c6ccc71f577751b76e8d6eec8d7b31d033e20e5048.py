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
    # Attempt to find '2016' explicitly, possibly with preceding text indicating a publication year
    # Common patterns: ConferenceName '16, 2016, Copyright 2016
    if re.search(r'(CHI|UbiComp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH)?\s*(?:\'16|2016)|Copyright 2016', text, re.IGNORECASE):
        year = 2016

    domain = None
    if 'physical activity' in text.lower():
        domain = 'physical activity'

    if year == 2016 and domain == 'physical activity':
        papers_data.append({'title': title, 'year': year, 'domain': domain})

filtered_papers_df = pd.DataFrame(papers_data)

print('__RESULT__:')
print(filtered_papers_df.to_json(orient='records'))"""

env_args = {'var_function-call-3869615726933000262': ['paper_docs'], 'var_function-call-4813969159932217082': 'file_storage/function-call-4813969159932217082.json', 'var_function-call-14316110536064693623': [], 'var_function-call-15112818109314081286': [], 'var_function-call-15130475667034523207': [{'title': 'A Lived Informatics Model of Personal Informatics', 'year': None, 'domain': 'physical activity'}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'year': None, 'domain': 'physical activity'}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': None, 'domain': 'physical activity'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': None, 'domain': 'physical activity'}], 'var_function-call-8875254147032335027': [], 'var_function-call-650437496942161048': [], 'var_function-call-15118086362885599179': [], 'var_function-call-13175390580521902847': []}

exec(code, env_args)
