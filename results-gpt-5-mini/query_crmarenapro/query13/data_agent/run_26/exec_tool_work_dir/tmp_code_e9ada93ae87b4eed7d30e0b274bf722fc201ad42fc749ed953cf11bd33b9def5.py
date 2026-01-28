code = """import json
import math

records = var_call_P9iUPcQrfqbCI2AeiP5gOvSp

sums = {}

for r in records:
    owner = r.get('OrderOwnerId')
    if owner is None:
        continue
    owner = owner.strip()
    if owner.startswith('#'):
        owner = owner[1:]
    # normalize
    try:
        qty = float(r.get('Quantity') or 0)
    except:
        # try to clean
        try:
            qty = float(str(r.get('Quantity')).strip())
        except:
            qty = 0.0
    try:
        price = float(r.get('UnitPrice') or 0)
    except:
        try:
            price = float(str(r.get('UnitPrice')).strip())
        except:
            price = 0.0
    amount = qty * price
    # avoid NaN
    if amount is None or (isinstance(amount, float) and (math.isnan(amount) or math.isinf(amount))):
        amount = 0.0
    sums[owner] = sums.get(owner, 0.0) + amount

# find max
if not sums:
    top_agent = None
else:
    # sort by amount desc, then by owner id
    top_agent = max(sums.items(), key=lambda x: (x[1], x[0]))[0]

print("__RESULT__:")
print(json.dumps(top_agent))"""

env_args = {'var_call_rjxYtssl9b7B7DskfsqOiVjo': ['ProductCategory', 'Product2', 'ProductCategoryProduct', 'Pricebook2', 'PricebookEntry', 'Order', 'OrderItem'], 'var_call_P9iUPcQrfqbCI2AeiP5gOvSp': [{'OrderId': '#801Wt00000PFt7UIAT', 'OrderOwnerId': '005Wt000003NIiUIAW', 'AccountId': '001Wt00000PGzSaIAL', 'EffectiveDate': '2022-09-15', 'OrderItemId': '802Wt0000078xq6IAA', 'Quantity': '8.0', 'UnitPrice': '569.9905'}, {'OrderId': '#801Wt00000PFt7UIAT', 'OrderOwnerId': '005Wt000003NIiUIAW', 'AccountId': '001Wt00000PGzSaIAL', 'EffectiveDate': '2022-09-15', 'OrderItemId': '802Wt0000079A5lIAE', 'Quantity': '10.0', 'UnitPrice': '359.991'}, {'OrderId': '801Wt00000PFyITIA1', 'OrderOwnerId': '005Wt000003NDJ0IAO', 'AccountId': '001Wt00000PGRnYIAX', 'EffectiveDate': '2022-07-10', 'OrderItemId': '802Wt00000797r3IAA', 'Quantity': '15.0', 'UnitPrice': '359.991'}, {'OrderId': '801Wt00000PFyITIA1', 'OrderOwnerId': '005Wt000003NDJ0IAO', 'AccountId': '001Wt00000PGRnYIAX', 'EffectiveDate': '2022-07-10', 'OrderItemId': '802Wt00000797sfIAA', 'Quantity': '8.0', 'UnitPrice': '503.4905'}, {'OrderId': '801Wt00000PGGhBIAX', 'OrderOwnerId': '005Wt000003NIaRIAW', 'AccountId': '001Wt00000PHVtpIAH', 'EffectiveDate': '2022-10-01', 'OrderItemId': '#802Wt000007953bIAA', 'Quantity': '14.0', 'UnitPrice': '476.991'}, {'OrderId': '801Wt00000PGGhBIAX', 'OrderOwnerId': '005Wt000003NIaRIAW', 'AccountId': '001Wt00000PHVtpIAH', 'EffectiveDate': '2022-10-01', 'OrderItemId': '#802Wt0000079AP7IAM', 'Quantity': '10.0', 'UnitPrice': '359.991'}, {'OrderId': '801Wt00000PGGhBIAX', 'OrderOwnerId': '005Wt000003NIaRIAW', 'AccountId': '001Wt00000PHVtpIAH', 'EffectiveDate': '2022-10-01', 'OrderItemId': '802Wt0000079ANVIA2', 'Quantity': '8.0', 'UnitPrice': '569.9905'}, {'OrderId': '#801Wt00000PGbdMIAT', 'OrderOwnerId': '#005Wt000003NGtcIAG', 'AccountId': '#001Wt00000PGZgHIAX', 'EffectiveDate': '2022-07-01', 'OrderItemId': '802Wt00000791h9IAA', 'Quantity': '30.0', 'UnitPrice': '390.9915'}, {'OrderId': '#801Wt00000PGbdMIAT', 'OrderOwnerId': '#005Wt000003NGtcIAG', 'AccountId': '#001Wt00000PGZgHIAX', 'EffectiveDate': '2022-07-01', 'OrderItemId': '802Wt00000794F3IAI', 'Quantity': '20.0', 'UnitPrice': '450.4915'}, {'OrderId': '801Wt00000PH4FMIA1', 'OrderOwnerId': '#005Wt000003NJmbIAG', 'AccountId': '#001Wt00000PGZmfIAH', 'EffectiveDate': '2022-09-15', 'OrderItemId': '802Wt00000796S1IAI', 'Quantity': '10.0', 'UnitPrice': '476.991'}, {'OrderId': '801Wt00000PH8yvIAD', 'OrderOwnerId': '005Wt000003NIXCIA4', 'AccountId': '001Wt00000PGovMIAT', 'EffectiveDate': '2022-07-01', 'OrderItemId': '802Wt00000794YHIAY', 'Quantity': '20.0', 'UnitPrice': '390.9915'}, {'OrderId': '801Wt00000PH8yvIAD', 'OrderOwnerId': '005Wt000003NIXCIA4', 'AccountId': '001Wt00000PGovMIAT', 'EffectiveDate': '2022-07-01', 'OrderItemId': '802Wt000007968gIAA', 'Quantity': '50.0', 'UnitPrice': '450.4915'}, {'OrderId': '801Wt00000PH8yvIAD', 'OrderOwnerId': '005Wt000003NIXCIA4', 'AccountId': '001Wt00000PGovMIAT', 'EffectiveDate': '2022-07-01', 'OrderItemId': '802Wt00000798YdIAI', 'Quantity': '30.0', 'UnitPrice': '552.4915'}, {'OrderId': '801Wt00000PHHMFIA5', 'OrderOwnerId': '005Wt000003NJ9uIAG', 'AccountId': '001Wt00000PFsjOIAT', 'EffectiveDate': '2022-07-01', 'OrderItemId': '802Wt00000795XyIAI', 'Quantity': '3.0', 'UnitPrice': '499.99'}, {'OrderId': '801Wt00000PHHMFIA5', 'OrderOwnerId': '005Wt000003NJ9uIAG', 'AccountId': '001Wt00000PFsjOIAT', 'EffectiveDate': '2022-07-01', 'OrderItemId': '802Wt00000796dJIAQ', 'Quantity': '1.0', 'UnitPrice': '399.99'}, {'OrderId': '801Wt00000PHHMFIA5', 'OrderOwnerId': '005Wt000003NJ9uIAG', 'AccountId': '001Wt00000PFsjOIAT', 'EffectiveDate': '2022-07-01', 'OrderItemId': '802Wt00000799CwIAI', 'Quantity': '7.0', 'UnitPrice': '455.9905'}, {'OrderId': '801Wt00000PHHMFIA5', 'OrderOwnerId': '005Wt000003NJ9uIAG', 'AccountId': '001Wt00000PFsjOIAT', 'EffectiveDate': '2022-07-01', 'OrderItemId': '802Wt00000799xhIAA', 'Quantity': '5.0', 'UnitPrice': '427.4905'}, {'OrderId': '801Wt00000PHHhDIAX', 'OrderOwnerId': '#005Wt000003NITxIAO', 'AccountId': '#001Wt00000PHVtpIAH', 'EffectiveDate': '2022-08-01', 'OrderItemId': '#802Wt00000798olIAA', 'Quantity': '12.0', 'UnitPrice': '314.991'}, {'OrderId': '801Wt00000PHLzNIAX', 'OrderOwnerId': '005Wt000003NEoYIAW', 'AccountId': '001Wt00000PGtdJIAT', 'EffectiveDate': '2022-09-15', 'OrderItemId': '#802Wt00000790WEIAY', 'Quantity': '12.0', 'UnitPrice': '476.991'}, {'OrderId': '801Wt00000PHLzNIAX', 'OrderOwnerId': '005Wt000003NEoYIAW', 'AccountId': '001Wt00000PGtdJIAT', 'EffectiveDate': '2022-09-15', 'OrderItemId': '802Wt00000797PdIAI', 'Quantity': '10.0', 'UnitPrice': '449.991'}, {'OrderId': '801Wt00000PHLzNIAX', 'OrderOwnerId': '005Wt000003NEoYIAW', 'AccountId': '001Wt00000PGtdJIAT', 'EffectiveDate': '2022-09-15', 'OrderItemId': '802Wt00000797RFIAY', 'Quantity': '8.0', 'UnitPrice': '569.9905'}, {'OrderId': '801Wt00000PHRFAIA5', 'OrderOwnerId': '#005Wt000003NIx1IAG', 'AccountId': '001Wt00000PGdwiIAD', 'EffectiveDate': '2022-07-01', 'OrderItemId': '#802Wt0000078z8mIAA', 'Quantity': '7.0', 'UnitPrice': '379.9905'}, {'OrderId': '801Wt00000PHRFAIA5', 'OrderOwnerId': '#005Wt000003NIx1IAG', 'AccountId': '001Wt00000PGdwiIAD', 'EffectiveDate': '2022-07-01', 'OrderItemId': '#802Wt00000797RIIAY', 'Quantity': '5.0', 'UnitPrice': '569.9905'}, {'OrderId': '801Wt00000PHRFAIA5', 'OrderOwnerId': '#005Wt000003NIx1IAG', 'AccountId': '001Wt00000PGdwiIAD', 'EffectiveDate': '2022-07-01', 'OrderItemId': '802Wt00000796AJIAY', 'Quantity': '8.0', 'UnitPrice': '569.9905'}, {'OrderId': '801Wt00000PHRFAIA5', 'OrderOwnerId': '#005Wt000003NIx1IAG', 'AccountId': '001Wt00000PGdwiIAD', 'EffectiveDate': '2022-07-01', 'OrderItemId': '802Wt00000796LWIAY', 'Quantity': '16.0', 'UnitPrice': '440.991'}, {'OrderId': '#801Wt00000PHVkDIAX', 'OrderOwnerId': '005Wt000003NJt3IAG', 'AccountId': '001Wt00000PGZZoIAP', 'EffectiveDate': '2022-08-15', 'OrderItemId': '802Wt0000079Ak6IAE', 'Quantity': '3.0', 'UnitPrice': '599.99'}, {'OrderId': '801Wt00000PHVqfIAH', 'OrderOwnerId': '005Wt000003NDEBIA4', 'AccountId': '#001Wt00000PGzM9IAL', 'EffectiveDate': '2022-09-20', 'OrderItemId': '802Wt000007937eIAA', 'Quantity': '10.0', 'UnitPrice': '539.991'}, {'OrderId': '#801Wt00000PHWptIAH', 'OrderOwnerId': '005Wt000003NJ0EIAW', 'AccountId': '#001Wt00000PGYx5IAH', 'EffectiveDate': '2022-09-25', 'OrderItemId': '802Wt00000795xPIAQ', 'Quantity': '2.0', 'UnitPrice': '339.99'}, {'OrderId': '#801Wt00000PHWptIAH', 'OrderOwnerId': '005Wt000003NJ0EIAW', 'AccountId': '#001Wt00000PGYx5IAH', 'EffectiveDate': '2022-09-25', 'OrderItemId': '802Wt0000079987IAA', 'Quantity': '3.0', 'UnitPrice': '529.99'}]}

exec(code, env_args)
