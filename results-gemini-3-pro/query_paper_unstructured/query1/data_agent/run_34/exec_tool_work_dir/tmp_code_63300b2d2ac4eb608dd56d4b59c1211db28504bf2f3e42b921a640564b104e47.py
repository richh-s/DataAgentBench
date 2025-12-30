code = """import json

file_path = locals()['var_function-call-1041647607165487633']

with open(file_path, 'r') as f:
    papers = json.load(f)

results = []
for paper in papers[:10]:
    title = paper['filename']
    text = paper['text'].lower()
    has_food = 'food' in text
    
    context = ""
    if has_food:
        idx = text.find('food')
        # simple slice
        start = max(0, idx-50)
        end = min(len(text), idx+50)
        context = text[start:end]
        # remove newlines
        context = context.replace(chr(10), ' ')
        
    results.append({
        "title": title,
        "has_food": has_food,
        "context": context
    })

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-17948406739355176464': 'file_storage/function-call-17948406739355176464.json', 'var_function-call-1041647607165485382': ['Citations', 'sqlite_sequence'], 'var_function-call-1041647607165487633': 'file_storage/function-call-1041647607165487633.json', 'var_function-call-17075501722390720700': []}

exec(code, env_args)
