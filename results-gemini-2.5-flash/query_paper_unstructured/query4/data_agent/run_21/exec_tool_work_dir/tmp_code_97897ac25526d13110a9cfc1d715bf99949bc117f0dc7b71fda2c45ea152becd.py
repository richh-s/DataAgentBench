code = """import json
import re

def extract_paper_info(text_content, filename):
    title = filename.replace('.txt', '')

    year_match = re.search(r'\b(19|20)\d{2}\b', text_content)
    year = int(year_match.group(0)) if year_match else None

    is_physical_activity_domain = 'physical activity' in text_content.lower()

    return {'title': title, 'year': year, 'is_physical_activity': is_physical_activity_domain}

file_path = locals()['var_function-call-12002591806772645320']
with open(file_path, 'r') as f:
    papers_data = json.load(f)

filtered_papers = []
for paper in papers_data:
    paper_info = extract_paper_info(paper['text'], paper['filename'])
    if paper_info['year'] == 2016 and paper_info['is_physical_activity']:
        filtered_papers.append({'title': paper_info['title'], 'year': paper_info['year']})

print('__RESULT__:')
print(json.dumps(filtered_papers))"""

env_args = {'var_function-call-17798319154585505742': ['paper_docs'], 'var_function-call-12002591806772645320': 'file_storage/function-call-12002591806772645320.json'}

exec(code, env_args)
