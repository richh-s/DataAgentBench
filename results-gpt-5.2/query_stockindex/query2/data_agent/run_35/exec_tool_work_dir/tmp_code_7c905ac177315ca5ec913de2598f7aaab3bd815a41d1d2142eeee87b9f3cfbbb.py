code = """import json
na = {'NYA':'New York Stock Exchange (NYSE Composite)','IXIC':'NASDAQ Composite','GSPTSE':'Toronto Stock Exchange (S&P/TSX Composite)'}
rows = var_call_GmGnRIvtPVM02DIxZIwI30W3
out=[]
for r in rows:
    idx=r['Index']
    up=float(r['up_days']); down=float(r['down_days'])
    if up>down:
        out.append({'Index': idx, 'Name': na.get(idx,''), 'UpDays': int(up), 'DownDays': int(down)})
out_sorted=sorted(out, key=lambda x: x['Index'])
print('__RESULT__:')
print(json.dumps(out_sorted))"""

env_args = {'var_call_h6hEex7VH3qYluAIrfdH2HLh': [{'Exchange': 'New York Stock Exchange'}, {'Exchange': 'NASDAQ'}, {'Exchange': 'Hong Kong Stock Exchange'}, {'Exchange': 'Shanghai Stock Exchange'}, {'Exchange': 'Tokyo Stock Exchange'}, {'Exchange': 'Euronext'}, {'Exchange': 'Shenzhen Stock Exchange'}, {'Exchange': 'Toronto Stock Exchange'}, {'Exchange': 'National Stock Exchange of India'}, {'Exchange': 'Frankfurt Stock Exchange'}, {'Exchange': 'Korea Exchange'}, {'Exchange': 'SIX Swiss Exchange'}, {'Exchange': 'Taiwan Stock Exchange'}, {'Exchange': 'Johannesburg Stock Exchange'}], 'var_call_1sSK06G3mcNuVljYlOXo4kH7': [{'Index': 'J203.JO'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_call_b6DHsU9qErec2GxqlrnfiwAl': [{'Index': 'GDAXI', 'n': '98'}, {'Index': 'SSMI', 'n': '93'}, {'Index': 'GSPTSE', 'n': '86'}, {'Index': 'HSI', 'n': '86'}, {'Index': '000001.SS', 'n': '84'}, {'Index': 'J203.JO', 'n': '81'}, {'Index': 'NYA', 'n': '79'}, {'Index': 'NSEI', 'n': '79'}, {'Index': 'TWII', 'n': '78'}, {'Index': '399001.SZ', 'n': '76'}, {'Index': 'IXIC', 'n': '75'}, {'Index': 'N225', 'n': '74'}, {'Index': 'N100', 'n': '68'}], 'var_call_GmGnRIvtPVM02DIxZIwI30W3': [{'Index': 'GSPTSE', 'up_days': '44.0', 'down_days': '41.0', 'flat_days': '1.0', 'total_days': '86'}, {'Index': 'IXIC', 'up_days': '44.0', 'down_days': '31.0', 'flat_days': '0.0', 'total_days': '75'}, {'Index': 'NYA', 'up_days': '37.0', 'down_days': '42.0', 'flat_days': '0.0', 'total_days': '79'}]}

exec(code, env_args)
