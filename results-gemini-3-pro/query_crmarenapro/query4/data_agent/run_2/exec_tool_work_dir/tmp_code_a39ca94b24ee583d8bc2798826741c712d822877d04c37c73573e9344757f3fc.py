code = """import pandas as pd
import json

# Load PricebookEntry
path_pbe = locals()['var_function-call-6862423570974461105']
with open(path_pbe, 'r') as f:
    pbes = json.load(f)

# Load OrderItem
path_orders = locals()['var_function-call-6862423570974458048']
with open(path_orders, 'r') as f:
    orders = json.load(f)

# Load Case
path_cases = locals()['var_function-call-8848634664430094508']
with open(path_cases, 'r') as f:
    cases = json.load(f)

target_product_id = '01tWt000006hVJdIAM'

# 1. Get valid PricebookEntry Ids
valid_pbe_ids = set()
for pbe in pbes:
    pid = pbe.get('Product2Id')
    pbe_id = pbe.get('Id')
    if pid and pbe_id:
        pid_clean = pid.strip().lstrip('#')
        if pid_clean == target_product_id:
            pbe_id_clean = pbe_id.strip().lstrip('#')
            valid_pbe_ids.add(pbe_id_clean)

# 2. Get valid OrderItem Ids
valid_order_ids = set()
for order in orders:
    pbe_id = order.get('PriceBookEntryId')
    oid = order.get('Id')
    if pbe_id and oid:
        pbe_id_clean = pbe_id.strip().lstrip('#')
        if pbe_id_clean in valid_pbe_ids:
            oid_clean = oid.strip().lstrip('#')
            valid_order_ids.add(oid_clean)

# 3. Match Cases
case_counts = {}
end_date = pd.Timestamp('2021-04-10').replace(tzinfo=None)
start_date = end_date - pd.DateOffset(months=10)

matched_dates = []

for case in cases:
    cdate_str = case.get('createddate')
    oid = case.get('orderitemid__c')
    
    if oid:
        oid_clean = oid.strip().lstrip('#')
        if oid_clean in valid_order_ids:
            if cdate_str:
                try:
                    cdate = pd.to_datetime(cdate_str).tz_localize(None)
                    # Track all matched dates to see distribution
                    matched_dates.append(cdate_str)
                    
                    if start_date <= cdate <= end_date:
                        month_key = cdate.strftime('%Y-%B')
                        case_counts[month_key] = case_counts.get(month_key, 0) + 1
                except:
                    pass

print("__RESULT__:")
print(json.dumps({"counts": case_counts, "all_matched_dates_count": len(matched_dates), "sample_dates": matched_dates[:10]}))"""

env_args = {'var_function-call-17653216939775560679': 'file_storage/function-call-17653216939775560679.json', 'var_function-call-8848634664430094508': 'file_storage/function-call-8848634664430094508.json', 'var_function-call-14765431148327615615': {'2021-January': 1, '2020-November': 2, '2020-September': 1, '2021-March': 1}, 'var_function-call-17298362015042363489': 'Done', 'var_function-call-2048997635547489170': {'valid_order_ids_count': 19, 'case_match_count': 6, 'matched_dates_sample': ['2021-01-25T09:30:00.000+0000', '2020-11-05T08:19:00.000+0000', '2023-06-30T13:03:00.000+0000', '2020-09-29T01:59:00.000+0000', '2021-03-07T11:25:00.000+0000', '2020-11-09T19:02:00.000+0000'], 'all_matched_dates': ['2021-01-25T09:30:00.000+0000', '2020-11-05T08:19:00.000+0000', '2023-06-30T13:03:00.000+0000', '2020-09-29T01:59:00.000+0000', '2021-03-07T11:25:00.000+0000', '2020-11-09T19:02:00.000+0000']}, 'var_function-call-12249704330102751871': [], 'var_function-call-10017371611995314110': [{'Id': '01tWt000006hOd8IAE', 'Name': 'AutoLayout Master'}, {'Id': '01tWt000006hPffIAE', 'Name': 'DevVision IDE'}, {'Id': '01tWt000006hPfgIAE', 'Name': 'EcoPower Convert'}, {'Id': '01tWt000006hRfqIAE', 'Name': 'FlexiDesign Pro'}, {'Id': '01tWt000006hTUkIAM', 'Name': 'CloudLink Designer'}, {'Id': '01tWt000006hUKMIA2', 'Name': 'CryptGuard Module'}, {'Id': '#01tWt000006hUUwIAM', 'Name': 'SimuFlow Xtreme'}, {'Id': '01tWt000006hUgwIAE', 'Name': 'AI DesignShift'}, {'Id': '01tWt000006hUsEIAU', 'Name': 'SimuCheck Ultra'}, {'Id': '01tWt000006hUtqIAE', 'Name': 'SecureTrack Pro '}, {'Id': '01tWt000006hV0IIAU', 'Name': 'NextGen IDE'}, {'Id': '01tWt000006hV57IAE', 'Name': 'PulseSim Pro'}, {'Id': '#01tWt000006hV58IAE', 'Name': 'SecureFlow Suite'}, {'Id': '01tWt000006hV6jIAE', 'Name': 'EcoPCB Creator   '}, {'Id': '01tWt000006hV8LIAU', 'Name': 'AI Cirku-Tech'}, {'Id': '#01tWt000006hV9xIAE', 'Name': 'OptiPower Manager'}, {'Id': '01tWt000006hVBZIA2', 'Name': 'EduTech Lab'}, {'Id': '#01tWt000006hVDBIA2', 'Name': 'CircuitMaster Analyzer'}, {'Id': '#01tWt000006hVEnIAM', 'Name': 'DesignWave Automation  '}, {'Id': '01tWt000006hVGPIA2', 'Name': 'QuantumPCB Modeler  '}, {'Id': '01tWt000006hVI1IAM', 'Name': 'AIOptics Vision'}, {'Id': '#01tWt000006hVJdIAM', 'Name': 'SecureAnalytics Pro'}, {'Id': '#01tWt000006hVJeIAM', 'Name': 'SecureData Nexus'}, {'Id': '01tWt000006hVLFIA2', 'Name': 'CollabCircuit Hub'}, {'Id': '01tWt000006hVMrIAM', 'Name': 'TrainEDU Suite'}, {'Id': '01tWt000006hVOTIA2', 'Name': 'UnitySim Essentials   '}, {'Id': '01tWt000006hVQ5IAM', 'Name': 'CircuitSync Pro'}, {'Id': '01tWt000006hVQ6IAM', 'Name': 'VeriSim Express  '}, {'Id': '01tWt000006hVRhIAM', 'Name': 'PCBProto Wizard'}, {'Id': '01tWt000006hVTJIA2', 'Name': 'IntegrGuard Secure'}, {'Id': '01tWt000006hVUvIAM', 'Name': 'OptiEnergy Suite'}, {'Id': '#01tWt000006hVWXIA2', 'Name': 'AutoGen IDE   '}, {'Id': '#01tWt000006hVY9IAM', 'Name': 'EduFlow Academy'}, {'Id': '01tWt000006hVZlIAM', 'Name': 'SecuManage Pro  '}, {'Id': '01tWt000006hVbNIAU', 'Name': 'EnergyReduce Pro'}, {'Id': '01tWt000006hVczIAE', 'Name': 'CollabDesign Studio'}, {'Id': '01tWt000006hVebIAE', 'Name': 'CircuitAI Innovator'}, {'Id': '01tWt000006hVgDIAU', 'Name': 'CloudInnovate Space '}, {'Id': '#01tWt000006hVhpIAE', 'Name': 'OptiPower Max'}, {'Id': '01tWt000006hVjRIAU', 'Name': 'Workflow Genius'}, {'Id': '01tWt000006hVjSIAU', 'Name': 'InnoTrain Hub'}, {'Id': '#01tWt000006hVl3IAE', 'Name': 'PCB QuickMaker'}, {'Id': '01tWt000006hVmfIAE', 'Name': 'EduTech Advance'}, {'Id': '#01tWt000006hVoHIAU', 'Name': 'CryptSecure Core'}, {'Id': '01tWt000006hVptIAE', 'Name': 'DesignEdge Pro'}, {'Id': '#01tWt000006hVrVIAU', 'Name': 'VerifySim Elite'}, {'Id': '#01tWt000006hVrWIAU', 'Name': 'PowerPro Optimize   '}, {'Id': '01tWt000006hVt7IAE', 'Name': 'PCB EcoModel  '}, {'Id': '01tWt000006hVujIAE', 'Name': 'CyberShield Core'}, {'Id': '01tWt000006hVwLIAU', 'Name': 'SimulateX Edge'}, {'Id': '#01tWt0000072LsLIAU', 'Name': 'Shipping Charge Product'}], 'var_function-call-15345003398763992692': [{'count': '1'}], 'var_function-call-17258773704807761579': [{'id': 'a03Wt00000JqhItIAJ', 'name': 'Software Installation Error', 'description__c': 'Users report encountering errors during the initial installation process, which hinders the setup of TechPulse solutions.'}, {'id': '#a03Wt00000JqmLvIAJ', 'name': 'Billing Discrepancy', 'description__c': 'Some clients encounter unexpected charges on their billing statements, leading to confusion and dissatisfaction.'}, {'id': 'a03Wt00000JqmX6IAJ', 'name': 'Customizability Limitation   ', 'description__c': 'Despite customization options, some users find it challenging to tailor solutions to fit extremely niche industry needs.'}, {'id': 'a03Wt00000JqnHwIAJ', 'name': 'User Interface Bug', 'description__c': "A segment of users face occasional glitches in the software's user interface, affecting their overall usability experience."}, {'id': '#a03Wt00000JqtOtIAJ', 'name': 'Support Response Delay', 'description__c': 'Some users face delays in getting timely responses from the TechPulse support team during peak times.'}, {'id': 'a03Wt00000JqvLsIAJ', 'name': 'License Renewal Confusion', 'description__c': 'Clients find the license renewal process unclear, causing unexpected service disruptions.'}, {'id': '#a03Wt00000JqvNUIAZ', 'name': 'Training Module Access   ', 'description__c': 'Customers report occasional technical difficulties accessing online training modules crucial for product adoption.'}, {'id': 'a03Wt00000JqvvOIAR', 'name': 'Data Loss Incident', 'description__c': 'In rare cases, clients experience unanticipated data loss during software updates, causing significant operational setbacks.'}, {'id': '#a03Wt00000JqxVjIAJ', 'name': 'AI Feature Malfunction', 'description__c': 'Some AI-powered features intermittently fail to operate, resulting in reduced efficiency and user frustration.'}, {'id': '#a03Wt00000JqxtvIAB', 'name': 'Scalability Issue', 'description__c': 'Some enterprises report difficulties in scaling TechPulse solutions to meet increasing demands, impacting their expansion efforts.'}], 'var_function-call-6862423570974461105': [{'Id': '01uWt0000027P3lIAE', 'Product2Id': '01tWt000006hV57IAE'}, {'Id': '01uWt0000027P3mIAE', 'Product2Id': '01tWt000006hVhpIAE'}, {'Id': '01uWt0000027P5NIAU', 'Product2Id': '#01tWt000006hV58IAE'}, {'Id': '#01uWt0000027P6zIAE', 'Product2Id': '01tWt000006hTUkIAM'}, {'Id': '#01uWt0000027P8bIAE', 'Product2Id': '01tWt000006hV6jIAE'}, {'Id': '01uWt0000027P8cIAE', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '01uWt0000027PADIA2', 'Product2Id': '01tWt000006hPffIAE'}, {'Id': '01uWt0000027PBpIAM', 'Product2Id': '01tWt000006hV9xIAE'}, {'Id': '01uWt0000027PDRIA2', 'Product2Id': '01tWt000006hVBZIA2'}, {'Id': '01uWt0000027PF3IAM', 'Product2Id': '01tWt000006hVDBIA2'}, {'Id': '#01uWt0000027PGfIAM', 'Product2Id': '01tWt000006hVEnIAM'}, {'Id': '01uWt0000027PIHIA2', 'Product2Id': '#01tWt000006hVGPIA2'}, {'Id': '01uWt0000027PIIIA2', 'Product2Id': '01tWt000006hVI1IAM'}, {'Id': '01uWt0000027PIJIA2', 'Product2Id': '01tWt000006hVptIAE'}, {'Id': '01uWt0000027PJtIAM', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '01uWt0000027PLVIA2', 'Product2Id': '#01tWt000006hVLFIA2'}, {'Id': '#01uWt0000027PN7IAM', 'Product2Id': '01tWt000006hPfgIAE'}, {'Id': '#01uWt0000027POjIAM', 'Product2Id': '01tWt000006hVMrIAM'}, {'Id': '01uWt0000027POkIAM', 'Product2Id': '#01tWt000006hRfqIAE'}, {'Id': '01uWt0000027PQLIA2', 'Product2Id': '#01tWt000006hUKMIA2'}, {'Id': '#01uWt0000027PRxIAM', 'Product2Id': '#01tWt000006hVOTIA2'}, {'Id': '01uWt0000027PTZIA2', 'Product2Id': '01tWt000006hV0IIAU'}, {'Id': '#01uWt0000027PTaIAM', 'Product2Id': '01tWt000006hVUvIAM'}, {'Id': '01uWt0000027PVBIA2', 'Product2Id': '01tWt000006hVQ5IAM'}, {'Id': '#01uWt0000027PWnIAM', 'Product2Id': '01tWt000006hVQ6IAM'}, {'Id': '01uWt0000027PYPIA2', 'Product2Id': '#01tWt000006hVRhIAM'}, {'Id': '01uWt0000027Pa1IAE', 'Product2Id': '01tWt000006hVTJIA2'}, {'Id': '01uWt0000027PbdIAE', 'Product2Id': '01tWt000006hVWXIA2'}, {'Id': '01uWt0000027PdFIAU', 'Product2Id': '01tWt000006hVY9IAM'}, {'Id': '01uWt0000027PerIAE', 'Product2Id': '01tWt000006hVZlIAM'}, {'Id': '01uWt0000027PgTIAU', 'Product2Id': '01tWt000006hVbNIAU'}, {'Id': '01uWt0000027PgUIAU', 'Product2Id': '01tWt000006hVt7IAE'}, {'Id': '01uWt0000027Pi5IAE', 'Product2Id': '01tWt000006hVczIAE'}, {'Id': '01uWt0000027PjhIAE', 'Product2Id': '01tWt000006hVebIAE'}, {'Id': '01uWt0000027PlJIAU', 'Product2Id': '01tWt000006hUsEIAU'}, {'Id': '#01uWt0000027PmvIAE', 'Product2Id': '01tWt000006hVJeIAM'}, {'Id': '01uWt0000027PoXIAU', 'Product2Id': '#01tWt000006hVgDIAU'}, {'Id': '#01uWt0000027Pq9IAE', 'Product2Id': '01tWt000006hVjRIAU'}, {'Id': '01uWt0000027PrlIAE', 'Product2Id': '01tWt000006hVl3IAE'}, {'Id': '#01uWt0000027PtNIAU', 'Product2Id': '01tWt000006hVmfIAE'}, {'Id': '01uWt0000027PtOIAU', 'Product2Id': '01tWt000006hVwLIAU'}, {'Id': '01uWt0000027PuzIAE', 'Product2Id': '01tWt000006hVoHIAU'}, {'Id': '01uWt0000027PwbIAE', 'Product2Id': '01tWt000006hUUwIAM'}, {'Id': '#01uWt0000027PyDIAU', 'Product2Id': '01tWt000006hVrVIAU'}, {'Id': '#01uWt0000027PzpIAE', 'Product2Id': '01tWt000006hVrWIAU'}, {'Id': '01uWt0000027Q1RIAU', 'Product2Id': '01tWt000006hVujIAE'}, {'Id': '#01uWt0000027Q33IAE', 'Product2Id': '01tWt000006hOd8IAE'}, {'Id': '#01uWt0000027Q34IAE', 'Product2Id': '01tWt000006hUgwIAE'}, {'Id': '01uWt0000027Q4fIAE', 'Product2Id': '01tWt000006hVjSIAU'}, {'Id': '01uWt0000027Q6HIAU', 'Product2Id': '01tWt000006hUtqIAE'}], 'var_function-call-6862423570974458048': 'file_storage/function-call-6862423570974458048.json'}

exec(code, env_args)
