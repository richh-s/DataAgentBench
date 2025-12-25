code = """import json

# Read the file containing the metadata results
with open('var_function-call-5438198083873646081.json', 'r') as f:
    metadata_list = json.load(f)

# Extract article_ids
article_ids = [int(item['article_id']) for item in metadata_list]
print(f"Total articles in 2015: {len(article_ids)}")

# Prepare the result for the next step (just printing the list size and maybe the first few to verify)
print("__RESULT__:")
print(json.dumps(article_ids))"""

env_args = {'var_function-call-5438198083873646081': 'file_storage/function-call-5438198083873646081.json'}

exec(code, env_args)
