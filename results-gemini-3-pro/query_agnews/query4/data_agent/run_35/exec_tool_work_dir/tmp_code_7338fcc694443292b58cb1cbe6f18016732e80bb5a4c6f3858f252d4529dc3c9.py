code = """import json

# Read the result from the previous step
with open('var_function-call-17404740365086201769', 'r') as f:
    metadata_records = json.load(f)

# Extract article_ids (ensure they are integers as per DB description, but the preview shows strings "13", "18". 
# The description says article_id is int. MongoDB usually stores what you put in. 
# SQL result seems to return them as strings or maybe the preview formatter did that. 
# I will convert them to integers for the MongoDB query just in case, or keep both if unsure.
# Let's check the type of the first one.
article_ids = [int(r['article_id']) for r in metadata_records]

print("__RESULT__:")
print(json.dumps({"count": len(article_ids), "sample_ids": article_ids[:10]}))"""

env_args = {'var_function-call-17404740365086201769': 'file_storage/function-call-17404740365086201769.json'}

exec(code, env_args)
