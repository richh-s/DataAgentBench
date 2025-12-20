code = """import json

# Read the previous result
with open(locals()['var_function-call-10971295442504843932'], 'r') as f:
    metadata_list = json.load(f)

# Extract article_ids (ensure they are integers as per MongoDB schema)
# Note: In the preview they looked like strings, but schema says int. 
# MongoDB might match ints even if we pass ints, but let's check one.
# The schema says article_id (int). The SQL result might have returned them as strings or the JSON dump did.
# I'll convert them to int.
article_ids = [int(item['article_id']) for item in metadata_list]

print("__RESULT__:")
print(json.dumps(article_ids))"""

env_args = {'var_function-call-10971295442504843932': 'file_storage/function-call-10971295442504843932.json'}

exec(code, env_args)
