code = """import json
from collections import Counter
# Accessing previous query results
cases = var_call_p8kmaxrNAd2eFpbbiwct1ng7
orderitems = var_call_9QJEnecrNns7O7ZL7gr2ApLR

# Normalize order item ids from product
def norm_id(x):
    if x is None:
        return None
    return x.strip().lstrip('#').strip()

order_ids = set()
for oi in orderitems:
    oid = oi.get('Id')
    if oid is None:
        continue
    order_ids.add(norm_id(oid))

# Filter cases whose orderitemid__c matches order_ids and within date range (already filtered)
matched_issue_ids = []
for c in cases:
    oic = c.get('orderitemid__c')
    if oic is None:
        continue
    if norm_id(oic) in order_ids:
        iid = c.get('issueid__c')
        if iid:
            matched_issue_ids.append(norm_id(iid))

# Count and pick most common
if matched_issue_ids:
    cnt = Counter(matched_issue_ids)
    most_common_issue, count = cnt.most_common(1)[0]
else:
    most_common_issue = None

# Prepare output as JSON string
out = json.dumps(most_common_issue)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_9QJEnecrNns7O7ZL7gr2ApLR': [{'Id': '802Wt0000078wz5IAA'}, {'Id': '802Wt0000078xAAIAY'}, {'Id': '802Wt0000078yXgIAI'}, {'Id': '802Wt0000078yXiIAI'}, {'Id': '802Wt0000078ypSIAQ'}, {'Id': '802Wt000007906mIAA'}, {'Id': '#802Wt00000790WEIAY'}, {'Id': '802Wt00000792gDIAQ'}, {'Id': '802Wt00000792zTIAQ'}, {'Id': '#802Wt0000079315IAA'}, {'Id': '802Wt00000793sTIAQ'}, {'Id': '802Wt00000794F3IAI'}, {'Id': '802Wt00000794F4IAI'}, {'Id': '#802Wt00000794JmIAI'}, {'Id': '#802Wt00000794YFIAY'}, {'Id': '802Wt00000794YJIAY'}, {'Id': '802Wt00000794bTIAQ'}, {'Id': '#802Wt00000794bXIAQ'}, {'Id': '802Wt000007959OIAQ'}, {'Id': '802Wt000007959PIAQ'}, {'Id': '#802Wt00000795PSIAY'}, {'Id': '802Wt00000795UKIAY'}, {'Id': '802Wt00000795akIAA'}, {'Id': '802Wt00000795ywIAA'}, {'Id': '802Wt000007962JIAQ'}, {'Id': '802Wt000007968hIAA'}, {'Id': '802Wt000007968iIAA'}, {'Id': '802Wt00000796F5IAI'}, {'Id': '#802Wt00000796IIIAY'}, {'Id': '#802Wt00000796N7IAI'}, {'Id': '802Wt00000796NAIAY'}, {'Id': '802Wt00000796RzIAI'}, {'Id': '802Wt00000796S0IAI'}, {'Id': '802Wt00000796S1IAI'}, {'Id': '802Wt00000796VDIAY'}, {'Id': '802Wt00000796YPIAY'}, {'Id': '802Wt00000796YQIAY'}, {'Id': '802Wt00000796a1IAA'}, {'Id': '802Wt00000796dFIAQ'}, {'Id': '#802Wt00000796dIIAQ'}, {'Id': '#802Wt00000796jiIAA'}, {'Id': '802Wt00000796lKIAQ'}, {'Id': '802Wt00000796myIAA'}, {'Id': '802Wt00000796n0IAA'}, {'Id': '802Wt00000796oaIAA'}, {'Id': '802Wt00000796rlIAA'}, {'Id': '802Wt00000796tTIAQ'}, {'Id': '802Wt00000796v0IAA'}, {'Id': '802Wt00000796wbIAA'}, {'Id': '802Wt00000796wcIAA'}, {'Id': '802Wt000007979WIAQ'}, {'Id': '802Wt00000797FxIAI'}, {'Id': '802Wt00000797MQIAY'}, {'Id': '#802Wt00000797O5IAI'}, {'Id': '802Wt00000797RGIAY'}, {'Id': '802Wt00000797SsIAI'}, {'Id': '#802Wt00000797axIAA'}, {'Id': '802Wt00000797e9IAA'}, {'Id': '802Wt00000797hNIAQ'}, {'Id': '802Wt00000797j0IAA'}, {'Id': '#802Wt00000797mDIAQ'}, {'Id': '#802Wt00000797nqIAA'}, {'Id': '802Wt00000797nsIAA'}, {'Id': '#802Wt00000797pSIAQ'}, {'Id': '802Wt00000797sfIAA'}, {'Id': '802Wt00000797z8IAA'}, {'Id': '802Wt000007982LIAQ'}, {'Id': '#802Wt000007983xIAA'}, {'Id': '802Wt000007987CIAQ'}, {'Id': '802Wt00000798IUIAY'}, {'Id': '802Wt00000798IVIAY'}, {'Id': '802Wt00000798NKIAY'}, {'Id': '#802Wt00000798NMIAY'}, {'Id': '#802Wt00000798S9IAI'}, {'Id': '802Wt00000798iIIAQ'}, {'Id': '#802Wt00000798nBIAQ'}, {'Id': '802Wt00000798rxIAA'}, {'Id': '802Wt00000798wpIAA'}, {'Id': '802Wt000007991dIAA'}, {'Id': '802Wt0000079987IAA'}, {'Id': '802Wt00000799EZIAY'}, {'Id': '802Wt00000799EaIAI'}, {'Id': '802Wt00000799HoIAI'}, {'Id': '#802Wt00000799JPIAY'}, {'Id': '802Wt00000799T3IAI'}, {'Id': '#802Wt00000799b7IAA'}, {'Id': '802Wt00000799ckIAA'}, {'Id': '#802Wt00000799fxIAA'}, {'Id': '802Wt00000799srIAA'}, {'Id': '802Wt00000799w5IAA'}, {'Id': '#802Wt0000079A0wIAE'}, {'Id': '802Wt0000079A2aIAE'}, {'Id': '802Wt0000079A49IAE'}, {'Id': '802Wt0000079A7NIAU'}, {'Id': '802Wt0000079AU1IAM'}, {'Id': '#802Wt0000079AfJIAU'}, {'Id': '802Wt0000079AgrIAE'}, {'Id': '802Wt0000079AqXIAU'}, {'Id': '802Wt0000079As9IAE'}], 'var_call_rU8vXtbKSvnsXAgTcoX9ohbx': [], 'var_call_s3e5LJaF6nhejAmV9yD0Qcuj': [], 'var_call_fxEpbJH55Ae1zGc5BmyQ6QFF': [{'id': '#500Wt00000DDYpHIAX', 'issueid__c': 'a03Wt00000JqmX6IAJ', 'accountid': '#001Wt00000PHHXXIA5', 'createddate': '2022-09-05T11:15:00.000+0000'}, {'id': '#500Wt00000DDZtKIAX', 'issueid__c': 'a03Wt00000JqzPSIAZ', 'accountid': '001Wt00000PFj4zIAD', 'createddate': '2023-01-04T08:47:00.000+0000'}, {'id': '500Wt00000DDfx8IAD', 'issueid__c': 'a03Wt00000JqvNUIAZ', 'accountid': '001Wt00000PGdBuIAL', 'createddate': '2023-01-03T10:15:00.000+0000'}, {'id': '500Wt00000DDg20IAD', 'issueid__c': 'a03Wt00000JqhItIAJ', 'accountid': '#001Wt00000PHRTfIAP', 'createddate': '2022-12-01T10:00:00.000+0000'}, {'id': '500Wt00000DDxScIAL', 'issueid__c': 'a03Wt00000JqnHwIAJ', 'accountid': '001Wt00000PGtdJIAT', 'createddate': '2022-10-01T14:45:00.000+0000'}, {'id': '500Wt00000DDxduIAD', 'issueid__c': 'a03Wt00000JqnHwIAJ', 'accountid': '001Wt00000PGtdJIAT', 'createddate': '2022-09-16T09:30:00.000+0000'}, {'id': '#500Wt00000DDyznIAD', 'issueid__c': 'a03Wt00000JqxtvIAB', 'accountid': '001Wt00000PGaZCIA1', 'createddate': '2022-09-22T19:28:00.000+0000'}, {'id': '#500Wt00000DDzJ8IAL', 'issueid__c': 'a03Wt00000JqmX6IAJ', 'accountid': '001Wt00000PHHXXIA5', 'createddate': '2022-09-03T15:30:00.000+0000'}, {'id': '#500Wt00000DDzXeIAL', 'issueid__c': 'a03Wt00000JqnHwIAJ', 'accountid': '001Wt00000PHVtpIAH', 'createddate': '2022-09-05T14:45:00.000+0000'}, {'id': '500Wt00000DE0K1IAL', 'issueid__c': 'a03Wt00000JqnHwIAJ', 'accountid': '001Wt00000PHVtpIAH', 'createddate': '2022-10-15T11:00:00.000+0000'}], 'var_call_p8kmaxrNAd2eFpbbiwct1ng7': [{'id': '#500Wt00000DDYpHIAX', 'orderitemid__c': '802Wt00000790mNIAQ', 'issueid__c': 'a03Wt00000JqmX6IAJ', 'createddate': '2022-09-05T11:15:00.000+0000'}, {'id': '#500Wt00000DDZtKIAX', 'orderitemid__c': '802Wt00000799mPIAQ', 'issueid__c': 'a03Wt00000JqzPSIAZ', 'createddate': '2023-01-04T08:47:00.000+0000'}, {'id': '500Wt00000DDfx8IAD', 'orderitemid__c': '802Wt00000798K5IAI', 'issueid__c': 'a03Wt00000JqvNUIAZ', 'createddate': '2023-01-03T10:15:00.000+0000'}, {'id': '500Wt00000DDg20IAD', 'orderitemid__c': '802Wt00000793bTIAQ', 'issueid__c': 'a03Wt00000JqhItIAJ', 'createddate': '2022-12-01T10:00:00.000+0000'}, {'id': '500Wt00000DDxScIAL', 'orderitemid__c': '802Wt00000790WEIAY', 'issueid__c': 'a03Wt00000JqnHwIAJ', 'createddate': '2022-10-01T14:45:00.000+0000'}, {'id': '500Wt00000DDxduIAD', 'orderitemid__c': '802Wt00000790WEIAY', 'issueid__c': 'a03Wt00000JqnHwIAJ', 'createddate': '2022-09-16T09:30:00.000+0000'}, {'id': '#500Wt00000DDyznIAD', 'orderitemid__c': '802Wt000007928FIAQ', 'issueid__c': 'a03Wt00000JqxtvIAB', 'createddate': '2022-09-22T19:28:00.000+0000'}, {'id': '#500Wt00000DDzJ8IAL', 'orderitemid__c': '802Wt0000079A4AIAU', 'issueid__c': 'a03Wt00000JqmX6IAJ', 'createddate': '2022-09-03T15:30:00.000+0000'}, {'id': '#500Wt00000DDzXeIAL', 'orderitemid__c': '802Wt00000798olIAA', 'issueid__c': 'a03Wt00000JqnHwIAJ', 'createddate': '2022-09-05T14:45:00.000+0000'}, {'id': '500Wt00000DE0K1IAL', 'orderitemid__c': '802Wt00000798olIAA', 'issueid__c': 'a03Wt00000JqnHwIAJ', 'createddate': '2022-10-15T11:00:00.000+0000'}]}

exec(code, env_args)
