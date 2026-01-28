code = """import pandas as pd, json, re

def parse_date(s):
    if s is None:
        return None
    s=str(s)
    # normalize common suffix
    s=s.replace(' at 12:00 AM','')
    # try multiple formats
    for fmt in ('%Y-%m-%d %H:%M:%S','%Y-%m-%d','%d %b %Y, %H:%M','%B %d, %Y','%b %d, %Y','%B %d, %Y %H:%M:%S','%d %b %Y'):
        try:
            return pd.to_datetime(s, format=fmt)
        except Exception:
            pass
    # fallback
    try:
        return pd.to_datetime(s, errors='coerce')
    except Exception:
        return pd.NaT

# quick test on sample dates
sample=[r['Date'] for r in var_call_oYCG8MlFBCwuPR7xHlWkVQRF]
parsed=[(d,str(parse_date(d))) for d in sample]
print('__RESULT__:')
print(json.dumps(parsed))"""

env_args = {'var_call_573u2hpe6FOd5xoZgzFGwUqh': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_call_oYCG8MlFBCwuPR7xHlWkVQRF': [{'Date': 'January 27, 2015 at 12:00 AM', 'n': '11'}, {'Date': '2017-10-12 00:00:00', 'n': '11'}, {'Date': '2015-01-16 00:00:00', 'n': '11'}, {'Date': '27 Sep 2013, 00:00', 'n': '10'}, {'Date': '2013-05-21 00:00:00', 'n': '10'}, {'Date': 'July 12, 2010 at 12:00 AM', 'n': '10'}, {'Date': '2012-05-25 00:00:00', 'n': '10'}, {'Date': 'June 19, 2019 at 12:00 AM', 'n': '10'}, {'Date': '07 Apr 2011, 00:00', 'n': '10'}, {'Date': 'April 15, 2005 at 12:00 AM', 'n': '10'}, {'Date': '16 Jan 2014, 00:00', 'n': '10'}, {'Date': '2017-06-14 00:00:00', 'n': '10'}, {'Date': '12 Nov 2010, 00:00', 'n': '10'}, {'Date': '15 May 2019, 00:00', 'n': '10'}, {'Date': '2012-06-18 00:00:00', 'n': '10'}, {'Date': '2016-12-29 00:00:00', 'n': '9'}, {'Date': 'January 15, 2021 at 12:00 AM', 'n': '9'}, {'Date': '2002-01-11 00:00:00', 'n': '9'}, {'Date': '01 Jun 2016, 00:00', 'n': '9'}, {'Date': '26 Apr 2013, 00:00', 'n': '9'}]}

exec(code, env_args)
