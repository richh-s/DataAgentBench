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
    # Try to find year using common patterns
    year_match = re.search(r'(?:(?:CHI|Ubicomp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH)\s+\'(\d{2})|(\d{4}))', text)
    if year_match:
        if year_match.group(1): # 'YY pattern
            year = int('20' + year_match.group(1))
        elif year_match.group(2): # YYYY pattern
            year = int(year_match.group(2))
    
    # Fallback: look for 4 digit numbers that could be a year, preferably in the first part of the text
    if not year:
        # Check first 500 characters
        year_match_fallback = re.search(r'\\b(20\\d{2}|19\\d{2})\\b', text[:500])
        if year_match_fallback:
            year = int(year_match_fallback.group(1))

    domain = None
    if re.search(r'physical activity', text, re.IGNORECASE):
        domain = 'physical activity'

    if year and domain == 'physical activity' and year == 2016:
        extracted_papers.append({'title': title, 'year': year, 'domain': domain})

print('__RESULT__:')
print(json.dumps(extracted_papers))"""

env_args = {'var_function-call-13855130215716654146': ['paper_docs'], 'var_function-call-12833057213824030696': 'file_storage/function-call-12833057213824030696.json'}

exec(code, env_args)
