code = """import json

with open(locals()['var_function-call-13793389442727890881'], 'r') as f:
    titles_2018 = json.load(f)

filenames_2018 = [title + ".txt" for title in titles_2018]
filenames_json = json.dumps(filenames_2018)

query_string = "{{\"collection\": \"paper_docs\", \"filter\": {{\"filename\": {{\"$in\": {}}}}}, \"projection\": {{\"filename\": 1, \"text\": 1}}}}".format(filenames_json)

print('__RESULT__:')
print(json.dumps(query_string))"""

env_args = {'var_function-call-2303352090281735151': 'file_storage/function-call-2303352090281735151.json', 'var_function-call-13793389442727890881': 'file_storage/function-call-13793389442727890881.json'}

exec(code, env_args)
