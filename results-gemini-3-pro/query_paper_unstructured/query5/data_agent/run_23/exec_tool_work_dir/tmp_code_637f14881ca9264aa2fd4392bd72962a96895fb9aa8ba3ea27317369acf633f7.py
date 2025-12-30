code = """import json

# Load the result from the previous tool call
with open(locals()['var_function-call-4239113770536719479'], 'r') as f:
    citations = json.load(f)

# Extract titles and convert to filenames
# Also keep a map of title -> citation_count for later use
title_citation_map = {item['title']: item['citation_count'] for item in citations}
filenames = [title + ".txt" for title in title_citation_map.keys()]

print("__RESULT__:")
print(json.dumps({"filenames": filenames, "title_citation_map": title_citation_map}))"""

env_args = {'var_function-call-4239113770536719479': 'file_storage/function-call-4239113770536719479.json'}

exec(code, env_args)
