code = """import json
import re

with open(locals()['var_function-call-9673377435246489263'], 'r') as f:
    papers_data = json.load(f)

titles = [p['filename'] for p in papers_data]
print("Titles sample:", titles[:5])

keywords_debug = []
for p in papers_data[:10]:
    text = p['text']
    match = re.search(r'Author Keywords(.*?)(?:ACM Classification Keywords|INTRODUCTION|General Terms|$)', text, re.DOTALL | re.IGNORECASE)
    kw = match.group(1).strip() if match else "None"
    keywords_debug.append({"file": p['filename'], "kw": kw})

print("Keywords sample:", keywords_debug)

food_in_text = 0
food_titles = []
for p in papers_data:
    if 'food' in p['text'].lower():
        food_in_text += 1
    if 'food' in p['filename'].lower():
        food_titles.append(p['filename'])

print("Papers with 'food' in text:", food_in_text)
print("Papers with 'food' in title:", food_titles)

print("__RESULT__:")
print(json.dumps("done"))"""

env_args = {'var_function-call-16442091982687073941': 'file_storage/function-call-16442091982687073941.json', 'var_function-call-8772526442893089747': 'file_storage/function-call-8772526442893089747.json', 'var_function-call-9673377435246489263': 'file_storage/function-call-9673377435246489263.json', 'var_function-call-17486704262329443494': 'file_storage/function-call-17486704262329443494.json', 'var_function-call-1266494665686074399': 0}

exec(code, env_args)
