code = """import json
import pandas as pd

# Correctly access the product data
product_data_str = locals()['var_function-call-15827185710880210202']['results'][0]
product_data = json.loads(product_data_str)
df = pd.DataFrame(product_data)

# Clean up trailing spaces in 'Name' column and remove leading # from Id
df['Name'] = df['Name'].str.strip()
df['Id'] = df['Id'].str.replace('#', '')

# Filter for relevant products
ai_processing_unit_products = df[df['Name'].str.contains('AI processing unit', case=False, na=False)]

if not ai_processing_unit_products.empty:
    print('__RESULT__:')
    print(json.dumps(ai_processing_unit_products.to_dict(orient='records')))
else:
    # If no direct match, try a broader search for 'AI processing'
    ai_processing_products = df[df['Name'].str.contains('AI processing', case=False, na=False)]
    print('__RESULT__:')
    print(json.dumps(ai_processing_products.to_dict(orient='records')))"""

env_args = {'var_function-call-15123287087143404249': [], 'var_function-call-17377259157549660691': [], 'var_function-call-15827185710880210202': [{'Id': '01tWt000006hOd8IAE', 'Name': 'AutoLayout Master'}, {'Id': '01tWt000006hPffIAE', 'Name': 'DevVision IDE'}, {'Id': '01tWt000006hPfgIAE', 'Name': 'EcoPower Convert'}, {'Id': '01tWt000006hRfqIAE', 'Name': 'FlexiDesign Pro'}, {'Id': '01tWt000006hTUkIAM', 'Name': 'CloudLink Designer'}, {'Id': '01tWt000006hUKMIA2', 'Name': 'CryptGuard Module'}, {'Id': '#01tWt000006hUUwIAM', 'Name': 'SimuFlow Xtreme'}, {'Id': '01tWt000006hUgwIAE', 'Name': 'AI DesignShift'}, {'Id': '01tWt000006hUsEIAU', 'Name': 'SimuCheck Ultra'}, {'Id': '01tWt000006hUtqIAE', 'Name': 'SecureTrack Pro '}, {'Id': '01tWt000006hV0IIAU', 'Name': 'NextGen IDE'}, {'Id': '01tWt000006hV57IAE', 'Name': 'PulseSim Pro'}, {'Id': '#01tWt000006hV58IAE', 'Name': 'SecureFlow Suite'}, {'Id': '01tWt000006hV6jIAE', 'Name': 'EcoPCB Creator   '}, {'Id': '01tWt000006hV8LIAU', 'Name': 'AI Cirku-Tech'}, {'Id': '#01tWt000006hV9xIAE', 'Name': 'OptiPower Manager'}, {'Id': '01tWt000006hVBZIA2', 'Name': 'EduTech Lab'}, {'Id': '#01tWt000006hVDBIA2', 'Name': 'CircuitMaster Analyzer'}, {'Id': '#01tWt000006hVEnIAM', 'Name': 'DesignWave Automation  '}, {'Id': '01tWt000006hVGPIA2', 'Name': 'QuantumPCB Modeler  '}, {'Id': '01tWt000006hVI1IAM', 'Name': 'AIOptics Vision'}, {'Id': '#01tWt000006hVJdIAM', 'Name': 'SecureAnalytics Pro'}, {'Id': '#01tWt000006hVJeIAM', 'Name': 'SecureData Nexus'}, {'Id': '01tWt000006hVLFIA2', 'Name': 'CollabCircuit Hub'}, {'Id': '01tWt000006hVMrIAM', 'Name': 'TrainEDU Suite'}, {'Id': '01tWt000006hVOTIA2', 'Name': 'UnitySim Essentials   '}, {'Id': '01tWt000006hVQ5IAM', 'Name': 'CircuitSync Pro'}, {'Id': '01tWt000006hVQ6IAM', 'Name': 'VeriSim Express  '}, {'Id': '01tWt000006hVRhIAM', 'Name': 'PCBProto Wizard'}, {'Id': '01tWt000006hVTJIA2', 'Name': 'IntegrGuard Secure'}, {'Id': '01tWt000006hVUvIAM', 'Name': 'OptiEnergy Suite'}, {'Id': '#01tWt000006hVWXIA2', 'Name': 'AutoGen IDE   '}, {'Id': '#01tWt000006hVY9IAM', 'Name': 'EduFlow Academy'}, {'Id': '01tWt000006hVZlIAM', 'Name': 'SecuManage Pro  '}, {'Id': '01tWt000006hVbNIAU', 'Name': 'EnergyReduce Pro'}, {'Id': '01tWt000006hVczIAE', 'Name': 'CollabDesign Studio'}, {'Id': '01tWt000006hVebIAE', 'Name': 'CircuitAI Innovator'}, {'Id': '01tWt000006hVgDIAU', 'Name': 'CloudInnovate Space '}, {'Id': '#01tWt000006hVhpIAE', 'Name': 'OptiPower Max'}, {'Id': '01tWt000006hVjRIAU', 'Name': 'Workflow Genius'}, {'Id': '01tWt000006hVjSIAU', 'Name': 'InnoTrain Hub'}, {'Id': '#01tWt000006hVl3IAE', 'Name': 'PCB QuickMaker'}, {'Id': '01tWt000006hVmfIAE', 'Name': 'EduTech Advance'}, {'Id': '#01tWt000006hVoHIAU', 'Name': 'CryptSecure Core'}, {'Id': '01tWt000006hVptIAE', 'Name': 'DesignEdge Pro'}, {'Id': '#01tWt000006hVrVIAU', 'Name': 'VerifySim Elite'}, {'Id': '#01tWt000006hVrWIAU', 'Name': 'PowerPro Optimize   '}, {'Id': '01tWt000006hVt7IAE', 'Name': 'PCB EcoModel  '}, {'Id': '01tWt000006hVujIAE', 'Name': 'CyberShield Core'}, {'Id': '01tWt000006hVwLIAU', 'Name': 'SimulateX Edge'}, {'Id': '#01tWt0000072LsLIAU', 'Name': 'Shipping Charge Product'}]}

exec(code, env_args)
