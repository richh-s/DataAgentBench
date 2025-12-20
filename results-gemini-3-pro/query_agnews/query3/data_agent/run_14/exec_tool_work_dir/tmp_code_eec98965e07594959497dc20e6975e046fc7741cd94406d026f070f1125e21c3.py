code = """import json

# Load the result from the previous step
with open('var_function-call-12987280970809318212', 'r') as f:
    metadata_list = json.load(f)

# Extract article_ids
# Convert to integer if necessary, but the preview shows them as strings "3". 
# The schema says article_id is int. The SQLite result seems to have given them as strings or maybe the preview formatter did.
# Let's check the type or just handle both. 
# Usually, SQLite returns integers for int columns. The JSON preview might be misleading or they are stored as strings.
# However, the MongoDB schema says article_id is int. So I should convert to int for the Mongo query.
article_ids = [int(item['article_id']) for item in metadata_list]

print("__RESULT__:")
print(json.dumps(article_ids))"""

env_args = {'var_function-call-12987280970809318212': 'file_storage/function-call-12987280970809318212.json'}

exec(code, env_args)
