code = """import json
import re

paper_docs_data = json.load(open(locals()['var_function-call-558217748425387803'], 'r'))

extracted_info = []

for doc in paper_docs_data:
    filename = doc['filename']
    title = filename.replace('.txt', '')
    text = doc['text']

    year_match = re.search('\b(19|20)\d{2}\b', text)
    year = int(year_match.group(0)) if year_match else None

    contribution_match = re.search('contribution(?:s)?:\\s*(.*?)(?:\\n|\\.|;)', text, re.IGNORECASE)
    contribution = contribution_match.group(1).strip() if contribution_match else ''

    extracted_info.append({
        'title': title,
        'year': year,
        'contribution': contribution
    })

print('__RESULT__:')
print(json.dumps(extracted_info))"""

env_args = {'var_function-call-11120416126101380269': ['paper_docs'], 'var_function-call-558217748425387803': 'file_storage/function-call-558217748425387803.json', 'var_function-call-18112218132182732411': []}

exec(code, env_args)
