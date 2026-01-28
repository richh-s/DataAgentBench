code = """import json
rows = var_call_gjkIdstCPsUNZNtTecQbewkw
ids = []
for r in rows:
    v = r.get('Id','')
    if v is None:
        continue
    v = v.strip()
    if v.startswith('#'):
        v = v[1:]
    v = v.strip()
    if v:
        ids.append(v)
# dedupe
ids = sorted(set(ids))
# build SQL IN list
if not ids:
    in_list = "('')"
else:
    in_list = '(' + ','.join("'{}'".format(x.replace("'","''")) for x in ids) + ')'
start = '2022-08-16'
end = '2023-01-16'
query = (
    'SELECT issueid__c, COUNT(*) AS cnt FROM "Case" '
    'WHERE replace(trim(orderitemid__c),\'#\',\'\') IN ' + in_list + ' '
    "AND createddate >= '" + start + "' AND createddate <= '" + end + "' "
    'GROUP BY issueid__c ORDER BY cnt DESC LIMIT 1;'
)
print('__RESULT__:')
print(json.dumps(query))"""

env_args = {'var_call_gjkIdstCPsUNZNtTecQbewkw': [{'Id': '802Wt0000078wz5IAA'}, {'Id': '802Wt0000078xAAIAY'}, {'Id': '802Wt0000078yXgIAI'}, {'Id': '802Wt0000078yXiIAI'}, {'Id': '802Wt0000078ypSIAQ'}, {'Id': '802Wt000007906mIAA'}, {'Id': '#802Wt00000790WEIAY'}, {'Id': '802Wt00000792gDIAQ'}, {'Id': '802Wt00000792zTIAQ'}, {'Id': '#802Wt0000079315IAA'}, {'Id': '802Wt00000793sTIAQ'}, {'Id': '802Wt00000794F3IAI'}, {'Id': '802Wt00000794F4IAI'}, {'Id': '#802Wt00000794JmIAI'}, {'Id': '#802Wt00000794YFIAY'}, {'Id': '802Wt00000794YJIAY'}, {'Id': '802Wt00000794bTIAQ'}, {'Id': '#802Wt00000794bXIAQ'}, {'Id': '802Wt000007959OIAQ'}, {'Id': '802Wt000007959PIAQ'}, {'Id': '#802Wt00000795PSIAY'}, {'Id': '802Wt00000795UKIAY'}, {'Id': '802Wt00000795akIAA'}, {'Id': '802Wt00000795ywIAA'}, {'Id': '802Wt000007962JIAQ'}, {'Id': '802Wt000007968hIAA'}, {'Id': '802Wt000007968iIAA'}, {'Id': '802Wt00000796F5IAI'}, {'Id': '#802Wt00000796IIIAY'}, {'Id': '#802Wt00000796N7IAI'}, {'Id': '802Wt00000796NAIAY'}, {'Id': '802Wt00000796RzIAI'}, {'Id': '802Wt00000796S0IAI'}, {'Id': '802Wt00000796S1IAI'}, {'Id': '802Wt00000796VDIAY'}, {'Id': '802Wt00000796YPIAY'}, {'Id': '802Wt00000796YQIAY'}, {'Id': '802Wt00000796a1IAA'}, {'Id': '802Wt00000796dFIAQ'}, {'Id': '#802Wt00000796dIIAQ'}, {'Id': '#802Wt00000796jiIAA'}, {'Id': '802Wt00000796lKIAQ'}, {'Id': '802Wt00000796myIAA'}, {'Id': '802Wt00000796n0IAA'}, {'Id': '802Wt00000796oaIAA'}, {'Id': '802Wt00000796rlIAA'}, {'Id': '802Wt00000796tTIAQ'}, {'Id': '802Wt00000796v0IAA'}, {'Id': '802Wt00000796wbIAA'}, {'Id': '802Wt00000796wcIAA'}, {'Id': '802Wt000007979WIAQ'}, {'Id': '802Wt00000797FxIAI'}, {'Id': '802Wt00000797MQIAY'}, {'Id': '#802Wt00000797O5IAI'}, {'Id': '802Wt00000797RGIAY'}, {'Id': '802Wt00000797SsIAI'}, {'Id': '#802Wt00000797axIAA'}, {'Id': '802Wt00000797e9IAA'}, {'Id': '802Wt00000797hNIAQ'}, {'Id': '802Wt00000797j0IAA'}, {'Id': '#802Wt00000797mDIAQ'}, {'Id': '#802Wt00000797nqIAA'}, {'Id': '802Wt00000797nsIAA'}, {'Id': '#802Wt00000797pSIAQ'}, {'Id': '802Wt00000797sfIAA'}, {'Id': '802Wt00000797z8IAA'}, {'Id': '802Wt000007982LIAQ'}, {'Id': '#802Wt000007983xIAA'}, {'Id': '802Wt000007987CIAQ'}, {'Id': '802Wt00000798IUIAY'}, {'Id': '802Wt00000798IVIAY'}, {'Id': '802Wt00000798NKIAY'}, {'Id': '#802Wt00000798NMIAY'}, {'Id': '#802Wt00000798S9IAI'}, {'Id': '802Wt00000798iIIAQ'}, {'Id': '#802Wt00000798nBIAQ'}, {'Id': '802Wt00000798rxIAA'}, {'Id': '802Wt00000798wpIAA'}, {'Id': '802Wt000007991dIAA'}, {'Id': '802Wt0000079987IAA'}, {'Id': '802Wt00000799EZIAY'}, {'Id': '802Wt00000799EaIAI'}, {'Id': '802Wt00000799HoIAI'}, {'Id': '#802Wt00000799JPIAY'}, {'Id': '802Wt00000799T3IAI'}, {'Id': '#802Wt00000799b7IAA'}, {'Id': '802Wt00000799ckIAA'}, {'Id': '#802Wt00000799fxIAA'}, {'Id': '802Wt00000799srIAA'}, {'Id': '802Wt00000799w5IAA'}, {'Id': '#802Wt0000079A0wIAE'}, {'Id': '802Wt0000079A2aIAE'}, {'Id': '802Wt0000079A49IAE'}, {'Id': '802Wt0000079A7NIAU'}, {'Id': '802Wt0000079AU1IAM'}, {'Id': '#802Wt0000079AfJIAU'}, {'Id': '802Wt0000079AgrIAE'}, {'Id': '802Wt0000079AqXIAU'}, {'Id': '802Wt0000079As9IAE'}], 'var_call_V8SEs6RPmlFSrCDUSrkA7sxG': 'SELECT issueid__c, COUNT(*) AS cnt FROM "Case" WHERE replace(trim(orderitemid__c),AND createddate >=  + start +  AND createddate <=  + end +  GROUP BY issueid__c ORDER BY cnt DESC LIMIT 1;'}

exec(code, env_args)
