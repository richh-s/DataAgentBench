code = """import json

stock_info_path = locals()['var_function-call-17865422632145074530']
trade_tables_path = locals()['var_function-call-14843570023963042041']

with open(stock_info_path, 'r') as f:
    stock_info = json.load(f)
nasdaq_capital_symbols = {item['Symbol'] for item in stock_info}

with open(trade_tables_path, 'r') as f:
    trade_tables = set(json.load(f))

valid_symbols = list(nasdaq_capital_symbols.intersection(trade_tables))

subqueries = []
for sym in valid_symbols:
    # Escape double quotes in symbol just in case, though usually symbols don't have them.
    safe_sym = sym.replace('"', '""')
    # Build query
    q = "SELECT '" + safe_sym + "' as Symbol, COUNT(*) as Count FROM \"" + safe_sym + "\" WHERE Date BETWEEN '2019-01-01' AND '2019-12-31' AND (High - Low) > 0.20 * Low"
    subqueries.append(q)

full_query = " UNION ALL ".join(subqueries)
final_query = "SELECT Symbol, Count FROM (" + full_query + ") ORDER BY Count DESC LIMIT 5"

print("__RESULT__:")
print(json.dumps(final_query))"""

env_args = {'var_function-call-17865422632145074530': 'file_storage/function-call-17865422632145074530.json', 'var_function-call-14843570023963042041': 'file_storage/function-call-14843570023963042041.json', 'var_function-call-14921926718025975657': {'count': 86, 'symbols': ['CBAT', 'MNPR', 'PCSB', 'BCLI', 'AMHC', 'MNCLU', 'SES', 'HRTX', 'BOTJ', 'CFFA', 'CLRB', 'IGIC', 'GLG', 'QRHC', 'FNCB', 'CPAAU', 'CPAH', 'GDYN', 'STKS', 'CFBK', 'PLIN', 'ORSNU', 'ISNS', 'VRRM', 'BWEN', 'NXTD', 'PBFS', 'HQI', 'BIOC', 'OPOF', 'PBTS', 'XPEL', 'HNNA', 'CDMOP', 'TMSR', 'PEIX', 'VMD', 'IDEX', 'CCCL', 'CORV', 'POPE', 'ORGO', 'MMAC', 'WHLR', 'CEMI', 'GTEC', 'CVV', 'VVPR', 'BKYI', 'MLND']}, 'var_function-call-1023783497759854650': [{'Date': '2005-02-14'}]}

exec(code, env_args)
