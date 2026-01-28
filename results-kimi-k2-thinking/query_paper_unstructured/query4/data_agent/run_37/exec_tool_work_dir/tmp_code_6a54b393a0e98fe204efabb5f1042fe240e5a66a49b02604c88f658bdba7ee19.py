code = """import json
import re

result_file = var_functions.query_db:0
with open(result_file, 'r') as f:
    papers = json.load(f)

def extract_year(text):
    if '2016' in text:
        year_matches = re.findall(r'\b2016\b', text)
        if year_matches:
            return 2016
    return None

def is_physical_activity_domain(text):
    text_lower = text.lower()
    indicators = ['physical activity', 'activity tracker', 'fitness tracker', 'exercise', 'steps per day', 'step count', 'sedentary behavior']
    for indicator in indicators:
        if indicator in text_lower:
            return True
    return False

papers_list = []
for paper in papers:
    text = paper.get('text', '')
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '')
    year = extract_year(text)
    is_pa = is_physical_activity_domain(text)
    if year == 2016 and is_pa:
        papers_list.append({'title': title})

print('__RESULT__:')
print(json.dumps({'papers': papers_list, 'count': len(papers_list)}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['paper_docs']}

exec(code, env_args)
