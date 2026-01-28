code = """import json
path = var_call_kBDXU6MJ9TW2Y1JhZyEOJbWu
with open(path,'r') as f:
    d=json.load(f)
sym=d['batches'][0][:3]
selects=[]
col='"Adj Close"'
for s in sym:
    part = "SELECT '{s}' AS Symbol, MAX({col}) AS max_adj_close_2015 FROM \"{s}\" WHERE \"Date\" >= '2015-01-01' AND \"Date\" <= '2015-12-31'".format(s=s, col=col)
    selects.append(part)
q=' UNION ALL '.join(selects)
print('__RESULT__:')
print(json.dumps({'query': q, 'sym': sym}))"""

env_args = {'var_call_7un3cbfUYFXu1BEzO9lTedgP': ['stockinfo'], 'var_call_xPgeMOXLTvmuFt8SHsxsB5Pb': 'file_storage/call_xPgeMOXLTvmuFt8SHsxsB5Pb.json', 'var_call_IIzelB2aZqN6Arw9eX5Xcqia': 'file_storage/call_IIzelB2aZqN6Arw9eX5Xcqia.json', 'var_call_kBDXU6MJ9TW2Y1JhZyEOJbWu': 'file_storage/call_kBDXU6MJ9TW2Y1JhZyEOJbWu.json', 'var_call_N4UWuF7jXBwnPdv9C85BSF7W': {'query': "SELECT 'AAAU' AS Symbol, MAX(`Adj Close`) AS max_adj_close_2015 FROM `AAAU` WHERE `Date` >= '2015-01-01' AND `Date` <= '2015-12-31' UNION ALL SELECT 'AADR' AS Symbol, MAX(`Adj Close`) AS max_adj_close_2015 FROM `AADR` WHERE `Date` >= '2015-01-01' AND `Date` <= '2015-12-31' UNION ALL SELECT 'ABEQ' AS Symbol, MAX(`Adj Close`) AS max_adj_close_2015 FROM `ABEQ` WHERE `Date` >= '2015-01-01' AND `Date` <= '2015-12-31' UNION ALL SELECT 'ACSG' AS Symbol, MAX(`Adj Close`) AS max_adj_close_2015 FROM `ACSG` WHERE `Date` >= '2015-01-01' AND `Date` <= '2015-12-31' UNION ALL SELECT 'ACWF' AS Symbol, MAX(`Adj Close`) AS max_adj_close_2015 FROM `ACWF` WHERE `Date` >= '2015-01-01' AND `Date` <= '2015-12-31' UNION ALL SELECT 'AFK' AS Symbol, MAX(`Adj Close`) AS max_adj_close_2015 FROM `AFK` WHERE `Date` >= '2015-01-01' AND `Date` <= '2015-12-31' UNION ALL SELECT 'AFLG' AS Symbol, MAX(`Adj Close`) AS max_adj_close_2015 FROM `AFLG` WHERE `Date` >= '2015-01-01' AND `Date` <= '2015-12-31' UNION ALL SELECT 'AFMC' AS Symbol, MAX(`Adj Close`) AS max_adj_close_2015 FROM `AFMC` WHERE `Date` >= '2015-01-01' AND `Date` <= '2015-12-31' UNION ALL SELECT 'AFSM' AS Symbol, MAX(`Adj Close`) AS max_adj_close_2015 FROM `AFSM` WHERE `Date` >= '2015-01-01' AND `Date` <= '2015-12-31' UNION ALL SELECT 'AFTY' AS Symbol, MAX(`Adj Close`) AS max_adj_close_2015 FROM `AFTY` WHERE `Date` >= '2015-01-01' AND `Date` <= '2015-12-31'", 'symbols': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY']}, 'var_call_qVL5nIh2B8PkyhjRRN62Jr3l': 'test "Adj Close" ok'}

exec(code, env_args)
