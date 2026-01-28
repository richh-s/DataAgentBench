code = """import json
import pandas as pd
from datetime import datetime, timezone
# load data
opp = var_call_NjiNkjD6EtajM2ornP9y4KY3
contracts = var_call_otCiXm0MgTJkJLUeLvmdo0Dn
# build contract map
contract_map = {}
for c in contracts:
    cid = c.get('Id')
    if cid is None:
        continue
    nid = cid.strip()
    if nid.startswith('#'):
        nid = nid.lstrip('#')
    contract_map[nid] = c.get('CompanySignedDate')

owner_deltas = {}
for r in opp:
    cid = r.get('ContractID__c')
    if cid is None:
        continue
    if isinstance(cid, str) and cid.strip().lower() == 'none':
        continue
    ncid = cid.strip()
    if ncid.startswith('#'):
        ncid = ncid.lstrip('#')
    csd = contract_map.get(ncid)
    if not csd:
        continue
    # parse company signed date as date (no tz)
    try:
        comp_date = pd.to_datetime(csd).to_pydatetime()
        # make naive by removing tzinfo if any
        if comp_date.tzinfo is not None:
            comp_date = comp_date.replace(tzinfo=None)
    except Exception:
        continue
    cd = r.get('CreatedDate')
    if not cd:
        continue
    try:
        created = pd.to_datetime(cd).to_pydatetime()
        # created has timezone offset in string; convert to naive UTC and then to date
        if created.tzinfo is not None:
            created = created.astimezone(timezone.utc).replace(tzinfo=None)
    except Exception:
        continue
    delta_days = (comp_date - created).total_seconds() / 86400.0
    owner = r.get('OwnerId')
    if owner is None:
        continue
    nowner = owner.strip()
    if nowner.startswith('#'):
        nowner = nowner.lstrip('#')
    owner_deltas.setdefault(nowner, []).append(delta_days)

owner_avg = {}
for o, vals in owner_deltas.items():
    if len(vals) == 0:
        continue
    owner_avg[o] = sum(vals) / len(vals)

if not owner_avg:
    result = None
else:
    min_owner = min(owner_avg.items(), key=lambda x: x[1])[0]
    result = min_owner

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_NjiNkjD6EtajM2ornP9y4KY3': [{'Id': '#006Wt000007B1klIAC', 'OwnerId': '#005Wt000003NBylIAG', 'CreatedDate': '2023-04-15T09:00:34.000+0000', 'ContractID__c': 'None'}, {'Id': '006Wt000007B49NIAS', 'OwnerId': '005Wt000003NIs9IAG', 'CreatedDate': '2023-04-25T14:32:51.000+0000', 'ContractID__c': 'None'}, {'Id': '006Wt000007B62sIAC', 'OwnerId': '005Wt000003NJZhIAO', 'CreatedDate': '2023-04-04T10:15:30.000+0000', 'ContractID__c': 'None'}, {'Id': '006Wt000007B6itIAC', 'OwnerId': '#005Wt000003NJMnIAO', 'CreatedDate': '2023-04-25T09:45:30.000+0000', 'ContractID__c': 'None'}, {'Id': '#006Wt000007B7tQIAS', 'OwnerId': '005Wt000003NIfGIAW', 'CreatedDate': '2023-04-15T10:20:30.000+0000', 'ContractID__c': 'None'}, {'Id': '#006Wt000007B7yJIAS', 'OwnerId': '#005Wt000003NEdJIAW', 'CreatedDate': '2023-04-15T10:30:45.000+0000', 'ContractID__c': 'None'}, {'Id': '006Wt000007B8CqIAK', 'OwnerId': '005Wt000003NInKIAW', 'CreatedDate': '2023-04-15T09:30:45.000+0000', 'ContractID__c': 'None'}, {'Id': '#006Wt000007B8FyIAK', 'OwnerId': '005Wt000003NIovIAG', 'CreatedDate': '2023-04-15T10:30:15.000+0000', 'ContractID__c': 'None'}, {'Id': '#006Wt000007BA3JIAW', 'OwnerId': '005Wt000003NF9WIAW', 'CreatedDate': '2023-04-02T10:15:30.000+0000', 'ContractID__c': 'None'}, {'Id': '006Wt000007BABLIA4', 'OwnerId': '005Wt000003NDEBIA4', 'CreatedDate': '2023-04-01T14:47:23.000+0000', 'ContractID__c': 'None'}, {'Id': '006Wt000007BAHlIAO', 'OwnerId': '#005Wt000003NFhPIAW', 'CreatedDate': '2023-04-19T15:30:45.000+0000', 'ContractID__c': 'None'}, {'Id': '006Wt000007BAPrIAO', 'OwnerId': '005Wt000003NJxtIAG', 'CreatedDate': '2023-04-15T10:15:32.000+0000', 'ContractID__c': 'None'}, {'Id': '006Wt000007BBDrIAO', 'OwnerId': '005Wt000003NJ1pIAG', 'CreatedDate': '2023-04-10T10:30:15.000+0000', 'ContractID__c': 'None'}, {'Id': '006Wt000007BBc1IAG', 'OwnerId': '005Wt000003NEtPIAW', 'CreatedDate': '2023-04-15T10:14:32.000+0000', 'ContractID__c': 'None'}, {'Id': '006Wt000007BCLEIA4', 'OwnerId': '005Wt000003NJBVIA4', 'CreatedDate': '2023-04-27T11:22:30.000+0000', 'ContractID__c': 'None'}, {'Id': '006Wt000007BCTFIA4', 'OwnerId': '#005Wt000003NBcBIAW', 'CreatedDate': '2023-04-20T11:15:33.000+0000', 'ContractID__c': 'None'}, {'Id': '#006Wt000007BChmIAG', 'OwnerId': '005Wt000003NJgAIAW', 'CreatedDate': '2023-04-25T10:45:30.000+0000', 'ContractID__c': '800Wt00000DE9FFIA1'}, {'Id': '006Wt000007BDApIAO', 'OwnerId': '005Wt000003NISMIA4', 'CreatedDate': '2023-04-10T10:15:30.000+0000', 'ContractID__c': '800Wt00000DE8sgIAD'}, {'Id': '#006Wt000007BDXPIA4', 'OwnerId': '005Wt000003NJ0EIAW', 'CreatedDate': '2023-04-15T10:45:00.000+0000', 'ContractID__c': 'None'}, {'Id': '006Wt000007BDcEIAW', 'OwnerId': '005Wt000003NIAbIAO', 'CreatedDate': '2023-04-15T10:32:45.000+0000', 'ContractID__c': 'None'}, {'Id': '006Wt000007BDpAIAW', 'OwnerId': '005Wt000003NEtPIAW', 'CreatedDate': '2023-04-15T10:30:15.000+0000', 'ContractID__c': 'None'}, {'Id': '006Wt000007BETVIA4', 'OwnerId': '#005Wt000003NJjNIAW', 'CreatedDate': '2023-04-20T11:34:22.000+0000', 'ContractID__c': 'None'}, {'Id': '#006Wt000007BEV4IAO', 'OwnerId': '005Wt000003NFRKIA4', 'CreatedDate': '2023-04-05T14:23:45.000+0000', 'ContractID__c': 'None'}, {'Id': '006Wt000007BFUOIA4', 'OwnerId': '005Wt000003NHpdIAG', 'CreatedDate': '2023-04-05T10:15:30.000+0000', 'ContractID__c': 'None'}, {'Id': '006Wt000007BGAIIA4', 'OwnerId': '005Wt000003NIdeIAG', 'CreatedDate': '2023-04-11T12:45:33.000+0000', 'ContractID__c': 'None'}, {'Id': '#006Wt000007BGDVIA4', 'OwnerId': '005Wt000003NBcBIAW', 'CreatedDate': '2023-04-10T11:20:45.000+0000', 'ContractID__c': 'None'}, {'Id': '006Wt000007BHPhIAO', 'OwnerId': '#005Wt000003NEa3IAG', 'CreatedDate': '2023-04-15T09:12:34.000+0000', 'ContractID__c': '800Wt00000DE9ryIAD'}, {'Id': '#006Wt000007BHZNIA4', 'OwnerId': '005Wt000003NIaPIAW', 'CreatedDate': '2023-04-10T14:25:30.000+0000', 'ContractID__c': 'None'}, {'Id': '#006Wt000007BHfpIAG', 'OwnerId': '005Wt000003NIqXIAW', 'CreatedDate': '2023-04-17T14:37:45.000+0000', 'ContractID__c': 'None'}, {'Id': '006Wt000007BHr7IAG', 'OwnerId': '005Wt000003NIfGIAW', 'CreatedDate': '2023-04-01T09:45:23.000+0000', 'ContractID__c': 'None'}], 'var_call_otCiXm0MgTJkJLUeLvmdo0Dn': [{'Id': '800Wt00000DE8sgIAD', 'CompanySignedDate': '2023-10-13'}, {'Id': '800Wt00000DE9ryIAD', 'CompanySignedDate': '2023-09-30'}], 'var_call_DDdu8l8hIXA0Dn4XQaXceCwS': ['800Wt00000DE8sgIAD', '800Wt00000DE9FFIA1', '800Wt00000DE9ryIAD']}

exec(code, env_args)
