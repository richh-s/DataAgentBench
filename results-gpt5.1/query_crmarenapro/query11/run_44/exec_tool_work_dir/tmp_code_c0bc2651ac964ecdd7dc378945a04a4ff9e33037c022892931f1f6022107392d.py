code = """import json, pandas as pd
products = pd.DataFrame(var_call_BmF8gESfizOFBOOuEZnvxAHm)
opp = pd.read_json(var_call_JwMCmOKvt3q1uoOzkq9RGnVw)
contact_acct = pd.DataFrame(var_call_vZI3Mw6Y7SxYCcyY4v4aOZP1)
opp_contact = opp[opp['ContactId'].str.replace('#','')=='003Wt00000Jqy8SIAR']
opp_contact = opp_contact.copy()
opp_contact['CloseDate'] = pd.to_datetime(opp_contact['CloseDate'], errors='coerce')
opp_last_month = opp_contact[(opp_contact['CloseDate']>=pd.to_datetime('2021-06-15')) & (opp_contact['CloseDate']<pd.to_datetime('2021-07-16'))]
if not opp_last_month.empty:
    opp_ids = opp_last_month['Id'].str.replace('#','').tolist()
else:
    acct_id = contact_acct['AccountId'].iloc[0].replace('#','')
    opp_acct = opp[opp['AccountId'].str.replace('#','')==acct_id].copy()
    opp_acct['CloseDate'] = pd.to_datetime(opp_acct['CloseDate'], errors='coerce')
    opp_last_month = opp_acct[(opp_acct['CloseDate']>=pd.to_datetime('2021-06-15')) & (opp_acct['CloseDate']<pd.to_datetime('2021-07-16'))]
    opp_ids = opp_last_month['Id'].str.replace('#','').tolist()
oli = pd.read_json(var_call_hxnmPub8kd9fmSq5BI44oIGA)
oli_opp = oli[oli['Id'].isin(opp_ids)]
prod_ids = oli_opp['Product2Id'].str.replace('#','').unique().tolist()
# identify AI processing unit by name containing 'AI ' and 'processing' or 'processor' or 'unit'
products['Name_clean'] = products['Name'].str.strip()
ai_prod = products[products['Id'].str.replace('#','').isin(prod_ids)]
ai_candidates = ai_prod[ai_prod['Name_clean'].str.contains('AI', case=False, na=False)]
result_id = ai_candidates['Id'].iloc[0] if not ai_candidates.empty else (ai_prod['Id'].iloc[0] if not ai_prod.empty else None)
result = json.dumps(result_id)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_BmF8gESfizOFBOOuEZnvxAHm': [{'Id': '01tWt000006hOd8IAE', 'Name': 'AutoLayout Master'}, {'Id': '01tWt000006hPffIAE', 'Name': 'DevVision IDE'}, {'Id': '01tWt000006hPfgIAE', 'Name': 'EcoPower Convert'}, {'Id': '01tWt000006hRfqIAE', 'Name': 'FlexiDesign Pro'}, {'Id': '01tWt000006hTUkIAM', 'Name': 'CloudLink Designer'}, {'Id': '01tWt000006hUKMIA2', 'Name': 'CryptGuard Module'}, {'Id': '#01tWt000006hUUwIAM', 'Name': 'SimuFlow Xtreme'}, {'Id': '01tWt000006hUgwIAE', 'Name': 'AI DesignShift'}, {'Id': '01tWt000006hUsEIAU', 'Name': 'SimuCheck Ultra'}, {'Id': '01tWt000006hUtqIAE', 'Name': 'SecureTrack Pro '}, {'Id': '01tWt000006hV0IIAU', 'Name': 'NextGen IDE'}, {'Id': '01tWt000006hV57IAE', 'Name': 'PulseSim Pro'}, {'Id': '#01tWt000006hV58IAE', 'Name': 'SecureFlow Suite'}, {'Id': '01tWt000006hV6jIAE', 'Name': 'EcoPCB Creator   '}, {'Id': '01tWt000006hV8LIAU', 'Name': 'AI Cirku-Tech'}, {'Id': '#01tWt000006hV9xIAE', 'Name': 'OptiPower Manager'}, {'Id': '01tWt000006hVBZIA2', 'Name': 'EduTech Lab'}, {'Id': '#01tWt000006hVDBIA2', 'Name': 'CircuitMaster Analyzer'}, {'Id': '#01tWt000006hVEnIAM', 'Name': 'DesignWave Automation  '}, {'Id': '01tWt000006hVGPIA2', 'Name': 'QuantumPCB Modeler  '}, {'Id': '01tWt000006hVI1IAM', 'Name': 'AIOptics Vision'}, {'Id': '#01tWt000006hVJdIAM', 'Name': 'SecureAnalytics Pro'}, {'Id': '#01tWt000006hVJeIAM', 'Name': 'SecureData Nexus'}, {'Id': '01tWt000006hVLFIA2', 'Name': 'CollabCircuit Hub'}, {'Id': '01tWt000006hVMrIAM', 'Name': 'TrainEDU Suite'}, {'Id': '01tWt000006hVOTIA2', 'Name': 'UnitySim Essentials   '}, {'Id': '01tWt000006hVQ5IAM', 'Name': 'CircuitSync Pro'}, {'Id': '01tWt000006hVQ6IAM', 'Name': 'VeriSim Express  '}, {'Id': '01tWt000006hVRhIAM', 'Name': 'PCBProto Wizard'}, {'Id': '01tWt000006hVTJIA2', 'Name': 'IntegrGuard Secure'}, {'Id': '01tWt000006hVUvIAM', 'Name': 'OptiEnergy Suite'}, {'Id': '#01tWt000006hVWXIA2', 'Name': 'AutoGen IDE   '}, {'Id': '#01tWt000006hVY9IAM', 'Name': 'EduFlow Academy'}, {'Id': '01tWt000006hVZlIAM', 'Name': 'SecuManage Pro  '}, {'Id': '01tWt000006hVbNIAU', 'Name': 'EnergyReduce Pro'}, {'Id': '01tWt000006hVczIAE', 'Name': 'CollabDesign Studio'}, {'Id': '01tWt000006hVebIAE', 'Name': 'CircuitAI Innovator'}, {'Id': '01tWt000006hVgDIAU', 'Name': 'CloudInnovate Space '}, {'Id': '#01tWt000006hVhpIAE', 'Name': 'OptiPower Max'}, {'Id': '01tWt000006hVjRIAU', 'Name': 'Workflow Genius'}, {'Id': '01tWt000006hVjSIAU', 'Name': 'InnoTrain Hub'}, {'Id': '#01tWt000006hVl3IAE', 'Name': 'PCB QuickMaker'}, {'Id': '01tWt000006hVmfIAE', 'Name': 'EduTech Advance'}, {'Id': '#01tWt000006hVoHIAU', 'Name': 'CryptSecure Core'}, {'Id': '01tWt000006hVptIAE', 'Name': 'DesignEdge Pro'}, {'Id': '#01tWt000006hVrVIAU', 'Name': 'VerifySim Elite'}, {'Id': '#01tWt000006hVrWIAU', 'Name': 'PowerPro Optimize   '}, {'Id': '01tWt000006hVt7IAE', 'Name': 'PCB EcoModel  '}, {'Id': '01tWt000006hVujIAE', 'Name': 'CyberShield Core'}, {'Id': '01tWt000006hVwLIAU', 'Name': 'SimulateX Edge'}, {'Id': '#01tWt0000072LsLIAU', 'Name': 'Shipping Charge Product'}], 'var_call_hxnmPub8kd9fmSq5BI44oIGA': 'file_storage/call_hxnmPub8kd9fmSq5BI44oIGA.json', 'var_call_8xXPbJNioYyAF0C8Bq25VceS': 'file_storage/call_8xXPbJNioYyAF0C8Bq25VceS.json', 'var_call_JwMCmOKvt3q1uoOzkq9RGnVw': 'file_storage/call_JwMCmOKvt3q1uoOzkq9RGnVw.json', 'var_call_vZI3Mw6Y7SxYCcyY4v4aOZP1': [{'Id': '003Wt00000Jqy8SIAR', 'AccountId': '#001Wt00000PGXrNIAX'}]}

exec(code, env_args)
