code = """import pandas as pd
import json

file_path = locals()['var_function-call-15839610252102377840']
with open(file_path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)
df['Date_Parsed'] = pd.to_datetime(df['Date'], errors='coerce')
df = df[df['Date_Parsed'] >= '2000-01-01']
df = df.sort_values(['Index', 'Date_Parsed'])
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'], errors='coerce')
df = df.dropna(subset=['CloseUSD'])

results = []
for idx, group in df.groupby('Index'):
    group = group.sort_values('Date_Parsed')
    if group['Date_Parsed'].iloc[0].year > 2000:
        continue
    group['Month'] = group['Date_Parsed'].dt.to_period('M')
    monthly = group.groupby('Month').first().reset_index()
    monthly['Units_Bought'] = 1.0 / monthly['CloseUSD']
    total_units = monthly['Units_Bought'].sum()
    total_invested = len(monthly)
    last_price = group['CloseUSD'].iloc[-1]
    final_value = total_units * last_price
    multiple = final_value / total_invested if total_invested > 0 else 0
    results.append({
        'Index': idx,
        'Multiple': multiple
    })

res_df = pd.DataFrame(results).sort_values('Multiple', ascending=False)
print("__RESULT__:")
print(json.dumps(res_df.to_dict(orient='records')))"""

env_args = {'var_function-call-18360343161845397000': ['index_info'], 'var_function-call-18360343161845398715': ['index_trade'], 'var_function-call-15998170493143971984': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}], 'var_function-call-15998170493143971577': [{'Index': 'J203.JO'}, {'Index': 'IXIC'}, {'Index': 'NYA'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'HSI'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_function-call-16188891357112266804': [{'Index': 'J203.JO', 'usd_count': '1854', 'adj_count': '1854', 'min_date': '2012-02-08 00:00:00', 'max_date': 'September 30, 2019 at 12:00 AM'}, {'Index': 'N225', 'usd_count': '7979', 'adj_count': '7979', 'min_date': '2000-01-04 00:00:00', 'max_date': 'September 30, 2020 at 12:00 AM'}, {'Index': 'GSPTSE', 'usd_count': '6506', 'adj_count': '6506', 'min_date': '2000-01-05 00:00:00', 'max_date': 'September 30, 2016 at 12:00 AM'}, {'Index': 'NSEI', 'usd_count': '2577', 'adj_count': '2577', 'min_date': '2007-09-25 00:00:00', 'max_date': 'September 30, 2014 at 12:00 AM'}, {'Index': 'GDAXI', 'usd_count': '5590', 'adj_count': '5590', 'min_date': '2000-01-05 00:00:00', 'max_date': 'September 30, 2016 at 12:00 AM'}, {'Index': 'IXIC', 'usd_count': '7351', 'adj_count': '7351', 'min_date': '2000-01-06 00:00:00', 'max_date': 'September 30, 2015 at 12:00 AM'}, {'Index': 'HSI', 'usd_count': '5604', 'adj_count': '5604', 'min_date': '2000-01-14 00:00:00', 'max_date': 'September 30, 2019 at 12:00 AM'}, {'Index': 'NYA', 'usd_count': '7960', 'adj_count': '7960', 'min_date': '2000-01-03 00:00:00', 'max_date': 'September 30, 2020 at 12:00 AM'}, {'Index': 'N100', 'usd_count': '4245', 'adj_count': '4245', 'min_date': '2000-01-10 00:00:00', 'max_date': 'September 30, 2019 at 12:00 AM'}, {'Index': '399001.SZ', 'usd_count': '4355', 'adj_count': '4355', 'min_date': '2000-01-05 00:00:00', 'max_date': 'September 30, 2015 at 12:00 AM'}, {'Index': '000001.SS', 'usd_count': '4354', 'adj_count': '4354', 'min_date': '2000-01-04 00:00:00', 'max_date': 'September 30, 2015 at 12:00 AM'}, {'Index': 'SSMI', 'usd_count': '5188', 'adj_count': '5188', 'min_date': '2000-01-05 00:00:00', 'max_date': 'September 30, 2020 at 12:00 AM'}, {'Index': 'TWII', 'usd_count': '4385', 'adj_count': '4385', 'min_date': '2000-01-17 00:00:00', 'max_date': 'September 30, 2020 at 12:00 AM'}], 'var_function-call-2242398351796785036': 'file_storage/function-call-2242398351796785036.json', 'var_function-call-15839610252102377840': 'file_storage/function-call-15839610252102377840.json', 'var_function-call-8013066965200397842': [{'Index': 'IXIC', 'Country': 'United States', 'Multiple': 4.675265045255041}, {'Index': '399001.SZ', 'Country': 'China', 'Multiple': 2.367753687239704}, {'Index': 'GDAXI', 'Country': 'Germany', 'Multiple': 2.3479710594327976}, {'Index': 'TWII', 'Country': 'Taiwan', 'Multiple': 2.296280572259542}, {'Index': 'N225', 'Country': 'Japan', 'Multiple': 2.1201609958018532}]}

exec(code, env_args)
