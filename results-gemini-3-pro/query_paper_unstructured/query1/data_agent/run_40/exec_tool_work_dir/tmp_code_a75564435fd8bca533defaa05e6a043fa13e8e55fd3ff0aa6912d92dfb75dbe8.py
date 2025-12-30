code = """import json

file_path = locals()['var_function-call-12545833755252698609']
with open(file_path, 'r') as f:
    papers = json.load(f)

titles = [p['filename'].replace('.txt', '') for p in papers]
food_in_text = []
for p in papers:
    if 'food' in p['text'].lower():
        food_in_text.append(p['filename'].replace('.txt', ''))

print("__RESULT__:")
print(json.dumps({"total_papers": len(titles), "titles_preview": titles[:10], "food_in_text_count": len(food_in_text), "food_in_text_titles": food_in_text[:10]}))"""

env_args = {'var_function-call-2991259327904718266': ['paper_docs'], 'var_function-call-2991259327904718481': ['Citations', 'sqlite_sequence'], 'var_function-call-10512507186521432510': 'file_storage/function-call-10512507186521432510.json', 'var_function-call-12545833755252698609': 'file_storage/function-call-12545833755252698609.json', 'var_function-call-10414038178410062022': []}

exec(code, env_args)
