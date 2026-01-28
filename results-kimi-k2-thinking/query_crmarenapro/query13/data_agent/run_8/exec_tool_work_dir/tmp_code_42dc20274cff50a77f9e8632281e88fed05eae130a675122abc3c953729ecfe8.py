code = """import json
import pandas as pd

# Convert the user results to DataFrame for analysis
users_df = pd.DataFrame(var_list_db_1)
print('__RESULT__:')
print(json.dumps({
    "columns": users_df.columns.tolist(),
    "count": len(users_df),
    "data": users_df.head().to_dict('records')
}))"""

env_args = {}

exec(code, env_args)
