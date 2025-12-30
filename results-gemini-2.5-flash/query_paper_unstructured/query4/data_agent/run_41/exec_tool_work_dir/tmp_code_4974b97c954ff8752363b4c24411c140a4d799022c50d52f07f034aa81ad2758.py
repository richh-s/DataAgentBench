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
    # Try to extract a 4-digit year that appears in the first ~1000 characters of the document.
    # This is a common place for publication years (e.g., in headers, copyright, or intro).
    year_search_area = text[:1000]
    # Look for patterns like "YYYY" or "'YY" after a common conference name or "Copyright"
    year_match = re.search(r'(?:CHI|UbiComp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH)?\s*(?:(?:19|20)\d{2}|\'\d{2})|Copyright\s+(?:19|20)\d{2}', year_search_area, re.IGNORECASE)
    if year_match:
        matched_string = year_match.group(0)
        four_digit_year = re.search(r'(19|20)\d{2}', matched_string)
        if four_digit_year:
            year = int(four_digit_year.group(0))
        else:
            short_year_match = re.search(r"\'(\d{2})", matched_string)
            if short_year_match:
                short_year = int(short_year_match.group(1))
                if short_year > 50: # Assume 19xx for >50
                    year = 1900 + short_year
                else: # Assume 20xx for <=50
                    year = 2000 + short_year


    domain = 'physical activity' if 'physical activity' in text.lower() else None

    if year == 2016 and domain == 'physical activity':
        papers_data.append({'title': title})

filtered_papers_df = pd.DataFrame(papers_data)

print('__RESULT__:')
print(filtered_papers_df.to_json(orient='records'))"""

env_args = {'var_function-call-3869615726933000262': ['paper_docs'], 'var_function-call-4813969159932217082': 'file_storage/function-call-4813969159932217082.json', 'var_function-call-14316110536064693623': [], 'var_function-call-15112818109314081286': [], 'var_function-call-15130475667034523207': [{'title': 'A Lived Informatics Model of Personal Informatics', 'year': None, 'domain': 'physical activity'}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'year': None, 'domain': 'physical activity'}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': None, 'domain': 'physical activity'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': None, 'domain': 'physical activity'}], 'var_function-call-8875254147032335027': [], 'var_function-call-650437496942161048': [], 'var_function-call-15118086362885599179': [], 'var_function-call-13175390580521902847': [], 'var_function-call-15773914921340073216': [], 'var_function-call-709345038532913717': []}

exec(code, env_args)
