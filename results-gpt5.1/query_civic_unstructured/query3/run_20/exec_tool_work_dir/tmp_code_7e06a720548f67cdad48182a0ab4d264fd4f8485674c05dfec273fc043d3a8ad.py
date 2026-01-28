code = """import json

funding = var_call_ychSnGxEyD6LmutQmtue78yd

related_funding = []
for row in funding:
    name = row['Project_Name']
    lname = name.lower()
    if 'fema' in lname or 'emergency' in lname:
        amt = row['Amount']
        try:
            amt_int = int(amt)
        except Exception:
            amt_int = amt
        related_funding.append({
            'Project_Name': name,
            'Funding_Source': row['Funding_Source'],
            'Amount': amt_int,
            'Status': None
        })

print("__RESULT__:")
print(json.dumps(related_funding))"""

env_args = {'var_call_ychSnGxEyD6LmutQmtue78yd': 'file_storage/call_ychSnGxEyD6LmutQmtue78yd.json', 'var_call_ARKTxcuByEvIhdGRDlu4dikK': 'file_storage/call_ARKTxcuByEvIhdGRDlu4dikK.json'}

exec(code, env_args)
