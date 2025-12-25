code = """import json
# use var_call_IyoK3TSjYGVRCFwvCXAwtbjN and var_call_k4trBdmY98zr9S1SazZnBe85
opp_lines = var_call_IyoK3TSjYGVRCFwvCXAwtbjN
products = var_call_k4trBdmY98zr9S1SazZnBe85

# We need last month's AI processing unit prior to 2021-07-15.
# "Last month" relative to 2021-07-15 is June 2021. Use CloseDate.
from datetime import datetime

cutoff = datetime.strptime('2021-07-15', '%Y-%m-%d')
start_last_month = datetime(2021,6,1)
end_last_month = datetime(2021,6,30)

# Filter opportunity line items in June 2021
lines_june = [l for l in opp_lines if start_last_month <= datetime.strptime(l['CloseDate'], '%Y-%m-%d') <= end_last_month]

# Build product lookup by normalized id
def norm(s):
    return s.replace('#','') if isinstance(s,str) else s

prod_by_id = {norm(p['Id']): p for p in products}

# Heuristic: AI processing unit likely has AI in name and sounds like hardware/processing
candidates = []
for l in lines_june:
    pid = norm(l['Product2Id'])
    p = prod_by_id.get(pid)
    if not p:
        continue
    name = p['Name'].strip()
    if 'AI' in name.upper() or 'AI ' in name.upper() or ' AI' in name.upper():
        candidates.append({'line': l, 'product': p})

# If no AI keyword match in June, fallback to any June product
if not candidates and lines_june:
    candidates = [{'line': lines_june[0], 'product': prod_by_id.get(norm(lines_june[0]['Product2Id']))}]

# If still none (no June purchases), look at latest before cutoff
if not candidates:
    before = [l for l in opp_lines if datetime.strptime(l['CloseDate'], '%Y-%m-%d') < cutoff]
    before.sort(key=lambda x: datetime.strptime(x['CloseDate'], '%Y-%m-%d'), reverse=True)
    for l in before:
        p = prod_by_id.get(norm(l['Product2Id']))
        if not p:
            continue
        name = p['Name'].strip()
        if 'AI' in name.upper():
            candidates.append({'line': l, 'product': p})
            break
    if not candidates and before:
        candidates = [{'line': before[0], 'product': prod_by_id.get(norm(before[0]['Product2Id']))}]

# Choose the first candidate as most relevant
product_id = None
if candidates:
    product_id = candidates[0]['product']['Id']

result = json.dumps(product_id)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_kooLQ72IzOiXbwE1wYE1lK9w': [{'Id': '#006Wt000007BIjxIAG', 'CloseDate': '2023-12-15'}, {'Id': '006Wt000007BInBIAW', 'CloseDate': '2022-06-20'}, {'Id': '006Wt000007BBx1IAG', 'CloseDate': '2021-11-01'}, {'Id': '006Wt000007B0g2IAC', 'CloseDate': '2021-06-15'}, {'Id': '006Wt000007B7TcIAK', 'CloseDate': '2021-06-15'}], 'var_call_k4trBdmY98zr9S1SazZnBe85': [{'Id': '01tWt000006hOd8IAE', 'Name': 'AutoLayout Master'}, {'Id': '01tWt000006hPffIAE', 'Name': 'DevVision IDE'}, {'Id': '01tWt000006hPfgIAE', 'Name': 'EcoPower Convert'}, {'Id': '01tWt000006hRfqIAE', 'Name': 'FlexiDesign Pro'}, {'Id': '01tWt000006hTUkIAM', 'Name': 'CloudLink Designer'}, {'Id': '01tWt000006hUKMIA2', 'Name': 'CryptGuard Module'}, {'Id': '#01tWt000006hUUwIAM', 'Name': 'SimuFlow Xtreme'}, {'Id': '01tWt000006hUgwIAE', 'Name': 'AI DesignShift'}, {'Id': '01tWt000006hUsEIAU', 'Name': 'SimuCheck Ultra'}, {'Id': '01tWt000006hUtqIAE', 'Name': 'SecureTrack Pro '}, {'Id': '01tWt000006hV0IIAU', 'Name': 'NextGen IDE'}, {'Id': '01tWt000006hV57IAE', 'Name': 'PulseSim Pro'}, {'Id': '#01tWt000006hV58IAE', 'Name': 'SecureFlow Suite'}, {'Id': '01tWt000006hV6jIAE', 'Name': 'EcoPCB Creator   '}, {'Id': '01tWt000006hV8LIAU', 'Name': 'AI Cirku-Tech'}, {'Id': '#01tWt000006hV9xIAE', 'Name': 'OptiPower Manager'}, {'Id': '01tWt000006hVBZIA2', 'Name': 'EduTech Lab'}, {'Id': '#01tWt000006hVDBIA2', 'Name': 'CircuitMaster Analyzer'}, {'Id': '#01tWt000006hVEnIAM', 'Name': 'DesignWave Automation  '}, {'Id': '01tWt000006hVGPIA2', 'Name': 'QuantumPCB Modeler  '}, {'Id': '01tWt000006hVI1IAM', 'Name': 'AIOptics Vision'}, {'Id': '#01tWt000006hVJdIAM', 'Name': 'SecureAnalytics Pro'}, {'Id': '#01tWt000006hVJeIAM', 'Name': 'SecureData Nexus'}, {'Id': '01tWt000006hVLFIA2', 'Name': 'CollabCircuit Hub'}, {'Id': '01tWt000006hVMrIAM', 'Name': 'TrainEDU Suite'}, {'Id': '01tWt000006hVOTIA2', 'Name': 'UnitySim Essentials   '}, {'Id': '01tWt000006hVQ5IAM', 'Name': 'CircuitSync Pro'}, {'Id': '01tWt000006hVQ6IAM', 'Name': 'VeriSim Express  '}, {'Id': '01tWt000006hVRhIAM', 'Name': 'PCBProto Wizard'}, {'Id': '01tWt000006hVTJIA2', 'Name': 'IntegrGuard Secure'}, {'Id': '01tWt000006hVUvIAM', 'Name': 'OptiEnergy Suite'}, {'Id': '#01tWt000006hVWXIA2', 'Name': 'AutoGen IDE   '}, {'Id': '#01tWt000006hVY9IAM', 'Name': 'EduFlow Academy'}, {'Id': '01tWt000006hVZlIAM', 'Name': 'SecuManage Pro  '}, {'Id': '01tWt000006hVbNIAU', 'Name': 'EnergyReduce Pro'}, {'Id': '01tWt000006hVczIAE', 'Name': 'CollabDesign Studio'}, {'Id': '01tWt000006hVebIAE', 'Name': 'CircuitAI Innovator'}, {'Id': '01tWt000006hVgDIAU', 'Name': 'CloudInnovate Space '}, {'Id': '#01tWt000006hVhpIAE', 'Name': 'OptiPower Max'}, {'Id': '01tWt000006hVjRIAU', 'Name': 'Workflow Genius'}, {'Id': '01tWt000006hVjSIAU', 'Name': 'InnoTrain Hub'}, {'Id': '#01tWt000006hVl3IAE', 'Name': 'PCB QuickMaker'}, {'Id': '01tWt000006hVmfIAE', 'Name': 'EduTech Advance'}, {'Id': '#01tWt000006hVoHIAU', 'Name': 'CryptSecure Core'}, {'Id': '01tWt000006hVptIAE', 'Name': 'DesignEdge Pro'}, {'Id': '#01tWt000006hVrVIAU', 'Name': 'VerifySim Elite'}, {'Id': '#01tWt000006hVrWIAU', 'Name': 'PowerPro Optimize   '}, {'Id': '01tWt000006hVt7IAE', 'Name': 'PCB EcoModel  '}, {'Id': '01tWt000006hVujIAE', 'Name': 'CyberShield Core'}, {'Id': '01tWt000006hVwLIAU', 'Name': 'SimulateX Edge'}, {'Id': '#01tWt0000072LsLIAU', 'Name': 'Shipping Charge Product'}], 'var_call_lGwgIkdws11QTFogsP2OHHaF': 'file_storage/call_lGwgIkdws11QTFogsP2OHHaF.json', 'var_call_CEdPyRwljsugpQ3MWXxKQ3T1': 'file_storage/call_CEdPyRwljsugpQ3MWXxKQ3T1.json', 'var_call_IyoK3TSjYGVRCFwvCXAwtbjN': [{'Id': '00kWt000002HJtMIAW', 'Product2Id': '#01tWt000006hVwLIAU', 'ContactId': '#003Wt00000Jqy8SIAR', 'CloseDate': '2023-12-15'}, {'Id': '00kWt000002HQObIAO', 'Product2Id': '01tWt000006hV57IAE', 'ContactId': '#003Wt00000Jqy8SIAR', 'CloseDate': '2023-12-15'}, {'Id': '00kWt000002HbBnIAK', 'Product2Id': '01tWt000006hVebIAE', 'ContactId': '#003Wt00000Jqy8SIAR', 'CloseDate': '2023-12-15'}, {'Id': '00kWt000002HcSkIAK', 'Product2Id': '01tWt000006hTUkIAM', 'ContactId': '#003Wt00000Jqy8SIAR', 'CloseDate': '2023-12-15'}, {'Id': '#00kWt000002HLwnIAG', 'Product2Id': '01tWt000006hUgwIAE', 'ContactId': '003Wt00000Jqy8SIAR', 'CloseDate': '2022-06-20'}, {'Id': '00kWt000002HOY1IAO', 'Product2Id': '01tWt000006hVgDIAU', 'ContactId': '003Wt00000Jqy8SIAR', 'CloseDate': '2022-06-20'}, {'Id': '00kWt000002HPp1IAG', 'Product2Id': '#01tWt000006hV58IAE', 'ContactId': '003Wt00000Jqy8SIAR', 'CloseDate': '2022-06-20'}, {'Id': '#00kWt000002HXo5IAG', 'Product2Id': '01tWt000006hVGPIA2', 'ContactId': '003Wt00000Jqy8SIAR', 'CloseDate': '2022-06-20'}, {'Id': '00kWt000002HHpvIAG', 'Product2Id': '01tWt000006hV57IAE', 'ContactId': '003Wt00000Jqy8SIAR', 'CloseDate': '2021-11-01'}, {'Id': '00kWt000002HLf9IAG', 'Product2Id': '01tWt000006hVmfIAE', 'ContactId': '003Wt00000Jqy8SIAR', 'CloseDate': '2021-11-01'}, {'Id': '00kWt000002HPdfIAG', 'Product2Id': '01tWt000006hVY9IAM', 'ContactId': '003Wt00000Jqy8SIAR', 'CloseDate': '2021-11-01'}, {'Id': '00kWt000002HPiQIAW', 'Product2Id': '01tWt000006hV6jIAE', 'ContactId': '003Wt00000Jqy8SIAR', 'CloseDate': '2021-11-01'}, {'Id': '00kWt000002HW2RIAW', 'Product2Id': '01tWt000006hV8LIAU', 'ContactId': '003Wt00000Jqy8SIAR', 'CloseDate': '2021-11-01'}, {'Id': '#00kWt000002Hce1IAC', 'Product2Id': '01tWt000006hV58IAE', 'ContactId': '003Wt00000Jqy8SIAR', 'CloseDate': '2021-11-01'}, {'Id': '#00kWt000002HKCZIA4', 'Product2Id': '#01tWt000006hV8LIAU', 'ContactId': '003Wt00000Jqy8SIAR', 'CloseDate': '2021-06-15'}, {'Id': '00kWt000002HKsYIAW', 'Product2Id': '#01tWt000006hV58IAE', 'ContactId': '003Wt00000Jqy8SIAR', 'CloseDate': '2021-06-15'}, {'Id': '00kWt000002HMXmIAO', 'Product2Id': '01tWt000006hTUkIAM', 'ContactId': '003Wt00000Jqy8SIAR', 'CloseDate': '2021-06-15'}, {'Id': '00kWt000002HSmqIAG', 'Product2Id': '01tWt000006hV8LIAU', 'ContactId': '003Wt00000Jqy8SIAR', 'CloseDate': '2021-06-15'}, {'Id': '00kWt000002HTEHIA4', 'Product2Id': '01tWt000006hV9xIAE', 'ContactId': '003Wt00000Jqy8SIAR', 'CloseDate': '2021-06-15'}, {'Id': '00kWt000002HXo4IAG', 'Product2Id': '01tWt000006hVczIAE', 'ContactId': '003Wt00000Jqy8SIAR', 'CloseDate': '2021-06-15'}]}

exec(code, env_args)
