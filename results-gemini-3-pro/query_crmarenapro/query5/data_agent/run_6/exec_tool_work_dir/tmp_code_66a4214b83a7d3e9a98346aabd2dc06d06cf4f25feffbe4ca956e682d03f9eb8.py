code = """import json

# Get file paths from locals
order_items_path = locals()['var_function-call-17891859246393286128']
cases_path = locals()['var_function-call-16060356968093879011']

with open(order_items_path, 'r') as f:
    order_items = json.load(f)

with open(cases_path, 'r') as f:
    cases = json.load(f)

target_product_id = "01tWt000006hV8LIAU"
start_date = "2022-08-16"
end_date = "2023-01-16T23:59:59" # Include the whole end day

def clean_id(val):
    if not val:
        return ""
    val = str(val).strip()
    if val.startswith("#"):
        val = val[1:]
    return val

target_order_item_ids = set()
for item in order_items:
    pid = clean_id(item.get("Product2Id"))
    if pid == target_product_id:
        target_order_item_ids.add(clean_id(item.get("Id")))

issue_counts = {}
for case in cases:
    c_date = case.get("createddate", "")
    if c_date < start_date or c_date > end_date:
        continue
    oid = clean_id(case.get("orderitemid__c"))
    if oid in target_order_item_ids:
        iid = clean_id(case.get("issueid__c"))
        if iid:
            issue_counts[iid] = issue_counts.get(iid, 0) + 1

# Sort by count desc
sorted_issues = sorted(issue_counts.items(), key=lambda x: x[1], reverse=True)

print("__RESULT__:")
print(json.dumps(sorted_issues))"""

env_args = {'var_function-call-11826657582006077550': [], 'var_function-call-41217853284029415': [], 'var_function-call-640798712778097113': [], 'var_function-call-7627161171148084762': [{'Id': '001Wt00000PFj4zIAD', 'Name': 'NaviCorp Tech '}, {'Id': '001Wt00000PFj50IAD', 'Name': 'FusionTech Systems'}, {'Id': '#001Wt00000PFluoIAD', 'Name': 'BlueSky Aerospace'}, {'Id': '#001Wt00000PFlupIAD', 'Name': 'NeuralWave Technologies'}, {'Id': '001Wt00000PFrk1IAD', 'Name': 'SkyNet Technologies'}, {'Id': '001Wt00000PFsjMIAT', 'Name': 'EvoTrend Systems'}, {'Id': '001Wt00000PFsjOIAT', 'Name': 'QuantumLeap Computing'}, {'Id': '001Wt00000PFsmZIAT', 'Name': 'EcoVision Engineering'}, {'Id': '001Wt00000PFsmaIAD', 'Name': 'EcoLite Innovations   '}, {'Id': '001Wt00000PFsmbIAD', 'Name': 'Innovative Robotics'}], 'var_function-call-5893619863818927727': [{'COUNT(*)': '689'}], 'var_function-call-5257289563377625987': [{'count': '153'}], 'var_function-call-14797416575717279827': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-17891859246393286128': 'file_storage/function-call-17891859246393286128.json', 'var_function-call-16060356968093879011': 'file_storage/function-call-16060356968093879011.json', 'var_function-call-3266637185180391841': 'a03Wt00000JqmX6IAJ', 'var_function-call-16338449719884338859': ['802Wt000007968iIAA', '802Wt00000799EZIAY', '802Wt00000798S9IAI', '802Wt00000794F3IAI', '802Wt00000798NMIAY', '802Wt00000798nBIAQ', '802Wt00000798iIIAQ', '802Wt00000790WEIAY', '802Wt00000794bXIAQ', '802Wt00000799ckIAA', '802Wt00000796jiIAA'], 'var_function-call-3513717873057241664': [], 'var_function-call-12166923431268534070': [{'Id': '802Wt00000794F3IAI', 'OrderId': '#801Wt00000PGbdMIAT'}, {'Id': '802Wt000007968iIAA', 'OrderId': '801Wt00000PGijTIAT'}, {'Id': '802Wt00000798iIIAQ', 'OrderId': '801Wt00000PHRTiIAP'}, {'Id': '802Wt00000799EZIAY', 'OrderId': '801Wt00000PGizbIAD'}, {'Id': '802Wt00000799ckIAA', 'OrderId': '#801Wt00000PGtLXIA1'}], 'var_function-call-8587239977540023211': 'file_storage/function-call-8587239977540023211.json', 'var_function-call-12295355184417417165': ['801Wt00000PHVicIAH', '801Wt00000PHLzNIAX', '801Wt00000PGizbIAD', '801Wt00000PHRTiIAP', '801Wt00000PGeG6IAL', '801Wt00000PGijTIAT', '801Wt00000PGtLXIA1', '801Wt00000PGtQRIA1', '801Wt00000PH8vfIAD', '801Wt00000PGbdMIAT', '801Wt00000PFtAnIAL'], 'var_function-call-1017436659124593689': [{'Id': '801Wt00000PFtAnIAL', 'AccountId': '#001Wt00000PGaNjIAL'}, {'Id': '801Wt00000PGeG6IAL', 'AccountId': '001Wt00000PGYgxIAH'}, {'Id': '801Wt00000PGijTIAT', 'AccountId': '001Wt00000PGSwYIAX'}, {'Id': '801Wt00000PGtQRIA1', 'AccountId': '#001Wt00000PHVtpIAH'}, {'Id': '801Wt00000PH8vfIAD', 'AccountId': '001Wt00000PGHsyIAH'}, {'Id': '801Wt00000PHLzNIAX', 'AccountId': '001Wt00000PGtdJIAT'}, {'Id': '801Wt00000PHRTiIAP', 'AccountId': '001Wt00000PHViZIAX'}, {'Id': '801Wt00000PHVicIAH', 'AccountId': '#001Wt00000PHViZIAX'}], 'var_function-call-16433349763477347663': [{'Id': '001Wt00000PGSwYIAX', 'Name': 'GreenLeaf Engineering  '}, {'Id': '001Wt00000PGaNjIAL', 'Name': 'MetaData Analytics'}, {'Id': '001Wt00000PGtdJIAT', 'Name': 'Quantum Innovations Inc.'}, {'Id': '001Wt00000PHVtpIAH', 'Name': 'EnergyNova Corp'}], 'var_function-call-13501640440257280544': [['a03Wt00000JqmX6IAJ', 4], ['a03Wt00000JqzSfIAJ', 4], ['a03Wt00000JqzR3IAJ', 4], ['a03Wt00000JqnHwIAJ', 3], ['a03Wt00000JqxVjIAJ', 2]]}

exec(code, env_args)
