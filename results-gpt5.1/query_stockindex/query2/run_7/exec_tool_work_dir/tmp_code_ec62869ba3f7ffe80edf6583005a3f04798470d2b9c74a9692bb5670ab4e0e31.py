code = """import json
indices = [
    {"Index": "J203.JO", "Region": "Africa"},
    {"Index": "N225", "Region": "Asia"},
    {"Index": "GSPTSE", "Region": "North America"},
    {"Index": "NSEI", "Region": "Asia"},
    {"Index": "GDAXI", "Region": "Europe"},
    {"Index": "IXIC", "Region": "North America"},
    {"Index": "HSI", "Region": "Asia"},
    {"Index": "NYA", "Region": "North America"},
    {"Index": "000001.SS", "Region": "Asia"},
    {"Index": "SSMI", "Region": "Europe"},
    {"Index": "TWII", "Region": "Asia"},
    {"Index": "N100", "Region": "Europe"},
    {"Index": "399001.SZ", "Region": "Asia"}
]

trade_data = var_call_IbNV01x9DGyzWUCqqtCW4C1N

region_map = {item["Index"]: item["Region"] for item in indices}

north_america_results = []
for row in trade_data:
    idx = row["Index"]
    region = region_map.get(idx)
    if region == "North America":
        up_days = float(row["up_days"])
        down_days = float(row["down_days"])
        if up_days > down_days:
            north_america_results.append({"Index": idx, "up_days": up_days, "down_days": down_days})

result = json.dumps(north_america_results)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_DnHlpn0zeP9mMOSRA7g1Inf5': ['index_info'], 'var_call_dp0vGYVVwJsCLxMXC3XiNbow': ['index_trade'], 'var_call_pEHyKqOq711La1pXN851AC7W': [{'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'J203.JO'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_call_EjiOw9usycv6xsbhwRDsKoqE': [{'min_date': '01 Apr 1969, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM'}], 'var_call_IbNV01x9DGyzWUCqqtCW4C1N': [{'Index': 'J203.JO', 'up_days': '125.0', 'down_days': '124.0'}, {'Index': 'N225', 'up_days': '118.0', 'down_days': '128.0'}, {'Index': 'GSPTSE', 'up_days': '115.0', 'down_days': '135.0'}, {'Index': 'NSEI', 'up_days': '115.0', 'down_days': '130.0'}, {'Index': 'GDAXI', 'up_days': '116.0', 'down_days': '135.0'}, {'Index': 'IXIC', 'up_days': '131.0', 'down_days': '120.0'}, {'Index': 'NYA', 'up_days': '125.0', 'down_days': '126.0'}, {'Index': '000001.SS', 'up_days': '125.0', 'down_days': '118.0'}, {'Index': 'SSMI', 'up_days': '127.0', 'down_days': '122.0'}, {'Index': 'TWII', 'up_days': '129.0', 'down_days': '116.0'}, {'Index': 'N100', 'up_days': '127.0', 'down_days': '128.0'}, {'Index': '399001.SZ', 'up_days': '115.0', 'down_days': '128.0'}, {'Index': 'HSI', 'up_days': '120.0', 'down_days': '126.0'}]}

exec(code, env_args)
