code = """import json
import re

# Load the papers
with open(locals()['var_function-call-8715248679689147439'], 'r') as f:
    papers = json.load(f)

print("__RESULT__:")
results = []
for p in papers[:10]:
    text = p['text']
    # Find all occurrences of "contribution" (case insensitive) and print surrounding text
    matches = [m.start() for m in re.finditer(r'contribution', text, re.IGNORECASE)]
    context = []
    for m in matches:
        start = max(0, m - 50)
        end = min(len(text), m + 50)
        context.append(text[start:end].replace('\n', ' '))
    results.append({"title": p['filename'], "contexts": context})

print(json.dumps(results))"""

env_args = {'var_function-call-12710699781919047137': 'file_storage/function-call-12710699781919047137.json', 'var_function-call-4291090424664498879': ['paper_docs'], 'var_function-call-15848114717037089156': [{'cid': '0', 'name': 'id', 'type': 'INTEGER', 'notnull': '0', 'dflt_value': 'None', 'pk': '1'}, {'cid': '1', 'name': 'title', 'type': 'TEXT', 'notnull': '1', 'dflt_value': 'None', 'pk': '0'}, {'cid': '2', 'name': 'citation_count', 'type': 'INTEGER', 'notnull': '1', 'dflt_value': 'None', 'pk': '0'}, {'cid': '3', 'name': 'citation_year', 'type': 'INTEGER', 'notnull': '1', 'dflt_value': 'None', 'pk': '0'}], 'var_function-call-6799070853489164674': 'file_storage/function-call-6799070853489164674.json', 'var_function-call-17861381846449372899': [], 'var_function-call-2694959544840446415': 'file_storage/function-call-2694959544840446415.json', 'var_function-call-8715248679689147439': 'file_storage/function-call-8715248679689147439.json'}

exec(code, env_args)
