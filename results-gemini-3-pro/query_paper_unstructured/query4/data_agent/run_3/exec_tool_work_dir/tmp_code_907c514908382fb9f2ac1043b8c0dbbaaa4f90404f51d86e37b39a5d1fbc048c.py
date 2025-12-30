code = """import json

with open(locals()['var_function-call-1669477486731597534'], 'r') as f:
    paper_docs = json.load(f)

print("Total docs:", len(paper_docs))

debug_count = 0
for doc in paper_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    is_physical = 'physical activity' in text.lower()
    is_2016 = '2016' in text[:2000]
    
    if is_physical or is_2016:
        print(f"Title: {filename}")
        print(f"  Has 'physical activity': {is_physical}")
        print(f"  Has '2016' in header: {is_2016}")
        # Print snippet where 2016 appears if present
        if is_2016:
            idx = text[:2000].find('2016')
            print(f"  Context 2016: {text[idx-20:idx+20].replace(chr(10), ' ')}")
        debug_count += 1
        if debug_count > 10:
            break

print("__RESULT__:")
print(json.dumps("Debug Complete"))"""

env_args = {'var_function-call-15838279633175563818': 'file_storage/function-call-15838279633175563818.json', 'var_function-call-1669477486731597489': 'file_storage/function-call-1669477486731597489.json', 'var_function-call-1669477486731597534': 'file_storage/function-call-1669477486731597534.json', 'var_function-call-2579067088761269272': []}

exec(code, env_args)
