code = """import json
from pathlib import Path
import pandas as pd

quote = var_call_zYhvqvx6BNqnBwrFQm6qi37M[0]
qli = pd.DataFrame(var_call_fBhyIkCBEoRAbgQumk20EvaD)
for c in ['Quantity','UnitPrice','Discount','TotalPrice']:
    if c in qli.columns:
        qli[c]=pd.to_numeric(qli[c], errors='coerce')

# evaluate volume discount policy: implied by KA article
ka_path = var_call_2oceKpgAjDMrXNSCONt4BoBZ
kas = json.loads(Path(ka_path).read_text()) if isinstance(ka_path,str) and Path(ka_path).exists() else ka_path
vol_ka = None
for a in kas:
    if str(a.get('title','')).strip().lower()=='volume-based discounts':
        vol_ka=a
        break

violate = False
if vol_ka is not None and not qli.empty:
    # total purchase threshold interpreted as total quote totalprice
    total = float(qli['TotalPrice'].sum())
    # expected max discount based on thresholds $5/$10/$20 => 5/10/15%
    if total >= 20:
        allowed = 15.0
    elif total >= 10:
        allowed = 10.0
    elif total >= 5:
        allowed = 5.0
    else:
        allowed = 0.0
    max_disc = float(qli['Discount'].max())
    # violation if any line discount greater than allowed tier
    if max_disc > allowed + 1e-9:
        violate = True

out = {'violate': violate, 'ka_id': (vol_ka.get('id') if vol_ka else None)}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_zYhvqvx6BNqnBwrFQm6qi37M': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_call_fBhyIkCBEoRAbgQumk20EvaD': [{'Id': '0QLWt0000022xB1OAI', 'QuoteId': '#0Q0Wt000001WSDVKA4', 'Product2Id': '#01tWt000006hVEnIAM', 'PricebookEntryId': '01uWt0000027PGfIAM', 'Quantity': '5.0', 'UnitPrice': '479.99', 'Discount': '5.0', 'TotalPrice': '2279.9525'}, {'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}], 'var_call_PXMUPIZ0r0q4AlXM3397k7Y4': 'file_storage/call_PXMUPIZ0r0q4AlXM3397k7Y4.json', 'var_call_KxR5pUgHlZd8L4kR81v7uKaQ': {'top_candidate_ids': ['ka0Wt000000Eq0MIAS', 'ka0Wt000000Em4zIAC', '#ka0Wt000000EpSUIA0', 'ka0Wt000000Ep2fIAC', 'ka0Wt000000EnthIAC', 'ka0Wt000000Eo9qIAC', 'ka0Wt000000EowFIAS', '#ka0Wt000000EqRlIAK', 'ka0Wt000000EnyXIAS', 'ka0Wt000000EoJWIA0'], 'found_candidates': 50}, 'var_call_2oceKpgAjDMrXNSCONt4BoBZ': 'file_storage/call_2oceKpgAjDMrXNSCONt4BoBZ.json'}

exec(code, env_args)
