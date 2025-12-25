code = """import json, pandas as pd
from pathlib import Path

# load a small sample to inspect columns
sample_path = var_call_NMtaYkzBIBTgNG3fZcQwBF79
with open(sample_path, 'r') as f:
    sample = json.load(f)
cols = list(sample[0].keys())

result = json.dumps(cols)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_31NRFTVHQIJgwNh3wn83HFPo': 'file_storage/call_31NRFTVHQIJgwNh3wn83HFPo.json', 'var_call_h7eF5NKZGPqQQAEwKLuCMfVF': ['clinical_info'], 'var_call_NMtaYkzBIBTgNG3fZcQwBF79': 'file_storage/call_NMtaYkzBIBTgNG3fZcQwBF79.json'}

exec(code, env_args)
