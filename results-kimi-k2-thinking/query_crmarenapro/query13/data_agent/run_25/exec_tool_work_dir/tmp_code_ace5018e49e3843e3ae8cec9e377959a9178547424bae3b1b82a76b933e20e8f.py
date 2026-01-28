code = """# Calculate date range for past 5 months
from datetime import datetime, timedelta

# Today's date: 2022-11-25
today = datetime(2022, 11, 25)
# 5 months ago: 2022-06-25
five_months_ago = datetime(2022, 6, 25)

print('__RESULT__:')
print(f"Date range: {five_months_ago.strftime('%Y-%m-%d')} to {today.strftime('%Y-%m-%d')}")"""

env_args = {}

exec(code, env_args)
