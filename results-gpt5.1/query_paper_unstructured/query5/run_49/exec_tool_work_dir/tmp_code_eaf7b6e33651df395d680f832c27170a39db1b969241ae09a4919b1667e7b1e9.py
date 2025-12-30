code = """import json
import re

# Load full mongo result
path = var_call_B6sRMW3GXb9A9FrKMPqus3OU
with open(path, 'r') as f:
    mongo_records = json.load(f)

# Extract unique paper titles from filenames (remove .txt)
titles = sorted({rec['filename'].rsplit('.txt', 1)[0] for rec in mongo_records if 'filename' in rec})

# Prepare a small subset string for SQL IN clause; we'll query all via join pattern, not IN list, so just output titles
result = json.dumps(titles)

print("__RESULT__:")
print(result)"""

env_args = {'var_call_B6sRMW3GXb9A9FrKMPqus3OU': 'file_storage/call_B6sRMW3GXb9A9FrKMPqus3OU.json'}

exec(code, env_args)
