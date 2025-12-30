code = """import json

file_path = locals()['var_function-call-5679032680150065306']
with open(file_path, 'r') as f:
    filenames = json.load(f)

chunk_size = 100
chunks = [filenames[i:i + chunk_size] for i in range(0, len(filenames), chunk_size)]

queries = []
for chunk in chunks:
    query = {
        "collection": "paper_docs",
        "filter": {"filename": {"$in": chunk}},
        "projection": {"filename": 1, "text": 1}
    }
    queries.append(json.dumps(query))

print("__RESULT__:")
print(json.dumps(queries))"""

env_args = {'var_function-call-5680722423366514432': ['Citations', 'sqlite_sequence'], 'var_function-call-5680722423366516433': 'file_storage/function-call-5680722423366516433.json', 'var_function-call-5680722423366514338': 'file_storage/function-call-5680722423366514338.json', 'var_function-call-1825670630710000632': 'file_storage/function-call-1825670630710000632.json', 'var_function-call-1380767849587936819': 188, 'var_function-call-5679032680150065306': 'file_storage/function-call-5679032680150065306.json'}

exec(code, env_args)
