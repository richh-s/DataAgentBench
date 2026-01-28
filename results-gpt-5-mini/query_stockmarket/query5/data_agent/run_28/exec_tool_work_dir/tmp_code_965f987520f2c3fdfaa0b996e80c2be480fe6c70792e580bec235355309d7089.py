code = """import json
import pandas as pd

# helper to load storage entries (which may be file paths or objects)
def load_var(v):
    if isinstance(v, str):
        with open(v, 'r') as f:
            return json.load(f)
    return v

trade_data = load_var(var_call_6a4HNWmiN3vEvQ5lSVSoRg6q)
stockinfo = load_var(var_call_Y7rxCrvX6WVPPi3ugiwhDD9v)

# Create DataFrame
if not trade_data:
    df = pd.DataFrame(columns=['Symbol','Date','High','Low'])
else:
    df = pd.DataFrame(trade_data)

# Ensure numeric
for col in ['High','Low']:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')

# Filter valid lows > 0
df = df[df['Low'] > 0]

# Condition: (High - Low) > 0.20 * Low
df['range_exceed'] = (df['High'] - df['Low']) > 0.20 * df['Low']

# Count days per symbol where condition true
counts = df[df['range_exceed']].groupby('Symbol')['Date'].nunique().reset_index()
counts.columns = ['Symbol','Count']

# Include symbols with zero count (from the provided list)
all_symbols = var_call_RNtUR2Dw95vvEF5iEVlFDfA4
all_counts_df = pd.DataFrame({'Symbol': all_symbols})
all_counts_df = all_counts_df.merge(counts, on='Symbol', how='left').fillna(0)
all_counts_df['Count'] = all_counts_df['Count'].astype(int)

# Map symbol to company description
desc_map = {rec['Symbol']: rec.get('Company Description','') for rec in stockinfo}
all_counts_df['Company'] = all_counts_df['Symbol'].map(desc_map).fillna('')

# Get top 5 by Count, tie-break by Symbol
top5 = all_counts_df.sort_values(['Count','Symbol'], ascending=[False,True]).head(5)

result_list = top5['Company'].tolist()

# If company description empty, use symbol
for i,v in enumerate(result_list):
    if not v:
        result_list[i] = top5.iloc[i]['Symbol']

output = json.dumps(result_list)
print('__RESULT__:')
print(output)"""

env_args = {'var_call_Y7rxCrvX6WVPPi3ugiwhDD9v': 'file_storage/call_Y7rxCrvX6WVPPi3ugiwhDD9v.json', 'var_call_VuyiRNBM8CKaNAkawM6Ve5v7': 'file_storage/call_VuyiRNBM8CKaNAkawM6Ve5v7.json', 'var_call_RNtUR2Dw95vvEF5iEVlFDfA4': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL'], 'var_call_6a4HNWmiN3vEvQ5lSVSoRg6q': 'file_storage/call_6a4HNWmiN3vEvQ5lSVSoRg6q.json'}

exec(code, env_args)
