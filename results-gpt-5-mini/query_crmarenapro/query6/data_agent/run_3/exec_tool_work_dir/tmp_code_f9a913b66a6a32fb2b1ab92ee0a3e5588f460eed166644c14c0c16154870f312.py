code = """import json
from pathlib import Path
path = Path(var_call_UBSEwzhCruvwIkjx6sEEhiRR)
with open(path, 'r', encoding='utf-8') as f:
    ka = json.load(f)
# Find the 'Volume-Based Discounts' article
target = None
for article in ka:
    if article.get('title','').strip().lower() == 'volume-based discounts':
        target = article
        break
# If not exact match, search for title containing 'volume' and 'discount'
if not target:
    for article in ka:
        t = article.get('title','').lower()
        if 'volume' in t and 'discount' in t:
            target = article
            break
# Prepare result
res = target if target else {}
import json
print("__RESULT__:")
print(json.dumps(res))"""

env_args = {'var_call_i25sxslZHda6XTnRwj17GXYS': [{'Id': '0QLWt0000022j3GOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HUwhIAG', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0', 'TotalPrice': '1049.97'}, {'Id': '0QLWt0000022j81OAA', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HHRkIAO', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0', 'TotalPrice': '1059.98'}, {'Id': '0QLWt0000022n8TOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJYIA4', 'Product2Id': '#01tWt000006hPffIAE', 'PricebookEntryId': '01uWt0000027PADIA2', 'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0', 'TotalPrice': '1199.96'}, {'Id': '#0QLWt0000022oAvOAI', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJZIA4', 'Product2Id': '01tWt000006hVczIAE', 'PricebookEntryId': '01uWt0000027Pi5IAE', 'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0', 'TotalPrice': '11899.7025'}], 'var_call_UBSEwzhCruvwIkjx6sEEhiRR': 'file_storage/call_UBSEwzhCruvwIkjx6sEEhiRR.json', 'var_call_UELP4a6Hx3N0cCOry9kYDBPf': 'file_storage/call_UELP4a6Hx3N0cCOry9kYDBPf.json', 'var_call_GRYq4ciMS62cvPigp4QNxtom': [{'Id': '01uWt0000027P8cIAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hV8LIAU', 'UnitPrice': '529.99'}, {'Id': '01uWt0000027PADIA2', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hPffIAE', 'UnitPrice': '299.99'}, {'Id': '01uWt0000027Pi5IAE', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVczIAE', 'UnitPrice': '399.99'}], 'var_call_mo85EFalNkRNgZyOaiabqjY8': [{'Id': '01sWt000000imiTIAQ', 'Name': 'Standard Price Book', 'IsActive': '1'}], 'var_call_DS6Bk9VrCM47JZcz60HMFIAH': []}

exec(code, env_args)
