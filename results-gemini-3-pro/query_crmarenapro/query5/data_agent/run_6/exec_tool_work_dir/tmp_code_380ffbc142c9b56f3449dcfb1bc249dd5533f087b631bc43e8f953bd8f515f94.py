code = """import json

order_items_path = locals()['var_function-call-8587239977540023211']
target_ids = ["802Wt000007968iIAA", "802Wt00000799EZIAY", "802Wt00000798S9IAI", "802Wt00000794F3IAI", "802Wt00000798NMIAY", "802Wt00000798nBIAQ", "802Wt00000798iIIAQ", "802Wt00000790WEIAY", "802Wt00000794bXIAQ", "802Wt00000799ckIAA", "802Wt00000796jiIAA"]

with open(order_items_path, 'r') as f:
    order_items = json.load(f)

def clean_id(val):
    if not val:
        return ""
    val = str(val).strip()
    if val.startswith("#"):
        val = val[1:]
    return val

order_ids = set()
for item in order_items:
    if clean_id(item.get("Id")) in target_ids:
        order_ids.add(clean_id(item.get("OrderId")))

print("__RESULT__:")
print(json.dumps(list(order_ids)))"""

env_args = {'var_function-call-11826657582006077550': [], 'var_function-call-41217853284029415': [], 'var_function-call-640798712778097113': [], 'var_function-call-7627161171148084762': [{'Id': '001Wt00000PFj4zIAD', 'Name': 'NaviCorp Tech '}, {'Id': '001Wt00000PFj50IAD', 'Name': 'FusionTech Systems'}, {'Id': '#001Wt00000PFluoIAD', 'Name': 'BlueSky Aerospace'}, {'Id': '#001Wt00000PFlupIAD', 'Name': 'NeuralWave Technologies'}, {'Id': '001Wt00000PFrk1IAD', 'Name': 'SkyNet Technologies'}, {'Id': '001Wt00000PFsjMIAT', 'Name': 'EvoTrend Systems'}, {'Id': '001Wt00000PFsjOIAT', 'Name': 'QuantumLeap Computing'}, {'Id': '001Wt00000PFsmZIAT', 'Name': 'EcoVision Engineering'}, {'Id': '001Wt00000PFsmaIAD', 'Name': 'EcoLite Innovations   '}, {'Id': '001Wt00000PFsmbIAD', 'Name': 'Innovative Robotics'}], 'var_function-call-5893619863818927727': [{'COUNT(*)': '689'}], 'var_function-call-5257289563377625987': [{'count': '153'}], 'var_function-call-14797416575717279827': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-17891859246393286128': 'file_storage/function-call-17891859246393286128.json', 'var_function-call-16060356968093879011': 'file_storage/function-call-16060356968093879011.json', 'var_function-call-3266637185180391841': 'a03Wt00000JqmX6IAJ', 'var_function-call-16338449719884338859': ['802Wt000007968iIAA', '802Wt00000799EZIAY', '802Wt00000798S9IAI', '802Wt00000794F3IAI', '802Wt00000798NMIAY', '802Wt00000798nBIAQ', '802Wt00000798iIIAQ', '802Wt00000790WEIAY', '802Wt00000794bXIAQ', '802Wt00000799ckIAA', '802Wt00000796jiIAA'], 'var_function-call-3513717873057241664': [], 'var_function-call-12166923431268534070': [{'Id': '802Wt00000794F3IAI', 'OrderId': '#801Wt00000PGbdMIAT'}, {'Id': '802Wt000007968iIAA', 'OrderId': '801Wt00000PGijTIAT'}, {'Id': '802Wt00000798iIIAQ', 'OrderId': '801Wt00000PHRTiIAP'}, {'Id': '802Wt00000799EZIAY', 'OrderId': '801Wt00000PGizbIAD'}, {'Id': '802Wt00000799ckIAA', 'OrderId': '#801Wt00000PGtLXIA1'}], 'var_function-call-8587239977540023211': 'file_storage/function-call-8587239977540023211.json'}

exec(code, env_args)
