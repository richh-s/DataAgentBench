code = """import json, pandas as pd

quote = pd.DataFrame(var_call_TFhXb7ws0PfMJADiP16jwiXD)
qli = pd.DataFrame(var_call_kheC5Lsjpv1ganpkwOYDchup)

# load full knowledge articles
path = var_call_vfKgz2F90Y8VX0PwpDDcnEFJ
with open(path, 'r', encoding='utf-8') as f:
    kav = json.load(f)
kav_df = pd.DataFrame(kav)

# Identify any article that is a quote approval / discount / pricing / setup policy
text = (kav_df.get('title','').fillna('') + ' ' + kav_df.get('summary','').fillna('') + ' ' + kav_df.get('faq_answer__c','').fillna('')).str.lower()
policy_mask = text.str.contains('quote') | text.str.contains('pricing') | text.str.contains('discount') | text.str.contains('approval') | text.str.contains('setup')
policy_df = kav_df[policy_mask].copy()

# Determine if quote has discount beyond common thresholds (10%) or any setup fee line items not present; we only have discounts.
# Extract max discount
qli['Discount'] = pd.to_numeric(qli['Discount'], errors='coerce')
max_disc = float(qli['Discount'].max()) if len(qli) else 0.0

# try find policy article mentioning max allowed discount 10% or 15% etc
violated_id = None
if len(policy_df):
    # find articles that mention a numeric discount threshold less than max_disc
    import re
    def extract_thresholds(s):
        nums = [float(m) for m in re.findall(r'(?:max(?:imum)?|up to|no more than)\s*(\d{1,2}(?:\.\d+)?)\s*%\s*discount', s)]
        return nums
    thr = []
    for _, r in policy_df.iterrows():
        s = (str(r.get('title',''))+' '+str(r.get('faq_answer__c',''))+' '+str(r.get('summary',''))).lower()
        nums = extract_thresholds(s)
        if nums:
            thr.append((r['id'], min(nums)))
    # if any threshold found and max_disc exceeds it, pick the most relevant (lowest threshold exceeded)
    exceeded = [(i,t) for i,t in thr if max_disc>t]
    if exceeded:
        # choose one with smallest threshold (strictest)
        violated_id = sorted(exceeded, key=lambda x: x[1])[0][0]

# If we couldn't find explicit threshold-based violation, return None
out = violated_id if violated_id is not None else None
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_TFhXb7ws0PfMJADiP16jwiXD': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_call_kheC5Lsjpv1ganpkwOYDchup': [{'Id': '0QLWt0000022xB1OAI', 'QuoteId': '#0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HHpqIAG', 'Product2Id': '#01tWt000006hVEnIAM', 'PricebookEntryId': '01uWt0000027PGfIAM', 'Quantity': '5.0', 'UnitPrice': '479.99', 'Discount': '5.0', 'TotalPrice': '2279.9525'}, {'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HavbIAC', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HXg4IAG', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HL76IAG', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}], 'var_call_vfKgz2F90Y8VX0PwpDDcnEFJ': 'file_storage/call_vfKgz2F90Y8VX0PwpDDcnEFJ.json', 'var_call_Ieat8pvMzSVLFwceDS4jQLun': 'file_storage/call_Ieat8pvMzSVLFwceDS4jQLun.json', 'var_call_1mx66jLXiS8HGUQjlbRFPBft': [{'Id': '006Wt000007BHHfIAO', 'ContractID__c': 'None', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '#003Wt00000JqkgYIAR', 'OwnerId': '#005Wt000003NIybIAG', 'Probability': '75.0', 'Amount': '11420.728', 'StageName': 'Negotiation  ', 'Name': 'InnovateX Solutions Technology Integration Opportunity', 'Description': 'TechPulse Solutions offers InnovateX Solutions a suite of tools, including AI-powered CircuitSync Pro and environmentally-focused EcoPCB Creator, to enhance their design capabilities. By incorporating DesignWave Automation, InnovateX can streamline workflows, ensuring faster project completion and higher client satisfaction. Integrating PulseSim Pro will optimize circuit design verification with precision and speed.', 'CreatedDate': '2021-05-20T14:15:30.000+0000', 'CloseDate': '2021-07-15'}]}

exec(code, env_args)
