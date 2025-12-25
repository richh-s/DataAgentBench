code = """import pandas as pd
import json

# Load data
with open(locals()['var_function-call-12731797609713319278'], 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'], errors='coerce')

# Filter for date >= 2000-01-01
df = df[df['Date'] >= '2000-01-01']

df = df.dropna(subset=['Date', 'CloseUSD'])
df = df.sort_values(['Index', 'Date'])

results = []

for idx, group in df.groupby('Index'):
    group = group.copy()
    group['Month'] = group['Date'].dt.to_period('M')
    monthly_investments = group.drop_duplicates(subset='Month', keep='first')
    monthly_investments = monthly_investments[monthly_investments['CloseUSD'] > 0]
    
    units = (1 / monthly_investments['CloseUSD']).sum()
    total_invested = len(monthly_investments)
    
    if not group.empty:
        final_price = group.iloc[-1]['CloseUSD']
        final_date = group.iloc[-1]['Date']
        final_value = units * final_price
        overall_return = (final_value - total_invested) / total_invested if total_invested > 0 else 0
        
        results.append({
            'Index': idx,
            'Return': overall_return,
            'FinalValue': final_value,
            'TotalInvested': total_invested,
            'Start': str(monthly_investments.iloc[0]['Date']) if not monthly_investments.empty else None,
            'End': str(final_date)
        })

results_df = pd.DataFrame(results).sort_values('Return', ascending=False)

print("__RESULT__:")
print(results_df.to_json(orient='records'))"""

env_args = {'var_function-call-16286307264463492830': ['index_info'], 'var_function-call-16286307264463494683': ['index_trade'], 'var_function-call-12146826697668835484': [{'cid': '0', 'name': 'Exchange', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '1', 'name': 'Currency', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}], 'var_function-call-1648360365740439576': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_function-call-1648360365740441073': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'NYA'}, {'Index': 'HSI'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_function-call-5799821590587801299': [{'Index': 'J203.JO', 'usd_count': '1854', 'close_count': '1854', 'total': '1854'}, {'Index': 'N225', 'usd_count': '7979', 'close_count': '7979', 'total': '7979'}, {'Index': 'GSPTSE', 'usd_count': '6506', 'close_count': '6506', 'total': '6506'}, {'Index': 'NSEI', 'usd_count': '2577', 'close_count': '2577', 'total': '2577'}, {'Index': 'GDAXI', 'usd_count': '5590', 'close_count': '5590', 'total': '5590'}, {'Index': 'IXIC', 'usd_count': '7351', 'close_count': '7351', 'total': '7351'}, {'Index': 'NYA', 'usd_count': '7960', 'close_count': '7960', 'total': '7960'}, {'Index': 'HSI', 'usd_count': '5604', 'close_count': '5604', 'total': '5604'}, {'Index': 'N100', 'usd_count': '4245', 'close_count': '4245', 'total': '4245'}, {'Index': '399001.SZ', 'usd_count': '4355', 'close_count': '4355', 'total': '4355'}, {'Index': '000001.SS', 'usd_count': '4354', 'close_count': '4354', 'total': '4354'}, {'Index': 'SSMI', 'usd_count': '5188', 'close_count': '5188', 'total': '5188'}, {'Index': 'TWII', 'usd_count': '4385', 'close_count': '4385', 'total': '4385'}], 'var_function-call-12731797609713319278': 'file_storage/function-call-12731797609713319278.json', 'var_function-call-4686361877987652280': [{'Index': 'IXIC', 'Return': 39.2222487639, 'FinalValue': 24294.2382533945, 'TotalInvested': 604, 'Start': '1971-02-17 00:00:00', 'End': '2021-05-28 00:00:00'}, {'Index': 'NYA', 'Return': 11.2680318352, 'FinalValue': 8170.5092022597, 'TotalInvested': 666, 'Start': '1965-12-31 00:00:00', 'End': '2021-05-28 00:00:00'}, {'Index': 'N225', 'Return': 3.6241681327, 'FinalValue': 3135.1859939999, 'TotalInvested': 678, 'Start': '1965-01-06 00:00:00', 'End': '2021-06-03 00:00:00'}, {'Index': 'GDAXI', 'Return': 3.2899857508, 'FinalValue': 1724.5742718196, 'TotalInvested': 402, 'Start': '1987-12-30 00:00:00', 'End': '2021-05-31 00:00:00'}, {'Index': 'GSPTSE', 'Return': 2.9656619215, 'FinalValue': 1998.6936084524, 'TotalInvested': 504, 'Start': '1979-06-29 00:00:00', 'End': '2021-05-31 00:00:00'}, {'Index': 'HSI', 'Return': 2.2287765696, 'FinalValue': 1336.713499802, 'TotalInvested': 414, 'Start': '1986-12-31 00:00:00', 'End': '2021-05-31 00:00:00'}, {'Index': '399001.SZ', 'Return': 1.5220753885, 'FinalValue': 723.8356365057, 'TotalInvested': 287, 'Start': '1997-08-22 00:00:00', 'End': '2021-06-02 00:00:00'}, {'Index': 'NSEI', 'Return': 1.3584343633, 'FinalValue': 389.1416699402, 'TotalInvested': 165, 'Start': '2007-09-18 00:00:00', 'End': '2021-05-31 00:00:00'}, {'Index': 'SSMI', 'Return': 1.3050012111, 'FinalValue': 845.9354444679, 'TotalInvested': 367, 'Start': '1990-11-09 00:00:00', 'End': '2021-05-28 00:00:00'}, {'Index': 'TWII', 'Return': 1.2899898288, 'FinalValue': 657.2270808771, 'TotalInvested': 287, 'Start': '1997-07-07 00:00:00', 'End': '2021-05-31 00:00:00'}, {'Index': '000001.SS', 'Return': 0.7694511337, 'FinalValue': 507.8324753723, 'TotalInvested': 287, 'Start': '1997-07-02 00:00:00', 'End': '2021-05-31 00:00:00'}, {'Index': 'N100', 'Return': 0.6125512204, 'FinalValue': 416.0382148683, 'TotalInvested': 258, 'Start': '2000-01-03 00:00:00', 'End': '2021-06-02 00:00:00'}, {'Index': 'J203.JO', 'Return': 0.3737161613, 'FinalValue': 153.8562100669, 'TotalInvested': 112, 'Start': '2012-02-08 00:00:00', 'End': '2021-05-31 00:00:00'}], 'var_function-call-58672412621797705': [{'Index': 'IXIC', 'Return': 3.8220467671, 'FinalValue': 1239.2660191494, 'TotalInvested': 257, 'Start': '2000-01-06 00:00:00', 'End': '2021-05-27 00:00:00'}, {'Index': 'NSEI', 'Return': 1.3608849755, 'FinalValue': 389.5460209596, 'TotalInvested': 165, 'Start': '2007-09-25 00:00:00', 'End': '2021-05-31 00:00:00'}, {'Index': 'GDAXI', 'Return': 1.3474623836, 'FinalValue': 603.2978325969, 'TotalInvested': 257, 'Start': '2000-01-05 00:00:00', 'End': '2021-05-31 00:00:00'}, {'Index': '399001.SZ', 'Return': 1.3445453364, 'FinalValue': 604.89269678, 'TotalInvested': 258, 'Start': '2000-01-05 00:00:00', 'End': '2021-06-02 00:00:00'}, {'Index': 'TWII', 'Return': 1.2374061754, 'FinalValue': 575.0133870841, 'TotalInvested': 257, 'Start': '2000-01-17 00:00:00', 'End': '2021-05-26 00:00:00'}]}

exec(code, env_args)
