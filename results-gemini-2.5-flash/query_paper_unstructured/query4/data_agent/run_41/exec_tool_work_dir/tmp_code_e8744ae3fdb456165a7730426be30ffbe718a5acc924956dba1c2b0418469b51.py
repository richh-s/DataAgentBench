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
    # More general year extraction from the first 500 characters
    search_area = text[:500]
    four_digit_years = re.findall(r'\b(19\d{2}|20\d{2})\b', search_area)
    if four_digit_years:
        year = int(four_digit_years[0])
    else:
        # Check for 'YY patterns like '16
        short_year_match = re.search(r"\'(\d{2})", search_area)
        if short_year_match:
            short_year = int(short_year_match.group(1))
            if short_year >= 0 and short_year <= 99: # Valid 2-digit year
                if short_year > 50: # Assume 19xx for >50
                    year = 1900 + short_year
                else: # Assume 20xx for <=50
                    year = 2000 + short_year

    domain = 'physical activity' if 'physical activity' in text.lower() else None

    if domain == 'physical activity': # Filter by domain first to reduce data
        papers_data.append({'title': title, 'year': year, 'domain': domain})

filtered_papers_df = pd.DataFrame(papers_data)

# Filter for 2016 papers from the extracted data
papers_2016_physical_activity_df = filtered_papers_df[filtered_papers_df['year'] == 2016]

print('__RESULT__:')
print(papers_2016_physical_activity_df.to_json(orient='records'))"""

env_args = {'var_function-call-3869615726933000262': ['paper_docs'], 'var_function-call-4813969159932217082': 'file_storage/function-call-4813969159932217082.json', 'var_function-call-14316110536064693623': [], 'var_function-call-15112818109314081286': [], 'var_function-call-15130475667034523207': [{'title': 'A Lived Informatics Model of Personal Informatics', 'year': None, 'domain': 'physical activity'}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'year': None, 'domain': 'physical activity'}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': None, 'domain': 'physical activity'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': None, 'domain': 'physical activity'}], 'var_function-call-8875254147032335027': [], 'var_function-call-650437496942161048': [], 'var_function-call-15118086362885599179': [], 'var_function-call-13175390580521902847': [], 'var_function-call-15773914921340073216': []}

exec(code, env_args)
