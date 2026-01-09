code = """import json

def load_maybe_path(v):
    if isinstance(v, str):
        with open(v,'r') as f:
            return json.load(f)
    return v

data = load_maybe_path(var_call_6utPHfBorwslFay1JD1BUoPb)
tickers = data['tickers']

# Use sampling to identify candidates likely >200: those with price scale high (e.g., by checking last adj close in 2015-12-31?)
# Build queries in manageable chunks using query_table and max over 2015.
chunks = [tickers[i:i+200] for i in range(0, len(tickers), 200)]
queries = []
for ch in chunks:
    values = ','.join(["('{}')".format(t.replace("'","''")) for t in ch])
    q = "WITH etf(Symbol) AS (VALUES {vals})\nSELECT Symbol FROM etf WHERE (SELECT MAX(CAST(\"Adj Close\" AS DOUBLE)) FROM query_table(Symbol) WHERE Date >= '2015-01-01' AND Date <= '2015-12-31') > 200".format(vals=values)
    queries.append(q)

print('__RESULT__:')
print(json.dumps({'n_chunks': len(queries), 'q0': queries[0][:600]}))"""

env_args = {'var_call_8RGLkP0mxzDDo92o9BkQ9JLL': 'file_storage/call_8RGLkP0mxzDDo92o9BkQ9JLL.json', 'var_call_m60gBb32NxffOTEy9S0C09DP': 'file_storage/call_m60gBb32NxffOTEy9S0C09DP.json', 'var_call_6utPHfBorwslFay1JD1BUoPb': 'file_storage/call_6utPHfBorwslFay1JD1BUoPb.json', 'var_call_thm6ei54l0e6pFUuac5abObE': [{'table_name': 'AAAU'}, {'table_name': 'AADR'}, {'table_name': 'AAME'}, {'table_name': 'AAWW'}, {'table_name': 'AAXJ'}], 'var_call_qC68T4mkWIs1M9TjPg0r2y6E': [{'Symbol': 'ADP'}], 'var_call_sI5KrhXo2vVKANR33gfvsdUq': [], 'var_call_pzzuYZ9TXTlXoCvpfgD3UhkH': [{'Symbol': 'ACWV'}, {'Symbol': 'ACWX'}, {'Symbol': 'AGG'}], 'var_call_5MXoGG88wzEdffakB8LJauK0': [], 'var_call_ztSen5iuFgqp7glZ3tk9gbjb': {'n_tickers': 1435}, 'var_call_HiyTDhuDzkiqftBCMLHYCnmH': {'query_prefix': "WITH etf_symbols(Symbol) AS (VALUES ('AAAU'),('AADR'),('ABEQ'),('ACSG'),('ACWF'),('AFK'),('AFLG'),('AFMC'),('AFSM'),('AFTY'),('AGG'),('AGGP'),('AGGY'),('AGQ'),('AGZ'),('AIEQ'),('AIIQ'),('AMLP'),('AMOM'),('AMZA'),('AOA'),('AOK'),('AOM'),('AOR'),('ARGT'),('ARKF'),('ARKK'),('ARKW'),('ARMR'),('ASEA'),('ASHR'),('ASHS'),('ASHX'),('AUSF'),('AVDE'),('AVDV'),('AVEM'),('AVUS'),('AVUV'),('AWAY'),('AWTM'),('AXJL'),('BAB'),('BATT'),('BBC'),('BBP'),('BCD'),('BCI'),('BDCY'),('BDRY'),('BFOR'),('BIBL'),('BIL'),(", 'query_len': 12433}, 'var_call_IOSDQVTWw7VXUh63Rt8Zj0Jz': [{'max_adj_close': '193.3121490478516'}], 'var_call_k4zWrDdx2RnQtAME2aIRCwrO': [{'max_adj_close': '193.5270538330078'}], 'var_call_88pZs4XV8cOc7FPuRzV0KRcT': [{'max_adj_close': '131.44960021972656'}], 'var_call_58tfhpmUCfdxYafisG5xYrta': [{'max_adj_close': '263.76544189453125'}], 'var_call_kEUT0lg1p1v62wEFzh2DBR3y': [{'max_adj_close': '120.37349700927734'}], 'var_call_BTIoGybjhRudkhlykRCzvr0z': [{'Symbol': 'MDY'}], 'var_call_OXMFcaVwh890UrIov5ktwFj1': [{'Date': '1995-05-04', 'Open': '37.625', 'High': '37.625', 'Low': '37.421875', 'Close': '37.421875', 'Adj Close': '26.78282165527344', 'Volume': '55800'}, {'Date': '1995-05-05', 'Open': '37.25', 'High': '37.25', 'Low': '37.0', 'Close': '37.1875', 'Adj Close': '26.615079879760746', 'Volume': '3000'}]}

exec(code, env_args)
