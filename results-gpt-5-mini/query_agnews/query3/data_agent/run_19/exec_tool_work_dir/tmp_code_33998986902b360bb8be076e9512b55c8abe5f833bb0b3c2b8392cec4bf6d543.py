code = """import json
path = var_call_FptZsboUs5IwWU1JjmsLWqRS
with open(path, 'r') as f:
    data = json.load(f)
ids = [int(item['article_id']) for item in data]
# chunk into size 1000
chunk_size = 1000
chunks = [ids[i:i+chunk_size] for i in range(0, len(ids), chunk_size)]
queries = []
for chunk in chunks:
    q = {"collection":"articles","filter":{"article_id":{"$in":chunk}},"projection":{"article_id":1,"title":1,"description":1},"limit":0}
    queries.append(json.dumps(q))
print('__RESULT__:')
print(json.dumps(queries))"""

env_args = {'var_call_FptZsboUs5IwWU1JjmsLWqRS': 'file_storage/call_FptZsboUs5IwWU1JjmsLWqRS.json', 'var_call_HBBdA6FPdUWa5BCoHOOdtJQd': 'file_storage/call_HBBdA6FPdUWa5BCoHOOdtJQd.json'}

exec(code, env_args)
