code = """import json

with open(locals()['var_function-call-1126646822741950899'], 'r') as f:
    citations_2020 = json.load(f)

# Get all titles
all_titles = [c['title'] for c in citations_2020]
# Batch 1: 0-50
batch_titles = all_titles[0:50]
batch_filenames = [t + ".txt" for t in batch_titles]

query = {
    "collection": "paper_docs",
    "filter": {"filename": {"$in": batch_filenames}},
    "projection": {"filename": 1, "text": 1}
}
print("__RESULT__:")
print(json.dumps(query))"""

env_args = {'var_function-call-12477106934681982051': ['Citations', 'sqlite_sequence'], 'var_function-call-12477106934681984716': ['paper_docs'], 'var_function-call-1126646822741950899': 'file_storage/function-call-1126646822741950899.json', 'var_function-call-16301554484232596395': 'file_storage/function-call-16301554484232596395.json', 'var_function-call-5968573917343467552': 'file_storage/function-call-5968573917343467552.json', 'var_function-call-16677263415172437177': 'file_storage/function-call-16677263415172437177.json', 'var_function-call-6526871705431083238': 188}

exec(code, env_args)
