code = """import json, pandas as pd, os
# load stockinfo to map symbols to company names
table_file = var_call_dkrKcwQT9rg1LAxzgWcAreHK
with open(table_file, 'r') as f:
    stockinfo = json.load(f)
stock_df = pd.DataFrame(stockinfo)

# top symbols
top = var_call_kWvj9CcuLXJb9VcfvUzpZbpS
symbols = [r['Symbol'] for r in top]

names = stock_df[stock_df['Symbol'].isin(symbols)][['Symbol', 'Company Description']]
merged = pd.merge(pd.DataFrame(top), names, on='Symbol', how='left')
# Extract company name as first part before period or comma
def extract_name(desc):
    if not isinstance(desc, str):
        return None
    for sep in ['.', ',']:
        if sep in desc:
            return desc.split(sep)[0].strip()
    return desc.strip()

merged['Company Name'] = merged['Company Description'].apply(extract_name)
result = merged[['Company Name']].to_dict(orient='list')['Company Name']
result_json = json.dumps(result)
print("__RESULT__:")
print(result_json)"""

env_args = {'var_call_s2uPdYaejgejFzJOxR2KtJjm': 'file_storage/call_s2uPdYaejgejFzJOxR2KtJjm.json', 'var_call_dkrKcwQT9rg1LAxzgWcAreHK': 'file_storage/call_dkrKcwQT9rg1LAxzgWcAreHK.json', 'var_call_UIhvbxgEIqIepnIVxvgXtPOU': 'file_storage/call_UIhvbxgEIqIepnIVxvgXtPOU.json', 'var_call_9cws8r3oXMPXd0pD3TZVUbIu': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL'], 'var_call_eWL5D26ST0rDYSsJNnrJi3Yg': 'file_storage/call_eWL5D26ST0rDYSsJNnrJi3Yg.json', 'var_call_kWvj9CcuLXJb9VcfvUzpZbpS': [{'Symbol': 'SES', 'Days': 51}, {'Symbol': 'GLG', 'Days': 42}, {'Symbol': 'TMSR', 'Days': 40}, {'Symbol': 'VERB', 'Days': 38}, {'Symbol': 'SNSS', 'Days': 32}]}

exec(code, env_args)
