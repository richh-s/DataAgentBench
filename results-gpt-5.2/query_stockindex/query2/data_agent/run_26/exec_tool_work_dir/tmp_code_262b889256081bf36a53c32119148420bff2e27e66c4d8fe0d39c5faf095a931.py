code = """import json
rows = var_call_2jQpj8QD0wdqHltwDiZOhQme
north_america = {'IXIC':'NASDAQ Composite (US)','NYA':'NYSE Composite (US)','GSPTSE':'S&P/TSX Composite (Canada)'}
res=[]
for r in rows:
    idx=r['Index']
    if idx in north_america:
        up=float(r['up_days']); down=float(r['down_days'])
        if up>down:
            res.append({'Index': idx, 'Name': north_america[idx], 'up_days': int(up), 'down_days': int(down)})
res_sorted=sorted(res, key=lambda x: x['Index'])
print('__RESULT__:')
print(json.dumps(res_sorted))"""

env_args = {'var_call_UPunNP6zy6pTtI9H8Q4MpXwz': ['index_info'], 'var_call_sFnsOo8AxA6pHj5hdZbRGkpI': ['index_trade'], 'var_call_wiO4dUlX14XGKO5Z19eomMBL': [], 'var_call_ohaLl9OIFllPFCDT8gZGEZyt': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_call_V2G0DgC6f6qz5G3dajMyeV9a': [{'Date': '31 Dec 1986, 00:00'}, {'Date': 'January 02, 1987 at 12:00 AM'}, {'Date': '1987-01-05 00:00:00'}, {'Date': '06 Jan 1987, 00:00'}, {'Date': '07 Jan 1987, 00:00'}], 'var_call_U4VhO3okT4xalOIuhWTbT7V8': [], 'var_call_2jQpj8QD0wdqHltwDiZOhQme': [{'Index': 'J203.JO', 'up_days': '41.0', 'down_days': '43.0'}, {'Index': 'IXIC', 'up_days': '51.0', 'down_days': '40.0'}, {'Index': 'N225', 'up_days': '40.0', 'down_days': '40.0'}, {'Index': 'NSEI', 'up_days': '39.0', 'down_days': '55.0'}, {'Index': 'GDAXI', 'up_days': '43.0', 'down_days': '50.0'}, {'Index': 'GSPTSE', 'up_days': '37.0', 'down_days': '46.0'}, {'Index': 'HSI', 'up_days': '37.0', 'down_days': '38.0'}, {'Index': 'NYA', 'up_days': '49.0', 'down_days': '57.0'}, {'Index': 'N100', 'up_days': '55.0', 'down_days': '47.0'}, {'Index': '399001.SZ', 'up_days': '46.0', 'down_days': '38.0'}, {'Index': '000001.SS', 'up_days': '44.0', 'down_days': '37.0'}, {'Index': 'SSMI', 'up_days': '39.0', 'down_days': '39.0'}, {'Index': 'TWII', 'up_days': '37.0', 'down_days': '46.0'}]}

exec(code, env_args)
