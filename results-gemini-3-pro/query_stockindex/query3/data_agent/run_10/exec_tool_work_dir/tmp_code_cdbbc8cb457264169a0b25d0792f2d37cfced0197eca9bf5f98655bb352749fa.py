code = """import pandas as pd
import json

# Load data again (or use previous if persistence allowed, but usually separate calls need reload or careful management. The system says "All previous tool results are available as variables", so I can access variables if I assign them? No, the tool says "storage entries using the provided key names". But I need to parse dates again if I reload the raw file.
# To save time, I will read the file and parse dates for all indices again, but just to check min/max.

with open(locals()['var_function-call-14265084757085608486'], 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Re-apply simplified parsing for check
# I'll just look at the string dates first or try to parse min/max
# Actually, let's just parse fully again, it's safer.
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
stats = df.groupby('Index')['Date'].agg(['min', 'max', 'count'])
print("__RESULT__:")
print(stats.to_json(date_format='iso'))"""

env_args = {'var_function-call-12184386225509086772': ['index_info'], 'var_function-call-2651222669085114326': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}], 'var_function-call-6542151878181096001': ['index_trade'], 'var_function-call-14272459974564012930': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_function-call-468282391932724668': [{'Date': '31 Dec 1986, 00:00', 'Index': 'HSI', 'Adj Close': '2568.300049'}, {'Date': 'January 02, 1987 at 12:00 AM', 'Index': 'HSI', 'Adj Close': '2540.100098'}, {'Date': '1987-01-05 00:00:00', 'Index': 'HSI', 'Adj Close': '2552.399902'}, {'Date': '06 Jan 1987, 00:00', 'Index': 'HSI', 'Adj Close': '2583.899902'}, {'Date': '07 Jan 1987, 00:00', 'Index': 'HSI', 'Adj Close': '2607.100098'}], 'var_function-call-15222818763261342873': [{'count_star()': '104224'}], 'var_function-call-14265084757085608486': 'file_storage/function-call-14265084757085608486.json', 'var_function-call-8314388414536678480': [{'Index': 'IXIC', 'Return': 382.6943154204, 'Total_Invested': 257, 'Final_Value': 1240.5243906305, 'Country': 'United States'}, {'Index': 'NSEI', 'Return': 135.842734458, 'Total_Invested': 165, 'Final_Value': 389.1405118557, 'Country': 'India'}, {'Index': '399001.SZ', 'Return': 134.7487523496, 'Total_Invested': 258, 'Final_Value': 605.6517810619, 'Country': 'China'}, {'Index': 'GDAXI', 'Return': 134.7028715908, 'Total_Invested': 257, 'Final_Value': 603.1863799884, 'Country': 'Germany'}, {'Index': 'TWII', 'Return': 129.8207618672, 'Total_Invested': 257, 'Final_Value': 590.6393579988, 'Country': 'Taiwan'}]}

exec(code, env_args)
