code = """import json
na = {'IXIC':'United States (NASDAQ Composite)','NYA':'United States (NYSE Composite)','GSPTSE':'Canada (S&P/TSX Composite)'}
rows = var_call_6E2MmPJQbRLZNws9gRMDAAFd
out = []
for r in rows:
    up = float(r['up_days'])
    down = float(r['down_days'])
    if up > down:
        out.append({'Index': r['idx'], 'Name/Region': na.get(r['idx'], None), 'Up days (2018)': int(up), 'Down days (2018)': int(down)})
answer = out
print('__RESULT__:')
print(json.dumps(answer))"""

env_args = {'var_call_XCwq9yciX09NINW9ow0Ibvhp': [], 'var_call_gf490JNuvCkQjTMXJST2R62I': [{'idx': '000001.SS'}, {'idx': '399001.SZ'}, {'idx': 'GDAXI'}, {'idx': 'GSPTSE'}, {'idx': 'HSI'}, {'idx': 'IXIC'}, {'idx': 'J203.JO'}, {'idx': 'N100'}, {'idx': 'N225'}, {'idx': 'NSEI'}, {'idx': 'NYA'}, {'idx': 'SSMI'}, {'idx': 'TWII'}], 'var_call_6E2MmPJQbRLZNws9gRMDAAFd': [{'idx': 'GSPTSE', 'up_days': '44.0', 'down_days': '41.0'}, {'idx': 'IXIC', 'up_days': '44.0', 'down_days': '31.0'}, {'idx': 'NYA', 'up_days': '37.0', 'down_days': '42.0'}]}

exec(code, env_args)
