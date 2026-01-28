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
    # Attempt to find year within the first 1000 characters of the document
    search_area = text[:1000]

    # Try to find '2016' specifically first, as it's the target year.
    if re.search(r'\b2016\b', search_area):
        year = 2016
    else:
        # Fallback to general 4-digit year extraction
        four_digit_years = re.findall(r'\b(19\d{2}|20\d{2})\b', search_area)
        if four_digit_years:
            # Take the first plausible year found, assume it's the publication year
            for potential_year_str in four_digit_years:
                potential_year = int(potential_year_str)
                if 1950 <= potential_year <= 2024: # Reasonable range for publication years
                    year = potential_year
                    break

    domain = None
    if 'physical activity' in text.lower():
        domain = 'physical activity'

    if domain == 'physical activity':
        papers_data.append({'title': title, 'year': year, 'domain': domain})

filtered_papers_df = pd.DataFrame(papers_data)

# Filter for 2016 papers from the extracted data
papers_2016_physical_activity_df = filtered_papers_df[filtered_papers_df['year'] == 2016]

print('__RESULT__:')
print(papers_2016_physical_activity_df.to_json(orient='records'))"""

env_args = {'var_function-call-3869615726933000262': ['paper_docs'], 'var_function-call-4813969159932217082': 'file_storage/function-call-4813969159932217082.json', 'var_function-call-14316110536064693623': [], 'var_function-call-15112818109314081286': [], 'var_function-call-15130475667034523207': [{'title': 'A Lived Informatics Model of Personal Informatics', 'year': None, 'domain': 'physical activity'}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'year': None, 'domain': 'physical activity'}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': None, 'domain': 'physical activity'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': None, 'domain': 'physical activity'}], 'var_function-call-8875254147032335027': [], 'var_function-call-650437496942161048': [], 'var_function-call-15118086362885599179': [], 'var_function-call-13175390580521902847': [], 'var_function-call-15773914921340073216': [], 'var_function-call-709345038532913717': [], 'var_function-call-43256416273635476': []}

exec(code, env_args)
