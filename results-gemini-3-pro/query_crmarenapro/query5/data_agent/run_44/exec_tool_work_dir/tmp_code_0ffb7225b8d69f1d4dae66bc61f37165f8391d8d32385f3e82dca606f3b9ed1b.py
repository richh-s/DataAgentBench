code = """import pandas as pd
import json
from collections import Counter

# Load OrderItems
order_items = locals()['var_function-call-4004564084506349322']
valid_order_item_ids = set()
target_product_id = '01tWt000006hV8LIAU'

for item in order_items:
    # Clean Product2Id
    pid = item['Product2Id']
    if pid:
        pid = pid.strip().lstrip('#')
    
    if pid == target_product_id:
        # Clean OrderItemId
        oid = item['Id']
        if oid:
            oid = oid.strip().lstrip('#')
            valid_order_item_ids.add(oid)

# Load Cases
with open(locals()['var_function-call-6928091500949245748'], 'r') as f:
    cases = json.load(f)

# Filter Cases
relevant_issues = []
# Date range: 2022-08-16 to 2023-01-16
start_date = pd.Timestamp('2022-08-16', tz='UTC')
end_date = pd.Timestamp('2023-01-16', tz='UTC') + pd.Timedelta(days=1) # Include end date fully

for case in cases:
    # Check date
    c_date_str = case['createddate']
    if not c_date_str:
        continue
    try:
        c_date = pd.to_datetime(c_date_str)
        # Ensure UTC
        if c_date.tz is None:
            c_date = c_date.tz_localize('UTC')
        else:
            c_date = c_date.tz_convert('UTC')
            
        if start_date <= c_date < end_date:
            # Check OrderItemId
            oid = case['orderitemid__c']
            if oid:
                oid = oid.strip().lstrip('#')
                if oid in valid_order_item_ids:
                    # Collect issue
                    iid = case['issueid__c']
                    if iid:
                        iid = iid.strip().lstrip('#')
                        relevant_issues.append(iid)
    except Exception as e:
        continue

# Count frequency
if not relevant_issues:
    result = "No issues found"
else:
    counts = Counter(relevant_issues)
    most_common_id = counts.most_common(1)[0][0]
    result = most_common_id

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_function-call-4004564084506347191': [], 'var_function-call-4004564084506349322': [{'Id': '802Wt0000078wz5IAA', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt0000078xAAIAY', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt0000078yXgIAI', 'Product2Id': '#01tWt000006hV8LIAU'}, {'Id': '802Wt0000078yXiIAI', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt0000078ypSIAQ', 'Product2Id': '#01tWt000006hV8LIAU'}, {'Id': '802Wt000007906mIAA', 'Product2Id': '#01tWt000006hV8LIAU'}, {'Id': '#802Wt00000790WEIAY', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000792gDIAQ', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000792zTIAQ', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '#802Wt0000079315IAA', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000793sTIAQ', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000794F3IAI', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000794F4IAI', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '#802Wt00000794JmIAI', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '#802Wt00000794YFIAY', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000794YJIAY', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000794bTIAQ', 'Product2Id': '#01tWt000006hV8LIAU'}, {'Id': '#802Wt00000794bXIAQ', 'Product2Id': '#01tWt000006hV8LIAU'}, {'Id': '802Wt000007959OIAQ', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt000007959PIAQ', 'Product2Id': '#01tWt000006hV8LIAU'}, {'Id': '#802Wt00000795PSIAY', 'Product2Id': '#01tWt000006hV8LIAU'}, {'Id': '802Wt00000795UKIAY', 'Product2Id': '#01tWt000006hV8LIAU'}, {'Id': '802Wt00000795akIAA', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000795ywIAA', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt000007962JIAQ', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt000007968hIAA', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt000007968iIAA', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000796F5IAI', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '#802Wt00000796IIIAY', 'Product2Id': '#01tWt000006hV8LIAU'}, {'Id': '#802Wt00000796N7IAI', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000796NAIAY', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000796RzIAI', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000796S0IAI', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000796S1IAI', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000796VDIAY', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000796YPIAY', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000796YQIAY', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000796a1IAA', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000796dFIAQ', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '#802Wt00000796dIIAQ', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '#802Wt00000796jiIAA', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000796lKIAQ', 'Product2Id': '#01tWt000006hV8LIAU'}, {'Id': '802Wt00000796myIAA', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000796n0IAA', 'Product2Id': '#01tWt000006hV8LIAU'}, {'Id': '802Wt00000796oaIAA', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000796rlIAA', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000796tTIAQ', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000796v0IAA', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000796wbIAA', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000796wcIAA', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt000007979WIAQ', 'Product2Id': '#01tWt000006hV8LIAU'}, {'Id': '802Wt00000797FxIAI', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000797MQIAY', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '#802Wt00000797O5IAI', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000797RGIAY', 'Product2Id': '#01tWt000006hV8LIAU'}, {'Id': '802Wt00000797SsIAI', 'Product2Id': '#01tWt000006hV8LIAU'}, {'Id': '#802Wt00000797axIAA', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000797e9IAA', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000797hNIAQ', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000797j0IAA', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '#802Wt00000797mDIAQ', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '#802Wt00000797nqIAA', 'Product2Id': '#01tWt000006hV8LIAU'}, {'Id': '802Wt00000797nsIAA', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '#802Wt00000797pSIAQ', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000797sfIAA', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000797z8IAA', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt000007982LIAQ', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '#802Wt000007983xIAA', 'Product2Id': '#01tWt000006hV8LIAU'}, {'Id': '802Wt000007987CIAQ', 'Product2Id': '#01tWt000006hV8LIAU'}, {'Id': '802Wt00000798IUIAY', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000798IVIAY', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000798NKIAY', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '#802Wt00000798NMIAY', 'Product2Id': '#01tWt000006hV8LIAU'}, {'Id': '#802Wt00000798S9IAI', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000798iIIAQ', 'Product2Id': '#01tWt000006hV8LIAU'}, {'Id': '#802Wt00000798nBIAQ', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000798rxIAA', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000798wpIAA', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt000007991dIAA', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt0000079987IAA', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000799EZIAY', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000799EaIAI', 'Product2Id': '#01tWt000006hV8LIAU'}, {'Id': '802Wt00000799HoIAI', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '#802Wt00000799JPIAY', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000799T3IAI', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '#802Wt00000799b7IAA', 'Product2Id': '#01tWt000006hV8LIAU'}, {'Id': '802Wt00000799ckIAA', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '#802Wt00000799fxIAA', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000799srIAA', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000799w5IAA', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '#802Wt0000079A0wIAE', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt0000079A2aIAE', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt0000079A49IAE', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt0000079A7NIAU', 'Product2Id': '#01tWt000006hV8LIAU'}, {'Id': '802Wt0000079AU1IAM', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '#802Wt0000079AfJIAU', 'Product2Id': '#01tWt000006hV8LIAU'}, {'Id': '802Wt0000079AgrIAE', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt0000079AqXIAU', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt0000079As9IAE', 'Product2Id': '01tWt000006hV8LIAU'}], 'var_function-call-6928091500949243693': [{'Name': 'AI Cirku-Tech'}], 'var_function-call-6928091500949245748': 'file_storage/function-call-6928091500949245748.json'}

exec(code, env_args)
