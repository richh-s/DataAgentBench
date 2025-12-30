code = """import json

with open(locals()['var_function-call-13793389442727890881'], 'r') as f:
    titles_2018 = json.load(f)

filenames_2018 = [title + ".txt" for title in titles_2018]

# Construct the MongoDB query as a Python dictionary
mongo_query_dict = {
    "collection": "paper_docs",
    "filter": {"filename": {"$in": filenames_2018}},
    "projection": {"filename": 1, "text": 1}
}

# Convert the dictionary to a JSON string
query_string = json.dumps(mongo_query_dict)

print('__RESULT__:')
print(json.dumps(query_string))"""

env_args = {'var_function-call-2303352090281735151': 'file_storage/function-call-2303352090281735151.json', 'var_function-call-13793389442727890881': 'file_storage/function-call-13793389442727890881.json'}

exec(code, env_args)
