code = """import re, json

funding = var_call_iXKQmSqNOtUStbPCKax21jbi
civics = var_call_lyic0f3E0crnxLpGiJSvd3FX

fund_fema_emerg = [r for r in funding if re.search(r'emergency|FEMA', r['Project_Name'], re.I)]

proj_names = {r['Project_Name'] for r in fund_fema_emerg}

result = []
for doc in civics:
    text = doc['text']
    for name in proj_names:
        if name in text:
            m = re.search(name + r".*?(design|completed|not started)", text, re.I|re.S)
            status = None
            if m:
                status = m.group(1).lower()
            for r in fund_fema_emerg:
                if r['Project_Name'] == name:
                    result.append({
                        'Project_Name': name,
                        'Funding_Source': r['Funding_Source'],
                        'Amount': int(r['Amount']),
                        'Status': status
                    })

if not result:
    for r in fund_fema_emerg:
        result.append({'Project_Name': r['Project_Name'], 'Funding_Source': r['Funding_Source'], 'Amount': int(r['Amount']), 'Status': None})

out = json.dumps(result, indent=2)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_iXKQmSqNOtUStbPCKax21jbi': 'file_storage/call_iXKQmSqNOtUStbPCKax21jbi.json', 'var_call_lyic0f3E0crnxLpGiJSvd3FX': 'file_storage/call_lyic0f3E0crnxLpGiJSvd3FX.json'}

exec(code, env_args)
