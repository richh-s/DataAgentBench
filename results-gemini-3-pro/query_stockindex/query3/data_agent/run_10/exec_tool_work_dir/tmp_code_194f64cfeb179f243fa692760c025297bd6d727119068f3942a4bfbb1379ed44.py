code = """import pandas as pd
import json
import datetime

with open(locals()['var_function-call-14265084757085608486'], 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

def parse_date(date_str):
    try:
        return pd.to_datetime(date_str)
    except:
        return pd.NaT

try:
    df['Date'] = pd.to_datetime(df['Date'], format='mixed')
except:
    df['Date'] = df['Date'].apply(parse_date)

df = df[df['Date'] >= '2000-01-01']
df = df.sort_values(['Index', 'Date'])
df['Adj Close'] = pd.to_numeric(df['Adj Close'], errors='coerce')
df = df.dropna(subset=['Adj Close'])

results = []
indices = df['Index'].unique()

for idx in indices:
    sub = df[df['Index'] == idx].copy()
    start_date = sub.iloc[0]['Date']
    
    # Check if start date is close to Jan 2000
    # Let's say, must be in Q1 2000.
    if start_date > pd.Timestamp('2000-03-31'):
        results.append({
            'Index': idx,
            'Return': -1, # Indicator to ignore
            'Start_Date': str(start_date),
            'Note': 'Starts late'
        })
        continue

    sub['YearMonth'] = sub['Date'].dt.to_period('M')
    monthly_buy = sub.drop_duplicates(subset=['YearMonth'], keep='first')
    monthly_buy['Units'] = 1 / monthly_buy['Adj Close']
    
    total_units = monthly_buy['Units'].sum()
    total_invested = len(monthly_buy)
    final_price = sub.iloc[-1]['Adj Close']
    final_value = total_units * final_price
    
    pct_return = (final_value - total_invested) / total_invested * 100
    
    results.append({
        'Index': idx,
        'Return': pct_return,
        'Start_Date': str(start_date),
        'Total_Invested': total_invested
    })

res_df = pd.DataFrame(results).sort_values('Return', ascending=False)

index_country_map = {
    "J203.JO": "South Africa",
    "N225": "Japan",
    "GSPTSE": "Canada",
    "NSEI": "India",
    "GDAXI": "Germany",
    "HSI": "Hong Kong",
    "IXIC": "United States",
    "NYA": "United States",
    "000001.SS": "China",
    "SSMI": "Switzerland",
    "TWII": "Taiwan",
    "N100": "Europe",
    "399001.SZ": "China"
}

res_df['Country'] = res_df['Index'].map(index_country_map)

print("__RESULT__:")
print(res_df.to_json(orient='records'))"""

env_args = {'var_function-call-12184386225509086772': ['index_info'], 'var_function-call-2651222669085114326': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}], 'var_function-call-6542151878181096001': ['index_trade'], 'var_function-call-14272459974564012930': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_function-call-468282391932724668': [{'Date': '31 Dec 1986, 00:00', 'Index': 'HSI', 'Adj Close': '2568.300049'}, {'Date': 'January 02, 1987 at 12:00 AM', 'Index': 'HSI', 'Adj Close': '2540.100098'}, {'Date': '1987-01-05 00:00:00', 'Index': 'HSI', 'Adj Close': '2552.399902'}, {'Date': '06 Jan 1987, 00:00', 'Index': 'HSI', 'Adj Close': '2583.899902'}, {'Date': '07 Jan 1987, 00:00', 'Index': 'HSI', 'Adj Close': '2607.100098'}], 'var_function-call-15222818763261342873': [{'count_star()': '104224'}], 'var_function-call-14265084757085608486': 'file_storage/function-call-14265084757085608486.json', 'var_function-call-8314388414536678480': [{'Index': 'IXIC', 'Return': 382.6943154204, 'Total_Invested': 257, 'Final_Value': 1240.5243906305, 'Country': 'United States'}, {'Index': 'NSEI', 'Return': 135.842734458, 'Total_Invested': 165, 'Final_Value': 389.1405118557, 'Country': 'India'}, {'Index': '399001.SZ', 'Return': 134.7487523496, 'Total_Invested': 258, 'Final_Value': 605.6517810619, 'Country': 'China'}, {'Index': 'GDAXI', 'Return': 134.7028715908, 'Total_Invested': 257, 'Final_Value': 603.1863799884, 'Country': 'Germany'}, {'Index': 'TWII', 'Return': 129.8207618672, 'Total_Invested': 257, 'Final_Value': 590.6393579988, 'Country': 'Taiwan'}], 'var_function-call-5695671454658302632': {'min': {'000001.SS': '2000-01-04T00:00:00.000', '399001.SZ': '2000-01-04T00:00:00.000', 'GDAXI': '2000-01-03T00:00:00.000', 'GSPTSE': '2000-01-04T00:00:00.000', 'HSI': '2000-01-03T00:00:00.000', 'IXIC': '2000-01-03T00:00:00.000', 'J203.JO': '2012-02-08T00:00:00.000', 'N100': '2000-01-03T00:00:00.000', 'N225': '2000-01-04T00:00:00.000', 'NSEI': '2007-09-17T00:00:00.000', 'NYA': '2000-01-03T00:00:00.000', 'SSMI': '2000-01-04T00:00:00.000', 'TWII': '2000-01-04T00:00:00.000'}, 'max': {'000001.SS': '2021-05-31T00:00:00.000', '399001.SZ': '2021-06-02T00:00:00.000', 'GDAXI': '2021-05-31T00:00:00.000', 'GSPTSE': '2021-05-31T00:00:00.000', 'HSI': '2021-05-31T00:00:00.000', 'IXIC': '2021-05-28T00:00:00.000', 'J203.JO': '2021-05-31T00:00:00.000', 'N100': '2021-06-02T00:00:00.000', 'N225': '2021-06-03T00:00:00.000', 'NSEI': '2021-05-31T00:00:00.000', 'NYA': '2021-05-28T00:00:00.000', 'SSMI': '2021-05-28T00:00:00.000', 'TWII': '2021-05-31T00:00:00.000'}, 'count': {'000001.SS': 5180, '399001.SZ': 5184, 'GDAXI': 5430, 'GSPTSE': 5379, 'HSI': 5272, 'IXIC': 5386, 'J203.JO': 2346, 'N100': 5473, 'N225': 5247, 'NSEI': 3346, 'NYA': 5386, 'SSMI': 5373, 'TWII': 5259}}}

exec(code, env_args)
