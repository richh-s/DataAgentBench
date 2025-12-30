code = """import json, pandas as pd
from pathlib import Path

# Load Funding table
path_funding = Path(var_call_Hrb72gHg47T3uGlOv7WnIRKg)
with open(path_funding, 'r') as f:
    funding = json.load(f)

# Filter to projects with 'Park' in the name
park_funding = [row for row in funding if 'park' in row['Project_Name'].lower()]

# We don't have explicit completion years here; approximate that all park projects with names suggesting completed items are candidates.
# Since the question is specifically about projects completed in 2022 and we lack dates, we cannot reliably filter by completion year.

result = json.dumps({"total_park_funding_all_years": sum(int(r['Amount']) for r in park_funding)})
print("__RESULT__:")
print(result)"""

env_args = {'var_call_0vENx1jeQZqtLRDGLGARccl0': 'file_storage/call_0vENx1jeQZqtLRDGLGARccl0.json', 'var_call_Hrb72gHg47T3uGlOv7WnIRKg': 'file_storage/call_Hrb72gHg47T3uGlOv7WnIRKg.json'}

exec(code, env_args)
