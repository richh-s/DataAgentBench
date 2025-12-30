code = """import json

with open(locals()['var_function-call-7332118063498685844'], 'r') as f:
    papers_data = json.load(f)

food_related_paper_titles = []
for paper in papers_data:
    text = paper['text'].lower()
    filename = paper['filename']
    title = filename.replace('.txt', '')
    
    if 'food' in text:
        food_related_paper_titles.append(title)
            
print('__RESULT__:')
print(json.dumps(food_related_paper_titles))"""

env_args = {'var_function-call-9698453009794764230': ['paper_docs'], 'var_function-call-11805892907595172719': [], 'var_function-call-7332118063498685844': 'file_storage/function-call-7332118063498685844.json', 'var_function-call-16620644718995955947': []}

exec(code, env_args)
