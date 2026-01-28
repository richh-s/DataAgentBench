code = """import json
with open(var_call_UpFSKAxq4enQyFMneNysTLNi, 'r') as f:
    nyse = json.load(f)
with open(var_call_kkqKOJniybxDUtWEO6yDgShT, 'r') as f:
    trade = json.load(f)
trade_set = set(trade)
common = [s for s in nyse if s in trade_set]
print("__RESULT__:")
print(json.dumps(common))"""

env_args = {'var_call_tRlSKUeszajxFebpOVmuqsde': ['stockinfo'], 'var_call_DG0vN5pLFilWu9tTK6nlcgSy': 'file_storage/call_DG0vN5pLFilWu9tTK6nlcgSy.json', 'var_call_UpFSKAxq4enQyFMneNysTLNi': 'file_storage/call_UpFSKAxq4enQyFMneNysTLNi.json', 'var_call_kkqKOJniybxDUtWEO6yDgShT': 'file_storage/call_kkqKOJniybxDUtWEO6yDgShT.json'}

exec(code, env_args)
