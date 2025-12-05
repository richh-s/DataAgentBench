code = """import json
orders = var_call_qrnGKKlki3OyRjTCSUAtXZFE
products = var_call_bXPdc7gdr7KBpS8MRnYsjxfT
ai_keywords = ['AI', 'A.I.', 'Artificial Intelligence']

# Normalize product IDs (remove leading #)
prod_name_by_id = {}
for p in products:
    pid = p['Id'].lstrip('#') if isinstance(p['Id'], str) else p['Id']
    name = (p.get('Name') or '').strip()
    prod_name_by_id[pid] = name

# Attach names to orders
candidates = []
for o in orders:
    pid = o['Product2Id'].lstrip('#') if isinstance(o['Product2Id'], str) else o['Product2Id']
    name = prod_name_by_id.get(pid, '')
    rec = {"Product2Id": pid, "Name": name, "EffectiveDate": o['EffectiveDate']}
    candidates.append(rec)

# Filter for AI-related products by name keyword
ai_candidates = [c for c in candidates if any(k.lower() in c['Name'].lower() for k in ai_keywords)]

# If multiple, pick the most recent by EffectiveDate
selected = None
if ai_candidates:
    ai_candidates.sort(key=lambda x: x['EffectiveDate'], reverse=True)
    selected = ai_candidates[0]['Product2Id']

result = selected

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_SjD0RXOMhPe7R0mcQZRle19X': [], 'var_call_ETlgJAioQCk6VXrqdlItvf2s': [], 'var_call_bXPdc7gdr7KBpS8MRnYsjxfT': [{'Id': '01tWt000006hOd8IAE', 'Name': 'AutoLayout Master'}, {'Id': '01tWt000006hPffIAE', 'Name': 'DevVision IDE'}, {'Id': '01tWt000006hPfgIAE', 'Name': 'EcoPower Convert'}, {'Id': '01tWt000006hRfqIAE', 'Name': 'FlexiDesign Pro'}, {'Id': '01tWt000006hTUkIAM', 'Name': 'CloudLink Designer'}, {'Id': '01tWt000006hUKMIA2', 'Name': 'CryptGuard Module'}, {'Id': '#01tWt000006hUUwIAM', 'Name': 'SimuFlow Xtreme'}, {'Id': '01tWt000006hUgwIAE', 'Name': 'AI DesignShift'}, {'Id': '01tWt000006hUsEIAU', 'Name': 'SimuCheck Ultra'}, {'Id': '01tWt000006hUtqIAE', 'Name': 'SecureTrack Pro '}, {'Id': '01tWt000006hV0IIAU', 'Name': 'NextGen IDE'}, {'Id': '01tWt000006hV57IAE', 'Name': 'PulseSim Pro'}, {'Id': '#01tWt000006hV58IAE', 'Name': 'SecureFlow Suite'}, {'Id': '01tWt000006hV6jIAE', 'Name': 'EcoPCB Creator   '}, {'Id': '01tWt000006hV8LIAU', 'Name': 'AI Cirku-Tech'}, {'Id': '#01tWt000006hV9xIAE', 'Name': 'OptiPower Manager'}, {'Id': '01tWt000006hVBZIA2', 'Name': 'EduTech Lab'}, {'Id': '#01tWt000006hVDBIA2', 'Name': 'CircuitMaster Analyzer'}, {'Id': '#01tWt000006hVEnIAM', 'Name': 'DesignWave Automation  '}, {'Id': '01tWt000006hVGPIA2', 'Name': 'QuantumPCB Modeler  '}, {'Id': '01tWt000006hVI1IAM', 'Name': 'AIOptics Vision'}, {'Id': '#01tWt000006hVJdIAM', 'Name': 'SecureAnalytics Pro'}, {'Id': '#01tWt000006hVJeIAM', 'Name': 'SecureData Nexus'}, {'Id': '01tWt000006hVLFIA2', 'Name': 'CollabCircuit Hub'}, {'Id': '01tWt000006hVMrIAM', 'Name': 'TrainEDU Suite'}, {'Id': '01tWt000006hVOTIA2', 'Name': 'UnitySim Essentials   '}, {'Id': '01tWt000006hVQ5IAM', 'Name': 'CircuitSync Pro'}, {'Id': '01tWt000006hVQ6IAM', 'Name': 'VeriSim Express  '}, {'Id': '01tWt000006hVRhIAM', 'Name': 'PCBProto Wizard'}, {'Id': '01tWt000006hVTJIA2', 'Name': 'IntegrGuard Secure'}, {'Id': '01tWt000006hVUvIAM', 'Name': 'OptiEnergy Suite'}, {'Id': '#01tWt000006hVWXIA2', 'Name': 'AutoGen IDE   '}, {'Id': '#01tWt000006hVY9IAM', 'Name': 'EduFlow Academy'}, {'Id': '01tWt000006hVZlIAM', 'Name': 'SecuManage Pro  '}, {'Id': '01tWt000006hVbNIAU', 'Name': 'EnergyReduce Pro'}, {'Id': '01tWt000006hVczIAE', 'Name': 'CollabDesign Studio'}, {'Id': '01tWt000006hVebIAE', 'Name': 'CircuitAI Innovator'}, {'Id': '01tWt000006hVgDIAU', 'Name': 'CloudInnovate Space '}, {'Id': '#01tWt000006hVhpIAE', 'Name': 'OptiPower Max'}, {'Id': '01tWt000006hVjRIAU', 'Name': 'Workflow Genius'}, {'Id': '01tWt000006hVjSIAU', 'Name': 'InnoTrain Hub'}, {'Id': '#01tWt000006hVl3IAE', 'Name': 'PCB QuickMaker'}, {'Id': '01tWt000006hVmfIAE', 'Name': 'EduTech Advance'}, {'Id': '#01tWt000006hVoHIAU', 'Name': 'CryptSecure Core'}, {'Id': '01tWt000006hVptIAE', 'Name': 'DesignEdge Pro'}, {'Id': '#01tWt000006hVrVIAU', 'Name': 'VerifySim Elite'}, {'Id': '#01tWt000006hVrWIAU', 'Name': 'PowerPro Optimize   '}, {'Id': '01tWt000006hVt7IAE', 'Name': 'PCB EcoModel  '}, {'Id': '01tWt000006hVujIAE', 'Name': 'CyberShield Core'}, {'Id': '01tWt000006hVwLIAU', 'Name': 'SimulateX Edge'}, {'Id': '#01tWt0000072LsLIAU', 'Name': 'Shipping Charge Product'}], 'var_call_qrnGKKlki3OyRjTCSUAtXZFE': [{'Product2Id': '#01tWt000006hV9xIAE', 'EffectiveDate': '2021-07-01'}, {'Product2Id': '01tWt000006hTUkIAM', 'EffectiveDate': '2021-07-01'}, {'Product2Id': '01tWt000006hV58IAE', 'EffectiveDate': '2021-07-01'}, {'Product2Id': '01tWt000006hV6jIAE', 'EffectiveDate': '2021-07-01'}, {'Product2Id': '#01tWt000006hV6jIAE', 'EffectiveDate': '2021-07-01'}, {'Product2Id': '01tWt000006hTUkIAM', 'EffectiveDate': '2021-07-01'}, {'Product2Id': '01tWt000006hV58IAE', 'EffectiveDate': '2021-07-01'}, {'Product2Id': '01tWt000006hV8LIAU', 'EffectiveDate': '2021-07-01'}, {'Product2Id': '01tWt000006hV58IAE', 'EffectiveDate': '2021-07-01'}, {'Product2Id': '01tWt000006hV6jIAE', 'EffectiveDate': '2021-07-01'}, {'Product2Id': '01tWt000006hV9xIAE', 'EffectiveDate': '2021-07-01'}, {'Product2Id': '01tWt000006hVBZIA2', 'EffectiveDate': '2021-07-01'}, {'Product2Id': '01tWt000006hVMrIAM', 'EffectiveDate': '2021-07-01'}, {'Product2Id': '01tWt000006hV8LIAU', 'EffectiveDate': '2021-06-15'}, {'Product2Id': '01tWt000006hTUkIAM', 'EffectiveDate': '2021-06-01'}, {'Product2Id': '01tWt000006hV58IAE', 'EffectiveDate': '2021-06-01'}, {'Product2Id': '01tWt000006hV57IAE', 'EffectiveDate': '2021-06-01'}, {'Product2Id': '01tWt000006hV58IAE', 'EffectiveDate': '2021-06-01'}]}

exec(code, env_args)
