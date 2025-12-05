code = """import pandas as pd, json

path = var_call_4cZg7WX9YqVoOW1PprPNHOJf
with open(path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Parse dates with explicit format
df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d %H:%M:%S', errors='coerce')

# Drop rows with invalid dates
df = df.dropna(subset=['Date'])

df['Adj Close'] = df['Adj Close'].astype(float)

df['YearMonth'] = df['Date'].dt.to_period('M')

first_days = df.sort_values('Date').groupby(['Index','YearMonth']).first().reset_index()
first_days['units'] = 1.0 / first_days['Adj Close']

units_per_index = first_days.groupby('Index')['units'].sum().reset_index()

last_prices = df.sort_values('Date').groupby('Index').tail(1)[['Index','Adj Close']].rename(columns={'Adj Close':'last_price'})

summary = units_per_index.merge(last_prices, on='Index')

months_invested = first_days.groupby('Index').size().reset_index(name='months')
summary = summary.merge(months_invested, on='Index')
summary['total_invested'] = summary['months'] * 1.0
summary['final_value'] = summary['units'] * summary['last_price']
summary['return_multiple'] = summary['final_value'] / summary['total_invested']

top5 = summary.sort_values('return_multiple', ascending=False).head(5)

result = top5[['Index','return_multiple']].to_json(orient='records')

print("__RESULT__:")
print(result)"""

env_args = {'var_call_4cZg7WX9YqVoOW1PprPNHOJf': 'file_storage/call_4cZg7WX9YqVoOW1PprPNHOJf.json'}

exec(code, env_args)
