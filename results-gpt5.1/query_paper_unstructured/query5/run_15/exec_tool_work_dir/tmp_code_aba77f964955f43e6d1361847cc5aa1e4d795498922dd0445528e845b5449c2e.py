code = """import json

citations_path = var_call_lPtT9kTwgt2fVMN54nVuJVkZ
with open(citations_path, 'r') as f:
    citations = json.load(f)

papers_path = var_call_sg6CgWNfa7fX85rzeucpIIB9
with open(papers_path, 'r') as f:
    papers = json.load(f)

chi_titles = set()
for doc in papers:
    filename = doc.get('filename', '') or ''
    text = doc.get('text', '') or ''
    title = filename[:-4] if filename.lower().endswith('.txt') else filename
    text_upper = text.upper()
    if ('CHI ' in text_upper) or ("CHI'" in text_upper) or ('\nCHI\n' in text_upper) or ('CONFERENCE ON HUMAN FACTORS IN COMPUTING SYSTEMS' in text_upper):
        chi_titles.add(title)

total_citations_chi_2020 = 0
for row in citations:
    title = row.get('title', '')
    if title in chi_titles:
        try:
            cnt = int(row.get('total_citations', 0))
        except (TypeError, ValueError):
            cnt = 0
        total_citations_chi_2020 += cnt

import json as json_module
result = json_module.dumps(total_citations_chi_2020)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_lPtT9kTwgt2fVMN54nVuJVkZ': 'file_storage/call_lPtT9kTwgt2fVMN54nVuJVkZ.json', 'var_call_sg6CgWNfa7fX85rzeucpIIB9': 'file_storage/call_sg6CgWNfa7fX85rzeucpIIB9.json'}

exec(code, env_args)
