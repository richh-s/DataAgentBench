code = """import json
import re

def extract_paper_info(text_content, filename):
    title = filename.replace('.txt', '')

    year_match = re.search(r'\b(19|20)\d{2}\b', text_content)
    year = int(year_match.group(0)) if year_match else None

    domain = None
    # Try to find domain explicitly mentioned
    domain_match = re.search(r'Domain[s]?:\s*(.*?)\n', text_content, re.IGNORECASE)
    if domain_match:
        domain = domain_match.group(1).strip()
    else:
        # Try to find domain in the abstract/keywords if not found explicitly
        abstract_keywords_match = re.search(r'(?:abstract|keywords):.*?((?:physical activity|food|sleep|mental|finances|productivity|screen time|social interactions|location|chronic|diabetes|health_behavior)(?:, | and )?)+', text_content, re.IGNORECASE | re.DOTALL)
        if abstract_keywords_match:
            domain = abstract_keywords_match.group(0)

    return {'title': title, 'year': year, 'domain': domain}

file_path = locals()['var_function-call-12002591806772645320']
with open(file_path, 'r') as f:
    papers_data = json.load(f)

filtered_papers = []
for paper in papers_data:
    paper_info = extract_paper_info(paper['text'], paper['filename'])
    if paper_info['year'] == 2016 and paper_info['domain'] and 'physical activity' in paper_info['domain'].lower():
        filtered_papers.append({'title': paper_info['title'], 'year': paper_info['year'], 'domain': paper_info['domain']})

print('__RESULT__:')
print(json.dumps(filtered_papers))"""

env_args = {'var_function-call-17798319154585505742': ['paper_docs'], 'var_function-call-12002591806772645320': 'file_storage/function-call-12002591806772645320.json'}

exec(code, env_args)
