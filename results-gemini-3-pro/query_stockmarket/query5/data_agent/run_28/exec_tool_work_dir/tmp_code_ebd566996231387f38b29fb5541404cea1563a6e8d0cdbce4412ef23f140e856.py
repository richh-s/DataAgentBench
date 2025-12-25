code = """import json

stock_info_path = locals()['var_function-call-17865422632145074530']
trade_tables_path = locals()['var_function-call-14843570023963042041']

with open(stock_info_path, 'r') as f:
    stock_info = json.load(f)
nasdaq_capital_symbols = {item['Symbol'] for item in stock_info}

with open(trade_tables_path, 'r') as f:
    trade_tables = set(json.load(f))

valid_symbols = sorted(list(nasdaq_capital_symbols.intersection(trade_tables)))

# Split into 2 batches
mid = len(valid_symbols) // 2
batch1 = valid_symbols[:mid]
batch2 = valid_symbols[mid:]

queries = []
for batch in [batch1, batch2]:
    subqueries = []
    for sym in batch:
        safe_sym = sym.replace('"', '""')
        # Use format to avoid concatenation issues
        q = "SELECT '{0}' as Symbol, COUNT(*) as Count FROM \"{0}\" WHERE Date BETWEEN '2019-01-01' AND '2019-12-31' AND (High - Low) > 0.20 * Low".format(safe_sym)
        subqueries.append(q)
    
    full_query = " UNION ALL ".join(subqueries)
    # Wrap in a select to sort later? No, just get the counts. I'll merge in python.
    queries.append(full_query)

print("__RESULT__:")
print(json.dumps(queries))"""

env_args = {'var_function-call-17865422632145074530': 'file_storage/function-call-17865422632145074530.json', 'var_function-call-14843570023963042041': 'file_storage/function-call-14843570023963042041.json', 'var_function-call-14921926718025975657': {'count': 86, 'symbols': ['CBAT', 'MNPR', 'PCSB', 'BCLI', 'AMHC', 'MNCLU', 'SES', 'HRTX', 'BOTJ', 'CFFA', 'CLRB', 'IGIC', 'GLG', 'QRHC', 'FNCB', 'CPAAU', 'CPAH', 'GDYN', 'STKS', 'CFBK', 'PLIN', 'ORSNU', 'ISNS', 'VRRM', 'BWEN', 'NXTD', 'PBFS', 'HQI', 'BIOC', 'OPOF', 'PBTS', 'XPEL', 'HNNA', 'CDMOP', 'TMSR', 'PEIX', 'VMD', 'IDEX', 'CCCL', 'CORV', 'POPE', 'ORGO', 'MMAC', 'WHLR', 'CEMI', 'GTEC', 'CVV', 'VVPR', 'BKYI', 'MLND']}, 'var_function-call-1023783497759854650': [{'Date': '2005-02-14'}], 'var_function-call-4777611762486325786': 'file_storage/function-call-4777611762486325786.json', 'var_function-call-2502080008816667096': "SELECT Symbol, Count FROM (SELECT 'SHSP' as Symbol, COUNT(*) as Count FROM  + safe_sym +  WHERE Date BETWEEN '2019-01-01' AND '2019-12-31' AND (High - Low) > 0.20 * Low UNION ALL SELECT 'OPTT' as Symbol, COUNT(*) as Count FROM  + safe_sym +  WHERE Date BETWEEN '2019-01-01' AND '2019-12-31' AND (High - Low) > 0.20 * Low UNION ALL SELECT 'OPOF' as Symbol, COUNT(*) as Count FROM  + safe_sym +  WHERE Date BETWEEN '2019-01-01' AND '2019-12-31' AND (High - Low) > 0.20 * Low UNION ALL SELECT 'HRTX' as "}

exec(code, env_args)
