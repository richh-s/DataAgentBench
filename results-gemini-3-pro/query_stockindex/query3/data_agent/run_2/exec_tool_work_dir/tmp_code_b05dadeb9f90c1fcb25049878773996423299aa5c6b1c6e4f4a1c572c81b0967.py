code = """import json
import pandas as pd
import dateutil.parser

file_path = locals()['var_function-call-16195887922252299573']

with open(file_path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

try:
    df['Date'] = pd.to_datetime(df['Date'], format='mixed')
except:
    df['Date'] = df['Date'].apply(lambda x: dateutil.parser.parse(x))

df['CloseUSD'] = pd.to_numeric(df['CloseUSD'], errors='coerce')
df = df.dropna(subset=['Date', 'CloseUSD'])
df = df[df['Date'] >= '2000-01-01']
df = df.sort_values(['Index', 'Date'])
df['YearMonth'] = df['Date'].dt.to_period('M')

monthly_investments = df.groupby(['Index', 'YearMonth']).head(1)

results = []
indices = df['Index'].unique()

for idx in indices:
    inv_data = monthly_investments[monthly_investments['Index'] == idx]
    if inv_data.empty:
        continue
    
    shares = (1.0 / inv_data['CloseUSD']).sum()
    total_invested = len(inv_data)
    last_row = df[df['Index'] == idx].iloc[-1]
    last_price = last_row['CloseUSD']
    final_value = shares * last_price
    roi = (final_value - total_invested) / total_invested * 100
    
    results.append({
        'Index': idx,
        'ROI': roi,
        'Count': total_invested
    })

res_df = pd.DataFrame(results).sort_values('ROI', ascending=False)

print("__RESULT__:")
print(json.dumps(res_df.to_dict(orient='records')))"""

env_args = {'var_function-call-11103673439672531261': ['index_info'], 'var_function-call-11103673439672530174': ['index_trade'], 'var_function-call-11103673439672529087': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}], 'var_function-call-11103673439672532096': [{'Index': 'HSI', 'Date': '31 Dec 1986, 00:00', 'Open': '2568.300049', 'High': '2568.300049', 'Low': '2568.300049', 'Close': '2568.300049', 'Adj Close': '2568.300049', 'CloseUSD': '333.87900637'}, {'Index': 'HSI', 'Date': 'January 02, 1987 at 12:00 AM', 'Open': '2540.100098', 'High': '2540.100098', 'Low': '2540.100098', 'Close': '2540.100098', 'Adj Close': '2540.100098', 'CloseUSD': '330.21301274'}, {'Index': 'HSI', 'Date': '1987-01-05 00:00:00', 'Open': '2552.399902', 'High': '2552.399902', 'Low': '2552.399902', 'Close': '2552.399902', 'Adj Close': '2552.399902', 'CloseUSD': '331.81198726'}, {'Index': 'HSI', 'Date': '06 Jan 1987, 00:00', 'Open': '2583.899902', 'High': '2583.899902', 'Low': '2583.899902', 'Close': '2583.899902', 'Adj Close': '2583.899902', 'CloseUSD': '335.90698726000005'}, {'Index': 'HSI', 'Date': '07 Jan 1987, 00:00', 'Open': '2607.100098', 'High': '2607.100098', 'Low': '2607.100098', 'Close': '2607.100098', 'Adj Close': '2607.100098', 'CloseUSD': '338.92301274'}, {'Index': 'HSI', 'Date': '1987-01-08 00:00:00', 'Open': '2603.300049', 'High': '2603.300049', 'Low': '2603.300049', 'Close': '2603.300049', 'Adj Close': '2603.300049', 'CloseUSD': '338.42900637'}, {'Index': 'HSI', 'Date': '1987-01-09 00:00:00', 'Open': '2561.699951', 'High': '2561.699951', 'Low': '2561.699951', 'Close': '2561.699951', 'Adj Close': '2561.699951', 'CloseUSD': '333.02099363'}, {'Index': 'HSI', 'Date': '1987-01-12 00:00:00', 'Open': '2614.899902', 'High': '2614.899902', 'Low': '2614.899902', 'Close': '2614.899902', 'Adj Close': '2614.899902', 'CloseUSD': '339.93698726'}, {'Index': 'HSI', 'Date': '1987-01-13 00:00:00', 'Open': '2590.800049', 'High': '2590.800049', 'Low': '2590.800049', 'Close': '2590.800049', 'Adj Close': '2590.800049', 'CloseUSD': '336.80400637'}, {'Index': 'HSI', 'Date': '1987-01-14 00:00:00', 'Open': '2578.199951', 'High': '2578.199951', 'Low': '2578.199951', 'Close': '2578.199951', 'Adj Close': '2578.199951', 'CloseUSD': '335.16599363'}], 'var_function-call-8652362811134081670': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'HSI'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'IXIC'}, {'Index': 'N100'}, {'Index': '399001.SZ'}, {'Index': 'NYA'}], 'var_function-call-8652362811134080107': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_function-call-6622336040025501380': [{'count_star()': '104224'}], 'var_function-call-16195887922252299573': 'file_storage/function-call-16195887922252299573.json', 'var_function-call-8550886626597199337': [{'Index': 'IXIC', 'ROI': 382.69431542041946, 'TotalInvested': 257, 'FinalValue': 1240.524390630478, 'StartDate': '2000-01-03', 'EndDate': '2021-05-28'}, {'Index': 'NSEI', 'ROI': 135.84273445798652, 'TotalInvested': 165, 'FinalValue': 389.1405118556778, 'StartDate': '2007-09-17', 'EndDate': '2021-05-31'}, {'Index': '399001.SZ', 'ROI': 134.74636718846307, 'TotalInvested': 258, 'FinalValue': 605.6456273462347, 'StartDate': '2000-01-04', 'EndDate': '2021-06-02'}, {'Index': 'GDAXI', 'ROI': 134.7028715908275, 'TotalInvested': 257, 'FinalValue': 603.1863799884267, 'StartDate': '2000-01-03', 'EndDate': '2021-05-31'}, {'Index': 'TWII', 'ROI': 129.82003158446506, 'TotalInvested': 257, 'FinalValue': 590.6374811720752, 'StartDate': '2000-01-04', 'EndDate': '2021-05-31'}]}

exec(code, env_args)
