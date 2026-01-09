code = """import json

data = var_call_xoRtxkFjrgJ0iyAAKsc6dUzh
# define North American index symbols in this dataset
north_america = {'IXIC','NYA','GSPTSE'}
res = []
for r in data:
    idx = r['Index']
    if idx in north_america:
        up = float(r['up_days'])
        down = float(r['down_days'])
        if up > down:
            res.append({'Index': idx, 'up_days': int(up), 'down_days': int(down)})
res_json = json.dumps(res)
print('__RESULT__:')
print(res_json)"""

env_args = {'var_call_d5vgiYt9eIfddxDxUCAihNLH': ['index_info'], 'var_call_9R2qGjgTJEyyT6En2yQJeYhw': [{'Date': '31 Dec 1986, 00:00'}, {'Date': 'January 02, 1987 at 12:00 AM'}, {'Date': '1987-01-05 00:00:00'}, {'Date': '06 Jan 1987, 00:00'}, {'Date': '07 Jan 1987, 00:00'}, {'Date': '1987-01-08 00:00:00'}, {'Date': '1987-01-09 00:00:00'}, {'Date': '1987-01-12 00:00:00'}, {'Date': '1987-01-13 00:00:00'}, {'Date': '1987-01-14 00:00:00'}, {'Date': 'January 15, 1987 at 12:00 AM'}, {'Date': 'January 16, 1987 at 12:00 AM'}, {'Date': 'January 19, 1987 at 12:00 AM'}, {'Date': '20 Jan 1987, 00:00'}, {'Date': 'January 21, 1987 at 12:00 AM'}, {'Date': '22 Jan 1987, 00:00'}, {'Date': 'January 23, 1987 at 12:00 AM'}, {'Date': 'January 26, 1987 at 12:00 AM'}, {'Date': '27 Jan 1987, 00:00'}, {'Date': 'January 28, 1987 at 12:00 AM'}], 'var_call_xoRtxkFjrgJ0iyAAKsc6dUzh': [{'Index': 'J203.JO', 'up_days': '125.0', 'down_days': '124.0'}, {'Index': 'N225', 'up_days': '118.0', 'down_days': '128.0'}, {'Index': 'GSPTSE', 'up_days': '115.0', 'down_days': '135.0'}, {'Index': 'NSEI', 'up_days': '115.0', 'down_days': '130.0'}, {'Index': 'GDAXI', 'up_days': '116.0', 'down_days': '135.0'}, {'Index': 'IXIC', 'up_days': '131.0', 'down_days': '120.0'}, {'Index': 'HSI', 'up_days': '120.0', 'down_days': '126.0'}, {'Index': '000001.SS', 'up_days': '125.0', 'down_days': '118.0'}, {'Index': 'SSMI', 'up_days': '127.0', 'down_days': '122.0'}, {'Index': 'TWII', 'up_days': '129.0', 'down_days': '116.0'}, {'Index': 'N100', 'up_days': '127.0', 'down_days': '128.0'}, {'Index': '399001.SZ', 'up_days': '115.0', 'down_days': '128.0'}, {'Index': 'NYA', 'up_days': '125.0', 'down_days': '126.0'}]}

exec(code, env_args)
