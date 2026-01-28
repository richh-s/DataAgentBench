code = """import json

def load_maybe_path(v):
    if isinstance(v, str):
        with open(v,'r') as f:
            return json.load(f)
    return v

data = load_maybe_path(var_call_6utPHfBorwslFay1JD1BUoPb)
tickers = data['tickers']
values = ','.join(["('{}')".format(t.replace("'","''")) for t in tickers])

sql = """WITH etf_symbols(Symbol) AS (VALUES {values})
SELECT s.Symbol,
       (SELECT MAX(t."Adj Close")
          FROM (SELECT * FROM query_table(s.Symbol)) t) AS max_adj
FROM etf_symbols s
LIMIT 1;""".format(values=values)

print('__RESULT__:')
print(json.dumps({'sql': sql[:800], 'len': len(sql)}))"""

env_args = {'var_call_8RGLkP0mxzDDo92o9BkQ9JLL': 'file_storage/call_8RGLkP0mxzDDo92o9BkQ9JLL.json', 'var_call_m60gBb32NxffOTEy9S0C09DP': 'file_storage/call_m60gBb32NxffOTEy9S0C09DP.json', 'var_call_6utPHfBorwslFay1JD1BUoPb': 'file_storage/call_6utPHfBorwslFay1JD1BUoPb.json', 'var_call_thm6ei54l0e6pFUuac5abObE': [{'table_name': 'AAAU'}, {'table_name': 'AADR'}, {'table_name': 'AAME'}, {'table_name': 'AAWW'}, {'table_name': 'AAXJ'}], 'var_call_qC68T4mkWIs1M9TjPg0r2y6E': [{'Symbol': 'ADP'}], 'var_call_sI5KrhXo2vVKANR33gfvsdUq': [], 'var_call_pzzuYZ9TXTlXoCvpfgD3UhkH': [{'Symbol': 'ACWV'}, {'Symbol': 'ACWX'}, {'Symbol': 'AGG'}], 'var_call_5MXoGG88wzEdffakB8LJauK0': [], 'var_call_ztSen5iuFgqp7glZ3tk9gbjb': {'n_tickers': 1435}, 'var_call_HiyTDhuDzkiqftBCMLHYCnmH': {'query_prefix': "WITH etf_symbols(Symbol) AS (VALUES ('AAAU'),('AADR'),('ABEQ'),('ACSG'),('ACWF'),('AFK'),('AFLG'),('AFMC'),('AFSM'),('AFTY'),('AGG'),('AGGP'),('AGGY'),('AGQ'),('AGZ'),('AIEQ'),('AIIQ'),('AMLP'),('AMOM'),('AMZA'),('AOA'),('AOK'),('AOM'),('AOR'),('ARGT'),('ARKF'),('ARKK'),('ARKW'),('ARMR'),('ASEA'),('ASHR'),('ASHS'),('ASHX'),('AUSF'),('AVDE'),('AVDV'),('AVEM'),('AVUS'),('AVUV'),('AWAY'),('AWTM'),('AXJL'),('BAB'),('BATT'),('BBC'),('BBP'),('BCD'),('BCI'),('BDCY'),('BDRY'),('BFOR'),('BIBL'),('BIL'),(", 'query_len': 12433}, 'var_call_IOSDQVTWw7VXUh63Rt8Zj0Jz': [{'max_adj_close': '193.3121490478516'}], 'var_call_k4zWrDdx2RnQtAME2aIRCwrO': [{'max_adj_close': '193.5270538330078'}], 'var_call_88pZs4XV8cOc7FPuRzV0KRcT': [{'max_adj_close': '131.44960021972656'}], 'var_call_58tfhpmUCfdxYafisG5xYrta': [{'max_adj_close': '263.76544189453125'}], 'var_call_kEUT0lg1p1v62wEFzh2DBR3y': [{'max_adj_close': '120.37349700927734'}], 'var_call_BTIoGybjhRudkhlykRCzvr0z': [{'Symbol': 'MDY'}]}

exec(code, env_args)
