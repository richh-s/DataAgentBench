code = """import pandas as pd
import json

# Load the data from the previous step
with open('var_function-call-15630352595722189252.json', 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Parse Date
# The dates are mixed format, but pd.to_datetime should handle them with format='mixed' or letting it infer (default behavior is usually good enough or use dateutil parser)
# pd.to_datetime in newer pandas versions has format='mixed'
df['Date'] = pd.to_datetime(df['Date'], format='mixed')

# Filter since 2020
df_filtered = df[df['Date'] >= '2020-01-01'].copy()

# Calculate volatility
# (High - Low) / Open
df_filtered['Volatility'] = (df_filtered['High'] - df_filtered['Low']) / df_filtered['Open']

# Group by Index and calculate mean volatility
result_df = df_filtered.groupby('Index')['Volatility'].mean().reset_index()
result_df = result_df.sort_values(by='Volatility', ascending=False)

print("__RESULT__:")
print(result_df.to_json(orient='records'))"""

env_args = {'var_function-call-3358674454692697114': ['index_info'], 'var_function-call-3358674454692699745': ['index_trade'], 'var_function-call-14262991151733187178': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}], 'var_function-call-14262991151733187489': [{'Index': 'HSI', 'Date': '31 Dec 1986, 00:00', 'Open': '2568.300049', 'High': '2568.300049', 'Low': '2568.300049', 'Close': '2568.300049', 'Adj Close': '2568.300049', 'CloseUSD': '333.87900637'}, {'Index': 'HSI', 'Date': 'January 02, 1987 at 12:00 AM', 'Open': '2540.100098', 'High': '2540.100098', 'Low': '2540.100098', 'Close': '2540.100098', 'Adj Close': '2540.100098', 'CloseUSD': '330.21301274'}, {'Index': 'HSI', 'Date': '1987-01-05 00:00:00', 'Open': '2552.399902', 'High': '2552.399902', 'Low': '2552.399902', 'Close': '2552.399902', 'Adj Close': '2552.399902', 'CloseUSD': '331.81198726'}, {'Index': 'HSI', 'Date': '06 Jan 1987, 00:00', 'Open': '2583.899902', 'High': '2583.899902', 'Low': '2583.899902', 'Close': '2583.899902', 'Adj Close': '2583.899902', 'CloseUSD': '335.90698726000005'}, {'Index': 'HSI', 'Date': '07 Jan 1987, 00:00', 'Open': '2607.100098', 'High': '2607.100098', 'Low': '2607.100098', 'Close': '2607.100098', 'Adj Close': '2607.100098', 'CloseUSD': '338.92301274'}, {'Index': 'HSI', 'Date': '1987-01-08 00:00:00', 'Open': '2603.300049', 'High': '2603.300049', 'Low': '2603.300049', 'Close': '2603.300049', 'Adj Close': '2603.300049', 'CloseUSD': '338.42900637'}, {'Index': 'HSI', 'Date': '1987-01-09 00:00:00', 'Open': '2561.699951', 'High': '2561.699951', 'Low': '2561.699951', 'Close': '2561.699951', 'Adj Close': '2561.699951', 'CloseUSD': '333.02099363'}, {'Index': 'HSI', 'Date': '1987-01-12 00:00:00', 'Open': '2614.899902', 'High': '2614.899902', 'Low': '2614.899902', 'Close': '2614.899902', 'Adj Close': '2614.899902', 'CloseUSD': '339.93698726'}, {'Index': 'HSI', 'Date': '1987-01-13 00:00:00', 'Open': '2590.800049', 'High': '2590.800049', 'Low': '2590.800049', 'Close': '2590.800049', 'Adj Close': '2590.800049', 'CloseUSD': '336.80400637'}, {'Index': 'HSI', 'Date': '1987-01-14 00:00:00', 'Open': '2578.199951', 'High': '2578.199951', 'Low': '2578.199951', 'Close': '2578.199951', 'Adj Close': '2578.199951', 'CloseUSD': '335.16599363'}], 'var_function-call-16946664369132183537': [{'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'J203.JO'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_function-call-478651197825511390': [{'Exchange': 'New York Stock Exchange'}, {'Exchange': 'NASDAQ'}, {'Exchange': 'Hong Kong Stock Exchange'}, {'Exchange': 'Shanghai Stock Exchange'}, {'Exchange': 'Tokyo Stock Exchange'}, {'Exchange': 'Euronext'}, {'Exchange': 'Shenzhen Stock Exchange'}, {'Exchange': 'Toronto Stock Exchange'}, {'Exchange': 'National Stock Exchange of India'}, {'Exchange': 'Frankfurt Stock Exchange'}, {'Exchange': 'Korea Exchange'}, {'Exchange': 'SIX Swiss Exchange'}, {'Exchange': 'Taiwan Stock Exchange'}, {'Exchange': 'Johannesburg Stock Exchange'}], 'var_function-call-16231026568693500653': [{'Index': 'HSI', 'Date': '02 Jan 2020, 00:00', 'Open': '28249.36914', 'High': '28543.51953', 'Low': '28245.9707', 'Close': '28543.51953', 'Adj Close': '28543.51953', 'CloseUSD': '3710.6575389'}, {'Index': 'HSI', 'Date': 'January 03, 2020 at 12:00 AM', 'Open': '28828.35938', 'High': '28883.30078', 'Low': '28428.16992', 'Close': '28451.5', 'Adj Close': '28451.5', 'CloseUSD': '3698.695'}, {'Index': 'HSI', 'Date': '06 Jan 2020, 00:00', 'Open': '28326.5', 'High': '28367.86914', 'Low': '28054.28906', 'Close': '28226.18945', 'Adj Close': '28226.18945', 'CloseUSD': '3669.4046285'}, {'Index': 'HSI', 'Date': '07 Jan 2020, 00:00', 'Open': '28352.67969', 'High': '28473.08008', 'Low': '28264.07031', 'Close': '28322.06055', 'Adj Close': '28322.06055', 'CloseUSD': '3681.8678715'}, {'Index': 'HSI', 'Date': '2020-01-08 00:00:00', 'Open': '27999.58008', 'High': '28198.60938', 'Low': '27857.73047', 'Close': '28087.91992', 'Adj Close': '28087.91992', 'CloseUSD': '3651.4295896'}], 'var_function-call-15630352595722189252': 'file_storage/function-call-15630352595722189252.json'}

exec(code, env_args)
