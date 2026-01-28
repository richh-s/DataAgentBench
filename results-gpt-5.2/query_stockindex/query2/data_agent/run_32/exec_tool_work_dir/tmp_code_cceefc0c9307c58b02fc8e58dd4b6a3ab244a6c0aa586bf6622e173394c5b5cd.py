code = """import json
recs = var_call_ae2cUnntRbRrW1cQ9WIPwcOr
# cast counts to int
out=[]
for r in recs:
    up=int(float(r['up_days']))
    down=int(float(r['down_days']))
    if up>down:
        out.append({'Index': r['idx'], 'up_days': up, 'down_days': down})
ans = json.dumps(out)
print('__RESULT__:')
print(ans)"""

env_args = {'var_call_yE4MX1xGOQsdpDrw59LPNw83': [], 'var_call_yeNTRiMKsyTGepqfBoZJ62IH': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_call_ae2cUnntRbRrW1cQ9WIPwcOr': [{'idx': 'GSPTSE', 'up_days': '44.0', 'down_days': '41.0'}, {'idx': 'IXIC', 'up_days': '44.0', 'down_days': '31.0'}, {'idx': 'NYA', 'up_days': '37.0', 'down_days': '42.0'}]}

exec(code, env_args)
