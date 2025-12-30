code = """import json
import re

# Load citations
file_path = locals()['var_function-call-264858034059979045']
with open(file_path, 'r') as f:
    citations = json.load(f)

# Extract titles
titles = [c['title'] for c in citations]
filenames = [t + ".txt" for t in titles]

# Prepare to query MongoDB
# I will output the filenames to be used in the next tool call
print("__RESULT__:")
print(json.dumps(filenames))"""

env_args = {'var_function-call-264858034059979045': 'file_storage/function-call-264858034059979045.json', 'var_function-call-16262197769178367218': {'count': 188, 'sample_title': 'Sundroid: Solar Radiation Awareness with Smartphones'}, 'var_function-call-2494524119581093015': 'file_storage/function-call-2494524119581093015.json'}

exec(code, env_args)
