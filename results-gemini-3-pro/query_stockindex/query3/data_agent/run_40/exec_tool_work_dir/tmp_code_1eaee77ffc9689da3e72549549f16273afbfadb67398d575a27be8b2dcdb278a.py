code = """import pandas as pd
import json
import dateutil.parser

# Load index_trade data
file_path = locals()['var_function-call-405685236303482527']
with open(file_path, 'r') as f:
    trade_data = json.load(f)

df = pd.DataFrame(trade_data)
def parse_date(date_str):
    try:
        return dateutil.parser.parse(date_str)
    except:
        return None
df['Date'] = df['Date'].apply(parse_date)
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'], errors='coerce')
df = df.dropna(subset=['Date', 'CloseUSD'])
df = df[df['Date'] >= pd.Timestamp('2000-01-01')]
df = df.sort_values(by=['Index', 'Date'])
df['YM'] = df['Date'].dt.to_period('M')
monthly_df = df.groupby(['Index', 'YM']).first().reset_index()

results = []
for index_name, group in monthly_df.groupby('Index'):
    group = group.sort_values('Date')
    
    # Check start date
    start_date = group['Date'].min()
    if start_date > pd.Timestamp('2000-12-31'):
        continue # Exclude indices that didn't start in 2000

    # Simulate monthly investment
    investment_per_month = 1.0
    units_bought = investment_per_month / group['CloseUSD']
    total_units = units_bought.sum()
    total_invested = len(group) * investment_per_month
    
    # Final value
    last_price = group['CloseUSD'].iloc[-1]
    final_value = total_units * last_price
    
    overall_return = (final_value - total_invested) / total_invested
    
    results.append({
        'Index': index_name,
        'Return': overall_return
    })

results_df = pd.DataFrame(results)
top_5 = results_df.sort_values('Return', ascending=False).head(5)

# Mapping dictionary
index_mapping = {
    "NYA": "USA", 
    "IXIC": "USA", 
    "HSI": "Hong Kong", 
    "000001.SS": "China", 
    "N225": "Japan", 
    "399001.SZ": "China", 
    "GSPTSE": "Canada", 
    "NSEI": "India", 
    "GDAXI": "Germany", 
    "SSMI": "Switzerland", 
    "TWII": "Taiwan", 
    "J203.JO": "South Africa", 
    "N100": "Europe" 
}

top_5['Country'] = top_5['Index'].map(index_mapping)

print("__RESULT__:")
print(top_5[['Index', 'Country', 'Return']].to_json(orient='records'))"""

env_args = {'var_function-call-7463530722576996683': ['index_info'], 'var_function-call-7463530722576994424': ['index_trade'], 'var_function-call-5165717859289830406': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}], 'var_function-call-5165717859289831787': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_function-call-16432162134560375367': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_function-call-8074681657804701164': [{'Date': '31 Dec 1986, 00:00'}, {'Date': 'January 02, 1987 at 12:00 AM'}, {'Date': '1987-01-05 00:00:00'}, {'Date': '06 Jan 1987, 00:00'}, {'Date': '07 Jan 1987, 00:00'}, {'Date': '1987-01-08 00:00:00'}, {'Date': '1987-01-09 00:00:00'}, {'Date': '1987-01-12 00:00:00'}, {'Date': '1987-01-13 00:00:00'}, {'Date': '1987-01-14 00:00:00'}, {'Date': 'January 15, 1987 at 12:00 AM'}, {'Date': 'January 16, 1987 at 12:00 AM'}, {'Date': 'January 19, 1987 at 12:00 AM'}, {'Date': '20 Jan 1987, 00:00'}, {'Date': 'January 21, 1987 at 12:00 AM'}, {'Date': '22 Jan 1987, 00:00'}, {'Date': 'January 23, 1987 at 12:00 AM'}, {'Date': 'January 26, 1987 at 12:00 AM'}, {'Date': '27 Jan 1987, 00:00'}, {'Date': 'January 28, 1987 at 12:00 AM'}], 'var_function-call-10280706891561696089': [{'count_star()': '104224'}], 'var_function-call-405685236303482527': 'file_storage/function-call-405685236303482527.json', 'var_function-call-9360015107115766469': [{'Index': 'IXIC', 'Country': 'USA', 'Return': 3.8783345832}, {'Index': '399001.SZ', 'Country': 'China', 'Return': 1.3754081239}, {'Index': 'TWII', 'Country': 'Taiwan', 'Return': 1.3189250583}, {'Index': 'GDAXI', 'Country': 'Germany', 'Return': 1.3189242464}, {'Index': 'NSEI', 'Country': 'India', 'Return': 1.2148510451}], 'var_function-call-3073113079127604335': [{'Index': 'IXIC', 'Return': 3.8783345832, 'FirstPrice': 4131.149902, 'LastPrice': 13895.12012, 'Count': 257, 'StartDate': '2000-01-03 00:00:00', 'EndDate': '2021-05-03 00:00:00'}, {'Index': '399001.SZ', 'Return': 1.3754081239, 'FirstPrice': 559.52960944, 'LastPrice': 2405.5648432, 'Count': 258, 'StartDate': '2000-01-04 00:00:00', 'EndDate': '2021-06-01 00:00:00'}, {'Index': 'TWII', 'Return': 1.3189250583, 'FirstPrice': 350.2619922, 'LastPrice': 688.8939844, 'Count': 257, 'StartDate': '2000-01-04 00:00:00', 'EndDate': '2021-05-03 00:00:00'}, {'Index': 'GDAXI', 'Return': 1.3189242464, 'FirstPrice': 8235.92691452, 'LastPrice': 18588.4930706, 'Count': 257, 'StartDate': '2000-01-03 00:00:00', 'EndDate': '2021-05-03 00:00:00'}, {'Index': 'NSEI', 'Return': 1.2148510451, 'FirstPrice': 44.94649902, 'LastPrice': 146.3415039, 'Count': 165, 'StartDate': '2007-09-17 00:00:00', 'EndDate': '2021-05-03 00:00:00'}, {'Index': 'N225', 'Return': 1.1508683946, 'FirstPrice': 190.0285938, 'LastPrice': 288.1433984, 'Count': 258, 'StartDate': '2000-01-04 00:00:00', 'EndDate': '2021-06-01 00:00:00'}, {'Index': 'NYA', 'Return': 0.987024638, 'FirstPrice': 6762.109863, 'LastPrice': 16325.24023, 'Count': 257, 'StartDate': '2000-01-03 00:00:00', 'EndDate': '2021-05-03 00:00:00'}, {'Index': 'GSPTSE', 'Return': 0.6848056068, 'FirstPrice': 6808.15767547, 'LastPrice': 15946.9553526, 'Count': 257, 'StartDate': '2000-01-04 00:00:00', 'EndDate': '2021-05-03 00:00:00'}, {'Index': 'N100', 'Return': 0.6061880273, 'FirstPrice': 1216.0594244, 'LastPrice': 1535.46754632, 'Count': 258, 'StartDate': '2000-01-03 00:00:00', 'EndDate': '2021-06-01 00:00:00'}, {'Index': '000001.SS', 'Return': 0.5636191397, 'FirstPrice': 225.01935552, 'LastPrice': 550.60480464, 'Count': 257, 'StartDate': '2000-01-04 00:00:00', 'EndDate': '2021-05-06 00:00:00'}, {'Index': 'HSI', 'Return': 0.5612315407, 'FirstPrice': 2258.0520118, 'LastPrice': 3686.4800778, 'Count': 257, 'StartDate': '2000-01-03 00:00:00', 'EndDate': '2021-05-03 00:00:00'}, {'Index': 'SSMI', 'Return': 0.5452807226, 'FirstPrice': 8067.59110878, 'LastPrice': 12342.09, 'Count': 257, 'StartDate': '2000-01-04 00:00:00', 'EndDate': '2021-05-03 00:00:00'}, {'Index': 'J203.JO', 'Return': 0.3468497741, 'FirstPrice': 2395.8711329, 'LastPrice': 4661.0369533, 'Count': 112, 'StartDate': '2012-02-08 00:00:00', 'EndDate': '2021-05-03 00:00:00'}]}

exec(code, env_args)
