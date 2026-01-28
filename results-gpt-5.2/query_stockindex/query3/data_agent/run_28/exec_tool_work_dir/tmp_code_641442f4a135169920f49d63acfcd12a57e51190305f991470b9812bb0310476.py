code = """import json, pandas as pd

top5 = pd.DataFrame(var_call_pbiz4c7NTanN44INj65fwEuW)

# Map index symbol to exchange/country (using provided exchanges + common knowledge)
map_info = {
    'IXIC': {'exchange':'NASDAQ','country':'United States'},
    '399001.SZ': {'exchange':'Shenzhen Stock Exchange','country':'China'},
    'GDAXI': {'exchange':'Frankfurt Stock Exchange','country':'Germany'},
    'NSEI': {'exchange':'National Stock Exchange of India','country':'India'},
    'TWII': {'exchange':'Taiwan Stock Exchange','country':'Taiwan'},
}

rows=[]
for _,r in top5.iterrows():
    idx=r['idx']
    info=map_info.get(idx, {})
    rows.append({
        'Index': idx,
        'Country': info.get('country'),
        'Exchange': info.get('exchange'),
        'Return_multiple_on_DCA_since_2000': float(r['multiple']),
        'Period_end': str(r['last_date'])
    })

answer = rows
print('__RESULT__:')
print(json.dumps(answer))"""

env_args = {'var_call_uXuq4qv02TuJJavjKbWSQ6G4': ['index_info'], 'var_call_M1WhtKD8xs0zZl3xi1fo04du': ['index_trade'], 'var_call_SEDHzV7YneXG9Z27iO20DeVG': [{'Date': '31 Dec 1986, 00:00'}, {'Date': 'January 02, 1987 at 12:00 AM'}, {'Date': '1987-01-05 00:00:00'}, {'Date': '06 Jan 1987, 00:00'}, {'Date': '07 Jan 1987, 00:00'}, {'Date': '1987-01-08 00:00:00'}, {'Date': '1987-01-09 00:00:00'}, {'Date': '1987-01-12 00:00:00'}, {'Date': '1987-01-13 00:00:00'}, {'Date': '1987-01-14 00:00:00'}, {'Date': 'January 15, 1987 at 12:00 AM'}, {'Date': 'January 16, 1987 at 12:00 AM'}, {'Date': 'January 19, 1987 at 12:00 AM'}, {'Date': '20 Jan 1987, 00:00'}, {'Date': 'January 21, 1987 at 12:00 AM'}, {'Date': '22 Jan 1987, 00:00'}, {'Date': 'January 23, 1987 at 12:00 AM'}, {'Date': 'January 26, 1987 at 12:00 AM'}, {'Date': '27 Jan 1987, 00:00'}, {'Date': 'January 28, 1987 at 12:00 AM'}, {'Date': '02 Feb 1987, 00:00'}, {'Date': '03 Feb 1987, 00:00'}, {'Date': 'February 04, 1987 at 12:00 AM'}, {'Date': 'February 05, 1987 at 12:00 AM'}, {'Date': '06 Feb 1987, 00:00'}, {'Date': '1987-02-09 00:00:00'}, {'Date': '1987-02-10 00:00:00'}, {'Date': '11 Feb 1987, 00:00'}, {'Date': '12 Feb 1987, 00:00'}, {'Date': 'February 13, 1987 at 12:00 AM'}, {'Date': '16 Feb 1987, 00:00'}, {'Date': 'February 17, 1987 at 12:00 AM'}, {'Date': 'February 18, 1987 at 12:00 AM'}, {'Date': '19 Feb 1987, 00:00'}, {'Date': '1987-02-20 00:00:00'}, {'Date': 'February 23, 1987 at 12:00 AM'}, {'Date': '24 Feb 1987, 00:00'}, {'Date': 'February 25, 1987 at 12:00 AM'}, {'Date': '26 Feb 1987, 00:00'}, {'Date': '27 Feb 1987, 00:00'}, {'Date': '1987-03-02 00:00:00'}, {'Date': '1987-03-03 00:00:00'}, {'Date': '1987-03-04 00:00:00'}, {'Date': 'March 05, 1987 at 12:00 AM'}, {'Date': 'March 06, 1987 at 12:00 AM'}, {'Date': '09 Mar 1987, 00:00'}, {'Date': 'March 10, 1987 at 12:00 AM'}, {'Date': '11 Mar 1987, 00:00'}, {'Date': '12 Mar 1987, 00:00'}, {'Date': 'March 13, 1987 at 12:00 AM'}], 'var_call_11KL8JFtCoJ6y0Mr6r5YGYvE': 'file_storage/call_11KL8JFtCoJ6y0Mr6r5YGYvE.json', 'var_call_pbiz4c7NTanN44INj65fwEuW': [{'idx': 'IXIC', 'total_units': 0.09017018591923191, 'n_months': 257, 'last_close_usd': 13748.74023, 'last_date': '2021-05-28 00:00:00', 'total_contrib': 257.0, 'final_value': 1239.7264626943233, 'multiple': 4.823838376242503}, {'idx': '399001.SZ', 'total_units': 0.25449700623228744, 'n_months': 258, 'last_close_usd': 2405.5648432, 'last_date': '2021-06-01 00:00:00', 'total_contrib': 258.0, 'final_value': 612.2090508920419, 'multiple': 2.37290329803117}, {'idx': 'GDAXI', 'total_units': 0.03206750240773371, 'n_months': 257, 'last_close_usd': 18867.4096048, 'last_date': '2021-05-25 00:00:00', 'total_contrib': 257.0, 'final_value': 605.0307029296222, 'multiple': 2.354205069765067}, {'idx': 'NSEI', 'total_units': 2.4951246716798203, 'n_months': 165, 'last_close_usd': 154.3565039, 'last_date': '2021-05-28 00:00:00', 'total_contrib': 165.0, 'final_value': 385.1387211151324, 'multiple': 2.334174067364439}, {'idx': 'TWII', 'total_units': 0.8647632070908243, 'n_months': 257, 'last_close_usd': 682.7371876000001, 'last_date': '2021-05-31 00:00:00', 'total_contrib': 257.0, 'final_value': 590.4059999491459, 'multiple': 2.2972996106970656}], 'var_call_u58VCrB009wELUGIpw4wQh39': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}]}

exec(code, env_args)
