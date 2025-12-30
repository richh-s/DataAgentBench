code = """import json

# Load the previous result
with open('var_function-call-1625930341030172972.json', 'r') as f:
    citations = json.load(f)

print(f"Total citation records: {len(citations)}")
filenames = [c['title'] + ".txt" for c in citations]
# Print first 5 to verify
print(filenames[:5])

# Prepare the query string for MongoDB
mongo_query = {"filename": {"$in": filenames}}
print("__RESULT__:")
print(json.dumps(mongo_query))"""

env_args = {'var_function-call-1625930341030172972': 'file_storage/function-call-1625930341030172972.json'}

exec(code, env_args)
