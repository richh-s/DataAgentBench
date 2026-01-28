code = """import json
import pandas as pd
# Load the query result stored in var_call_jTt2PrRqpVudAVnIrj5x1a3X
df = pd.DataFrame(var_call_jTt2PrRqpVudAVnIrj5x1a3X)
# Ensure types
if 'avg_days' in df.columns:
    df['avg_days'] = pd.to_numeric(df['avg_days'], errors='coerce')
# Prepare final output: just the Id string
agent_id = None
if not df.empty:
    agent_id = df.iloc[0]['AgentId']
# Print in required format
print("__RESULT__:")
print(json.dumps(agent_id))"""

env_args = {'var_call_jTt2PrRqpVudAVnIrj5x1a3X': [{'AgentId': '005Wt000003NJgAIAW', 'avg_days': '49.0'}]}

exec(code, env_args)
