code = """import json
import re

def extract_paper_info(paper_text, filename):
    title = filename.replace(".txt", "")
    year = None
    contribution = None

    # Extract year
    year_match = re.search(r'\b(19|20)\d{2}\b', paper_text)
    if year_match: 
        year = int(year_match.group(0))
    
    # Extract contribution (looking for "contribution: [type]" or "contributions: [type]")
    contribution_match = re.search(r'contribution[s]?:\s*([a-zA-Z, ]+)', paper_text, re.IGNORECASE)
    if contribution_match:
        contribution = contribution_match.group(1).lower()

    return {'title': title, 'year': year, 'contribution': contribution}


file_path = locals()['var_function-call-17384357217489800854']
with open(file_path, 'r') as f:
    paper_docs = json.load(f)

papers_info = []
for doc in paper_docs:
    info = extract_paper_info(doc['text'], doc['filename'])
    papers_info.append(info)

filtered_papers = []
for paper in papers_info:
    if paper['year'] is not None and paper['year'] > 2016 and \
       paper['contribution'] is not None and 'empirical' in paper['contribution']:
        filtered_papers.append(paper)

print("__RESULT__:")
print(json.dumps(filtered_papers))"""

env_args = {'var_function-call-8876707072609632946': ['Citations', 'sqlite_sequence'], 'var_function-call-9424252978014940020': ['paper_docs'], 'var_function-call-17384357217489800854': 'file_storage/function-call-17384357217489800854.json'}

exec(code, env_args)
