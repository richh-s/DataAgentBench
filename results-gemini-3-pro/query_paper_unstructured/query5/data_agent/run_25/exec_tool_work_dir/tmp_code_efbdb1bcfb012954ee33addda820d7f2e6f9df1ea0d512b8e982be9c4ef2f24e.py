code = """import json

# Get the file path from the variable
file_path = locals()['var_function-call-3704779829923578766']

# Load citations
with open(file_path, 'r') as f:
    citations = json.load(f)

# Extract titles and map title to citation count
title_to_citations = {}
for c in citations:
    title = c['title']
    try:
        count = int(c['citation_count'])
    except:
        count = 0
    title_to_citations[title] = count

titles = list(title_to_citations.keys())
filenames = [t + ".txt" for t in titles]

print(f"Total papers cited in 2020: {len(titles)}")

# I will return the filenames list to use in the next step (MongoDB query)
# But since the list might be large, I might need to batch the query or rely on storage.
# For now, let's just print the count and maybe split the work if needed.
# But `query_db` can take large queries? 
# If the list is huge, I might exceed query length limits.
# Let's check the length.

print("__RESULT__:")
print(json.dumps(filenames))"""

env_args = {'var_function-call-3704779829923578766': 'file_storage/function-call-3704779829923578766.json', 'var_function-call-4076760790261236942': 'file_storage/function-call-4076760790261236942.json'}

exec(code, env_args)
