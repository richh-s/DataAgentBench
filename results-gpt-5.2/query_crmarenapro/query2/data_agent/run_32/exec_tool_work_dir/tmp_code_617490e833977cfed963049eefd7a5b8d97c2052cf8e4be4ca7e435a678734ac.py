code = """import json, pandas as pd

quote = pd.DataFrame(var_call_JvaIfIruBlm3kqeQLG5ulJsi)
qli = pd.DataFrame(var_call_zavKFJBLfuMREhDpn8G9nibo)

# Load knowledge
kn_path = var_call_XpKHU0D54PD1cJuX9be9Iknu
with open(kn_path, 'r', encoding='utf-8') as f:
    kn = pd.DataFrame(json.load(f))

# Load pricebook entry map
pbe_path = var_call_xgvDoqnMm2hPXyWtAXlh6j6r
with open(pbe_path, 'r', encoding='utf-8') as f:
    pbe = pd.DataFrame(json.load(f))

# Normalize ids
for df, col in [(qli,'PricebookEntryId'), (pbe,'PricebookEntryId')]:
    df[col+'_norm'] = df[col].astype(str).str.replace('#','', regex=False).str.strip()

# Prepare numeric columns
for col in ['Quantity','UnitPrice','Discount','TotalPrice']:
    if col in qli.columns:
        qli[col] = pd.to_numeric(qli[col], errors='coerce')

pbe['ListUnitPrice'] = pd.to_numeric(pbe['ListUnitPrice'], errors='coerce')

# Join to get list prices
qli = qli.merge(pbe[['PricebookEntryId_norm','ListUnitPrice']], on='PricebookEntryId_norm', how='left')

# Compute discount percent vs list when possible
qli['disc_pct_vs_list'] = (1 - (qli['UnitPrice'] / qli['ListUnitPrice'])) * 100

# Detect potential violations with simple heuristics based on typical policy terms
violations = []

# Heuristic 1: explicit discount field > 10% (common approval threshold)
if (qli['Discount'] > 10).any():
    violations.append('discount_over_10')

# Heuristic 2: unit price below list by > 10%
if (qli['disc_pct_vs_list'] > 10).fillna(False).any():
    violations.append('unit_price_below_list_over_10')

# Heuristic 3: quote status needs review might require approval but not violation

# Find knowledge article about discount/approval by keyword search
text_cols = ['title','summary','faq_answer__c','urlname']
kn_filled = kn.copy()
for c in text_cols:
    if c in kn_filled.columns:
        kn_filled[c] = kn_filled[c].fillna('').astype(str)
kn_filled['blob'] = kn_filled[text_cols].agg(' '.join, axis=1).str.lower()

# keywords relevant to discount/setup/cost policy
keywords = ['discount','pricing','price','quote approval','approval','setup','implementation fee','professional services','tco']
mask = False
for kw in keywords:
    mask = mask | kn_filled['blob'].str.contains(kw)
rel = kn_filled[mask].copy()

# If violations found, pick best matching article: prefer those mentioning discount/pricing/approval
article_id = None
if violations and len(rel):
    # score by keyword hits and presence of 'discount' and 'approval'
    def score(blob):
        s = 0
        for kw in keywords:
            if kw in blob:
                s += 1
        if 'discount' in blob:
            s += 3
        if 'quote' in blob and 'approval' in blob:
            s += 2
        if 'setup' in blob:
            s += 2
        return s
    rel['score'] = rel['blob'].apply(score)
    article_id = rel.sort_values(['score','id'], ascending=[False, True]).iloc[0]['id']

# If no relevant article found or no violations, return None
out = article_id if article_id else None
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_JvaIfIruBlm3kqeQLG5ulJsi': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_call_zavKFJBLfuMREhDpn8G9nibo': [{'Id': '0QLWt0000022xB1OAI', 'QuoteId': '#0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HHpqIAG', 'Product2Id': '#01tWt000006hVEnIAM', 'PricebookEntryId': '01uWt0000027PGfIAM', 'Quantity': '5.0', 'UnitPrice': '479.99', 'Discount': '5.0', 'TotalPrice': '2279.9525'}, {'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HavbIAC', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HXg4IAG', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HL76IAG', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}], 'var_call_XpKHU0D54PD1cJuX9be9Iknu': 'file_storage/call_XpKHU0D54PD1cJuX9be9Iknu.json', 'var_call_s49DFFbq1SXAStMkjwBWXMyA': [{'OpportunityId': '006Wt000007BHHfIAO', 'OpportunityAmount': '11420.728', 'StageName': 'Negotiation  ', 'Probability': '75.0', 'OpportunityName': 'InnovateX Solutions Technology Integration Opportunity', 'OpportunityDescription': 'TechPulse Solutions offers InnovateX Solutions a suite of tools, including AI-powered CircuitSync Pro and environmentally-focused EcoPCB Creator, to enhance their design capabilities. By incorporating DesignWave Automation, InnovateX can streamline workflows, ensuring faster project completion and higher client satisfaction. Integrating PulseSim Pro will optimize circuit design verification with precision and speed.', 'ContractId': 'None', 'ContractStatus': 'None', 'ContractTerm': 'None', 'StartDate': 'None'}], 'var_call_xgvDoqnMm2hPXyWtAXlh6j6r': 'file_storage/call_xgvDoqnMm2hPXyWtAXlh6j6r.json'}

exec(code, env_args)
