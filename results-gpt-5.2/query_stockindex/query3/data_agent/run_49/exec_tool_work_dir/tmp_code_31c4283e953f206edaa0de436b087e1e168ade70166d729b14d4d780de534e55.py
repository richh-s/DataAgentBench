code = """import json, pandas as pd

top = pd.DataFrame(var_call_qwjSs53kmPZa9xEhKYdEr2ds)

def country_from_index(idx):
    m = {
        'NSEI': 'India',
        'IXIC': 'United States',
        '399001.SZ': 'China',
        'GSPTSE': 'Canada',
        'J203.JO': 'South Africa'
    }
    return m.get(idx)

top['Country'] = top['Index'].map(country_from_index)
# format return as percent
for c in ['total_return','months']:
    top[c] = pd.to_numeric(top[c], errors='coerce')

top['Overall return since 2000 (USD, compounded monthly)'] = (top['total_return']*100).round(2).astype(str) + '%'
res = top[['Index','Country','Overall return since 2000 (USD, compounded monthly)','months']].rename(columns={'months':'Months of data used'}).to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(res))"""

env_args = {'var_call_4dJkZT69SDJyFOpVX43a5vMl': ['index_trade'], 'var_call_E8lvNNs9ubJdzdmBgJE3f1wk': ['index_info'], 'var_call_4mOW74IxdpNEVR5Kavytyc1c': [{'Date': '31 Dec 1986, 00:00'}, {'Date': 'January 02, 1987 at 12:00 AM'}, {'Date': '1987-01-05 00:00:00'}, {'Date': '06 Jan 1987, 00:00'}, {'Date': '07 Jan 1987, 00:00'}, {'Date': '1987-01-08 00:00:00'}, {'Date': '1987-01-09 00:00:00'}, {'Date': '1987-01-12 00:00:00'}, {'Date': '1987-01-13 00:00:00'}, {'Date': '1987-01-14 00:00:00'}, {'Date': 'January 15, 1987 at 12:00 AM'}, {'Date': 'January 16, 1987 at 12:00 AM'}, {'Date': 'January 19, 1987 at 12:00 AM'}, {'Date': '20 Jan 1987, 00:00'}, {'Date': 'January 21, 1987 at 12:00 AM'}, {'Date': '22 Jan 1987, 00:00'}, {'Date': 'January 23, 1987 at 12:00 AM'}, {'Date': 'January 26, 1987 at 12:00 AM'}, {'Date': '27 Jan 1987, 00:00'}, {'Date': 'January 28, 1987 at 12:00 AM'}], 'var_call_qwjSs53kmPZa9xEhKYdEr2ds': [{'Index': 'NSEI', 'total_return': '1.43221906459967', 'months': '165'}, {'Index': 'IXIC', 'total_return': '1.1408406831681774', 'months': '257'}, {'Index': '399001.SZ', 'total_return': '0.8789456697406242', 'months': '258'}, {'Index': 'GSPTSE', 'total_return': '0.7403778339994684', 'months': '257'}, {'Index': 'J203.JO', 'total_return': '0.6735227770198748', 'months': '112'}]}

exec(code, env_args)
