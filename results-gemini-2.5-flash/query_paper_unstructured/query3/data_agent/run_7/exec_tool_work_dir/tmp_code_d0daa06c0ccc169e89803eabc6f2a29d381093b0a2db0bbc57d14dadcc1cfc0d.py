code = """import json
import re

file_path = locals()['var_function-call-6604890257152561261']

with open(file_path, 'r') as f:
    paper_docs = json.load(f)

extracted_papers = []
for doc in paper_docs:
    title = doc['filename'].replace('.txt', '')
    text = doc['text']
    year = None
    contribution = []

    # Extract year: look for 4-digit years first, then 2-digit years
    # General 4-digit year pattern
    year_match_4digit = re.search(r'\\b(19|20)\\d{2}\\b', text)
    if year_match_4digit:
        year = int(year_match_4digit.group(0))
    else:
        # Pattern for 2-digit years following common conference abbreviations
        year_match_2digit = re.search(r'(?:CHI|UbiComp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH)\\s+\'\\d{2}', text, re.IGNORECASE)
        if year_match_2digit:
            # Extract the 2-digit year part
            two_digit_year = re.search(r'\\d{2}', year_match_2digit.group(0)).group(0)
            year = int('20' + two_digit_year) # Assuming '15' means 2015, '18' means 2018 etc.

    # Extract contribution
    if re.search(r'empirical', text, re.IGNORECASE):
        contribution.append('empirical')
    if re.search(r'artifact', text, re.IGNORECASE):
        contribution.append('artifact')
    if re.search(r'theoretical', text, re.IGNORECASE):
        contribution.append('theoretical')
    if re.search(r'survey', text, re.IGNORECASE):
        contribution.append('survey')
    if re.search(r'methodological', text, re.IGNORECASE):
        contribution.append('methodological')

    extracted_papers.append({
        'title': title,
        'year': year,
        'contribution': contribution
    })

# Filter papers published after 2016 with an 'empirical' contribution
filtered_papers = [
    p for p in extracted_papers
    if p['year'] is not None and p['year'] > 2016 and 'empirical' in p['contribution']
]

print('__RESULT__:')
print(json.dumps(filtered_papers))"""

env_args = {'var_function-call-14474643791060089691': ['paper_docs'], 'var_function-call-6604890257152561261': 'file_storage/function-call-6604890257152561261.json', 'var_function-call-3273880440063485916': []}

exec(code, env_args)
