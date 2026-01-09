code = """import pandas as pd, json, re

def parse_date(s):
    if s is None:
        return pd.NaT
    s=str(s)
    fmts=[
        '%Y-%m-%d %H:%M:%S',
        '%Y-%m-%d',
        '%d %b %Y, %H:%M',
        '%B %d, %Y at %I:%M %p',
        '%b %d, %Y at %I:%M %p',
        '%d %B %Y, %H:%M',
        '%m/%d/%Y',
    ]
    for f in fmts:
        try:
            return pd.to_datetime(s, format=f)
        except Exception:
            pass
    try:
        return pd.to_datetime(s, errors='coerce')
    except Exception:
        return pd.NaT

# fetch all needed rows: Index, Date, CloseUSD
# (query directly here to avoid large tool results?) We'll use duckdb query with minimal cols.
print('__RESULT__:')
print(json.dumps({'note':'ready'}))"""

env_args = {'var_call_Vj1pRZVtgU4aThYZAJEzI9cf': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_call_L0QtvdtnmkRG1Y5tqH9aVKVw': [], 'var_call_kxPk2Hg81KWGTE301029i0DB': [{'sample_date': '31 Dec 1986, 00:00'}, {'sample_date': 'January 02, 1987 at 12:00 AM'}, {'sample_date': '1987-01-05 00:00:00'}, {'sample_date': '06 Jan 1987, 00:00'}, {'sample_date': '07 Jan 1987, 00:00'}, {'sample_date': '1987-01-08 00:00:00'}, {'sample_date': '1987-01-09 00:00:00'}, {'sample_date': '1987-01-12 00:00:00'}, {'sample_date': '1987-01-13 00:00:00'}, {'sample_date': '1987-01-14 00:00:00'}, {'sample_date': 'January 15, 1987 at 12:00 AM'}, {'sample_date': 'January 16, 1987 at 12:00 AM'}, {'sample_date': 'January 19, 1987 at 12:00 AM'}, {'sample_date': '20 Jan 1987, 00:00'}, {'sample_date': 'January 21, 1987 at 12:00 AM'}, {'sample_date': '22 Jan 1987, 00:00'}, {'sample_date': 'January 23, 1987 at 12:00 AM'}, {'sample_date': 'January 26, 1987 at 12:00 AM'}, {'sample_date': '27 Jan 1987, 00:00'}, {'sample_date': 'January 28, 1987 at 12:00 AM'}], 'var_call_2XBKrJPr8vyvXHnuclabti5d': [{'Index': 'HSI', 'Date': '31 Dec 1986, 00:00', 'Open': '2568.300049', 'High': '2568.300049', 'Low': '2568.300049', 'Close': '2568.300049', 'Adj Close': '2568.300049', 'CloseUSD': '333.87900637'}, {'Index': 'HSI', 'Date': 'January 02, 1987 at 12:00 AM', 'Open': '2540.100098', 'High': '2540.100098', 'Low': '2540.100098', 'Close': '2540.100098', 'Adj Close': '2540.100098', 'CloseUSD': '330.21301274'}, {'Index': 'HSI', 'Date': '1987-01-05 00:00:00', 'Open': '2552.399902', 'High': '2552.399902', 'Low': '2552.399902', 'Close': '2552.399902', 'Adj Close': '2552.399902', 'CloseUSD': '331.81198726'}, {'Index': 'HSI', 'Date': '06 Jan 1987, 00:00', 'Open': '2583.899902', 'High': '2583.899902', 'Low': '2583.899902', 'Close': '2583.899902', 'Adj Close': '2583.899902', 'CloseUSD': '335.90698726000005'}, {'Index': 'HSI', 'Date': '07 Jan 1987, 00:00', 'Open': '2607.100098', 'High': '2607.100098', 'Low': '2607.100098', 'Close': '2607.100098', 'Adj Close': '2607.100098', 'CloseUSD': '338.92301274'}], 'var_call_nnQClJoB5FtcIss7D3qxs2zG': [{'idx': '000001.SS'}, {'idx': '399001.SZ'}, {'idx': 'GDAXI'}, {'idx': 'GSPTSE'}, {'idx': 'HSI'}, {'idx': 'IXIC'}, {'idx': 'J203.JO'}, {'idx': 'N100'}, {'idx': 'N225'}, {'idx': 'NSEI'}, {'idx': 'NYA'}, {'idx': 'SSMI'}, {'idx': 'TWII'}], 'var_call_sZpkjVyAFiG9eRqSrEzB0BBM': [{'idx': 'J203.JO', 'n': '2346'}, {'idx': 'N225', 'n': '13874'}, {'idx': 'GSPTSE', 'n': '10526'}, {'idx': 'NSEI', 'n': '3346'}, {'idx': 'GDAXI', 'n': '8438'}, {'idx': 'IXIC', 'n': '12690'}, {'idx': 'HSI', 'n': '8492'}, {'idx': 'NYA', 'n': '13947'}, {'idx': '000001.SS', 'n': '5791'}, {'idx': 'SSMI', 'n': '7671'}, {'idx': 'TWII', 'n': '5869'}, {'idx': 'N100', 'n': '5474'}, {'idx': '399001.SZ', 'n': '5760'}]}

exec(code, env_args)
