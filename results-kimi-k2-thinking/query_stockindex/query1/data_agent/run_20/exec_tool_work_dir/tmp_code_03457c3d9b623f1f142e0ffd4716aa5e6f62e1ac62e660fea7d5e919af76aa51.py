code = """import json
import pandas as pd
from datetime import datetime
import re

# Read the full result from the file
file_path = '/home/user/.tmp/1d0b64f22dca4f41a3de2fead8aa8e7b.json'
with open(file_path, 'r') as f:
    trade_data = json.load(f)

print(f"Total records: {len(trade_data)}")
print(f"Sample records: {trade_data[:3]}")

# Clean the date formats - need to handle various date formats
def parse_date(date_str):
    # Try different date formats
    patterns = [
        (r'(\d{2})\s*(\w{3})\s*(\d{4,4})', '%d %b %Y'),
        (r'(\d{2})\s*(\w{4,9})\s*(\d{4,4})', '%d %B %Y'),
        (r'(\d{4,4})-(\d{2})-(\d{2})', '%Y-%m-%d'),
    ]
    
    date_str_clean = date_str.split(',')[0].split('at')[0].strip()
    
    for pattern, fmt in patterns:
        match = re.match(pattern, date_str_clean)
        if match:
            try:
                if fmt == '%d %b %Y':
                    day, month, year = match.groups()
                    return datetime.strptime(f"{day} {month} {year}", fmt).date()
                elif fmt == '%d %B %Y':
                    day, month, year = match.groups()
                    return datetime.strptime(f"{day} {month} {year}", fmt).date()
                elif fmt == '%Y-%m-%d':
                    year, month, day = match.groups()
                    return datetime.strptime(f"{year}-{month}-{day}", fmt).date()
            except:
                continue
    
    # Try direct parsing
    try:
        return datetime.strptime(date_str_clean, '%d %b %Y').date()
    except:
        pass
    
    try:
        return datetime.strptime(date_str_clean, '%Y-%m-%d').date()
    except:
        pass
    
    return None

# Process the data
df = pd.DataFrame(trade_data)

# Parse dates and filter for 2020 onwards
df['Date_parsed'] = df['Date'].apply(parse_date)
df['Year'] = df['Date_parsed'].apply(lambda x: x.year if x else None)

# Filter for 2020 onwards
df_filtered = df[(df['Year'] >= 2020) & (df['Date_parsed'].notna())].copy()

# Convert price columns to numeric
df_filtered['Open'] = pd.to_numeric(df_filtered['Open'], errors='coerce')
df_filtered['High'] = pd.to_numeric(df_filtered['High'], errors='coerce')
df_filtered['Low'] = pd.to_numeric(df_filtered['Low'], errors='coerce')
df_filtered['Close'] = pd.to_numeric(df_filtered['Close'], errors='coerce')

# Calculate intraday volatility (High - Low) / Open
df_filtered['Intraday_Volatility'] = (df_filtered['High'] - df_filtered['Low']) / df_filtered['Open']

# Group by index and calculate average intraday volatility
volatility_by_index = df_filtered.groupby('Index')['Intraday_Volatility'].mean().resetIndex()
volatility_by_index = volatility_by_index.sort_values('Intraday_Volatility', ascending=False)

print(f"Average intraday volatility by index:")
for _, row in volatility_by_index.iterrows():
    print(f"{row['Index']}: {row['Intraday_Volatility']:.6f}")

result = volatility_by_index.to_dict('records')"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.list_db:5': ['index_trade'], 'var_functions.query_db:6': [{'Index': 'HSI', 'Date': '31 Dec 1986, 00:00', 'Open': '2568.300049', 'High': '2568.300049', 'Low': '2568.300049', 'Close': '2568.300049', 'Adj Close': '2568.300049', 'CloseUSD': '333.87900637'}, {'Index': 'HSI', 'Date': 'January 02, 1987 at 12:00 AM', 'Open': '2540.100098', 'High': '2540.100098', 'Low': '2540.100098', 'Close': '2540.100098', 'Adj Close': '2540.100098', 'CloseUSD': '330.21301274'}, {'Index': 'HSI', 'Date': '1987-01-05 00:00:00', 'Open': '2552.399902', 'High': '2552.399902', 'Low': '2552.399902', 'Close': '2552.399902', 'Adj Close': '2552.399902', 'CloseUSD': '331.81198726'}, {'Index': 'HSI', 'Date': '06 Jan 1987, 00:00', 'Open': '2583.899902', 'High': '2583.899902', 'Low': '2583.899902', 'Close': '2583.899902', 'Adj Close': '2583.899902', 'CloseUSD': '335.90698726000005'}, {'Index': 'HSI', 'Date': '07 Jan 1987, 00:00', 'Open': '2607.100098', 'High': '2607.100098', 'Low': '2607.100098', 'Close': '2607.100098', 'Adj Close': '2607.100098', 'CloseUSD': '338.92301274'}, {'Index': 'HSI', 'Date': '1987-01-08 00:00:00', 'Open': '2603.300049', 'High': '2603.300049', 'Low': '2603.300049', 'Close': '2603.300049', 'Adj Close': '2603.300049', 'CloseUSD': '338.42900637'}, {'Index': 'HSI', 'Date': '1987-01-09 00:00:00', 'Open': '2561.699951', 'High': '2561.699951', 'Low': '2561.699951', 'Close': '2561.699951', 'Adj Close': '2561.699951', 'CloseUSD': '333.02099363'}, {'Index': 'HSI', 'Date': '1987-01-12 00:00:00', 'Open': '2614.899902', 'High': '2614.899902', 'Low': '2614.899902', 'Close': '2614.899902', 'Adj Close': '2614.899902', 'CloseUSD': '339.93698726'}, {'Index': 'HSI', 'Date': '1987-01-13 00:00:00', 'Open': '2590.800049', 'High': '2590.800049', 'Low': '2590.800049', 'Close': '2590.800049', 'Adj Close': '2590.800049', 'CloseUSD': '336.80400637'}, {'Index': 'HSI', 'Date': '1987-01-14 00:00:00', 'Open': '2578.199951', 'High': '2578.199951', 'Low': '2578.199951', 'Close': '2578.199951', 'Adj Close': '2578.199951', 'CloseUSD': '335.16599363'}, {'Index': 'HSI', 'Date': 'January 15, 1987 at 12:00 AM', 'Open': '2559.100098', 'High': '2559.100098', 'Low': '2559.100098', 'Close': '2559.100098', 'Adj Close': '2559.100098', 'CloseUSD': '332.68301274'}, {'Index': 'HSI', 'Date': 'January 16, 1987 at 12:00 AM', 'Open': '2542.600098', 'High': '2542.600098', 'Low': '2542.600098', 'Close': '2542.600098', 'Adj Close': '2542.600098', 'CloseUSD': '330.53801274'}, {'Index': 'HSI', 'Date': 'January 19, 1987 at 12:00 AM', 'Open': '2460.5', 'High': '2460.5', 'Low': '2460.5', 'Close': '2460.5', 'Adj Close': '2460.5', 'CloseUSD': '319.865'}, {'Index': 'HSI', 'Date': '20 Jan 1987, 00:00', 'Open': '2449.899902', 'High': '2449.899902', 'Low': '2449.899902', 'Close': '2449.899902', 'Adj Close': '2449.899902', 'CloseUSD': '318.48698726000003'}, {'Index': 'HSI', 'Date': 'January 21, 1987 at 12:00 AM', 'Open': '2533.899902', 'High': '2533.899902', 'Low': '2533.899902', 'Close': '2533.899902', 'Adj Close': '2533.899902', 'CloseUSD': '329.40698726000005'}, {'Index': 'HSI', 'Date': '22 Jan 1987, 00:00', 'Open': '2536.899902', 'High': '2536.899902', 'Low': '2536.899902', 'Close': '2536.899902', 'Adj Close': '2536.899902', 'CloseUSD': '329.79698726000004'}, {'Index': 'HSI', 'Date': 'January 23, 1987 at 12:00 AM', 'Open': '2499.399902', 'High': '2499.399902', 'Low': '2499.399902', 'Close': '2499.399902', 'Adj Close': '2499.399902', 'CloseUSD': '324.92198726000004'}, {'Index': 'HSI', 'Date': 'January 26, 1987 at 12:00 AM', 'Open': '2484.399902', 'High': '2484.399902', 'Low': '2484.399902', 'Close': '2484.399902', 'Adj Close': '2484.399902', 'CloseUSD': '322.97198726000005'}, {'Index': 'HSI', 'Date': '27 Jan 1987, 00:00', 'Open': '2524.0', 'High': '2524.0', 'Low': '2524.0', 'Close': '2524.0', 'Adj Close': '2524.0', 'CloseUSD': '328.12'}, {'Index': 'HSI', 'Date': 'January 28, 1987 at 12:00 AM', 'Open': '2553.300049', 'High': '2553.300049', 'Low': '2553.300049', 'Close': '2553.300049', 'Adj Close': '2553.300049', 'CloseUSD': '331.92900637'}], 'var_functions.query_db:8': [{'Index': 'HSI', 'Date': '02 Jan 2020, 00:00', 'Open': '28249.36914', 'High': '28543.51953', 'Low': '28245.9707', 'Close': '28543.51953', 'Adj Close': '28543.51953', 'CloseUSD': '3710.6575389'}, {'Index': 'HSI', 'Date': 'January 03, 2020 at 12:00 AM', 'Open': '28828.35938', 'High': '28883.30078', 'Low': '28428.16992', 'Close': '28451.5', 'Adj Close': '28451.5', 'CloseUSD': '3698.695'}, {'Index': 'HSI', 'Date': '06 Jan 2020, 00:00', 'Open': '28326.5', 'High': '28367.86914', 'Low': '28054.28906', 'Close': '28226.18945', 'Adj Close': '28226.18945', 'CloseUSD': '3669.4046285'}, {'Index': 'HSI', 'Date': '07 Jan 2020, 00:00', 'Open': '28352.67969', 'High': '28473.08008', 'Low': '28264.07031', 'Close': '28322.06055', 'Adj Close': '28322.06055', 'CloseUSD': '3681.8678715'}, {'Index': 'HSI', 'Date': '2020-01-08 00:00:00', 'Open': '27999.58008', 'High': '28198.60938', 'Low': '27857.73047', 'Close': '28087.91992', 'Adj Close': '28087.91992', 'CloseUSD': '3651.4295896'}, {'Index': 'HSI', 'Date': '09 Jan 2020, 00:00', 'Open': '28367.65039', 'High': '28561.0', 'Low': '28325.85938', 'Close': '28561.0', 'Adj Close': '28561.0', 'CloseUSD': '3712.93'}, {'Index': 'HSI', 'Date': '2020-01-10 00:00:00', 'Open': '28665.14063', 'High': '28665.14063', 'Low': '28504.26953', 'Close': '28638.19922', 'Adj Close': '28638.19922', 'CloseUSD': '3722.9658986'}, {'Index': 'HSI', 'Date': 'January 13, 2020 at 12:00 AM', 'Open': '28772.36914', 'High': '28971.40039', 'Low': '28671.83984', 'Close': '28954.93945', 'Adj Close': '28954.93945', 'CloseUSD': '3764.1421285'}, {'Index': 'HSI', 'Date': '2020-01-14 00:00:00', 'Open': '29149.5293', 'High': '29149.5293', 'Low': '28790.49023', 'Close': '28885.14063', 'Adj Close': '28885.14063', 'CloseUSD': '3755.0682819'}, {'Index': 'HSI', 'Date': '15 Jan 2020, 00:00', 'Open': '28891.07031', 'High': '28972.67969', 'Low': '28619.09961', 'Close': '28773.58984', 'Adj Close': '28773.58984', 'CloseUSD': '3740.5666792'}, {'Index': 'HSI', 'Date': '2020-01-16 00:00:00', 'Open': '28806.11914', 'High': '28987.73047', 'Low': '28709.57031', 'Close': '28883.03906', 'Adj Close': '28883.03906', 'CloseUSD': '3754.7950778'}, {'Index': 'HSI', 'Date': '2020-01-17 00:00:00', 'Open': '28988.16016', 'High': '29101.15039', 'Low': '28813.13086', 'Close': '29056.41992', 'Adj Close': '29056.41992', 'CloseUSD': '3777.3345896'}, {'Index': 'HSI', 'Date': '2020-01-20 00:00:00', 'Open': '29169.11914', 'High': '29174.91992', 'Low': '28795.41992', 'Close': '28795.91016', 'Adj Close': '28795.91016', 'CloseUSD': '3743.4683208'}, {'Index': 'HSI', 'Date': 'January 21, 2020 at 12:00 AM', 'Open': '28449.38086', 'High': '28492.0293', 'Low': '27980.5', 'Close': '27985.33008', 'Adj Close': '27985.33008', 'CloseUSD': '3638.0929104'}, {'Index': 'HSI', 'Date': '2020-01-22 00:00:00', 'Open': '28116.5', 'High': '28393.92969', 'Low': '27937.67969', 'Close': '28341.03906', 'Adj Close': '28341.03906', 'CloseUSD': '3684.3350778'}, {'Index': 'HSI', 'Date': '2020-01-23 00:00:00', 'Open': '28109.75', 'High': '28133.0293', 'Low': '27706.36914', 'Close': '27909.11914', 'Adj Close': '27909.11914', 'CloseUSD': '3628.1854882'}, {'Index': 'HSI', 'Date': '24 Jan 2020, 00:00', 'Open': '27935.41992', 'High': '27977.63086', 'Low': '27774.5', 'Close': '27949.64063', 'Adj Close': '27949.64063', 'CloseUSD': '3633.453281900001'}, {'Index': 'HSI', 'Date': '29 Jan 2020, 00:00', 'Open': '27101.53906', 'High': '27333.30078', 'Low': '27101.53906', 'Close': '27160.63086', 'Adj Close': '27160.63086', 'CloseUSD': '3530.8820118000003'}, {'Index': 'HSI', 'Date': '30 Jan 2020, 00:00', 'Open': '27030.60938', 'High': '27134.55078', 'Low': '26330.05078', 'Close': '26449.13086', 'Adj Close': '26449.13086', 'CloseUSD': '3438.3870118000004'}, {'Index': 'HSI', 'Date': '31 Jan 2020, 00:00', 'Open': '26757.60938', 'High': '26818.83984', 'Low': '26295.49023', 'Close': '26312.63086', 'Adj Close': '26312.63086', 'CloseUSD': '3420.6420118'}], 'var_functions.query_db:10': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_functions.query_db:12': [{'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': '000001.SS'}, {'Index': 'TWII'}, {'Index': '399001.SZ'}, {'Index': 'HSI'}], 'var_functions.execute_python:16': ['N225', 'NSEI', '000001.SS', 'TWII', '399001.SZ', 'HSI'], 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json'}

exec(code, env_args)
