code = """import json
# load the query result file path from storage variable
path = var_call_EJDnqfTdPKQTvUTBa42yj7YA
with open(path, 'r') as f:
    data = json.load(f)
# get column names from first record
cols = list(data[0].keys())
print("__RESULT__:")
print(json.dumps(cols))"""

env_args = {'var_call_7VPsp2nmm0BFOeMooG8FVxj7': ['clinical_info'], 'var_call_jwp5Ztyo54VKQSLLNASnS5Mq': ['Mutation_Data', 'RNASeq_Expression'], 'var_call_EJDnqfTdPKQTvUTBa42yj7YA': 'file_storage/call_EJDnqfTdPKQTvUTBa42yj7YA.json'}

exec(code, env_args)
