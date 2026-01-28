code = """import json
import pandas as pd

# Load previous tool results
knowledge_file = var_call_NBzLA7n19shAjPZY0LiwUykW
with open(knowledge_file, 'r') as f:
    knowledge = json.load(f)

quotes = var_call_skmsgzWFQncFcDwuEtSKHJmp
qli = var_call_hUK3vhYT85oY7vMwSni8MfZ1
pbe = var_call_utlF3Mo3Vi0pGxctKEchQ6i3
prod = var_call_vHaLu5A2QnNnIDshYGoQGtXo

# Normalize lists
knowledge_df = pd.DataFrame(knowledge)
qli_df = pd.DataFrame(qli)
pbe_df = pd.DataFrame(pbe)
prod_df = pd.DataFrame(prod)

# Clean numeric fields
qli_df['UnitPrice'] = qli_df['UnitPrice'].astype(float)
qli_df['Discount'] = qli_df['Discount'].astype(float)
qli_df['Quantity'] = qli_df['Quantity'].astype(float)
qli_df['TotalPrice'] = qli_df['TotalPrice'].astype(float)

# Compute total quote value and max discount
total_quote = qli_df['TotalPrice'].sum()
max_discount = qli_df['Discount'].max()
average_discount = qli_df['Discount'].mean()

# Merge pricebook entry info to compare unit prices
pbe_df['UnitPrice'] = pbe_df['UnitPrice'].astype(float)
merged = qli_df.merge(pbe_df[['Id','UnitPrice']], left_on='PricebookEntryId', right_on='Id', how='left', suffixes=('','_PBE'))
merged['PBE_UnitPrice'] = merged['UnitPrice_PBE']

# Prepare search
def text_of_article(r):
    parts = []
    for k in ('title','faq_answer__c','summary','urlname'):
        if k in r and r[k]:
            parts.append(str(r[k]))
    return "\n".join(parts)

# Search for policy articles related to discount or setup
candidates = []
keywords = ['discount','approval','setup','installation','pricing','pricebook','maximum','authorization','approval matrix','approval required','discount threshold']
for row in knowledge:
    text = text_of_article(row).lower()
    if any(kw in text for kw in keywords):
        candidates.append({'id': row.get('id'), 'title': row.get('title'), 'text': text})

# For each candidate, try to extract numeric thresholds (percent)
import re
violations = []
for c in candidates:
    text = c['text']
    # find percent numbers
    percents = [float(x.replace('%','')) for x in re.findall(r'(\d+(?:\.\d+)?)\s*%',''.join([text]))]
    # find numbers in plain that might indicate dollars or percent
    # Simple heuristics: if mention 'discount' near a percent
    if 'discount' in text:
        # if any percent threshold exists, check if quote exceeds
        if percents:
            threshold = max(percents) # assume threshold is the maximum percent mentioned
            if max_discount > threshold:
                violations.append({'article_id': c['id'], 'article_title': c['title'], 'threshold_percent': threshold, 'max_discount': max_discount})
        else:
            # if text says 'no discounts above' without percent, mark as candidate
            if 'no discounts' in text or 'requires approval' in text:
                # assume requires approval for any discount above 0
                if max_discount > 0:
                    violations.append({'article_id': c['id'], 'article_title': c['title'], 'threshold_percent': None, 'max_discount': max_discount})
    # check setup/installation fee policies
    if 'setup' in text or 'installation' in text:
        # if article says 'no setup fees' or 'setup fees require approval'
        if 'no setup' in text or 'no installation' in text or 'setup fees are not allowed' in text:
            # We need to detect if quote includes setup fees: search products or descriptions for 'setup' or 'installation'
            has_setup = False
            for _, r in prod_df.iterrows():
                name_desc = (str(r.get('Name','')) + ' ' + str(r.get('Description',''))).lower()
                if 'setup' in name_desc or 'installation' in name_desc:
                    has_setup = True
            if has_setup:
                violations.append({'article_id': c['id'], 'article_title': c['title'], 'reason': 'setup_present'})

# If no candidate found by keyword search, also look for explicit titles like 'Pricing Policy' or 'Quote Approval'
for row in knowledge:
    title = str(row.get('title','')).lower()
    if 'pricing policy' in title or 'quote approval' in title or 'discount policy' in title or 'approval required' in title:
        # add if not already in candidates
        if row.get('id') not in [v['article_id'] for v in violations]:
            text = text_of_article(row).lower()
            percents = [float(x.replace('%','')) for x in re.findall(r'(\d+(?:\.\d+)?)\s*%',''.join([text]))]
            if percents and max_discount > max(percents):
                violations.append({'article_id': row.get('id'), 'article_title': row.get('title'), 'threshold_percent': max(percents), 'max_discount': max_discount})

# If still no violations found, return None
result_id = None
if violations:
    # Prefer the first violation
    result_id = violations[0]['article_id']

output = json.dumps(result_id)
print("__RESULT__:")
print(output)"""

env_args = {'var_call_skmsgzWFQncFcDwuEtSKHJmp': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_call_hUK3vhYT85oY7vMwSni8MfZ1': [{'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HavbIAC', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HXg4IAG', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HL76IAG', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}], 'var_call_1YNW0H5gEItNSVvdXOm5pU57': [], 'var_call_utlF3Mo3Vi0pGxctKEchQ6i3': [{'Id': '01uWt0000027P3lIAE', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hV57IAE', 'UnitPrice': '499.99'}, {'Id': '01uWt0000027PVBIA2', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVQ5IAM', 'UnitPrice': '339.99'}], 'var_call_vHaLu5A2QnNnIDshYGoQGtXo': [{'Id': '01tWt000006hV57IAE', 'Name': 'PulseSim Pro', 'Description': 'Advanced simulation and verification software for optimizing circuit designs.', 'IsActive': '1', 'External_ID__c': 'Simulation and Verification Software,AI-Powered Circuit Design Tools_1'}], 'var_call_NBzLA7n19shAjPZY0LiwUykW': 'file_storage/call_NBzLA7n19shAjPZY0LiwUykW.json'}

exec(code, env_args)
