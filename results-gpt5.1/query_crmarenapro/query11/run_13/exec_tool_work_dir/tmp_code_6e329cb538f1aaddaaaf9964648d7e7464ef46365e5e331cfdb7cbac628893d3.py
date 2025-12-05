code = """import json
from datetime import datetime

opps = var_call_BkyiVMA3UkbgJZkIqMcGPiqL
lines = var_call_7hwSa0IMQnt9a5JFCvz6dZi6
products = var_call_KGopMsJjJ109EYWoNwO85nsQ

cutoff = datetime.strptime('2021-07-15', '%Y-%m-%d').date()
start = datetime.strptime('2021-06-15', '%Y-%m-%d').date()

# find relevant opportunities in last month window
opp_dates = []
for o in opps:
    try:
        d = datetime.strptime(o['CloseDate'], '%Y-%m-%d').date()
    except Exception:
        continue
    if start <= d < cutoff:
        opp_dates.append(d)

if not opp_dates:
    result = None
else:
    last_date = max(opp_dates)
    # find product line items on that date
    candidates = [l['Product2Id'].lstrip('#') for l in lines if datetime.strptime(l['CloseDate'], '%Y-%m-%d').date() == last_date]
    # narrow to those that look like AI processing unit: choose product whose name suggests hardware/"CircuitAI" etc.
    id_to_name = {p['Id']: p['Name'].strip() for p in products}
    chosen = None
    for pid in candidates:
        name = id_to_name.get(pid)
        if not name:
            continue
        lname = name.lower()
        if 'circuit' in lname or 'processing' in lname or 'unit' in lname:
            chosen = pid
            break
    if not chosen and candidates:
        chosen = candidates[0]
    result = chosen

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_cW8aKFDWFmDlWTYWPEyLJE9L': [], 'var_call_BkyiVMA3UkbgJZkIqMcGPiqL': [{'Id': '#006Wt000007BIjxIAG', 'CloseDate': '2023-12-15'}, {'Id': '006Wt000007BInBIAW', 'CloseDate': '2022-06-20'}, {'Id': '006Wt000007BBx1IAG', 'CloseDate': '2021-11-01'}, {'Id': '006Wt000007B0g2IAC', 'CloseDate': '2021-06-15'}, {'Id': '006Wt000007B7TcIAK', 'CloseDate': '2021-06-15'}], 'var_call_7hwSa0IMQnt9a5JFCvz6dZi6': [{'Product2Id': '01tWt000006hVebIAE', 'CloseDate': '2023-12-15'}, {'Product2Id': '01tWt000006hUgwIAE', 'CloseDate': '2022-06-20'}, {'Product2Id': '01tWt000006hVgDIAU', 'CloseDate': '2022-06-20'}, {'Product2Id': '01tWt000006hV58IAE', 'CloseDate': '2021-11-01'}, {'Product2Id': '01tWt000006hV57IAE', 'CloseDate': '2021-11-01'}, {'Product2Id': '01tWt000006hVmfIAE', 'CloseDate': '2021-11-01'}, {'Product2Id': '01tWt000006hVY9IAM', 'CloseDate': '2021-11-01'}, {'Product2Id': '01tWt000006hV6jIAE', 'CloseDate': '2021-11-01'}, {'Product2Id': '01tWt000006hV8LIAU', 'CloseDate': '2021-11-01'}, {'Product2Id': '#01tWt000006hV8LIAU', 'CloseDate': '2021-06-15'}, {'Product2Id': '01tWt000006hTUkIAM', 'CloseDate': '2021-06-15'}, {'Product2Id': '01tWt000006hV8LIAU', 'CloseDate': '2021-06-15'}, {'Product2Id': '01tWt000006hV9xIAE', 'CloseDate': '2021-06-15'}], 'var_call_KGopMsJjJ109EYWoNwO85nsQ': [{'Id': '01tWt000006hUgwIAE', 'Name': 'AI DesignShift'}, {'Id': '01tWt000006hV8LIAU', 'Name': 'AI Cirku-Tech'}, {'Id': '01tWt000006hVI1IAM', 'Name': 'AIOptics Vision'}, {'Id': '01tWt000006hVMrIAM', 'Name': 'TrainEDU Suite'}, {'Id': '01tWt000006hVOTIA2', 'Name': 'UnitySim Essentials   '}, {'Id': '01tWt000006hVebIAE', 'Name': 'CircuitAI Innovator'}, {'Id': '01tWt000006hVjSIAU', 'Name': 'InnoTrain Hub'}]}

exec(code, env_args)
