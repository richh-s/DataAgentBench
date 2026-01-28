code = """import json
import pandas as pd
# Load knowledge articles from file path stored in var_call_6beJp8PYlGuF2RlcQuCQHn4f
path = var_call_6beJp8PYlGuF2RlcQuCQHn4f
with open(path, 'r', encoding='utf-8') as f:
    ka = json.load(f)
# Load other vars
quote = var_call_NvvbHvvrUVhX1ROL9EjurIhO[0] if var_call_NvvbHvvrUVhX1ROL9EjurIhO else None
qli = var_call_0OAL3wqr4lpYrwkpnBVsOMrt
pricebook_entries = var_call_yEc4qUPCTXa4Q4jJUPk5aAJY
opportunity = var_call_kdmjennm6JhuQ7yBUiTgQ2sq[0] if var_call_kdmjennm6JhuQ7yBUiTgQ2sq else None

# Compute maximum discount on the quote
max_discount = None
violations = []
if qli:
    discounts = []
    for row in qli:
        try:
            discounts.append(float(row.get('Discount') or 0))
        except:
            try:
                discounts.append(float(str(row.get('Discount')).strip()))
            except:
                discounts.append(0.0)
    if discounts:
        max_discount = max(discounts)

# Find knowledge articles related to discount/approval or setup
matches = []
for a in ka:
    combined = ' '.join([str(a.get('title','') or ''), str(a.get('faq_answer__c','') or ''), str(a.get('summary','') or '')]).lower()
    if 'discount' in combined or 'approval' in combined or 'setup' in combined or 'installation' in combined or 'price' in combined or 'pricing' in combined:
        matches.append({'id': a.get('id'), 'title': a.get('title'), 'combined': combined})

# Prefer articles that mention both discount and approval
chosen_id = None
if max_discount is not None and max_discount > 10.0:
    # find article with both
    for m in matches:
        if 'discount' in m['combined'] and 'approval' in m['combined']:
            chosen_id = m['id']
            break
    if not chosen_id:
        # fallback to any article mentioning discount
        for m in matches:
            if 'discount' in m['combined']:
                chosen_id = m['id']
                break
    # If still not found, return None

# If no discount violation detected, check for setup fees mention - but quote data has no explicit setup fees
# For completeness, check if any product name or description or quote description contains 'setup' and there's an article enforcing policy
if chosen_id is None:
    if max_discount is not None and max_discount > 10.0:
        chosen_id = None
    else:
        # no violation found
        chosen_id = None

# Prepare final JSON-serializable result: the chosen_id or None as a JSON string
result = json.dumps(chosen_id)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_NvvbHvvrUVhX1ROL9EjurIhO': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_call_0OAL3wqr4lpYrwkpnBVsOMrt': [{'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HavbIAC', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HXg4IAG', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HL76IAG', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}], 'var_call_3yPQ37vL2JC9qoDainC0OCNT': [], 'var_call_yEc4qUPCTXa4Q4jJUPk5aAJY': [{'Id': '01uWt0000027P3lIAE', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hV57IAE', 'UnitPrice': '499.99'}, {'Id': '01uWt0000027PVBIA2', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVQ5IAM', 'UnitPrice': '339.99'}], 'var_call_FpkVI8wLvnF9YojlwJ2y3epw': [{'Id': '01sWt000000imiTIAQ', 'Name': 'Standard Price Book', 'Description': 'None', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}], 'var_call_kdmjennm6JhuQ7yBUiTgQ2sq': [{'Id': '006Wt000007BHHfIAO', 'ContractID__c': 'None', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '#003Wt00000JqkgYIAR', 'OwnerId': '#005Wt000003NIybIAG', 'Probability': '75.0', 'Amount': '11420.728', 'StageName': 'Negotiation  ', 'Name': 'InnovateX Solutions Technology Integration Opportunity', 'Description': 'TechPulse Solutions offers InnovateX Solutions a suite of tools, including AI-powered CircuitSync Pro and environmentally-focused EcoPCB Creator, to enhance their design capabilities. By incorporating DesignWave Automation, InnovateX can streamline workflows, ensuring faster project completion and higher client satisfaction. Integrating PulseSim Pro will optimize circuit design verification with precision and speed.', 'CreatedDate': '2021-05-20T14:15:30.000+0000', 'CloseDate': '2021-07-15'}], 'var_call_NJUzkbJigjodIm9FtSnMYUqU': [{'Id': '00kWt000002HHpqIAG', 'OpportunityId': '006Wt000007BHHfIAO', 'Product2Id': '01tWt000006hVEnIAM', 'PricebookEntryId': '01uWt0000027PGfIAM', 'Quantity': '5.0', 'TotalPrice': '2279.9525'}, {'Id': '00kWt000002HL76IAG', 'OpportunityId': '006Wt000007BHHfIAO', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'TotalPrice': '2260.9335'}, {'Id': '#00kWt000002HXg4IAG', 'OpportunityId': '006Wt000007BHHfIAO', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'TotalPrice': '4499.91'}, {'Id': '00kWt000002HavbIAC', 'OpportunityId': '#006Wt000007BHHfIAO', 'Product2Id': '01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'TotalPrice': '2379.932'}], 'var_call_6beJp8PYlGuF2RlcQuCQHn4f': 'file_storage/call_6beJp8PYlGuF2RlcQuCQHn4f.json'}

exec(code, env_args)
