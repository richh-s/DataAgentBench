code = """import json
pref = json.load(open(var_call_s5csHGp8Zcz3HPrbTQq7V1C9))["union_sql_prefix"]
# complete query: aggregate up/down days and pick top 5 by (up_days - down_days)
query = pref + "SELECT Symbol, SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) AS up_days, SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) AS down_days FROM all_data GROUP BY Symbol HAVING up_days > down_days ORDER BY (up_days - down_days) DESC LIMIT 5;"
print("__RESULT__:")
print(json.dumps({"query": query}))"""

env_args = {'var_call_Q4TUNNhQcj1EUic3uk4c7EwM': 'file_storage/call_Q4TUNNhQcj1EUic3uk4c7EwM.json', 'var_call_Cc3eRRR6J0KHUKBg4fNL3Eu0': 'file_storage/call_Cc3eRRR6J0KHUKBg4fNL3Eu0.json', 'var_call_s5csHGp8Zcz3HPrbTQq7V1C9': 'file_storage/call_s5csHGp8Zcz3HPrbTQq7V1C9.json'}

exec(code, env_args)
