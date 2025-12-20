code = """import json

# Load the metadata results
with open(locals()['var_function-call-7590950680837321910'], 'r') as f:
    metadata = json.load(f)

# Extract IDs and map to year
article_ids = []
id_to_year = {}

for record in metadata:
    # article_id in preview is string, convert to int
    aid = int(record['article_id'])
    pub_date = record['publication_date']
    year = int(pub_date.split('-')[0])
    
    article_ids.append(aid)
    id_to_year[aid] = year

print(f"Total articles found: {len(article_ids)}")
print("__RESULT__:")
print(json.dumps(article_ids))"""

env_args = {'var_function-call-7590950680837321910': 'file_storage/function-call-7590950680837321910.json'}

exec(code, env_args)
