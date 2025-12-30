code = """import json, statistics
import pandas as pd

path = var_call_IaBG0B1dNp4Ilzxbp57s8a1J
with open(path, 'r') as f:
    data = json.load(f)

# convert citation_count to int
counts = [int(r['citation_count']) for r in data]
avg = statistics.mean(counts) if counts else None

res = json.dumps(avg)
print("__RESULT__:")
print(res)"""

env_args = {'var_call_IaBG0B1dNp4Ilzxbp57s8a1J': 'file_storage/call_IaBG0B1dNp4Ilzxbp57s8a1J.json'}

exec(code, env_args)
