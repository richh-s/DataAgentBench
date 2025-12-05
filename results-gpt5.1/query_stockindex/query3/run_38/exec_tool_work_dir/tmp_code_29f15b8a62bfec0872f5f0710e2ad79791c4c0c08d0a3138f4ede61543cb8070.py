code = """import json
import pandas as pd

indices_info = pd.DataFrame(var_call_qoeSgQs8RvTtSszcrQ6hexRu)

file_path = var_call_lxxuk0iwBsZEVClRNX5g5V0b
with open(file_path, 'r') as f:
    all_prices = pd.DataFrame(json.load(f))

all_prices['Date'] = pd.to_datetime(all_prices['Date'], errors='coerce')
all_prices = all_prices[all_prices['Date'] >= '2000-01-01']
all_prices['Adj Close'] = pd.to_numeric(all_prices['Adj Close'], errors='coerce')

start_dates = indices_info.set_index('Index')['first_date']
start_dates = pd.to_datetime(start_dates, errors='coerce')

monthly_investment = 100
results = []

for index in all_prices['Index'].unique():
    if index not in start_dates.index:
        continue
    first_date = start_dates.loc[index]
    if pd.isna(first_date) or first_date > pd.Timestamp('2000-12-31'):
        continue
    df = all_prices[all_prices['Index'] == index].copy()
    df = df.sort_values('Date')
    df_2000_on = df[df['Date'] >= '2000-01-01']
    if df_2000_on.empty:
        continue
    # group by year and month explicitly
    df_2000_on['year'] = df_2000_on['Date'].dt.year
    df_2000_on['month'] = df_2000_on['Date'].dt.month
    df_monthly = df_2000_on.sort_values('Date').groupby(['year', 'month']).first().reset_index()
    if df_monthly.empty:
        continue
    units_bought = monthly_investment / df_monthly['Adj Close']
    total_units = units_bought.sum()
    final_price = df_2000_on.iloc[-1]['Adj Close']
    final_value = total_units * final_price
    total_invested = monthly_investment * len(df_monthly)
    results.append({'Index': index, 'final_value': float(final_value), 'total_invested': float(total_invested)})

results_df = pd.DataFrame(results)
results_df['return_multiple'] = results_df['final_value'] / results_df['total_invested']

results_top5 = results_df.sort_values('return_multiple', ascending=False).head(5)

results_top5_list = results_top5.to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(results_top5_list))"""

env_args = {'var_call_qoeSgQs8RvTtSszcrQ6hexRu': [{'Index': 'N225', 'first_date': '01 Apr 1971, 00:00'}, {'Index': 'GSPTSE', 'first_date': '01 Apr 1981, 00:00'}, {'Index': 'NSEI', 'first_date': '01 Apr 2014, 00:00'}, {'Index': 'GDAXI', 'first_date': '01 Apr 1992, 00:00'}, {'Index': 'IXIC', 'first_date': '01 Apr 1974, 00:00'}, {'Index': 'HSI', 'first_date': '01 Apr 1992, 00:00'}, {'Index': 'NYA', 'first_date': '01 Apr 1969, 00:00'}, {'Index': '000001.SS', 'first_date': '01 Apr 2003, 00:00'}, {'Index': 'SSMI', 'first_date': '01 Apr 1996, 00:00'}, {'Index': 'TWII', 'first_date': '01 Apr 2004, 00:00'}, {'Index': 'N100', 'first_date': '01 Apr 2003, 00:00'}, {'Index': '399001.SZ', 'first_date': '01 Apr 2004, 00:00'}, {'Index': 'J203.JO', 'first_date': '01 Apr 2016, 00:00'}], 'var_call_lxxuk0iwBsZEVClRNX5g5V0b': 'file_storage/call_lxxuk0iwBsZEVClRNX5g5V0b.json'}

exec(code, env_args)
