code = """import json
import re

with open(locals()['var_function-call-14289855941331527050'], 'r') as f:
    papers_data = json.load(f)

extracted_papers = []
for paper in papers_data:
    text = paper['text']
    filename = paper['filename']

    title_match = re.search(r'\n\n([A-Za-z0-9 ,'\-_:]+)\n\n', text)
    title = title_match.group(1).strip() if title_match else filename.replace('.txt', '')

    year_match = re.search(r'year: (\d{4})', text, re.IGNORECASE)
    year = int(year_match.group(1)) if year_match else None

    domain_match = re.search(r'domain: ([A-Za-z0-9 ,\-_]+)', text, re.IGNORECASE)
    domain = domain_match.group(1).strip() if domain_match else None

    if year == 2016 and domain and 'physical activity' in domain.lower():
        extracted_papers.append({'title': title, 'year': year, 'domain': domain})

print('__RESULT__:')
print(json.dumps(extracted_papers))"""

env_args = {'var_function-call-2464579052909698935': [], 'var_function-call-8810550685737390910': [], 'var_function-call-14289855941331527050': 'file_storage/function-call-14289855941331527050.json'}

exec(code, env_args)
