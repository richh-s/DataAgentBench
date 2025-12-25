code = """import pandas as pd
import json

# Load data
file_path = locals()['var_function-call-15093468966041299533']
with open(file_path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)
df['Adj Close'] = pd.to_numeric(df['Adj Close'], errors='coerce')
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df = df[df['Date'] >= '2000-01-01']

stats = df.groupby('Index')['Date'].agg(['min', 'max'])
print("__RESULT__:")
print(stats.to_json(date_format='iso'))"""

env_args = {'var_function-call-5293628446074717249': ['index_info'], 'var_function-call-5293628446074718162': ['index_trade'], 'var_function-call-4876716323590813781': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}], 'var_function-call-4876716323590814276': [{'Index': 'HSI', 'Date': '31 Dec 1986, 00:00', 'Open': '2568.300049', 'High': '2568.300049', 'Low': '2568.300049', 'Close': '2568.300049', 'Adj Close': '2568.300049', 'CloseUSD': '333.87900637'}, {'Index': 'HSI', 'Date': 'January 02, 1987 at 12:00 AM', 'Open': '2540.100098', 'High': '2540.100098', 'Low': '2540.100098', 'Close': '2540.100098', 'Adj Close': '2540.100098', 'CloseUSD': '330.21301274'}, {'Index': 'HSI', 'Date': '1987-01-05 00:00:00', 'Open': '2552.399902', 'High': '2552.399902', 'Low': '2552.399902', 'Close': '2552.399902', 'Adj Close': '2552.399902', 'CloseUSD': '331.81198726'}, {'Index': 'HSI', 'Date': '06 Jan 1987, 00:00', 'Open': '2583.899902', 'High': '2583.899902', 'Low': '2583.899902', 'Close': '2583.899902', 'Adj Close': '2583.899902', 'CloseUSD': '335.90698726000005'}, {'Index': 'HSI', 'Date': '07 Jan 1987, 00:00', 'Open': '2607.100098', 'High': '2607.100098', 'Low': '2607.100098', 'Close': '2607.100098', 'Adj Close': '2607.100098', 'CloseUSD': '338.92301274'}], 'var_function-call-15582080887316221947': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_function-call-15582080887316220318': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_function-call-15093468966041299533': 'file_storage/function-call-15093468966041299533.json', 'var_function-call-11609010243090065683': [{'Index': 'IXIC', 'ROI': 3.6752650453, 'Country': 'United States', 'ROI_Percent': 367.5265045255}, {'Index': '399001.SZ', 'ROI': 1.3677777544, 'Country': 'China', 'ROI_Percent': 136.7777754384}, {'Index': 'GDAXI', 'ROI': 1.3479710594, 'Country': 'Germany', 'ROI_Percent': 134.7971059433}, {'Index': 'NSEI', 'ROI': 1.341098543, 'Country': 'India', 'ROI_Percent': 134.1098542988}, {'Index': 'TWII', 'ROI': 1.2962878758, 'Country': 'Taiwan', 'ROI_Percent': 129.6287875761}]}

exec(code, env_args)
