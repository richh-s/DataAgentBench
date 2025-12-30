code = """import json
import re

with open(locals()['var_function-call-9673377435246489263'], 'r') as f:
    papers_data = json.load(f)

debug_info = {}
debug_info['titles'] = [p['filename'] for p in papers_data]

keywords_list = []
for p in papers_data:
    text = p['text']
    match = re.search(r'Author Keywords(.*?)(?:ACM Classification Keywords|INTRODUCTION|General Terms|$)', text, re.DOTALL | re.IGNORECASE)
    kw = match.group(1).strip() if match else "None"
    keywords_list.append({"file": p['filename'], "kw": kw})
debug_info['keywords_sample'] = keywords_list

food_titles = [p['filename'] for p in papers_data if 'food' in p['filename'].lower()]
debug_info['food_titles'] = food_titles

print("__RESULT__:")
print(json.dumps(debug_info))"""

env_args = {'var_function-call-16442091982687073941': 'file_storage/function-call-16442091982687073941.json', 'var_function-call-8772526442893089747': 'file_storage/function-call-8772526442893089747.json', 'var_function-call-9673377435246489263': 'file_storage/function-call-9673377435246489263.json', 'var_function-call-17486704262329443494': 'file_storage/function-call-17486704262329443494.json', 'var_function-call-1266494665686074399': 0, 'var_function-call-4508597791168486055': 'done'}

exec(code, env_args)
