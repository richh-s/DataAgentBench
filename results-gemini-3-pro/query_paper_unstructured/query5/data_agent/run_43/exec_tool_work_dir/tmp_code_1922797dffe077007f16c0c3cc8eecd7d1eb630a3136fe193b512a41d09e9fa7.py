code = """import json
import re

# Load citations
file_path = locals()['var_function-call-15099835547672752747'] # The list of 188 citations
with open(file_path, 'r') as f:
    citations = json.load(f)

# Create map and filename list
title_to_count = {}
filenames = []
for c in citations:
    title = c['title']
    count = c['citation_count']
    title_to_count[title] = count
    filenames.append(title + ".txt")

# We need to query MongoDB. I will print the filenames list to be used in the next query_db call.
# However, passing a large list in query_db string might be messy if I can't variable substitution.
# But query_db takes a string. I can construct the JSON string in Python and print it, 
# then copy-paste it? No, I must assume the system runs the next tool.
# I can't pass variables between tool calls except via the storage.
# query_db requires a "query" string. 
# If the list is long, the query string will be long. 188 * ~50 chars ~ 10KB. That's acceptable.

print("__RESULT__:")
print(json.dumps(filenames))"""

env_args = {'var_function-call-16511466985029168842': 'file_storage/function-call-16511466985029168842.json', 'var_function-call-15099835547672752747': 188, 'var_function-call-5147540656333355159': 'file_storage/function-call-5147540656333355159.json'}

exec(code, env_args)
