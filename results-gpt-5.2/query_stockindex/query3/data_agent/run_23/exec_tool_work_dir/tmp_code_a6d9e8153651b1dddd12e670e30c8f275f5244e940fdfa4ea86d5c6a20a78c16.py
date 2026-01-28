code = """import json, pandas as pd

top5 = pd.DataFrame(var_call_dTrxelqFGHzq0cVcMBVjwzG3)

def country_for_index(idx):
    mapping = {
        '399001.SZ': 'China',   # Shenzhen Component
        '000001.SS': 'China',   # SSE Composite
        'IXIC': 'United States',# NASDAQ Composite
        'NYA': 'United States', # NYSE Composite
        'NSEI': 'India',        # NIFTY 50
    }
    return mapping.get(idx, None)

top5['country'] = top5['idx'].map(country_for_index)
# format returns as percent
for c in ['total_return']:
    top5[c] = top5[c].astype(float)

top5 = top5.sort_values('total_return', ascending=False)
rows = []
for _, r in top5.iterrows():
    rows.append({
        'Index': r['idx'],
        'Country': r['country'],
        'TotalReturnSince2000': r['total_return'],
        'TotalReturnPctSince2000': r['total_return']*100,
        'MonthsUsed': int(r['n_months'])
    })

print('__RESULT__:')
print(json.dumps(rows))"""

env_args = {'var_call_Htnv5CUZOU25JqXWjIWzd61Q': ['index_info'], 'var_call_omqxOnx0gb4LKo267Vk3MnVQ': [{'Date': '31 Dec 1986, 00:00'}, {'Date': 'January 02, 1987 at 12:00 AM'}, {'Date': '1987-01-05 00:00:00'}, {'Date': '06 Jan 1987, 00:00'}, {'Date': '07 Jan 1987, 00:00'}, {'Date': '1987-01-08 00:00:00'}, {'Date': '1987-01-09 00:00:00'}, {'Date': '1987-01-12 00:00:00'}, {'Date': '1987-01-13 00:00:00'}, {'Date': '1987-01-14 00:00:00'}, {'Date': 'January 15, 1987 at 12:00 AM'}, {'Date': 'January 16, 1987 at 12:00 AM'}, {'Date': 'January 19, 1987 at 12:00 AM'}, {'Date': '20 Jan 1987, 00:00'}, {'Date': 'January 21, 1987 at 12:00 AM'}, {'Date': '22 Jan 1987, 00:00'}, {'Date': 'January 23, 1987 at 12:00 AM'}, {'Date': 'January 26, 1987 at 12:00 AM'}, {'Date': '27 Jan 1987, 00:00'}, {'Date': 'January 28, 1987 at 12:00 AM'}], 'var_call_TcQfFEFvolT7vnRnv9WqrRxn': [{'total_rows': '104224', 'null_parsed': '0.0'}], 'var_call_dTrxelqFGHzq0cVcMBVjwzG3': [{'idx': '399001.SZ', 'n_months': '257', 'total_return': '2.7592027372691175'}, {'idx': 'IXIC', 'n_months': '256', 'total_return': '2.4892179344618204'}, {'idx': 'NSEI', 'n_months': '164', 'total_return': '2.103308772715655'}, {'idx': 'NYA', 'n_months': '256', 'total_return': '1.518350405505012'}, {'idx': '000001.SS', 'n_months': '256', 'total_return': '1.3553662336011332'}], 'var_call_PA4zwT3Q4qDDs0qj1ePeeEXJ': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}]}

exec(code, env_args)
