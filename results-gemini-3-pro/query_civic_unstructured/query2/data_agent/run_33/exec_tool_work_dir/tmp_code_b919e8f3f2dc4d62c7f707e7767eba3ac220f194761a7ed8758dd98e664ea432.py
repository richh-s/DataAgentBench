code = """import json
import re

with open(locals()['var_function-call-3179318639355232823']) as f:
    docs = json.load(f)

target = "Legacy Park"
snippets = []

for doc in docs:
    text = doc['text']
    for m in re.finditer(re.escape(target), text, re.IGNORECASE):
        start = m.start()
        snippets.append(text[start:start+300].replace('\n', ' '))

print("__RESULT__:")
print(json.dumps(snippets))"""

env_args = {'var_function-call-4554034855452536121': ['civic_docs'], 'var_function-call-4554034855452533864': ['Funding'], 'var_function-call-4554034855452535703': 'file_storage/function-call-4554034855452535703.json', 'var_function-call-7560016992368588221': 'file_storage/function-call-7560016992368588221.json', 'var_function-call-3179318639355232823': 'file_storage/function-call-3179318639355232823.json', 'var_function-call-15240581338442732047': 21000, 'var_function-call-15316970010288403584': ['Bluffs Park Shade Structure', 'Broad Beach Road Water Quality Repair', 'Point Dume Walkway Repairs'], 'var_function-call-9561095300841000714': {'Broad Beach Road Water Quality Repair': False, 'Point Dume Walkway Repairs': False}, 'var_function-call-13248264942745016138': [{'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}], 'var_function-call-9911764383178724774': [{'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}]}

exec(code, env_args)
