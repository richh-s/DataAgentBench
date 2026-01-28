code = """import json
rows = var_call_b8vKrCgowNYKllIK4FQJQTO5
# convert counts to ints
out=[]
for r in rows:
    up=int(float(r['up_days']))
    down=int(float(r['down_days']))
    if up>down:
        out.append({'Index': r['Index'], 'up_days': up, 'down_days': down})
answer = out
print('__RESULT__:')
print(json.dumps(answer))"""

env_args = {'var_call_TWPuQCsqGIHlASFrvfHHrBJt': ['index_info'], 'var_call_XIUkw7pNdKtON9MPntbtUhZZ': ['index_trade'], 'var_call_0gPCoRJuYhLgUUeLDBf7GHWI': [{'Exchange': 'New York Stock Exchange'}, {'Exchange': 'NASDAQ'}, {'Exchange': 'Hong Kong Stock Exchange'}, {'Exchange': 'Shanghai Stock Exchange'}, {'Exchange': 'Tokyo Stock Exchange'}, {'Exchange': 'Euronext'}, {'Exchange': 'Shenzhen Stock Exchange'}, {'Exchange': 'Toronto Stock Exchange'}, {'Exchange': 'National Stock Exchange of India'}, {'Exchange': 'Frankfurt Stock Exchange'}, {'Exchange': 'Korea Exchange'}, {'Exchange': 'SIX Swiss Exchange'}, {'Exchange': 'Taiwan Stock Exchange'}, {'Exchange': 'Johannesburg Stock Exchange'}], 'var_call_jX4kHinst4WtBCfR9qQbwLaO': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_call_XDvPSI2h82M69t4Iq1BE22xC': [{'Date': '31 Dec 1986, 00:00'}, {'Date': 'January 02, 1987 at 12:00 AM'}, {'Date': '1987-01-05 00:00:00'}, {'Date': '06 Jan 1987, 00:00'}, {'Date': '07 Jan 1987, 00:00'}], 'var_call_pl3OuUJ1nNuRKuw81ZG98Lx8': [{'Index': 'NYA', 'Date': '2018-01-09 00:00:00', 'Open': '13123.83008', 'Close': '13120.83984'}, {'Index': 'NYA', 'Date': '2018-01-16 00:00:00', 'Open': '13343.82031', 'Close': '13246.86035'}, {'Index': 'NYA', 'Date': '2018-01-18 00:00:00', 'Open': '13341.75977', 'Close': '13315.91016'}, {'Index': 'NYA', 'Date': '2018-01-22 00:00:00', 'Open': '13388.32031', 'Close': '13470.37012'}, {'Index': 'NYA', 'Date': '2018-01-30 00:00:00', 'Open': '13441.24023', 'Close': '13375.50977'}], 'var_call_b8vKrCgowNYKllIK4FQJQTO5': [{'Index': 'GSPTSE', 'up_days': '44.0', 'down_days': '41.0'}, {'Index': 'NYA', 'up_days': '37.0', 'down_days': '42.0'}, {'Index': 'IXIC', 'up_days': '44.0', 'down_days': '31.0'}]}

exec(code, env_args)
