code = """import json

# Access the file path from the variable
file_path = locals()['var_function-call-8881788724553702350']

with open(file_path, 'r') as f:
    articles_metadata = json.load(f)

article_ids = []
id_to_year = {}

for item in articles_metadata:
    try:
        aid = int(item['article_id'])
        article_ids.append(aid)
        id_to_year[aid] = int(item['publication_date'][:4])
    except ValueError:
        pass

print("__RESULT__:")
print(json.dumps({"article_ids": article_ids, "id_to_year": id_to_year}))"""

env_args = {'var_function-call-12051989784931741793': ['authors', 'article_metadata'], 'var_function-call-8881788724553702350': 'file_storage/function-call-8881788724553702350.json'}

exec(code, env_args)
