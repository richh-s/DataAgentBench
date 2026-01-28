code = """import pandas as pd, json, re

def parse_date(s):
    if s is None:
        return pd.NaT
    s = str(s)
    # remove trailing time text like ' at 12:00 AM'
    s = re.sub(r"\s+at\s+\d{1,2}:\d{2}\s+[AP]M$", "", s)
    s = re.sub(r",\s*\d{2}:\d{2}$", "", s)
    # try multiple formats
    for fmt in ["%d %b %Y", "%B %d, %Y", "%b %d, %Y", "%d %B %Y", "%Y-%m-%d"]:
        try:
            return pd.to_datetime(s, format=fmt)
        except Exception:
            pass
    return pd.to_datetime(s, errors='coerce')

# test the sample pulled
rows = var_call_konmcszwMtTDjMZs1aWQrecK
out = []
for r in rows:
    out.append({"raw": r['Date'], "parsed": None if pd.isna(parse_date(r['Date'])) else parse_date(r['Date']).strftime('%Y-%m-%d')})

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_IPrUJXbJ0Rv3sNMRI7W96rYp': ['index_trade'], 'var_call_XGJ2iM3oMOFoXJyGBSDD4Ikq': ['index_info'], 'var_call_SQYvS4Wf4oX4BIq1xVszh5EC': [{'min_date': '01 Apr 1969, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM', 'n_rows': '104224', 'n_indices': '13'}], 'var_call_U9UQ8PN66xH14CfnOSMKpLtY': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_call_konmcszwMtTDjMZs1aWQrecK': [{'Index': 'HSI', 'Date': '31 Dec 1986, 00:00', 'CloseUSD': '333.87900637'}, {'Index': 'HSI', 'Date': 'January 02, 1987 at 12:00 AM', 'CloseUSD': '330.21301274'}, {'Index': 'HSI', 'Date': 'January 15, 1987 at 12:00 AM', 'CloseUSD': '332.68301274'}, {'Index': 'HSI', 'Date': 'January 16, 1987 at 12:00 AM', 'CloseUSD': '330.53801274'}, {'Index': 'HSI', 'Date': 'January 19, 1987 at 12:00 AM', 'CloseUSD': '319.865'}]}

exec(code, env_args)
