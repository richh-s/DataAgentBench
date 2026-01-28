code = """import json
import re

with open(locals()['var_function-call-7332118063498685844'], 'r') as f:
    papers_data = json.load(f)

food_domain_papers = []
for paper in papers_data:
    text = paper['text'].lower()
    filename = paper['filename']
    title = filename.replace('.txt', '')
    
    # Regex to find 'domain: ' followed by potential domains.
    # The hint says "domain: Research domain/topic (e.g., "food", "physical activity", "sleep", "mental")"
    # So I'm looking for "domain:" and then if "food" is in the text that follows.
    match = re.search(r"domain:([^\n]+)", text)
    if match:
        domains_str = match.group(1).strip()
        if 'food' in domains_str:
            food_domain_papers.append(title)
            
print('__RESULT__:')
print(json.dumps(food_domain_papers))"""

env_args = {'var_function-call-9698453009794764230': ['paper_docs'], 'var_function-call-11805892907595172719': [], 'var_function-call-7332118063498685844': 'file_storage/function-call-7332118063498685844.json'}

exec(code, env_args)
