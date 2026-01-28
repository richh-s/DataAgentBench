code = """import json
from collections import defaultdict
rows = var_call_zYVd1u7ahGpzbdzSpAncVD38

totals = defaultdict(float)
for r in rows:
    owner = r.get('OwnerId')
    if owner is None:
        owner = r.get('OwnerID')
    if owner is None:
        continue
    owner = owner.strip()
    if owner.startswith('#'):
        owner = owner[1:]
    qty = r.get('Quantity', 0)
    price = r.get('UnitPrice', 0)
    try:
        q = float(qty)
    except Exception:
        q = 0.0
    try:
        p = float(price)
    except Exception:
        p = 0.0
    totals[owner] += q * p

if totals:
    top_agent = max(totals.items(), key=lambda x: x[1])[0]
else:
    top_agent = None

print("__RESULT__:")
print(json.dumps(top_agent))"""

env_args = {'var_call_UF1U5CnloF6osD3PTycq5g5k': ['Contract', 'Lead', 'Opportunity', 'OpportunityLineItem', 'Quote', 'QuoteLineItem'], 'var_call_zYVd1u7ahGpzbdzSpAncVD38': [{'OrderId': '#801Wt00000PFt7UIAT', 'AccountId': '001Wt00000PGzSaIAL', 'OwnerId': '005Wt000003NIiUIAW', 'EffectiveDate': '2022-09-15', 'OrderItemId': '802Wt0000078xq6IAA', 'Quantity': '8.0', 'UnitPrice': '569.9905'}, {'OrderId': '#801Wt00000PFt7UIAT', 'AccountId': '001Wt00000PGzSaIAL', 'OwnerId': '005Wt000003NIiUIAW', 'EffectiveDate': '2022-09-15', 'OrderItemId': '802Wt0000079A5lIAE', 'Quantity': '10.0', 'UnitPrice': '359.991'}, {'OrderId': '801Wt00000PFyITIA1', 'AccountId': '001Wt00000PGRnYIAX', 'OwnerId': '005Wt000003NDJ0IAO', 'EffectiveDate': '2022-07-10', 'OrderItemId': '802Wt00000797r3IAA', 'Quantity': '15.0', 'UnitPrice': '359.991'}, {'OrderId': '801Wt00000PFyITIA1', 'AccountId': '001Wt00000PGRnYIAX', 'OwnerId': '005Wt000003NDJ0IAO', 'EffectiveDate': '2022-07-10', 'OrderItemId': '802Wt00000797sfIAA', 'Quantity': '8.0', 'UnitPrice': '503.4905'}, {'OrderId': '801Wt00000PGGhBIAX', 'AccountId': '001Wt00000PHVtpIAH', 'OwnerId': '005Wt000003NIaRIAW', 'EffectiveDate': '2022-10-01', 'OrderItemId': '#802Wt000007953bIAA', 'Quantity': '14.0', 'UnitPrice': '476.991'}, {'OrderId': '801Wt00000PGGhBIAX', 'AccountId': '001Wt00000PHVtpIAH', 'OwnerId': '005Wt000003NIaRIAW', 'EffectiveDate': '2022-10-01', 'OrderItemId': '#802Wt0000079AP7IAM', 'Quantity': '10.0', 'UnitPrice': '359.991'}, {'OrderId': '801Wt00000PGGhBIAX', 'AccountId': '001Wt00000PHVtpIAH', 'OwnerId': '005Wt000003NIaRIAW', 'EffectiveDate': '2022-10-01', 'OrderItemId': '802Wt0000079ANVIA2', 'Quantity': '8.0', 'UnitPrice': '569.9905'}, {'OrderId': '#801Wt00000PGbdMIAT', 'AccountId': '#001Wt00000PGZgHIAX', 'OwnerId': '#005Wt000003NGtcIAG', 'EffectiveDate': '2022-07-01', 'OrderItemId': '802Wt00000791h9IAA', 'Quantity': '30.0', 'UnitPrice': '390.9915'}, {'OrderId': '#801Wt00000PGbdMIAT', 'AccountId': '#001Wt00000PGZgHIAX', 'OwnerId': '#005Wt000003NGtcIAG', 'EffectiveDate': '2022-07-01', 'OrderItemId': '802Wt00000794F3IAI', 'Quantity': '20.0', 'UnitPrice': '450.4915'}, {'OrderId': '801Wt00000PH4FMIA1', 'AccountId': '#001Wt00000PGZmfIAH', 'OwnerId': '#005Wt000003NJmbIAG', 'EffectiveDate': '2022-09-15', 'OrderItemId': '802Wt00000796S1IAI', 'Quantity': '10.0', 'UnitPrice': '476.991'}, {'OrderId': '801Wt00000PH8yvIAD', 'AccountId': '001Wt00000PGovMIAT', 'OwnerId': '005Wt000003NIXCIA4', 'EffectiveDate': '2022-07-01', 'OrderItemId': '802Wt00000794YHIAY', 'Quantity': '20.0', 'UnitPrice': '390.9915'}, {'OrderId': '801Wt00000PH8yvIAD', 'AccountId': '001Wt00000PGovMIAT', 'OwnerId': '005Wt000003NIXCIA4', 'EffectiveDate': '2022-07-01', 'OrderItemId': '802Wt000007968gIAA', 'Quantity': '50.0', 'UnitPrice': '450.4915'}, {'OrderId': '801Wt00000PH8yvIAD', 'AccountId': '001Wt00000PGovMIAT', 'OwnerId': '005Wt000003NIXCIA4', 'EffectiveDate': '2022-07-01', 'OrderItemId': '802Wt00000798YdIAI', 'Quantity': '30.0', 'UnitPrice': '552.4915'}, {'OrderId': '801Wt00000PHHMFIA5', 'AccountId': '001Wt00000PFsjOIAT', 'OwnerId': '005Wt000003NJ9uIAG', 'EffectiveDate': '2022-07-01', 'OrderItemId': '802Wt00000795XyIAI', 'Quantity': '3.0', 'UnitPrice': '499.99'}, {'OrderId': '801Wt00000PHHMFIA5', 'AccountId': '001Wt00000PFsjOIAT', 'OwnerId': '005Wt000003NJ9uIAG', 'EffectiveDate': '2022-07-01', 'OrderItemId': '802Wt00000796dJIAQ', 'Quantity': '1.0', 'UnitPrice': '399.99'}, {'OrderId': '801Wt00000PHHMFIA5', 'AccountId': '001Wt00000PFsjOIAT', 'OwnerId': '005Wt000003NJ9uIAG', 'EffectiveDate': '2022-07-01', 'OrderItemId': '802Wt00000799CwIAI', 'Quantity': '7.0', 'UnitPrice': '455.9905'}, {'OrderId': '801Wt00000PHHMFIA5', 'AccountId': '001Wt00000PFsjOIAT', 'OwnerId': '005Wt000003NJ9uIAG', 'EffectiveDate': '2022-07-01', 'OrderItemId': '802Wt00000799xhIAA', 'Quantity': '5.0', 'UnitPrice': '427.4905'}, {'OrderId': '801Wt00000PHHhDIAX', 'AccountId': '#001Wt00000PHVtpIAH', 'OwnerId': '#005Wt000003NITxIAO', 'EffectiveDate': '2022-08-01', 'OrderItemId': '#802Wt00000798olIAA', 'Quantity': '12.0', 'UnitPrice': '314.991'}, {'OrderId': '801Wt00000PHLzNIAX', 'AccountId': '001Wt00000PGtdJIAT', 'OwnerId': '005Wt000003NEoYIAW', 'EffectiveDate': '2022-09-15', 'OrderItemId': '#802Wt00000790WEIAY', 'Quantity': '12.0', 'UnitPrice': '476.991'}, {'OrderId': '801Wt00000PHLzNIAX', 'AccountId': '001Wt00000PGtdJIAT', 'OwnerId': '005Wt000003NEoYIAW', 'EffectiveDate': '2022-09-15', 'OrderItemId': '802Wt00000797PdIAI', 'Quantity': '10.0', 'UnitPrice': '449.991'}, {'OrderId': '801Wt00000PHLzNIAX', 'AccountId': '001Wt00000PGtdJIAT', 'OwnerId': '005Wt000003NEoYIAW', 'EffectiveDate': '2022-09-15', 'OrderItemId': '802Wt00000797RFIAY', 'Quantity': '8.0', 'UnitPrice': '569.9905'}, {'OrderId': '801Wt00000PHRFAIA5', 'AccountId': '001Wt00000PGdwiIAD', 'OwnerId': '#005Wt000003NIx1IAG', 'EffectiveDate': '2022-07-01', 'OrderItemId': '#802Wt0000078z8mIAA', 'Quantity': '7.0', 'UnitPrice': '379.9905'}, {'OrderId': '801Wt00000PHRFAIA5', 'AccountId': '001Wt00000PGdwiIAD', 'OwnerId': '#005Wt000003NIx1IAG', 'EffectiveDate': '2022-07-01', 'OrderItemId': '#802Wt00000797RIIAY', 'Quantity': '5.0', 'UnitPrice': '569.9905'}, {'OrderId': '801Wt00000PHRFAIA5', 'AccountId': '001Wt00000PGdwiIAD', 'OwnerId': '#005Wt000003NIx1IAG', 'EffectiveDate': '2022-07-01', 'OrderItemId': '802Wt00000796AJIAY', 'Quantity': '8.0', 'UnitPrice': '569.9905'}, {'OrderId': '801Wt00000PHRFAIA5', 'AccountId': '001Wt00000PGdwiIAD', 'OwnerId': '#005Wt000003NIx1IAG', 'EffectiveDate': '2022-07-01', 'OrderItemId': '802Wt00000796LWIAY', 'Quantity': '16.0', 'UnitPrice': '440.991'}, {'OrderId': '#801Wt00000PHVkDIAX', 'AccountId': '001Wt00000PGZZoIAP', 'OwnerId': '005Wt000003NJt3IAG', 'EffectiveDate': '2022-08-15', 'OrderItemId': '802Wt0000079Ak6IAE', 'Quantity': '3.0', 'UnitPrice': '599.99'}, {'OrderId': '801Wt00000PHVqfIAH', 'AccountId': '#001Wt00000PGzM9IAL', 'OwnerId': '005Wt000003NDEBIA4', 'EffectiveDate': '2022-09-20', 'OrderItemId': '802Wt000007937eIAA', 'Quantity': '10.0', 'UnitPrice': '539.991'}, {'OrderId': '#801Wt00000PHWptIAH', 'AccountId': '#001Wt00000PGYx5IAH', 'OwnerId': '005Wt000003NJ0EIAW', 'EffectiveDate': '2022-09-25', 'OrderItemId': '802Wt00000795xPIAQ', 'Quantity': '2.0', 'UnitPrice': '339.99'}, {'OrderId': '#801Wt00000PHWptIAH', 'AccountId': '#001Wt00000PGYx5IAH', 'OwnerId': '005Wt000003NJ0EIAW', 'EffectiveDate': '2022-09-25', 'OrderItemId': '802Wt0000079987IAA', 'Quantity': '3.0', 'UnitPrice': '529.99'}]}

exec(code, env_args)
