code = """import json

with open(locals()['var_function-call-9592996467849275882'], 'r') as f:
    citations_data = json.load(f)

filenames = [item['title'] + ".txt" for item in citations_data]

# Chunk size 50
chunks = [filenames[i:i + 50] for i in range(0, len(filenames), 50)]

print("__RESULT__:")
print(json.dumps(chunks))"""

env_args = {'var_function-call-9592996467849275882': 'file_storage/function-call-9592996467849275882.json', 'var_function-call-8827078559982422440': 'file_storage/function-call-8827078559982422440.json', 'var_function-call-2196265177759855413': 188, 'var_function-call-10885420759070414019': 'file_storage/function-call-10885420759070414019.json', 'var_function-call-1623150383067545539': [{'_id': '694f5530284b10b11dc0a869'}, {'_id': '694f5530284b10b11dc0a86a'}, {'_id': '694f5530284b10b11dc0a86b'}, {'_id': '694f5530284b10b11dc0a86c'}, {'_id': '694f5530284b10b11dc0a86d'}], 'var_function-call-5903998820821374632': 'file_storage/function-call-5903998820821374632.json'}

exec(code, env_args)
