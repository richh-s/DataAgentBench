code = """import json

def load_json(maybe_path_or_obj):
    if isinstance(maybe_path_or_obj, str) and maybe_path_or_obj.endswith('.json'):
        with open(maybe_path_or_obj,'r') as f:
            return json.load(f)
    return maybe_path_or_obj

etfs = load_json(var_call_HB4X7789w5RugKPxR8cyQbNE)
tables = set(load_json(var_call_IxW6haiTFueyDjZZpfh1Pko3))

arca_etf = sorted({r['Symbol'] for r in etfs if r.get('Symbol') in tables})

# Build duckdb SQL union
parts = []
for t in arca_etf:
    parts.append("SELECT '{t}' AS Symbol, MAX(\"Adj Close\") AS max_adj_close FROM \"{t}\" WHERE \"Date\" BETWEEN '2015-01-01' AND '2015-12-31'".format(t=t))

sql = "SELECT Symbol FROM (" + " UNION ALL ".join(parts) + ") WHERE max_adj_close > 200 ORDER BY Symbol;"

print('__RESULT__:')
print(json.dumps({"sql": sql, "n_arca_etf_with_tables": len(arca_etf)}))"""

env_args = {'var_call_IGFXHUnqBZxLEESlaW1VjsQS': ['stockinfo'], 'var_call_HB4X7789w5RugKPxR8cyQbNE': 'file_storage/call_HB4X7789w5RugKPxR8cyQbNE.json', 'var_call_IxW6haiTFueyDjZZpfh1Pko3': 'file_storage/call_IxW6haiTFueyDjZZpfh1Pko3.json', 'var_call_SbEU7E8vKUtf8YIKBmQDT6p9': 'ok', 'var_call_QJVNL104rt2NljWI4EsxMDNz': [], 'var_call_evWhunqq7cZzmI0uTpCnNl92': [{'symbol': 'SPY', 'max_adj_close': '193.3121490478516'}], 'var_call_Kc5frUohgrCwACulL7Thdm9K': []}

exec(code, env_args)
