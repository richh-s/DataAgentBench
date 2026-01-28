code = """import json
import re

with open(locals()['var_function-call-6893631717039984758'], 'r') as f:
    paper_docs = json.load(f)

food_domain_papers_titles = []
for doc in paper_docs:
    text = doc['text']
    title = doc['filename'].replace('.txt', '')

    found_in_domain_line = False
    for line in text.splitlines():
        domain_match = re.match(r'^\s*domains?:\s*(.*)', line, re.IGNORECASE)
        if domain_match:
            domains_str = domain_match.group(1)
            if 'food' in domains_str.lower():
                food_domain_papers_titles.append(title)
                found_in_domain_line = True
                break

    if not found_in_domain_line:
        if re.search(r'\bfood\b', text, re.IGNORECASE):
            food_domain_papers_titles.append(title)

food_domain_papers_titles = list(set(food_domain_papers_titles))

print("__RESULT__:")
print(json.dumps(food_domain_papers_titles))"""

env_args = {'var_function-call-8792593880583760035': ['paper_docs'], 'var_function-call-9978232910626699419': [], 'var_function-call-6497029258880074568': ['Citations', 'sqlite_sequence'], 'var_function-call-6893631717039984758': 'file_storage/function-call-6893631717039984758.json', 'var_function-call-9273036665786985738': [], 'var_function-call-14011650007027942934': []}

exec(code, env_args)
