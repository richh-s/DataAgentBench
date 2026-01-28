code = """import json
import re

file_path = locals()['var_function-call-12833057213824030696']
with open(file_path, 'r') as f:
    papers_data = json.load(f)

extracted_papers = []
for paper in papers_data:
    filename = paper['filename']
    title = filename.replace('.txt', '')
    text = paper['text']

    year = None
    # Try to find year using a general 4-digit pattern, preferably in the first 500 characters
    year_match = re.search(r'\b(19[8-9]\d|20[0-2]\d)\b', text[:500])
    if year_match:
        year = int(year_match.group(1))
    else:
        # If not found in the first 500 chars, try in the whole text (less precise, but better than nothing)
        year_match_fallback = re.search(r'\b(19[8-9]\d|20[0-2]\d)\b', text)
        if year_match_fallback:
            year = int(year_match_fallback.group(1))

    domain = None
    if re.search(r'physical activity', text, re.IGNORECASE):
        domain = 'physical activity'

    if year == 2016 and domain == 'physical activity':
        extracted_papers.append({'title': title, 'year': year, 'domain': domain})

print('__RESULT__:')
print(json.dumps(extracted_papers))"""

env_args = {'var_function-call-13855130215716654146': ['paper_docs'], 'var_function-call-12833057213824030696': 'file_storage/function-call-12833057213824030696.json'}

exec(code, env_args)
