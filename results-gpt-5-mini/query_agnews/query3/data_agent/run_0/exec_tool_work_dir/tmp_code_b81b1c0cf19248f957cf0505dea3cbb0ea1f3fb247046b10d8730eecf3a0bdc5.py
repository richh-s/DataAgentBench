code = """import json
# Read the metadata query result from the stored JSON file path variable
path = var_call_3X1uWWrdhN43YDBssiV1HmmL
with open(path, 'r') as f:
    records = json.load(f)
# Build list of article_ids and mapping to publication year
article_ids = []
id_year = {}
for r in records:
    aid = int(r['article_id'])
    pub = r.get('publication_date')
    year = None
    if pub and len(pub) >= 4:
        year = int(pub[:4])
    article_ids.append(aid)
    id_year[str(aid)] = year
# Prepare output
out = {"article_ids": article_ids, "id_year": id_year}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_3X1uWWrdhN43YDBssiV1HmmL': 'file_storage/call_3X1uWWrdhN43YDBssiV1HmmL.json'}

exec(code, env_args)
