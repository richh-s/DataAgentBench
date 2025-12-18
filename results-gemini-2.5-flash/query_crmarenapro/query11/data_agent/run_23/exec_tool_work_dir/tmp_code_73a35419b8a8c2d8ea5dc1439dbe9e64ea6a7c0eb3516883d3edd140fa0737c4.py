code = """import pandas as pd

account_id_data = locals()['var_function-call-8595579920075190144']['query_db_response']['results'][0]['AccountId']
account_id = account_id_data.lstrip('#')

print("__RESULT__:")
print(account_id)"""

env_args = {'var_function-call-8595579920075190144': [{'AccountId': '#001Wt00000PGXrNIAX'}]}

exec(code, env_args)
