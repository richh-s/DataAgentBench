code = """import json

file_path = locals()['var_function-call-4917074217222485168']
with open(file_path, 'r') as f:
    citations = json.load(f)

# Batch 1: 0-50
batch = citations[0:50]
filenames = [c['title'] + ".txt" for c in batch]
query = {
    "collection": "paper_docs",
    "filter": {"filename": {"$in": filenames}},
    "projection": {"filename": 1, "text": 1}
}

print("__RESULT__:")
print(json.dumps(query))"""

env_args = {'var_function-call-3341314182081163111': ['Citations', 'sqlite_sequence'], 'var_function-call-3341314182081161134': ['paper_docs'], 'var_function-call-4917074217222485168': 'file_storage/function-call-4917074217222485168.json', 'var_function-call-4917074217222486491': 'file_storage/function-call-4917074217222486491.json', 'var_function-call-6807615227403179817': 188, 'var_function-call-10601754551730080791': 'file_storage/function-call-10601754551730080791.json', 'var_function-call-6544344674714623327': 'file_storage/function-call-6544344674714623327.json', 'var_function-call-15063728012922695990': 5}

exec(code, env_args)
