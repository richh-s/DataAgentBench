code = """import json
p = var_call_zvKqKs2UuoKuM7MS6uPMuq33
with open(p, 'r') as f:
    data = json.load(f)
ids = []
for rec in data:
    if rec.get('author_name') == 'Amy Jones':
        try:
            ids.append(int(rec.get('article_id')))
        except:
            pass
# produce JSON string
result = json.dumps(ids)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_tXahDRctxmEOP97nShef4R9k': ['authors', 'article_metadata'], 'var_call_zvKqKs2UuoKuM7MS6uPMuq33': 'file_storage/call_zvKqKs2UuoKuM7MS6uPMuq33.json'}

exec(code, env_args)
