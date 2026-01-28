code = """import json
# Load the citations result file produced by the previous query
path = var_call_DRNGZlVCXMdCfLRYYfFPdEJB
with open(path, 'r', encoding='utf-8') as f:
    citations = json.load(f)
# Extract titles and produce filenames
filenames = [rec['title'] + '.txt' for rec in citations]
# Print according to required format
print("__RESULT__:")
print(json.dumps(filenames))"""

env_args = {'var_call_DRNGZlVCXMdCfLRYYfFPdEJB': 'file_storage/call_DRNGZlVCXMdCfLRYYfFPdEJB.json'}

exec(code, env_args)
