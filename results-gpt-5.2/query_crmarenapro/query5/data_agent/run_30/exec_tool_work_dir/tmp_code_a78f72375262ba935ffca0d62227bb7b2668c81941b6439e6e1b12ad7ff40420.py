code = """import json

orderitems = var_call_5vODk9ciguoNDh6l4PtsZSjy
cases = var_call_D5Ju66Ga12fQ5gJbs2m3PUe8

# Clean IDs: remove leading '#', trim whitespace
prod_orderitem_ids = set()
for r in orderitems:
    oid = (r.get('orderitem_id') or '').strip()
    if oid.startswith('#'):
        oid = oid[1:]
    if oid:
        prod_orderitem_ids.add(oid)

counts = {}
for r in cases:
    oid = (r.get('orderitem_id') or '').strip()
    if oid.startswith('#'):
        oid = oid[1:]
    if oid not in prod_orderitem_ids:
        continue
    issue = (r.get('issue_id') or '').strip()
    if issue.startswith('#'):
        issue = issue[1:]
    if not issue:
        continue
    counts[issue] = counts.get(issue, 0) + 1

# get top issue id by count, tie-breaker lexicographically for determinism
best_issue = None
best_cnt = -1
for issue, cnt in counts.items():
    if cnt > best_cnt or (cnt == best_cnt and (best_issue is None or issue < best_issue)):
        best_issue = issue
        best_cnt = cnt

print('__RESULT__:')
print(json.dumps({'issue_id': best_issue, 'count': best_cnt}))"""

env_args = {'var_call_5vODk9ciguoNDh6l4PtsZSjy': [{'orderitem_id': '802Wt0000078wz5IAA'}, {'orderitem_id': '802Wt0000078xAAIAY'}, {'orderitem_id': '802Wt0000078yXgIAI'}, {'orderitem_id': '802Wt0000078yXiIAI'}, {'orderitem_id': '802Wt0000078ypSIAQ'}, {'orderitem_id': '802Wt000007906mIAA'}, {'orderitem_id': '#802Wt00000790WEIAY'}, {'orderitem_id': '802Wt00000792gDIAQ'}, {'orderitem_id': '802Wt00000792zTIAQ'}, {'orderitem_id': '#802Wt0000079315IAA'}, {'orderitem_id': '802Wt00000793sTIAQ'}, {'orderitem_id': '802Wt00000794F3IAI'}, {'orderitem_id': '802Wt00000794F4IAI'}, {'orderitem_id': '#802Wt00000794JmIAI'}, {'orderitem_id': '#802Wt00000794YFIAY'}, {'orderitem_id': '802Wt00000794YJIAY'}, {'orderitem_id': '802Wt00000794bTIAQ'}, {'orderitem_id': '#802Wt00000794bXIAQ'}, {'orderitem_id': '802Wt000007959OIAQ'}, {'orderitem_id': '802Wt000007959PIAQ'}, {'orderitem_id': '#802Wt00000795PSIAY'}, {'orderitem_id': '802Wt00000795UKIAY'}, {'orderitem_id': '802Wt00000795akIAA'}, {'orderitem_id': '802Wt00000795ywIAA'}, {'orderitem_id': '802Wt000007962JIAQ'}, {'orderitem_id': '802Wt000007968hIAA'}, {'orderitem_id': '802Wt000007968iIAA'}, {'orderitem_id': '802Wt00000796F5IAI'}, {'orderitem_id': '#802Wt00000796IIIAY'}, {'orderitem_id': '#802Wt00000796N7IAI'}, {'orderitem_id': '802Wt00000796NAIAY'}, {'orderitem_id': '802Wt00000796RzIAI'}, {'orderitem_id': '802Wt00000796S0IAI'}, {'orderitem_id': '802Wt00000796S1IAI'}, {'orderitem_id': '802Wt00000796VDIAY'}, {'orderitem_id': '802Wt00000796YPIAY'}, {'orderitem_id': '802Wt00000796YQIAY'}, {'orderitem_id': '802Wt00000796a1IAA'}, {'orderitem_id': '802Wt00000796dFIAQ'}, {'orderitem_id': '#802Wt00000796dIIAQ'}, {'orderitem_id': '#802Wt00000796jiIAA'}, {'orderitem_id': '802Wt00000796lKIAQ'}, {'orderitem_id': '802Wt00000796myIAA'}, {'orderitem_id': '802Wt00000796n0IAA'}, {'orderitem_id': '802Wt00000796oaIAA'}, {'orderitem_id': '802Wt00000796rlIAA'}, {'orderitem_id': '802Wt00000796tTIAQ'}, {'orderitem_id': '802Wt00000796v0IAA'}, {'orderitem_id': '802Wt00000796wbIAA'}, {'orderitem_id': '802Wt00000796wcIAA'}, {'orderitem_id': '802Wt000007979WIAQ'}, {'orderitem_id': '802Wt00000797FxIAI'}, {'orderitem_id': '802Wt00000797MQIAY'}, {'orderitem_id': '#802Wt00000797O5IAI'}, {'orderitem_id': '802Wt00000797RGIAY'}, {'orderitem_id': '802Wt00000797SsIAI'}, {'orderitem_id': '#802Wt00000797axIAA'}, {'orderitem_id': '802Wt00000797e9IAA'}, {'orderitem_id': '802Wt00000797hNIAQ'}, {'orderitem_id': '802Wt00000797j0IAA'}, {'orderitem_id': '#802Wt00000797mDIAQ'}, {'orderitem_id': '#802Wt00000797nqIAA'}, {'orderitem_id': '802Wt00000797nsIAA'}, {'orderitem_id': '#802Wt00000797pSIAQ'}, {'orderitem_id': '802Wt00000797sfIAA'}, {'orderitem_id': '802Wt00000797z8IAA'}, {'orderitem_id': '802Wt000007982LIAQ'}, {'orderitem_id': '#802Wt000007983xIAA'}, {'orderitem_id': '802Wt000007987CIAQ'}, {'orderitem_id': '802Wt00000798IUIAY'}, {'orderitem_id': '802Wt00000798IVIAY'}, {'orderitem_id': '802Wt00000798NKIAY'}, {'orderitem_id': '#802Wt00000798NMIAY'}, {'orderitem_id': '#802Wt00000798S9IAI'}, {'orderitem_id': '802Wt00000798iIIAQ'}, {'orderitem_id': '#802Wt00000798nBIAQ'}, {'orderitem_id': '802Wt00000798rxIAA'}, {'orderitem_id': '802Wt00000798wpIAA'}, {'orderitem_id': '802Wt000007991dIAA'}, {'orderitem_id': '802Wt0000079987IAA'}, {'orderitem_id': '802Wt00000799EZIAY'}, {'orderitem_id': '802Wt00000799EaIAI'}, {'orderitem_id': '802Wt00000799HoIAI'}, {'orderitem_id': '#802Wt00000799JPIAY'}, {'orderitem_id': '802Wt00000799T3IAI'}, {'orderitem_id': '#802Wt00000799b7IAA'}, {'orderitem_id': '802Wt00000799ckIAA'}, {'orderitem_id': '#802Wt00000799fxIAA'}, {'orderitem_id': '802Wt00000799srIAA'}, {'orderitem_id': '802Wt00000799w5IAA'}, {'orderitem_id': '#802Wt0000079A0wIAE'}, {'orderitem_id': '802Wt0000079A2aIAE'}, {'orderitem_id': '802Wt0000079A49IAE'}, {'orderitem_id': '802Wt0000079A7NIAU'}, {'orderitem_id': '802Wt0000079AU1IAM'}, {'orderitem_id': '#802Wt0000079AfJIAU'}, {'orderitem_id': '802Wt0000079AgrIAE'}, {'orderitem_id': '802Wt0000079AqXIAU'}, {'orderitem_id': '802Wt0000079As9IAE'}], 'var_call_j6e2pQ4yevMo4PbBKqUyGYnt': [{'issue_id': 'a03Wt00000JqmX6IAJ', 'createddate': '2022-09-05T11:15:00.000+0000'}, {'issue_id': 'a03Wt00000JqzPSIAZ', 'createddate': '2023-01-04T08:47:00.000+0000'}, {'issue_id': 'a03Wt00000JqvNUIAZ', 'createddate': '2023-01-03T10:15:00.000+0000'}, {'issue_id': 'a03Wt00000JqhItIAJ', 'createddate': '2022-12-01T10:00:00.000+0000'}, {'issue_id': 'a03Wt00000JqnHwIAJ', 'createddate': '2022-10-01T14:45:00.000+0000'}, {'issue_id': 'a03Wt00000JqnHwIAJ', 'createddate': '2022-09-16T09:30:00.000+0000'}, {'issue_id': 'a03Wt00000JqxtvIAB', 'createddate': '2022-09-22T19:28:00.000+0000'}, {'issue_id': 'a03Wt00000JqmX6IAJ', 'createddate': '2022-09-03T15:30:00.000+0000'}, {'issue_id': 'a03Wt00000JqnHwIAJ', 'createddate': '2022-09-05T14:45:00.000+0000'}, {'issue_id': 'a03Wt00000JqnHwIAJ', 'createddate': '2022-10-15T11:00:00.000+0000'}], 'var_call_D5Ju66Ga12fQ5gJbs2m3PUe8': [{'orderitem_id': '802Wt00000790mNIAQ', 'issue_id': 'a03Wt00000JqmX6IAJ'}, {'orderitem_id': '802Wt00000799mPIAQ', 'issue_id': 'a03Wt00000JqzPSIAZ'}, {'orderitem_id': '802Wt00000798K5IAI', 'issue_id': 'a03Wt00000JqvNUIAZ'}, {'orderitem_id': '802Wt00000793bTIAQ', 'issue_id': 'a03Wt00000JqhItIAJ'}, {'orderitem_id': '802Wt00000790WEIAY', 'issue_id': 'a03Wt00000JqnHwIAJ'}, {'orderitem_id': '802Wt00000790WEIAY', 'issue_id': 'a03Wt00000JqnHwIAJ'}, {'orderitem_id': '802Wt000007928FIAQ', 'issue_id': 'a03Wt00000JqxtvIAB'}, {'orderitem_id': '802Wt0000079A4AIAU', 'issue_id': 'a03Wt00000JqmX6IAJ'}, {'orderitem_id': '802Wt00000798olIAA', 'issue_id': 'a03Wt00000JqnHwIAJ'}, {'orderitem_id': '802Wt00000798olIAA', 'issue_id': 'a03Wt00000JqnHwIAJ'}]}

exec(code, env_args)
