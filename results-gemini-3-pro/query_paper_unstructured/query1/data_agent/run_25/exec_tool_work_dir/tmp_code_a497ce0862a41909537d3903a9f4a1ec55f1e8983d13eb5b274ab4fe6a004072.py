code = """import json
import re

with open(locals()['var_function-call-9673377435246489263'], 'r') as f:
    papers_data = json.load(f)

print("Total papers:", len(papers_data))

print("--- Titles ---")
for p in papers_data:
    print(p['filename'])

print("\n--- Keyword Extraction Debug ---")
for p in papers_data[:5]:
    text = p['text']
    match = re.search(r'Author Keywords(.*?)(?:ACM Classification Keywords|INTRODUCTION|General Terms|$)', text, re.DOTALL | re.IGNORECASE)
    if match:
        print(f"File: {p['filename']}")
        print(f"Keywords: {match.group(1).strip()}")
    else:
        print(f"File: {p['filename']} - NO KEYWORDS FOUND")

print("\n--- 'food' check ---")
count_food_in_text = 0
for p in papers_data:
    if 'food' in p['text'].lower():
        count_food_in_text += 1
print(f"Papers with 'food' in text: {count_food_in_text}")
print("__RESULT__:")
print(json.dumps("debug_done"))"""

env_args = {'var_function-call-16442091982687073941': 'file_storage/function-call-16442091982687073941.json', 'var_function-call-8772526442893089747': 'file_storage/function-call-8772526442893089747.json', 'var_function-call-9673377435246489263': 'file_storage/function-call-9673377435246489263.json', 'var_function-call-17486704262329443494': 'file_storage/function-call-17486704262329443494.json', 'var_function-call-1266494665686074399': 0}

exec(code, env_args)
