code = """import json
# Load symbols list from storage file
path = var_call_pn9uL8oO0XhouUrL0WSnFI85
with open(path,'r') as f:
    symbols = json.load(f)
# Build SQL in chunks to avoid extremely long single SELECT? We'll create one big union
parts = []
for s in symbols:
    # ensure symbol is safe
    sym = s.replace('"','')
    part = f"SELECT '{sym}' AS Symbol, MAX(\"Adj Close\") AS max_adj FROM \"{sym}\" WHERE Date BETWEEN '2015-01-01' AND '2015-12-31'"
    parts.append(part)
sql = " UNION ALL ".join(parts)
sql_full = f"SELECT Symbol, max_adj FROM ( {sql} ) AS t WHERE max_adj > 200 ORDER BY Symbol;"
# Output the SQL string as JSON string
print("__RESULT__:")
print(json.dumps(sql_full))"""

env_args = {'var_call_CkOett6RT3NpMdVOnQ5Rdezm': 'file_storage/call_CkOett6RT3NpMdVOnQ5Rdezm.json', 'var_call_DSMBYKQmd3iXKyKYg6Sw5gVC': 'file_storage/call_DSMBYKQmd3iXKyKYg6Sw5gVC.json', 'var_call_pn9uL8oO0XhouUrL0WSnFI85': 'file_storage/call_pn9uL8oO0XhouUrL0WSnFI85.json', 'var_call_VzWYsN2RIz49f8fQuyJnsKO1': [{'cnt': '0'}], 'var_call_viQldcTHcTVJdLmrQFhyAd6b': [{'cnt': '0'}], 'var_call_4e22MSnOzmljdX3wSbK7yAEi': [{'cnt': '0'}], 'var_call_HXlDkIpKt2bJIZ5sFt1n5QLt': [{'cnt': '0'}], 'var_call_RArGQ2q7eeIvMLLjJ1dwWiv0': [{'cnt': '0'}], 'var_call_4hGv6nzwdbS3HFE6MQkg06GF': [{'cnt': '0'}], 'var_call_EprUCjn6cWqsoe0dVGAHItxR': [{'cnt': '0'}], 'var_call_WSl3Qtw19Z026tDiB80EzjH2': [{'cnt': '0'}], 'var_call_nHYPMMiMLS690VDxN0QlGHfz': [{'cnt': '0'}], 'var_call_9qx32aDt81uGVEWMQUdCBCEX': [{'cnt': '0'}], 'var_call_ZKKpgLDLBG3QhqN6AQ5xB6wQ': [{'cnt': '0'}]}

exec(code, env_args)
