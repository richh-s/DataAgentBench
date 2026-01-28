code = """import json
with open(var_call_Ti97GwP3KOtpGVOK9UyyqFym, 'r') as f:
    symbols = json.load(f)

batch_size = 200
sqls = []
for i in range(0, len(symbols), batch_size):
    batch = symbols[i:i+batch_size]
    parts = []
    for s in batch:
        dq = chr(34)
        part = "SELECT '{}' as symbol, MAX({}Adj Close{}) as mx FROM {}{}{} WHERE Date >= '2015-01-01' AND Date <= '2015-12-31'".format(s, dq, dq, dq, s, dq)
        parts.append(part)
    sql = '\nUNION ALL\n'.join(parts) + ';'
    sqls.append(sql)
print('__RESULT__:')
print(json.dumps(sqls))"""

env_args = {'var_call_tIp3uAHrqYsL9oZ7Zyo00Eyv': 'file_storage/call_tIp3uAHrqYsL9oZ7Zyo00Eyv.json', 'var_call_F8SrY8Nb3ckIzQWbP6D1vZEC': 'file_storage/call_F8SrY8Nb3ckIzQWbP6D1vZEC.json', 'var_call_Ti97GwP3KOtpGVOK9UyyqFym': 'file_storage/call_Ti97GwP3KOtpGVOK9UyyqFym.json', 'var_call_fleuqoTcRdlTxC1s1Wpo03qp': [], 'var_call_WFKhPaQE3fWUL9rt0ddw9oha': [{'mx': '193.3121490478516'}], 'var_call_IbSibmaYFzUgWYpD9zmx1PVj': 1435}

exec(code, env_args)
