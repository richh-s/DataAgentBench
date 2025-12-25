code = """import json
from datetime import datetime, timedelta

# Calculate date 5 months ago
today = datetime(2023, 1, 16)
five_months_ago = today - timedelta(days=5*30) # Approx
date_str = five_months_ago.strftime('%Y-%m-%d')

# Process IDs
order_item_ids_raw = locals()['var_function-call-5114374313652700189']
order_item_ids = [item['Id'] for item in order_item_ids_raw]

def clean_id(id_str):
    return id_str.lstrip('#')

all_ids = set()
for oid in order_item_ids:
    clean = clean_id(oid)
    all_ids.add(clean)
    all_ids.add('#' + clean)

# Create the IN clause string for SQL
# Use double quotes for the list elements in the python string representation if passing to SQL, 
# but SQL standard uses single quotes for string literals.
id_list_sql = ", ".join([f"'{oid}'" for oid in all_ids])

result = {
    "date_filter": date_str,
    "id_list_sql": id_list_sql
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-5114374313652700462': [], 'var_function-call-5114374313652700189': [{'Id': '802Wt0000078wz5IAA'}, {'Id': '802Wt0000078xAAIAY'}, {'Id': '802Wt0000078yXgIAI'}, {'Id': '802Wt0000078yXiIAI'}, {'Id': '802Wt0000078ypSIAQ'}, {'Id': '802Wt000007906mIAA'}, {'Id': '#802Wt00000790WEIAY'}, {'Id': '802Wt00000792gDIAQ'}, {'Id': '802Wt00000792zTIAQ'}, {'Id': '#802Wt0000079315IAA'}, {'Id': '802Wt00000793sTIAQ'}, {'Id': '802Wt00000794F3IAI'}, {'Id': '802Wt00000794F4IAI'}, {'Id': '#802Wt00000794JmIAI'}, {'Id': '#802Wt00000794YFIAY'}, {'Id': '802Wt00000794YJIAY'}, {'Id': '802Wt00000794bTIAQ'}, {'Id': '#802Wt00000794bXIAQ'}, {'Id': '802Wt000007959OIAQ'}, {'Id': '802Wt000007959PIAQ'}, {'Id': '#802Wt00000795PSIAY'}, {'Id': '802Wt00000795UKIAY'}, {'Id': '802Wt00000795akIAA'}, {'Id': '802Wt00000795ywIAA'}, {'Id': '802Wt000007962JIAQ'}, {'Id': '802Wt000007968hIAA'}, {'Id': '802Wt000007968iIAA'}, {'Id': '802Wt00000796F5IAI'}, {'Id': '#802Wt00000796IIIAY'}, {'Id': '#802Wt00000796N7IAI'}, {'Id': '802Wt00000796NAIAY'}, {'Id': '802Wt00000796RzIAI'}, {'Id': '802Wt00000796S0IAI'}, {'Id': '802Wt00000796S1IAI'}, {'Id': '802Wt00000796VDIAY'}, {'Id': '802Wt00000796YPIAY'}, {'Id': '802Wt00000796YQIAY'}, {'Id': '802Wt00000796a1IAA'}, {'Id': '802Wt00000796dFIAQ'}, {'Id': '#802Wt00000796dIIAQ'}, {'Id': '#802Wt00000796jiIAA'}, {'Id': '802Wt00000796lKIAQ'}, {'Id': '802Wt00000796myIAA'}, {'Id': '802Wt00000796n0IAA'}, {'Id': '802Wt00000796oaIAA'}, {'Id': '802Wt00000796rlIAA'}, {'Id': '802Wt00000796tTIAQ'}, {'Id': '802Wt00000796v0IAA'}, {'Id': '802Wt00000796wbIAA'}, {'Id': '802Wt00000796wcIAA'}, {'Id': '802Wt000007979WIAQ'}, {'Id': '802Wt00000797FxIAI'}, {'Id': '802Wt00000797MQIAY'}, {'Id': '#802Wt00000797O5IAI'}, {'Id': '802Wt00000797RGIAY'}, {'Id': '802Wt00000797SsIAI'}, {'Id': '#802Wt00000797axIAA'}, {'Id': '802Wt00000797e9IAA'}, {'Id': '802Wt00000797hNIAQ'}, {'Id': '802Wt00000797j0IAA'}, {'Id': '#802Wt00000797mDIAQ'}, {'Id': '#802Wt00000797nqIAA'}, {'Id': '802Wt00000797nsIAA'}, {'Id': '#802Wt00000797pSIAQ'}, {'Id': '802Wt00000797sfIAA'}, {'Id': '802Wt00000797z8IAA'}, {'Id': '802Wt000007982LIAQ'}, {'Id': '#802Wt000007983xIAA'}, {'Id': '802Wt000007987CIAQ'}, {'Id': '802Wt00000798IUIAY'}, {'Id': '802Wt00000798IVIAY'}, {'Id': '802Wt00000798NKIAY'}, {'Id': '#802Wt00000798NMIAY'}, {'Id': '#802Wt00000798S9IAI'}, {'Id': '802Wt00000798iIIAQ'}, {'Id': '#802Wt00000798nBIAQ'}, {'Id': '802Wt00000798rxIAA'}, {'Id': '802Wt00000798wpIAA'}, {'Id': '802Wt000007991dIAA'}, {'Id': '802Wt0000079987IAA'}, {'Id': '802Wt00000799EZIAY'}, {'Id': '802Wt00000799EaIAI'}, {'Id': '802Wt00000799HoIAI'}, {'Id': '#802Wt00000799JPIAY'}, {'Id': '802Wt00000799T3IAI'}, {'Id': '#802Wt00000799b7IAA'}, {'Id': '802Wt00000799ckIAA'}, {'Id': '#802Wt00000799fxIAA'}, {'Id': '802Wt00000799srIAA'}, {'Id': '802Wt00000799w5IAA'}, {'Id': '#802Wt0000079A0wIAE'}, {'Id': '802Wt0000079A2aIAE'}, {'Id': '802Wt0000079A49IAE'}, {'Id': '802Wt0000079A7NIAU'}, {'Id': '802Wt0000079AU1IAM'}, {'Id': '#802Wt0000079AfJIAU'}, {'Id': '802Wt0000079AgrIAE'}, {'Id': '802Wt0000079AqXIAU'}, {'Id': '802Wt0000079As9IAE'}], 'var_function-call-11440438699229176556': [], 'var_function-call-1980747926870922517': [{'Id': '001Wt00000PFj4zIAD', 'Name': 'NaviCorp Tech '}, {'Id': '001Wt00000PFj50IAD', 'Name': 'FusionTech Systems'}, {'Id': '#001Wt00000PFluoIAD', 'Name': 'BlueSky Aerospace'}, {'Id': '#001Wt00000PFlupIAD', 'Name': 'NeuralWave Technologies'}, {'Id': '001Wt00000PFrk1IAD', 'Name': 'SkyNet Technologies'}, {'Id': '001Wt00000PFsjMIAT', 'Name': 'EvoTrend Systems'}, {'Id': '001Wt00000PFsjOIAT', 'Name': 'QuantumLeap Computing'}, {'Id': '001Wt00000PFsmZIAT', 'Name': 'EcoVision Engineering'}, {'Id': '001Wt00000PFsmaIAD', 'Name': 'EcoLite Innovations   '}, {'Id': '001Wt00000PFsmbIAD', 'Name': 'Innovative Robotics'}], 'var_function-call-1980747926870924680': []}

exec(code, env_args)
