code = """import json
# load batches list
with open(var_call_bII4uSRXbc6KQ18RxRply5yP, 'r') as f:
    batches = json.load(f)
# we'll prepare SQL queries for the first 5 batches only to avoid too many parallel calls
sqls = []
for batch in batches[:5]:
    parts = []
    for s in batch:
        parts.append(f"SELECT '{s}' as symbol, MAX(\"Adj Close\") as mx FROM \"{s}\" WHERE Date >= '2015-01-01' AND Date <= '2015-12-31'")
    sqls.append('\nUNION ALL\n'.join(parts) + ';')
print('__RESULT__:')
print(json.dumps(sqls))"""

env_args = {'var_call_tIp3uAHrqYsL9oZ7Zyo00Eyv': 'file_storage/call_tIp3uAHrqYsL9oZ7Zyo00Eyv.json', 'var_call_F8SrY8Nb3ckIzQWbP6D1vZEC': 'file_storage/call_F8SrY8Nb3ckIzQWbP6D1vZEC.json', 'var_call_Ti97GwP3KOtpGVOK9UyyqFym': 'file_storage/call_Ti97GwP3KOtpGVOK9UyyqFym.json', 'var_call_fleuqoTcRdlTxC1s1Wpo03qp': [], 'var_call_WFKhPaQE3fWUL9rt0ddw9oha': [{'mx': '193.3121490478516'}], 'var_call_IbSibmaYFzUgWYpD9zmx1PVj': 1435, 'var_call_o2X5fuRhW3zaGP3lQwVNg9eZ': [{'symbol': 'AAAU', 'mx': 'nan'}], 'var_call_O4jEVBbOcWDMeJiclWK9nGnL': [{'symbol': 'AADR', 'mx': '39.58057403564453'}], 'var_call_dtyIT1TK1OkU8HRwr3ojaL5M': [{'symbol': 'ABEQ', 'mx': 'nan'}], 'var_call_xJW30sgLziWjoWOunk8EWaLQ': [{'symbol': 'ACSG', 'mx': 'nan'}], 'var_call_6roRiKVpzONvnEMdSoWDLfnY': [{'symbol': 'ACWF', 'mx': '23.251304626464844'}], 'var_call_b9EEwU36EcQk2Y8KOgk0x98j': [{'symbol': 'AFK', 'mx': '23.345184326171875'}], 'var_call_ck1ADEdJmsa5nHU3NDEep9rv': [{'symbol': 'AFLG', 'mx': 'nan'}], 'var_call_d5q0HVSw12dDMrSMc701SAPw': [{'symbol': 'AFMC', 'mx': 'nan'}], 'var_call_7eSEq7Bs1plIxGaLkfpzKW8t': [{'symbol': 'AFSM', 'mx': 'nan'}], 'var_call_BeSPsuJ3t12bA4U2VkhEqjHJ': [{'symbol': 'AFTY', 'mx': '18.35982131958008'}], 'var_call_bII4uSRXbc6KQ18RxRply5yP': 'file_storage/call_bII4uSRXbc6KQ18RxRply5yP.json'}

exec(code, env_args)
