code = """import pandas as pd, json

# Load index list that has data starting before or on Jan 2000
eligible = pd.DataFrame(var_call_pLJFv63s2vRDgQPFfoUmS66I)
eligible_indexes = set(eligible['Index'])

# Load full adj close data from file
with open(var_call_aOoBfMeJ19CaeMoNld6l0PIX, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Normalize date
df['Date'] = pd.to_datetime(df['Date'])

# Filter from 2000-01-01 onward and eligible indices
start_date = pd.Timestamp('2000-01-01')
df = df[df['Date'] >= start_date]
df = df[df['Index'].isin(eligible_indexes)]

# Convert Adj Close to float
df['Adj Close'] = df['Adj Close'].astype(float)

# Compute month-end prices (use last available trading day of each month)
df['YearMonth'] = df['Date'].dt.to_period('M')
month_end = df.sort_values('Date').groupby(['Index','YearMonth']).tail(1)

# Assume investing 1 unit of currency each month at month-end price => units = 1/price
month_end['units_bought'] = 1.0 / month_end['Adj Close']

# Aggregate per index
agg = month_end.groupby('Index').agg(
    total_units=('units_bought','sum'),
    total_contrib=('units_bought','size')  # number of months = total dollars invested
).reset_index()

# Need final price (last available date per index)
last_prices = df.sort_values('Date').groupby('Index').tail(1)[['Index','Adj Close']].rename(columns={'Adj Close':'final_price'})

res = agg.merge(last_prices, on='Index')

# Portfolio value and total invested
res['final_value'] = res['total_units'] * res['final_price']
res['total_invested'] = res['total_contrib'] * 1.0
res['return_multiple'] = res['final_value'] / res['total_invested']

# Top 5 indices
top5 = res.sort_values('return_multiple', ascending=False).head(5)

result = top5[['Index','return_multiple']].to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_pLJFv63s2vRDgQPFfoUmS66I': [{'Index': 'J203.JO', 'first_date': '01 Apr 2016, 00:00'}, {'Index': 'N225', 'first_date': '01 Apr 1971, 00:00'}, {'Index': 'GSPTSE', 'first_date': '01 Apr 1981, 00:00'}, {'Index': 'NSEI', 'first_date': '01 Apr 2014, 00:00'}, {'Index': 'GDAXI', 'first_date': '01 Apr 1992, 00:00'}, {'Index': 'IXIC', 'first_date': '01 Apr 1974, 00:00'}, {'Index': 'HSI', 'first_date': '01 Apr 1992, 00:00'}, {'Index': 'NYA', 'first_date': '01 Apr 1969, 00:00'}, {'Index': 'N100', 'first_date': '01 Apr 2003, 00:00'}, {'Index': '399001.SZ', 'first_date': '01 Apr 2004, 00:00'}, {'Index': '000001.SS', 'first_date': '01 Apr 2003, 00:00'}, {'Index': 'SSMI', 'first_date': '01 Apr 1996, 00:00'}, {'Index': 'TWII', 'first_date': '01 Apr 2004, 00:00'}], 'var_call_aOoBfMeJ19CaeMoNld6l0PIX': 'file_storage/call_aOoBfMeJ19CaeMoNld6l0PIX.json'}

exec(code, env_args)
