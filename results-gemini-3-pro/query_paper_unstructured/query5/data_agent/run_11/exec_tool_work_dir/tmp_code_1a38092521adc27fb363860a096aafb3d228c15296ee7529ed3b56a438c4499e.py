code = """import json

file_path = locals()['var_function-call-9730938913871448610']
with open(file_path, 'r') as f:
    citations_2020 = json.load(f)

titles = [rec['title'] for rec in citations_2020]
filenames = [t + ".txt" for t in titles]

mongo_query = {
    "collection": "paper_docs",
    "filter": {
        "filename": {"$in": filenames}
    },
    "projection": {"filename": 1, "text": 1} # Need text to identify venue
}

print("__RESULT__:")
print(json.dumps(mongo_query))"""

env_args = {'var_function-call-9582957559039433718': ['Citations', 'sqlite_sequence'], 'var_function-call-9582957559039434257': ['paper_docs'], 'var_function-call-9730938913871448610': 'file_storage/function-call-9730938913871448610.json', 'var_function-call-9730938913871447677': 'file_storage/function-call-9730938913871447677.json', 'var_function-call-4287235649051513': {'count': 188}}

exec(code, env_args)
