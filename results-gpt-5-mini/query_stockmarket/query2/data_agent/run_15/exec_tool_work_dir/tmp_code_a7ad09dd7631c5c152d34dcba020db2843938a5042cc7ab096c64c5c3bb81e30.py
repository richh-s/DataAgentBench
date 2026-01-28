code = """import json
etf_symbols = json.load(open(var_call_vx11m3QWslYyh6hwWLDiNRzH))
trade_tables = json.load(open(var_call_7SX4OTiie9zyF0VBnTgJFMJl))
common = sorted([s for s in etf_symbols if s in trade_tables])
# batch size
batch_size = 200
sql_list = []
for i in range(0, len(common), batch_size):
    batch = common[i:i+batch_size]
    parts = []
    for s in batch:
        parts.append("SELECT '{sym}' AS Symbol, MAX(\"Adj Close\") AS max_adj FROM \"{sym}\" WHERE \"Date\" BETWEEN '2015-01-01' AND '2015-12-31'".format(sym=s))
    union_sql = " UNION ALL ".join(parts)
    wrapped = "SELECT Symbol, max_adj FROM ( {} ) WHERE max_adj > 200 ORDER BY Symbol;".format(union_sql)
    sql_list.append(wrapped)
output = {"num_batches": len(sql_list), "batch_size": batch_size, "sql_list": sql_list}
print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_Sl50zQtw5dxdaDLjE4E9ejzh': ['stockinfo'], 'var_call_l7OaIGTJy1Lsdgg6paZF0Mtd': 'file_storage/call_l7OaIGTJy1Lsdgg6paZF0Mtd.json', 'var_call_vx11m3QWslYyh6hwWLDiNRzH': 'file_storage/call_vx11m3QWslYyh6hwWLDiNRzH.json', 'var_call_7SX4OTiie9zyF0VBnTgJFMJl': 'file_storage/call_7SX4OTiie9zyF0VBnTgJFMJl.json', 'var_call_r6sc3gyUY0F5Khf1D1m5tPuc': {'len_a': 1435, 'len_b': 2753}, 'var_call_GVFnjyJlGo5ttNdq95XlWGcV': {'count_common': 1435, 'sample_common_first_50': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY', 'AGG', 'AGGP', 'AGGY', 'AGQ', 'AGZ', 'AIEQ', 'AIIQ', 'AMLP', 'AMOM', 'AMZA', 'AOA', 'AOK', 'AOM', 'AOR', 'ARGT', 'ARKF', 'ARKK', 'ARKW', 'ARMR', 'ASEA', 'ASHR', 'ASHS', 'ASHX', 'AUSF', 'AVDE', 'AVDV', 'AVEM', 'AVUS', 'AVUV', 'AWAY', 'AWTM', 'AXJL', 'BAB', 'BATT', 'BBC', 'BBP', 'BCD', 'BCI', 'BDCY', 'BDRY']}}

exec(code, env_args)
