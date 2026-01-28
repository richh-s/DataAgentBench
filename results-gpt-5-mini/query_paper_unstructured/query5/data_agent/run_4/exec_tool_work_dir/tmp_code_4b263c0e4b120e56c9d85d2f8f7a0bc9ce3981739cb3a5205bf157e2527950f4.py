code = """import json
path = var_call_iflfUGr6Fd9ctqILCoEqURaa
with open(path, 'r', encoding='utf-8') as f:
    chi_docs = json.load(f)
# Extract filenames for CHI papers
chi_filenames = [rec['filename'] for rec in chi_docs]
print("__RESULT__:")
print(json.dumps(chi_filenames))"""

env_args = {'var_call_DRNGZlVCXMdCfLRYYfFPdEJB': 'file_storage/call_DRNGZlVCXMdCfLRYYfFPdEJB.json', 'var_call_bKXfIw7c04xSKoAxn5RY0FMS': 'file_storage/call_bKXfIw7c04xSKoAxn5RY0FMS.json', 'var_call_iflfUGr6Fd9ctqILCoEqURaa': 'file_storage/call_iflfUGr6Fd9ctqILCoEqURaa.json'}

exec(code, env_args)
