code = """import json

with open(locals()['var_function-call-1669477486731597534'], 'r') as f:
    paper_docs = json.load(f)

debug_info = []
count = 0
for doc in paper_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    has_pa = 'physical activity' in text.lower()
    has_2016_top = '2016' in text[:2000]
    has_2016_any = '2016' in text
    
    if count < 10:
        debug_info.append({
            "title": filename,
            "has_pa": has_pa,
            "has_2016_top": has_2016_top,
            "has_2016_any": has_2016_any,
            "snippet": text[:100]
        })
        count += 1

print("__RESULT__:")
print(json.dumps(debug_info))"""

env_args = {'var_function-call-15838279633175563818': 'file_storage/function-call-15838279633175563818.json', 'var_function-call-1669477486731597489': 'file_storage/function-call-1669477486731597489.json', 'var_function-call-1669477486731597534': 'file_storage/function-call-1669477486731597534.json', 'var_function-call-2579067088761269272': [], 'var_function-call-13126364427078448234': 'Debug Complete'}

exec(code, env_args)
