code = """import json
cases = var_call_QbMVvcU715w3J1dqSsMQN26B
accts = var_call_Cy0Qr4MA4ucEl4l6BULjsf1y
acct_by_clean = {c['accountid'].replace('#',''): float(c['avg_close_days']) for c in cases}
state_by_clean = {a['clean_id']: a['state'] for a in accts if a['state']}
state_times = {}
for aid, days in acct_by_clean.items():
    state = state_by_clean.get(aid)
    if not state:
        continue
    state_times.setdefault(state, []).append(days)
avg_by_state = {s: sum(v)/len(v) for s,v in state_times.items()}
state = min(avg_by_state, key=avg_by_state.get) if avg_by_state else None
result = json.dumps(state if state is not None else '')
print("__RESULT__:")
print(result)"""

env_args = {'var_call_QbMVvcU715w3J1dqSsMQN26B': [{'accountid': '#001Wt00000PGRnYIAX', 'avg_close_days': '0.00662037037037037'}, {'accountid': '001Wt00000PGtmwIAD', 'avg_close_days': '0.009560185185185185'}, {'accountid': '001Wt00000PGSwYIAX', 'avg_close_days': '0.010034722222222223'}, {'accountid': '001Wt00000PGb5MIAT', 'avg_close_days': '0.010763888888888889'}, {'accountid': '001Wt00000PGZmfIAH', 'avg_close_days': '0.011087962962962963'}, {'accountid': '001Wt00000PFsmcIAD', 'avg_close_days': '0.011655092592592592'}, {'accountid': '001Wt00000PHVqdIAH', 'avg_close_days': '0.012326388888888888'}, {'accountid': '001Wt00000PGdzxIAD', 'avg_close_days': '0.012476851851851852'}, {'accountid': '#001Wt00000PGZZoIAP', 'avg_close_days': '0.013726851851851851'}, {'accountid': '#001Wt00000PHVnNIAX', 'avg_close_days': '0.014988425925925926'}], 'var_call_Cy0Qr4MA4ucEl4l6BULjsf1y': [{'clean_id': '001Wt00000PGSwYIAX', 'state': 'IA'}, {'clean_id': '001Wt00000PGZmfIAH', 'state': 'MI'}, {'clean_id': '001Wt00000PGtmwIAD', 'state': 'IL'}, {'clean_id': '001Wt00000PHVqdIAH', 'state': 'CA'}]}

exec(code, env_args)
