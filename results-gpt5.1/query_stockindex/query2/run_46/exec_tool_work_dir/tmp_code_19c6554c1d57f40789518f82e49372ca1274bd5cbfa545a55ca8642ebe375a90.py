code = """import json

rows = var_call_iqbuz2XaYZWwdAeFDdBPwriQ
na_indices = {"GSPTSE", "IXIC", "NYA"}
res = []
for r in rows:
    idx = r["Index"]
    if idx in na_indices and float(r["up_days"]) > float(r["down_days"]):
        res.append({"Index": idx, "up_days": int(float(r["up_days"])), "down_days": int(float(r["down_days"]))})

result = json.dumps(res)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_M4xStYs1d384fW26G17D5kfB': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}, {'Index': 'NYA'}], 'var_call_iqbuz2XaYZWwdAeFDdBPwriQ': [{'Index': 'N225', 'up_days': '32.0', 'down_days': '42.0'}, {'Index': 'GSPTSE', 'up_days': '44.0', 'down_days': '41.0'}, {'Index': 'NSEI', 'up_days': '40.0', 'down_days': '38.0'}, {'Index': 'GDAXI', 'up_days': '50.0', 'down_days': '48.0'}, {'Index': 'IXIC', 'up_days': '44.0', 'down_days': '31.0'}, {'Index': 'J203.JO', 'up_days': '37.0', 'down_days': '44.0'}, {'Index': 'NYA', 'up_days': '36.0', 'down_days': '42.0'}, {'Index': '000001.SS', 'up_days': '47.0', 'down_days': '37.0'}, {'Index': 'SSMI', 'up_days': '54.0', 'down_days': '39.0'}, {'Index': 'TWII', 'up_days': '39.0', 'down_days': '39.0'}, {'Index': 'HSI', 'up_days': '43.0', 'down_days': '42.0'}, {'Index': 'N100', 'up_days': '31.0', 'down_days': '36.0'}, {'Index': '399001.SZ', 'up_days': '33.0', 'down_days': '43.0'}]}

exec(code, env_args)
