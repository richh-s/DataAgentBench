code = """from datetime import datetime, timedelta
import json

today = datetime(2023, 4, 10)
four_quarters_ago = today - timedelta(days=4 * 91) # Approximating a quarter as 91 days
result = {"date": four_quarters_ago.strftime("%Y-%m-%d")}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {}

exec(code, env_args)
