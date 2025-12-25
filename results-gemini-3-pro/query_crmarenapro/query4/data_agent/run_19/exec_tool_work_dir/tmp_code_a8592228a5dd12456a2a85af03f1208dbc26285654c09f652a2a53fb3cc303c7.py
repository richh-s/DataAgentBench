code = """import json
from collections import Counter
from datetime import datetime

# Load Product2 to confirm ID (already known but good practice)
# Product: SecureAnalytics Pro -> ID: 01tWt000006hVJdIAM

target_pid = "01tWt000006hVJdIAM"

# Load OrderItems
with open(locals()['var_function-call-7131368775766885696'], 'r') as f:
    order_items = json.load(f)

# Map OrderItemId -> Product2Id
oid_to_pid = {}
for item in order_items:
    oid = item['Id']
    pid = item['Product2Id']
    if oid.startswith('#'): oid = oid[1:]
    if pid.startswith('#'): pid = pid[1:]
    oid_to_pid[oid] = pid

# Load Cases
with open(locals()['var_function-call-6182685443246566889'], 'r') as f:
    cases = json.load(f)

# Count
monthly_counts = Counter()
total_target_cases = 0

start_date = datetime(2020, 6, 10)
end_date = datetime(2021, 4, 10)

for case in cases:
    c_date_str = case['createddate']
    oid = case.get('orderitemid__c')
    
    if not oid:
        continue
    
    if oid.startswith('#'): oid = oid[1:]
    
    pid = oid_to_pid.get(oid)
    
    if pid == target_pid:
        # Check date
        try:
            dt = datetime.strptime(c_date_str[:10], "%Y-%m-%d")
            if start_date <= dt <= end_date:
                month_name = dt.strftime("%B")
                monthly_counts[month_name] += 1
                total_target_cases += 1
        except:
            continue

print("__RESULT__:")
print(json.dumps({"total_target_cases": total_target_cases, "monthly_counts": monthly_counts}))"""

env_args = {'var_function-call-5668392397130027000': ['ProductCategory', 'Product2', 'ProductCategoryProduct', 'Pricebook2', 'PricebookEntry', 'Order', 'OrderItem'], 'var_function-call-5668392397130026911': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-6182685443246565004': [{'Id': '#802Wt0000078yuGIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000790mOIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000790zGIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000794F2IAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt000007968eIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000796bfIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000796qFIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt0000079734IAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000797W5IAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000797awIAA', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt00000797z7IAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '#802Wt00000798VPIAY', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt00000798YdIAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000798okIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '#802Wt00000799o1IAA', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt0000079A2bIAE', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt0000079ACGIA2', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt0000079B0EIAU', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt0000079B6gIAE', 'Product2Id': '#01tWt000006hVJdIAM'}], 'var_function-call-6182685443246566889': 'file_storage/function-call-6182685443246566889.json', 'var_function-call-4677988440214606885': {'January': 1, 'November': 2, 'September': 1, 'March': 1}, 'var_function-call-2583504869033761794': [{'Id': '#01tWt000006hVJdIAM', 'Name': 'SecureAnalytics Pro'}], 'var_function-call-12315915375688508117': {'total_cases_with_oid': 153, 'target_orderitem_ids_count': 19, 'matches': 6}, 'var_function-call-12362982969333848871': [{'count(*)': '689'}], 'var_function-call-7131368775766888141': [{'Id': '01tWt000006hOd8IAE', 'Name': 'AutoLayout Master'}, {'Id': '01tWt000006hPffIAE', 'Name': 'DevVision IDE'}, {'Id': '01tWt000006hPfgIAE', 'Name': 'EcoPower Convert'}, {'Id': '01tWt000006hRfqIAE', 'Name': 'FlexiDesign Pro'}, {'Id': '01tWt000006hTUkIAM', 'Name': 'CloudLink Designer'}, {'Id': '01tWt000006hUKMIA2', 'Name': 'CryptGuard Module'}, {'Id': '#01tWt000006hUUwIAM', 'Name': 'SimuFlow Xtreme'}, {'Id': '01tWt000006hUgwIAE', 'Name': 'AI DesignShift'}, {'Id': '01tWt000006hUsEIAU', 'Name': 'SimuCheck Ultra'}, {'Id': '01tWt000006hUtqIAE', 'Name': 'SecureTrack Pro '}, {'Id': '01tWt000006hV0IIAU', 'Name': 'NextGen IDE'}, {'Id': '01tWt000006hV57IAE', 'Name': 'PulseSim Pro'}, {'Id': '#01tWt000006hV58IAE', 'Name': 'SecureFlow Suite'}, {'Id': '01tWt000006hV6jIAE', 'Name': 'EcoPCB Creator   '}, {'Id': '01tWt000006hV8LIAU', 'Name': 'AI Cirku-Tech'}, {'Id': '#01tWt000006hV9xIAE', 'Name': 'OptiPower Manager'}, {'Id': '01tWt000006hVBZIA2', 'Name': 'EduTech Lab'}, {'Id': '#01tWt000006hVDBIA2', 'Name': 'CircuitMaster Analyzer'}, {'Id': '#01tWt000006hVEnIAM', 'Name': 'DesignWave Automation  '}, {'Id': '01tWt000006hVGPIA2', 'Name': 'QuantumPCB Modeler  '}, {'Id': '01tWt000006hVI1IAM', 'Name': 'AIOptics Vision'}, {'Id': '#01tWt000006hVJdIAM', 'Name': 'SecureAnalytics Pro'}, {'Id': '#01tWt000006hVJeIAM', 'Name': 'SecureData Nexus'}, {'Id': '01tWt000006hVLFIA2', 'Name': 'CollabCircuit Hub'}, {'Id': '01tWt000006hVMrIAM', 'Name': 'TrainEDU Suite'}, {'Id': '01tWt000006hVOTIA2', 'Name': 'UnitySim Essentials   '}, {'Id': '01tWt000006hVQ5IAM', 'Name': 'CircuitSync Pro'}, {'Id': '01tWt000006hVQ6IAM', 'Name': 'VeriSim Express  '}, {'Id': '01tWt000006hVRhIAM', 'Name': 'PCBProto Wizard'}, {'Id': '01tWt000006hVTJIA2', 'Name': 'IntegrGuard Secure'}, {'Id': '01tWt000006hVUvIAM', 'Name': 'OptiEnergy Suite'}, {'Id': '#01tWt000006hVWXIA2', 'Name': 'AutoGen IDE   '}, {'Id': '#01tWt000006hVY9IAM', 'Name': 'EduFlow Academy'}, {'Id': '01tWt000006hVZlIAM', 'Name': 'SecuManage Pro  '}, {'Id': '01tWt000006hVbNIAU', 'Name': 'EnergyReduce Pro'}, {'Id': '01tWt000006hVczIAE', 'Name': 'CollabDesign Studio'}, {'Id': '01tWt000006hVebIAE', 'Name': 'CircuitAI Innovator'}, {'Id': '01tWt000006hVgDIAU', 'Name': 'CloudInnovate Space '}, {'Id': '#01tWt000006hVhpIAE', 'Name': 'OptiPower Max'}, {'Id': '01tWt000006hVjRIAU', 'Name': 'Workflow Genius'}, {'Id': '01tWt000006hVjSIAU', 'Name': 'InnoTrain Hub'}, {'Id': '#01tWt000006hVl3IAE', 'Name': 'PCB QuickMaker'}, {'Id': '01tWt000006hVmfIAE', 'Name': 'EduTech Advance'}, {'Id': '#01tWt000006hVoHIAU', 'Name': 'CryptSecure Core'}, {'Id': '01tWt000006hVptIAE', 'Name': 'DesignEdge Pro'}, {'Id': '#01tWt000006hVrVIAU', 'Name': 'VerifySim Elite'}, {'Id': '#01tWt000006hVrWIAU', 'Name': 'PowerPro Optimize   '}, {'Id': '01tWt000006hVt7IAE', 'Name': 'PCB EcoModel  '}, {'Id': '01tWt000006hVujIAE', 'Name': 'CyberShield Core'}, {'Id': '01tWt000006hVwLIAU', 'Name': 'SimulateX Edge'}, {'Id': '#01tWt0000072LsLIAU', 'Name': 'Shipping Charge Product'}], 'var_function-call-7131368775766885696': 'file_storage/function-call-7131368775766885696.json'}

exec(code, env_args)
