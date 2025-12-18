code = """import pandas as pd
import json

file_path = locals()['var_function-call-9940923227919821351']
with open(file_path, 'r') as f:
    sales_data = json.load(f) # Read the entire JSON file

df = pd.DataFrame(sales_data)
df['sales_amount'] = pd.to_numeric(df['sales_amount'])

total_sales_by_agent = df.groupby('cleaned_OwnerId')['sales_amount'].sum()
top_agent_id = total_sales_by_agent.idxmax()

print("__RESULT__:")
print(json.dumps(top_agent_id))"""

env_args = {'var_function-call-9940923227919821351': 'file_storage/function-call-9940923227919821351.json'}

exec(code, env_args)
