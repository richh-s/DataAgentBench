code = """import json
import pandas as pd
from datetime import datetime

# Read the full data from the file
with open('/var/folders/7p/2q86b23n1lgffsj0qs1p5gpr0000gn/T/tmpschm3m3h.json', 'r') as f:
    price_data = json.load(f)

# Convert to DataFrame
df = pd.DataFrame(price_data)

# Parse dates (handle different formats)
def parse_date(date_str):
    try:
        return pd.to_datetime(date_str, format='%Y-%m-%d %H:%M:%S')
    except:
        try:
            return pd.to_datetime(date_str, format='%Y-%m-%d')
        except:
            return pd.to_datetime(date_str, errors='coerce')

df['Date'] = df['Date'].apply(parse_date)
df = df.dropna(subset=['Date'])

# Sort by Index and Date
df = df.sort_values(['Index', 'Date'])

# Filter from 2000 onwards
df = df[df['Date'] >= '2000-01-01']

# Convert CloseUSD to numeric
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'], errors='coerce')

# Remove rows with missing CloseUSD values
df = df.dropna(subset=['CloseUSD'])

# For each index, find the first trading day of each month
df['YearMonth'] = df['Date'].dt.to_period('M')

# Group by index and month to get the first trading day of each month
first_trading_days = df.groupby(['Index', 'YearMonth']).first().reset_index()

# Remove any data before 2000-01
first_trading_days = first_trading_days[first_trading_days['YearMonth'] >= pd.Period('2000-01', 'M')]

# Simulate monthly investment of $100 in each index
investment_per_month = 100
results = []

for index in first_trading_days['Index'].unique():
    index_data = first_trading_days[first_trading_days['Index'] == index].copy()
    index_data = index_data.sort_values('Date')
    
    # Calculate cumulative investment and shares
    index_data['Investment'] = investment_per_month
    index_data['Shares'] = investment_per_month / index_data['CloseUSD']
    index_data['Cumulative_Investment'] = index_data['Investment'].cumsum()
    index_data['Cumulative_Shares'] = index_data['Shares'].cumsum()
    
    # Get the final values
    final_investment = index_data['Cumulative_Investment'].iloc[-1]
    final_shares = index_data['Cumulative_Shares'].iloc[-1]
    final_price = index_data['CloseUSD'].iloc[-1]
    final_value = final_shares * final_price
    total_return = final_value - final_investment
    return_pct = (total_return / final_investment) * 100
    
    # Calculate number of months
    months_invested = len(index_data)
    
    results.append({
        'Index': index,
        'Total_Investment': final_investment,
        'Final_Value': final_value,
        'Total_Return': total_return,
        'Return_Percentage': return_pct,
        'Months_Invested': months_invested,
        'Final_Price': final_price,
        'Final_Shares': final_shares
    })

# Convert to DataFrame and sort by return percentage
results_df = pd.DataFrame(results)
results_df = results_df.sort_values('Return_Percentage', ascending=False)

print("Top 5 Indices by Return (Monthly $100 investment since 2000):")
print("="*70)
for i, row in results_df.head(5).iterrows():
    print(f"{row['Index']}: {row['Return_Percentage']:.2f}% return")
    print(f"  Invested: ${row['Total_Investment']:.2f}, Value: ${row['Final_Value']:.2f}")
    print(f"  Months: {row['Months_Invested']}")
    print()

__RESULT__:
print(json.dumps(results_df.head(5).to_dict('records')))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.query_db:3': [{'Index': 'HSI', 'Date': '31 Dec 1986, 00:00', 'Open': '2568.300049', 'High': '2568.300049', 'Low': '2568.300049', 'Close': '2568.300049', 'Adj Close': '2568.300049', 'CloseUSD': '333.87900637'}, {'Index': 'HSI', 'Date': 'January 02, 1987 at 12:00 AM', 'Open': '2540.100098', 'High': '2540.100098', 'Low': '2540.100098', 'Close': '2540.100098', 'Adj Close': '2540.100098', 'CloseUSD': '330.21301274'}, {'Index': 'HSI', 'Date': '1987-01-05 00:00:00', 'Open': '2552.399902', 'High': '2552.399902', 'Low': '2552.399902', 'Close': '2552.399902', 'Adj Close': '2552.399902', 'CloseUSD': '331.81198726'}, {'Index': 'HSI', 'Date': '06 Jan 1987, 00:00', 'Open': '2583.899902', 'High': '2583.899902', 'Low': '2583.899902', 'Close': '2583.899902', 'Adj Close': '2583.899902', 'CloseUSD': '335.90698726000005'}, {'Index': 'HSI', 'Date': '07 Jan 1987, 00:00', 'Open': '2607.100098', 'High': '2607.100098', 'Low': '2607.100098', 'Close': '2607.100098', 'Adj Close': '2607.100098', 'CloseUSD': '338.92301274'}, {'Index': 'HSI', 'Date': '1987-01-08 00:00:00', 'Open': '2603.300049', 'High': '2603.300049', 'Low': '2603.300049', 'Close': '2603.300049', 'Adj Close': '2603.300049', 'CloseUSD': '338.42900637'}, {'Index': 'HSI', 'Date': '1987-01-09 00:00:00', 'Open': '2561.699951', 'High': '2561.699951', 'Low': '2561.699951', 'Close': '2561.699951', 'Adj Close': '2561.699951', 'CloseUSD': '333.02099363'}, {'Index': 'HSI', 'Date': '1987-01-12 00:00:00', 'Open': '2614.899902', 'High': '2614.899902', 'Low': '2614.899902', 'Close': '2614.899902', 'Adj Close': '2614.899902', 'CloseUSD': '339.93698726'}, {'Index': 'HSI', 'Date': '1987-01-13 00:00:00', 'Open': '2590.800049', 'High': '2590.800049', 'Low': '2590.800049', 'Close': '2590.800049', 'Adj Close': '2590.800049', 'CloseUSD': '336.80400637'}, {'Index': 'HSI', 'Date': '1987-01-14 00:00:00', 'Open': '2578.199951', 'High': '2578.199951', 'Low': '2578.199951', 'Close': '2578.199951', 'Adj Close': '2578.199951', 'CloseUSD': '335.16599363'}, {'Index': 'HSI', 'Date': 'January 15, 1987 at 12:00 AM', 'Open': '2559.100098', 'High': '2559.100098', 'Low': '2559.100098', 'Close': '2559.100098', 'Adj Close': '2559.100098', 'CloseUSD': '332.68301274'}, {'Index': 'HSI', 'Date': 'January 16, 1987 at 12:00 AM', 'Open': '2542.600098', 'High': '2542.600098', 'Low': '2542.600098', 'Close': '2542.600098', 'Adj Close': '2542.600098', 'CloseUSD': '330.53801274'}, {'Index': 'HSI', 'Date': 'January 19, 1987 at 12:00 AM', 'Open': '2460.5', 'High': '2460.5', 'Low': '2460.5', 'Close': '2460.5', 'Adj Close': '2460.5', 'CloseUSD': '319.865'}, {'Index': 'HSI', 'Date': '20 Jan 1987, 00:00', 'Open': '2449.899902', 'High': '2449.899902', 'Low': '2449.899902', 'Close': '2449.899902', 'Adj Close': '2449.899902', 'CloseUSD': '318.48698726000003'}, {'Index': 'HSI', 'Date': 'January 21, 1987 at 12:00 AM', 'Open': '2533.899902', 'High': '2533.899902', 'Low': '2533.899902', 'Close': '2533.899902', 'Adj Close': '2533.899902', 'CloseUSD': '329.40698726000005'}, {'Index': 'HSI', 'Date': '22 Jan 1987, 00:00', 'Open': '2536.899902', 'High': '2536.899902', 'Low': '2536.899902', 'Close': '2536.899902', 'Adj Close': '2536.899902', 'CloseUSD': '329.79698726000004'}, {'Index': 'HSI', 'Date': 'January 23, 1987 at 12:00 AM', 'Open': '2499.399902', 'High': '2499.399902', 'Low': '2499.399902', 'Close': '2499.399902', 'Adj Close': '2499.399902', 'CloseUSD': '324.92198726000004'}, {'Index': 'HSI', 'Date': 'January 26, 1987 at 12:00 AM', 'Open': '2484.399902', 'High': '2484.399902', 'Low': '2484.399902', 'Close': '2484.399902', 'Adj Close': '2484.399902', 'CloseUSD': '322.97198726000005'}, {'Index': 'HSI', 'Date': '27 Jan 1987, 00:00', 'Open': '2524.0', 'High': '2524.0', 'Low': '2524.0', 'Close': '2524.0', 'Adj Close': '2524.0', 'CloseUSD': '328.12'}, {'Index': 'HSI', 'Date': 'January 28, 1987 at 12:00 AM', 'Open': '2553.300049', 'High': '2553.300049', 'Low': '2553.300049', 'Close': '2553.300049', 'Adj Close': '2553.300049', 'CloseUSD': '331.92900637'}, {'Index': 'HSI', 'Date': '02 Feb 1987, 00:00', 'Open': '2585.199951', 'High': '2585.199951', 'Low': '2585.199951', 'Close': '2585.199951', 'Adj Close': '2585.199951', 'CloseUSD': '336.07599363'}, {'Index': 'HSI', 'Date': '03 Feb 1987, 00:00', 'Open': '2606.399902', 'High': '2606.399902', 'Low': '2606.399902', 'Close': '2606.399902', 'Adj Close': '2606.399902', 'CloseUSD': '338.83198726'}, {'Index': 'HSI', 'Date': 'February 04, 1987 at 12:00 AM', 'Open': '2636.600098', 'High': '2636.600098', 'Low': '2636.600098', 'Close': '2636.600098', 'Adj Close': '2636.600098', 'CloseUSD': '342.75801274'}, {'Index': 'HSI', 'Date': 'February 05, 1987 at 12:00 AM', 'Open': '2672.399902', 'High': '2672.399902', 'Low': '2672.399902', 'Close': '2672.399902', 'Adj Close': '2672.399902', 'CloseUSD': '347.41198726000005'}, {'Index': 'HSI', 'Date': '06 Feb 1987, 00:00', 'Open': '2673.600098', 'High': '2673.600098', 'Low': '2673.600098', 'Close': '2673.600098', 'Adj Close': '2673.600098', 'CloseUSD': '347.56801274'}, {'Index': 'HSI', 'Date': '1987-02-09 00:00:00', 'Open': '2713.699951', 'High': '2713.699951', 'Low': '2713.699951', 'Close': '2713.699951', 'Adj Close': '2713.699951', 'CloseUSD': '352.78099363'}, {'Index': 'HSI', 'Date': '1987-02-10 00:00:00', 'Open': '2694.899902', 'High': '2694.899902', 'Low': '2694.899902', 'Close': '2694.899902', 'Adj Close': '2694.899902', 'CloseUSD': '350.33698726'}, {'Index': 'HSI', 'Date': '11 Feb 1987, 00:00', 'Open': '2739.5', 'High': '2739.5', 'Low': '2739.5', 'Close': '2739.5', 'Adj Close': '2739.5', 'CloseUSD': '356.135'}, {'Index': 'HSI', 'Date': '12 Feb 1987, 00:00', 'Open': '2754.699951', 'High': '2754.699951', 'Low': '2754.699951', 'Close': '2754.699951', 'Adj Close': '2754.699951', 'CloseUSD': '358.11099363'}, {'Index': 'HSI', 'Date': 'February 13, 1987 at 12:00 AM', 'Open': '2740.5', 'High': '2740.5', 'Low': '2740.5', 'Close': '2740.5', 'Adj Close': '2740.5', 'CloseUSD': '356.265'}, {'Index': 'HSI', 'Date': '16 Feb 1987, 00:00', 'Open': '2766.100098', 'High': '2766.100098', 'Low': '2766.100098', 'Close': '2766.100098', 'Adj Close': '2766.100098', 'CloseUSD': '359.59301274'}, {'Index': 'HSI', 'Date': 'February 17, 1987 at 12:00 AM', 'Open': '2792.100098', 'High': '2792.100098', 'Low': '2792.100098', 'Close': '2792.100098', 'Adj Close': '2792.100098', 'CloseUSD': '362.97301274'}, {'Index': 'HSI', 'Date': 'February 18, 1987 at 12:00 AM', 'Open': '2801.5', 'High': '2801.5', 'Low': '2801.5', 'Close': '2801.5', 'Adj Close': '2801.5', 'CloseUSD': '364.195'}, {'Index': 'HSI', 'Date': '19 Feb 1987, 00:00', 'Open': '2775.800049', 'High': '2775.800049', 'Low': '2775.800049', 'Close': '2775.800049', 'Adj Close': '2775.800049', 'CloseUSD': '360.85400637'}, {'Index': 'HSI', 'Date': '1987-02-20 00:00:00', 'Open': '2827.399902', 'High': '2827.399902', 'Low': '2827.399902', 'Close': '2827.399902', 'Adj Close': '2827.399902', 'CloseUSD': '367.56198726'}, {'Index': 'HSI', 'Date': 'February 23, 1987 at 12:00 AM', 'Open': '2879.0', 'High': '2879.0', 'Low': '2879.0', 'Close': '2879.0', 'Adj Close': '2879.0', 'CloseUSD': '374.27'}, {'Index': 'HSI', 'Date': '24 Feb 1987, 00:00', 'Open': '2848.199951', 'High': '2848.199951', 'Low': '2848.199951', 'Close': '2848.199951', 'Adj Close': '2848.199951', 'CloseUSD': '370.26599363'}, {'Index': 'HSI', 'Date': 'February 25, 1987 at 12:00 AM', 'Open': '2873.600098', 'High': '2873.600098', 'Low': '2873.600098', 'Close': '2873.600098', 'Adj Close': '2873.600098', 'CloseUSD': '373.56801274'}, {'Index': 'HSI', 'Date': '26 Feb 1987, 00:00', 'Open': '2843.600098', 'High': '2843.600098', 'Low': '2843.600098', 'Close': '2843.600098', 'Adj Close': '2843.600098', 'CloseUSD': '369.66801274'}, {'Index': 'HSI', 'Date': '27 Feb 1987, 00:00', 'Open': '2877.899902', 'High': '2877.899902', 'Low': '2877.899902', 'Close': '2877.899902', 'Adj Close': '2877.899902', 'CloseUSD': '374.12698726'}, {'Index': 'HSI', 'Date': '1987-03-02 00:00:00', 'Open': '2894.300049', 'High': '2894.300049', 'Low': '2894.300049', 'Close': '2894.300049', 'Adj Close': '2894.300049', 'CloseUSD': '376.25900637'}, {'Index': 'HSI', 'Date': '1987-03-03 00:00:00', 'Open': '2939.100098', 'High': '2939.100098', 'Low': '2939.100098', 'Close': '2939.100098', 'Adj Close': '2939.100098', 'CloseUSD': '382.08301274'}, {'Index': 'HSI', 'Date': '1987-03-04 00:00:00', 'Open': '2890.899902', 'High': '2890.899902', 'Low': '2890.899902', 'Close': '2890.899902', 'Adj Close': '2890.899902', 'CloseUSD': '375.81698726'}, {'Index': 'HSI', 'Date': 'March 05, 1987 at 12:00 AM', 'Open': '2798.399902', 'High': '2798.399902', 'Low': '2798.399902', 'Close': '2798.399902', 'Adj Close': '2798.399902', 'CloseUSD': '363.79198726'}, {'Index': 'HSI', 'Date': 'March 06, 1987 at 12:00 AM', 'Open': '2798.600098', 'High': '2798.600098', 'Low': '2798.600098', 'Close': '2798.600098', 'Adj Close': '2798.600098', 'CloseUSD': '363.81801274'}, {'Index': 'HSI', 'Date': '09 Mar 1987, 00:00', 'Open': '2820.399902', 'High': '2820.399902', 'Low': '2820.399902', 'Close': '2820.399902', 'Adj Close': '2820.399902', 'CloseUSD': '366.65198726000006'}, {'Index': 'HSI', 'Date': 'March 10, 1987 at 12:00 AM', 'Open': '2731.100098', 'High': '2731.100098', 'Low': '2731.100098', 'Close': '2731.100098', 'Adj Close': '2731.100098', 'CloseUSD': '355.04301274'}, {'Index': 'HSI', 'Date': '11 Mar 1987, 00:00', 'Open': '2760.899902', 'High': '2760.899902', 'Low': '2760.899902', 'Close': '2760.899902', 'Adj Close': '2760.899902', 'CloseUSD': '358.91698726000004'}, {'Index': 'HSI', 'Date': '12 Mar 1987, 00:00', 'Open': '2750.100098', 'High': '2750.100098', 'Low': '2750.100098', 'Close': '2750.100098', 'Adj Close': '2750.100098', 'CloseUSD': '357.51301274'}, {'Index': 'HSI', 'Date': 'March 13, 1987 at 12:00 AM', 'Open': '2721.199951', 'High': '2721.199951', 'Low': '2721.199951', 'Close': '2721.199951', 'Adj Close': '2721.199951', 'CloseUSD': '353.75599363000003'}], 'var_functions.query_db:7': [{'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'J203.JO'}, {'Index': 'IXIC'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'HSI'}, {'Index': 'N100'}, {'Index': '399001.SZ'}, {'Index': 'NYA'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:14': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}]}

exec(code, env_args)
