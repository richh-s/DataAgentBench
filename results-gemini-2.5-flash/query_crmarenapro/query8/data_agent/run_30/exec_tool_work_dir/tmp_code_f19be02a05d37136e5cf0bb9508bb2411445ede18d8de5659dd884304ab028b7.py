code = """from datetime import datetime, timedelta

today = datetime(2023, 4, 10)
four_quarters_ago = today - timedelta(days=4 * 91) # Approximating a quarter as 91 days
print('__RESULT__:')
print(f'\"date\": \"{four_quarters_ago.strftime("%Y-%m-%d")}\"'))"""

env_args = {}

exec(code, env_args)
