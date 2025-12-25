code = """import json

# Get file paths from locals
order_items_path = locals()['var_function-call-17891859246393286128']
cases_path = locals()['var_function-call-16060356968093879011']

with open(order_items_path, 'r') as f:
    order_items = json.load(f)

with open(cases_path, 'r') as f:
    cases = json.load(f)

target_product_id = "01tWt000006hV8LIAU"
target_date = "2022-08-16"

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

# Find relevant OrderItem IDs from cases
relevant_order_item_ids = set()
for case in cases:
    c_date = case.get("createddate", "")
    if c_date < target_date:
        continue
    oid = clean_id(case.get("orderitemid__c"))
    if oid in target_order_item_ids:
        relevant_order_item_ids.add(oid)

print("__RESULT__:")
print(json.dumps(list(relevant_order_item_ids)))"""

env_args = {'var_function-call-11826657582006077550': [], 'var_function-call-41217853284029415': [], 'var_function-call-640798712778097113': [], 'var_function-call-7627161171148084762': [{'Id': '001Wt00000PFj4zIAD', 'Name': 'NaviCorp Tech '}, {'Id': '001Wt00000PFj50IAD', 'Name': 'FusionTech Systems'}, {'Id': '#001Wt00000PFluoIAD', 'Name': 'BlueSky Aerospace'}, {'Id': '#001Wt00000PFlupIAD', 'Name': 'NeuralWave Technologies'}, {'Id': '001Wt00000PFrk1IAD', 'Name': 'SkyNet Technologies'}, {'Id': '001Wt00000PFsjMIAT', 'Name': 'EvoTrend Systems'}, {'Id': '001Wt00000PFsjOIAT', 'Name': 'QuantumLeap Computing'}, {'Id': '001Wt00000PFsmZIAT', 'Name': 'EcoVision Engineering'}, {'Id': '001Wt00000PFsmaIAD', 'Name': 'EcoLite Innovations   '}, {'Id': '001Wt00000PFsmbIAD', 'Name': 'Innovative Robotics'}], 'var_function-call-5893619863818927727': [{'COUNT(*)': '689'}], 'var_function-call-5257289563377625987': [{'count': '153'}], 'var_function-call-14797416575717279827': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-17891859246393286128': 'file_storage/function-call-17891859246393286128.json', 'var_function-call-16060356968093879011': 'file_storage/function-call-16060356968093879011.json', 'var_function-call-3266637185180391841': 'a03Wt00000JqmX6IAJ'}

exec(code, env_args)
