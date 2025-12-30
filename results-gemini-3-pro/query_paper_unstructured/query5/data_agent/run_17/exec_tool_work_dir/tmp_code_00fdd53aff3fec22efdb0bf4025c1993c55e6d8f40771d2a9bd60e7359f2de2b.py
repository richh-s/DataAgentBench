code = """import json
import re

p_citations = locals()['var_function-call-1858146419099260835']
with open(p_citations, 'r') as f:
    c_data = json.load(f)

c_map = {}
for i in c_data:
    try:
        val = int(i['citation_count'])
    except:
        val = 0
    c_map[i['title'] + ".txt"] = val

p_docs = locals()['var_function-call-9448533248759791427']
with open(p_docs, 'r') as f:
    docs = json.load(f)

total = 0
found_count = 0

for d in docs:
    fname = d.get('filename')
    if fname in c_map:
        txt = d.get('text', '')
        # Check first 1000 chars
        head = txt[:1000]
        # Regex for CHI year or CHI 'year
        # We match CHI followed by space/quote and 2-4 digits
        if re.search(r"CHI[\s']+\d{2}", head) or "Conference on Human Factors in Computing Systems" in head:
            total += c_map[fname]
            found_count += 1

print(f"Found {found_count} papers.")
print(f"Total citations: {total}")

print("__RESULT__:")
print(json.dumps(total))"""

env_args = {'var_function-call-1858146419099260835': 'file_storage/function-call-1858146419099260835.json', 'var_function-call-15380122331926952136': 'file_storage/function-call-15380122331926952136.json', 'var_function-call-9448533248759791427': 'file_storage/function-call-9448533248759791427.json', 'var_function-call-4705747550331622406': 16}

exec(code, env_args)
