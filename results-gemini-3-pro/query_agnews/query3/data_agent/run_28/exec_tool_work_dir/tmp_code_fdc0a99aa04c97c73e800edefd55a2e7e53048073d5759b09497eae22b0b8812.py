code = """import json

file_path = locals()['var_function-call-3293774840587708961']
with open(file_path, 'r') as f:
    metadata = json.load(f)

ids = [r['article_id'] for r in metadata]
# article_id in metadata seems to be string in the preview? 
# "article_id": "3"
# Let's verify type and get min/max.
# The database description says article_id is int. The preview shows strings. 
# It might be that the SQL driver returned them as strings or the preview formatting did.
# I will convert to int to be safe.

ids_int = [int(x) for x in ids]
print("__RESULT__:")
print(json.dumps({"min": min(ids_int), "max": max(ids_int), "count": len(ids_int)}))"""

env_args = {'var_function-call-3293774840587708961': 'file_storage/function-call-3293774840587708961.json', 'var_function-call-16961470035374201743': 14860}

exec(code, env_args)
