code = """import json
import os

# Load the result from the SQL query
file_path = locals()['var_function-call-1413150651152435569']
with open(file_path, 'r') as f:
    citations = json.load(f)

# Extract titles
titles = [c['title'] for c in citations]
print(f"Total citations in 2018: {len(titles)}")

# We need to query MongoDB for these titles.
# The filename is title + ".txt"
filenames = [t + ".txt" for t in titles]

# I will create a query to fetch the text for these filenames.
# Limit to a reasonable number to avoid huge query if too many. 
# If there are many, I might need to do it in batches or just fetch all and filter in Python if the DB is small.
# But I don't know the DB size.
# Let's print the first few filenames to verify.
print(f"First 5 filenames: {filenames[:5]}")

print("__RESULT__:")
print(json.dumps(filenames))"""

env_args = {'var_function-call-1413150651152435569': 'file_storage/function-call-1413150651152435569.json'}

exec(code, env_args)
