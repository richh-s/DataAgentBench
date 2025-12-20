code = """import json
import pandas as pd

# Load data
file_path = var_call_rWa77RE4k4zOSbSK5RWdV8sd
with open(file_path, 'r') as f:
    data = json.load(f)

# Create DataFrame
df = pd.DataFrame(data)

# Compute length of descriptions and find max
df['desc_len'] = df['description'].astype(str).str.len()
max_row = df.loc[df['desc_len'].idxmax()]

result = json.dumps({"title": max_row['title']})

print("__RESULT__:")
print(result)"""

env_args = {'var_call_rWa77RE4k4zOSbSK5RWdV8sd': 'file_storage/call_rWa77RE4k4zOSbSK5RWdV8sd.json'}

exec(code, env_args)
