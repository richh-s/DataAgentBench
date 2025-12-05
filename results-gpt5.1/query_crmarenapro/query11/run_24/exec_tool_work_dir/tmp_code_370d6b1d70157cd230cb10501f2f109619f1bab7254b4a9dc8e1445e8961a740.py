code = """import json
opps = var_call_xQ9C1Q5m6N0ScCr9SSzfnGXN
olis = var_call_WAIpJEDzJyPZ3MePRQtKInZA
products = var_call_evUSoG0SvunQJZzKPfh9T9sg
# Determine latest opportunity (first in opps list)
latest_opp_id = opps[0]['Id'].replace('#','') if opps else None
# Filter OLIs for that opportunity
candidate_olis = [o for o in olis if o['OpportunityId'].replace('#','') == latest_opp_id]
# Map Product2Id -> name
id_to_name = {p['Id'].replace('#',''): p['Name'].strip() for p in products}
# Find first OLI whose product name suggests AI processing unit
ai_keywords = ['AI', 'Quantum', 'Neural', 'Vision']
ai_product_id = None
for o in candidate_olis:
    pid_norm = o['Product2Id'].replace('#','')
    name = id_to_name.get(pid_norm, '')
    if any(k in name for k in ai_keywords):
        ai_product_id = pid_norm
        break
# Fallback: any product on that opp with 'AI' in name
if not ai_product_id:
    for o in candidate_olis:
        pid_norm = o['Product2Id'].replace('#','')
        name = id_to_name.get(pid_norm, '')
        if 'AI' in name:
            ai_product_id = pid_norm
            break
result = ai_product_id
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_xQ9C1Q5m6N0ScCr9SSzfnGXN': [{'Id': '#006Wt000007BIjxIAG'}, {'Id': '006Wt000007BInBIAW'}, {'Id': '006Wt000007BBx1IAG'}, {'Id': '006Wt000007B7TcIAK'}, {'Id': '006Wt000007B0g2IAC'}], 'var_call_WAIpJEDzJyPZ3MePRQtKInZA': [{'OLI_Id': '00kWt000002HHpvIAG', 'OpportunityId': '006Wt000007BBx1IAG', 'Product2Id': '01tWt000006hV57IAE'}, {'OLI_Id': '#00kWt000002HKCZIA4', 'OpportunityId': '006Wt000007B0g2IAC', 'Product2Id': '#01tWt000006hV8LIAU'}, {'OLI_Id': '00kWt000002HLf9IAG', 'OpportunityId': '006Wt000007BBx1IAG', 'Product2Id': '01tWt000006hVmfIAE'}, {'OLI_Id': '#00kWt000002HLwnIAG', 'OpportunityId': '006Wt000007BInBIAW', 'Product2Id': '01tWt000006hUgwIAE'}, {'OLI_Id': '00kWt000002HMXmIAO', 'OpportunityId': '006Wt000007B7TcIAK', 'Product2Id': '01tWt000006hTUkIAM'}, {'OLI_Id': '00kWt000002HOY1IAO', 'OpportunityId': '006Wt000007BInBIAW', 'Product2Id': '01tWt000006hVgDIAU'}, {'OLI_Id': '00kWt000002HPdfIAG', 'OpportunityId': '006Wt000007BBx1IAG', 'Product2Id': '01tWt000006hVY9IAM'}, {'OLI_Id': '00kWt000002HPiQIAW', 'OpportunityId': '006Wt000007BBx1IAG', 'Product2Id': '01tWt000006hV6jIAE'}, {'OLI_Id': '00kWt000002HSmqIAG', 'OpportunityId': '006Wt000007B7TcIAK', 'Product2Id': '01tWt000006hV8LIAU'}, {'OLI_Id': '00kWt000002HTEHIA4', 'OpportunityId': '006Wt000007B0g2IAC', 'Product2Id': '01tWt000006hV9xIAE'}, {'OLI_Id': '00kWt000002HW2RIAW', 'OpportunityId': '006Wt000007BBx1IAG', 'Product2Id': '01tWt000006hV8LIAU'}, {'OLI_Id': '00kWt000002HbBnIAK', 'OpportunityId': '#006Wt000007BIjxIAG', 'Product2Id': '01tWt000006hVebIAE'}, {'OLI_Id': '#00kWt000002Hce1IAC', 'OpportunityId': '006Wt000007BBx1IAG', 'Product2Id': '01tWt000006hV58IAE'}], 'var_call_evUSoG0SvunQJZzKPfh9T9sg': [{'Id': '01tWt000006hOd8IAE', 'Name': 'AutoLayout Master'}, {'Id': '01tWt000006hPffIAE', 'Name': 'DevVision IDE'}, {'Id': '01tWt000006hPfgIAE', 'Name': 'EcoPower Convert'}, {'Id': '01tWt000006hRfqIAE', 'Name': 'FlexiDesign Pro'}, {'Id': '01tWt000006hTUkIAM', 'Name': 'CloudLink Designer'}, {'Id': '01tWt000006hUKMIA2', 'Name': 'CryptGuard Module'}, {'Id': '#01tWt000006hUUwIAM', 'Name': 'SimuFlow Xtreme'}, {'Id': '01tWt000006hUgwIAE', 'Name': 'AI DesignShift'}, {'Id': '01tWt000006hUsEIAU', 'Name': 'SimuCheck Ultra'}, {'Id': '01tWt000006hUtqIAE', 'Name': 'SecureTrack Pro '}, {'Id': '01tWt000006hV0IIAU', 'Name': 'NextGen IDE'}, {'Id': '01tWt000006hV57IAE', 'Name': 'PulseSim Pro'}, {'Id': '#01tWt000006hV58IAE', 'Name': 'SecureFlow Suite'}, {'Id': '01tWt000006hV6jIAE', 'Name': 'EcoPCB Creator   '}, {'Id': '01tWt000006hV8LIAU', 'Name': 'AI Cirku-Tech'}, {'Id': '#01tWt000006hV9xIAE', 'Name': 'OptiPower Manager'}, {'Id': '01tWt000006hVBZIA2', 'Name': 'EduTech Lab'}, {'Id': '#01tWt000006hVDBIA2', 'Name': 'CircuitMaster Analyzer'}, {'Id': '#01tWt000006hVEnIAM', 'Name': 'DesignWave Automation  '}, {'Id': '01tWt000006hVGPIA2', 'Name': 'QuantumPCB Modeler  '}, {'Id': '01tWt000006hVI1IAM', 'Name': 'AIOptics Vision'}, {'Id': '#01tWt000006hVJdIAM', 'Name': 'SecureAnalytics Pro'}, {'Id': '#01tWt000006hVJeIAM', 'Name': 'SecureData Nexus'}, {'Id': '01tWt000006hVLFIA2', 'Name': 'CollabCircuit Hub'}, {'Id': '01tWt000006hVMrIAM', 'Name': 'TrainEDU Suite'}, {'Id': '01tWt000006hVOTIA2', 'Name': 'UnitySim Essentials   '}, {'Id': '01tWt000006hVQ5IAM', 'Name': 'CircuitSync Pro'}, {'Id': '01tWt000006hVQ6IAM', 'Name': 'VeriSim Express  '}, {'Id': '01tWt000006hVRhIAM', 'Name': 'PCBProto Wizard'}, {'Id': '01tWt000006hVTJIA2', 'Name': 'IntegrGuard Secure'}, {'Id': '01tWt000006hVUvIAM', 'Name': 'OptiEnergy Suite'}, {'Id': '#01tWt000006hVWXIA2', 'Name': 'AutoGen IDE   '}, {'Id': '#01tWt000006hVY9IAM', 'Name': 'EduFlow Academy'}, {'Id': '01tWt000006hVZlIAM', 'Name': 'SecuManage Pro  '}, {'Id': '01tWt000006hVbNIAU', 'Name': 'EnergyReduce Pro'}, {'Id': '01tWt000006hVczIAE', 'Name': 'CollabDesign Studio'}, {'Id': '01tWt000006hVebIAE', 'Name': 'CircuitAI Innovator'}, {'Id': '01tWt000006hVgDIAU', 'Name': 'CloudInnovate Space '}, {'Id': '#01tWt000006hVhpIAE', 'Name': 'OptiPower Max'}, {'Id': '01tWt000006hVjRIAU', 'Name': 'Workflow Genius'}, {'Id': '01tWt000006hVjSIAU', 'Name': 'InnoTrain Hub'}, {'Id': '#01tWt000006hVl3IAE', 'Name': 'PCB QuickMaker'}, {'Id': '01tWt000006hVmfIAE', 'Name': 'EduTech Advance'}, {'Id': '#01tWt000006hVoHIAU', 'Name': 'CryptSecure Core'}, {'Id': '01tWt000006hVptIAE', 'Name': 'DesignEdge Pro'}, {'Id': '#01tWt000006hVrVIAU', 'Name': 'VerifySim Elite'}, {'Id': '#01tWt000006hVrWIAU', 'Name': 'PowerPro Optimize   '}, {'Id': '01tWt000006hVt7IAE', 'Name': 'PCB EcoModel  '}, {'Id': '01tWt000006hVujIAE', 'Name': 'CyberShield Core'}, {'Id': '01tWt000006hVwLIAU', 'Name': 'SimulateX Edge'}, {'Id': '#01tWt0000072LsLIAU', 'Name': 'Shipping Charge Product'}]}

exec(code, env_args)
