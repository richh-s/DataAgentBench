code = """import pandas as pd
import json

# Load data
with open(locals()['var_function-call-15418031616304384514'], 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'], format='mixed', dayfirst=False, errors='coerce')
df = df[df['Date'] >= '2000-01-01']
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'])
df = df.sort_values(['Index', 'Date'])

country_map = {
    "J203.JO": "South Africa",
    "N225": "Japan",
    "GSPTSE": "Canada",
    "NSEI": "India",
    "GDAXI": "Germany",
    "IXIC": "United States",
    "HSI": "Hong Kong",
    "NYA": "United States",
    "000001.SS": "China",
    "SSMI": "Switzerland",
    "TWII": "Taiwan",
    "N100": "Europe",
    "399001.SZ": "China"
}

results = []

for index_name, group in df.groupby('Index'):
    # Check start date
    if group['Date'].min() > pd.Timestamp('2000-01-31'):
        continue
        
    # Resample to month start
    group = group.set_index('Date')
    monthly_data = group.resample('MS').first().dropna()
    
    monthly_investment = 1000.0
    total_units = 0.0
    total_invested = 0.0
    
    for date, row in monthly_data.iterrows():
        price = row['CloseUSD']
        if price > 0:
            units = monthly_investment / price
            total_units += units
            total_invested += monthly_investment
            
    # Final value
    if not group.empty:
        last_price = group.iloc[-1]['CloseUSD']
        final_value = total_units * last_price
        
        if total_invested > 0:
            overall_return = (final_value - total_invested) / total_invested
        else:
            overall_return = 0
            
        results.append({
            "Index": index_name,
            "Country": country_map.get(index_name, "Unknown"),
            "Return": overall_return
        })

results_df = pd.DataFrame(results)
results_df = results_df.sort_values('Return', ascending=False)
print("__RESULT__:")
print(results_df.head(5).to_json(orient='records'))"""

env_args = {'var_function-call-12320111116943804548': ['index_info'], 'var_function-call-12320111116943804071': ['index_trade'], 'var_function-call-7371888173575617540': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}], 'var_function-call-3489654952358117405': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_function-call-10331012001117657373': 'file_storage/function-call-10331012001117657373.json', 'var_function-call-8974196404492106585': [{'Index': 'IXIC', 'Country': 'USA', 'Return': 39.2222487639}, {'Index': 'NYA', 'Country': 'USA', 'Return': 11.2680318352}, {'Index': 'N225', 'Country': 'Japan', 'Return': 3.6241681327}, {'Index': 'GDAXI', 'Country': 'Germany', 'Return': 3.2899857508}, {'Index': 'GSPTSE', 'Country': 'Canada', 'Return': 2.9656619215}], 'var_function-call-1916111007274748501': {'Min': 55.48, 'Max': 14138.78027, 'Count': 7351, 'First': 3727.129883, 'Last': 4620.160156}, 'var_function-call-4715541387608823558': {'Min_Date': 'October 01, 1974 at 12:00 AM', 'Min_Val': 55.48, 'Max_Date': 'April 26, 2021 at 12:00 AM', 'Max_Val': 14138.78027, 'Last_Date': 'September 30, 2015 at 12:00 AM', 'Last_Val': 4620.160156}, 'var_function-call-15418031616304384514': 'file_storage/function-call-15418031616304384514.json', 'var_function-call-7812723058100869502': [{'Index': 'IXIC', 'Country': 'USA', 'Return': 3.8269431542}, {'Index': 'NSEI', 'Country': 'India', 'Return': 1.3584273446}, {'Index': '399001.SZ', 'Country': 'China', 'Return': 1.3474636719}, {'Index': 'GDAXI', 'Country': 'Germany', 'Return': 1.3470287159}, {'Index': 'TWII', 'Country': 'Taiwan', 'Return': 1.2982003158}], 'var_function-call-4773802726259585352': [{'Index': 'IXIC', 'Start': '2000-01-03 00:00:00', 'End': '2021-05-28 00:00:00', 'StartPrice': 4131.149902, 'EndPrice': 13748.74023}, {'Index': 'NSEI', 'Start': '2007-09-17 00:00:00', 'End': '2021-05-31 00:00:00', 'StartPrice': 44.946499020000005, 'EndPrice': 155.8279981}, {'Index': '399001.SZ', 'Start': '2000-01-04 00:00:00', 'End': '2021-06-02 00:00:00', 'StartPrice': 559.52960944, 'EndPrice': 2377.2656256}, {'Index': 'GDAXI', 'Start': '2000-01-03 00:00:00', 'End': '2021-05-31 00:00:00', 'StartPrice': 8235.92691452, 'EndPrice': 18813.7784536}, {'Index': 'TWII', 'Start': '2000-01-04 00:00:00', 'End': '2021-05-31 00:00:00', 'StartPrice': 350.2619922, 'EndPrice': 682.7371876000001}], 'var_function-call-7832883874624162398': {'GDAXI': '2000-01-03', 'HSI': '2000-01-03', 'IXIC': '2000-01-03', 'N100': '2000-01-03', 'NYA': '2000-01-03', '000001.SS': '2000-01-04', '399001.SZ': '2000-01-04', 'GSPTSE': '2000-01-04', 'N225': '2000-01-04', 'SSMI': '2000-01-04', 'TWII': '2000-01-04', 'NSEI': '2007-09-17', 'J203.JO': '2012-02-08'}}

exec(code, env_args)
