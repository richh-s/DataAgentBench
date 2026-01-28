code = """import json, pandas as pd, re

def load_records(maybe_path):
    if isinstance(maybe_path, str) and maybe_path.endswith('.json'):
        with open(maybe_path, 'r') as f:
            return json.load(f)
    return maybe_path

def parse_date(s):
    if s is None:
        return pd.NaT
    s=str(s)
    s=re.sub(r'\s+at\s+\d{1,2}:\d{2}\s+(AM|PM)\s*',' ',s)
    s=re.sub(r'\s+at\s+\d{1,2}:\d{2}:\d{2}\s*',' ',s)
    s=s.replace('00:00','')
    s=s.strip()
    return pd.to_datetime(s, errors='coerce')

asia_indices = {
    'N225': 'Japan (Tokyo Stock Exchange) - Nikkei 225',
    'TWII': 'Taiwan (Taiwan Stock Exchange) - TAIEX',
}

rows=[]
for idx in asia_indices:
    data = load_records(var_call_WSqGiYG2KXBiMbhn5uls4OF1 if idx=='N225' else var_call_LwYxfZjyAjVwJOK67TXQjy0b)
    df=pd.DataFrame(data)
    df['dt']=df['Date'].map(parse_date)
    df=df[df['dt']>=pd.Timestamp('2020-01-01')]
    for c in ['Open','High','Low']:
        df[c]=pd.to_numeric(df[c], errors='coerce')
    df=df.dropna(subset=['Open','High','Low'])
    df=df[df['Open']!=0]
    df['intraday_vol']=(df['High']-df['Low'])/df['Open']
    rows.append({'Index':idx,'days':int(df.shape[0]),'avg_intraday_vol':float(df['intraday_vol'].mean())})

res=sorted(rows, key=lambda x: x['avg_intraday_vol'], reverse=True)
print('__RESULT__:')
print(json.dumps(res))"""

env_args = {'var_call_Bd3juBN2NQZFyeVmWB1F45vQ': ['index_info'], 'var_call_kzTE364IS4JZuzVvapCZs3bA': ['index_trade'], 'var_call_b4OULgk8Dr1djgNy1jK8XyBa': [{'Index': '000001.SS', 'n': '5791', 'min_date': '01 Apr 2003, 00:00', 'max_date': 'September 30, 2015 at 12:00 AM'}, {'Index': '399001.SZ', 'n': '5760', 'min_date': '01 Apr 2004, 00:00', 'max_date': 'September 30, 2015 at 12:00 AM'}, {'Index': 'GDAXI', 'n': '8438', 'min_date': '01 Apr 1992, 00:00', 'max_date': 'September 30, 2016 at 12:00 AM'}, {'Index': 'GSPTSE', 'n': '10526', 'min_date': '01 Apr 1981, 00:00', 'max_date': 'September 30, 2016 at 12:00 AM'}, {'Index': 'HSI', 'n': '8492', 'min_date': '01 Apr 1992, 00:00', 'max_date': 'September 30, 2019 at 12:00 AM'}, {'Index': 'IXIC', 'n': '12690', 'min_date': '01 Apr 1974, 00:00', 'max_date': 'September 30, 2015 at 12:00 AM'}, {'Index': 'J203.JO', 'n': '2346', 'min_date': '01 Apr 2016, 00:00', 'max_date': 'September 30, 2019 at 12:00 AM'}, {'Index': 'N100', 'n': '5474', 'min_date': '01 Apr 2003, 00:00', 'max_date': 'September 30, 2019 at 12:00 AM'}, {'Index': 'N225', 'n': '13874', 'min_date': '01 Apr 1971, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM'}, {'Index': 'NSEI', 'n': '3346', 'min_date': '01 Apr 2014, 00:00', 'max_date': 'September 30, 2014 at 12:00 AM'}, {'Index': 'NYA', 'n': '13947', 'min_date': '01 Apr 1969, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM'}, {'Index': 'SSMI', 'n': '7671', 'min_date': '01 Apr 1996, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM'}, {'Index': 'TWII', 'n': '5869', 'min_date': '01 Apr 2004, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM'}], 'var_call_LTeScfm9ZIUGxqdRJ8qXDFgS': [{'Index': 'N225', 'Date': 'September 30, 2020 at 12:00 AM', 'Open': '23478.84961', 'High': '23522.38086', 'Low': '23170.89063', 'Close': '23185.11914'}, {'Index': 'N225', 'Date': 'September 30, 2011 at 12:00 AM', 'Open': '8713.910156', 'High': '8756.0', 'Low': '8653.620117', 'Close': '8700.290039'}, {'Index': 'N225', 'Date': 'September 30, 2010 at 12:00 AM', 'Open': '9554.830078', 'High': '9566.839844', 'Low': '9369.349609', 'Close': '9369.349609'}, {'Index': 'N225', 'Date': 'September 30, 2009 at 12:00 AM', 'Open': '10105.16992', 'High': '10138.04004', 'Low': '10063.69043', 'Close': '10133.23047'}, {'Index': 'N225', 'Date': 'September 30, 1993 at 12:00 AM', 'Open': '20097.60938', 'High': '20158.32031', 'Low': '20032.19922', 'Close': '20105.71094'}], 'var_call_jPffsP6SxsH0hgGG5XB1di7I': [{'Index': 'N225', 'Date': 'September 30, 2020 at 12:00 AM', 'dt': '2020-09-30 00:00:00'}, {'Index': 'N225', 'Date': 'September 30, 2011 at 12:00 AM', 'dt': '2011-09-30 00:00:00'}, {'Index': 'N225', 'Date': 'September 30, 2010 at 12:00 AM', 'dt': '2010-09-30 00:00:00'}, {'Index': 'N225', 'Date': 'September 30, 2009 at 12:00 AM', 'dt': '2009-09-30 00:00:00'}, {'Index': 'N225', 'Date': 'September 30, 1993 at 12:00 AM', 'dt': '1993-09-30 00:00:00'}], 'var_call_BU6KWcLQ79jawgRhLIpNQpwl': [{'Index': 'N225', 'Date': '06 Jan 2020, 00:00', 'Open': '23319.75977', 'High': '23365.35938', 'Low': '23148.5293'}, {'Index': 'N225', 'Date': '2020-01-07 00:00:00', 'Open': '23320.11914', 'High': '23577.43945', 'Low': '23299.91992'}, {'Index': 'N225', 'Date': 'January 08, 2020 at 12:00 AM', 'Open': '23217.49023', 'High': '23303.21094', 'Low': '22951.17969'}, {'Index': 'N225', 'Date': '09 Jan 2020, 00:00', 'Open': '23530.28906', 'High': '23767.08984', 'Low': '23506.15039'}, {'Index': 'N225', 'Date': 'January 10, 2020 at 12:00 AM', 'Open': '23813.2793', 'High': '23903.28906', 'Low': '23761.08008'}], 'var_call_GzR8wH2ruB93NNYZqm4SiAKv': [{'Index': 'N225', 'Date': '2021-01-04 00:00:00', 'Open': '27575.57031', 'High': '27602.10938', 'Low': '27042.32031'}, {'Index': 'N225', 'Date': '05 Jan 2021, 00:00', 'Open': '27151.38086', 'High': '27279.7793', 'Low': '27073.46094'}, {'Index': 'N225', 'Date': 'January 06, 2021 at 12:00 AM', 'Open': '27102.84961', 'High': '27196.40039', 'Low': '27002.17969'}, {'Index': 'N225', 'Date': 'January 07, 2021 at 12:00 AM', 'Open': '27340.46094', 'High': '27624.73047', 'Low': '27340.46094'}, {'Index': 'N225', 'Date': 'January 08, 2021 at 12:00 AM', 'Open': '27720.14063', 'High': '28139.0293', 'Low': '27667.75'}], 'var_call_BPdwem4G5rQbGovziNtKlijH': [], 'var_call_U7JxeoCSXOVmPkOOS88aWF3S': [{'Index': 'TWII', 'Date': 'September 30, 2020 at 12:00 AM', 'Open': '12483.65039', 'High': '12568.67969', 'Low': '12466.58008'}, {'Index': 'TWII', 'Date': 'September 30, 2014 at 12:00 AM', 'Open': '8954.580078', 'High': '8998.830078', 'Low': '8860.169922'}, {'Index': 'TWII', 'Date': 'September 30, 2011 at 12:00 AM', 'Open': '7222.160156', 'High': '7251.870117', 'Low': '7163.75'}], 'var_call_WSqGiYG2KXBiMbhn5uls4OF1': 'file_storage/call_WSqGiYG2KXBiMbhn5uls4OF1.json', 'var_call_LwYxfZjyAjVwJOK67TXQjy0b': 'file_storage/call_LwYxfZjyAjVwJOK67TXQjy0b.json'}

exec(code, env_args)
