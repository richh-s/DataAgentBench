code = """import json
import pandas as pd
# load data from storage variables
qlis = pd.DataFrame(var_call_Zxg3MN2WVt7fVGt5SX5gbx0k)
prods = pd.DataFrame(var_call_m0iTOYSArcqoeFnjOsdpTBbZ)
pbes = pd.DataFrame(var_call_wAehBl62H4wdhYI0zffGADqH)
pricebooks = pd.DataFrame(var_call_OXHW8QHWshnvv9yJS6MVtNCP)
quote = pd.DataFrame(var_call_GQfncz0p0sYKyMWBTLXSzTqd)
account = pd.DataFrame(var_call_kOitzp1VJUXYca3Kw2uj6Ag9)
opis = pd.DataFrame(var_call_5wpIZFYPZudG1zZlbRQXw56X)
# normalize ids (strip leading #)
for df in [qlis, prods, pbes, pricebooks, quote, account, opis]:
    if 'Id' in df.columns:
        df['Id'] = df['Id'].astype(str).str.lstrip('#')
    if 'Product2Id' in df.columns:
        df['Product2Id'] = df['Product2Id'].astype(str).str.lstrip('#')
    if 'PricebookEntryId' in df.columns:
        df['PricebookEntryId'] = df['PricebookEntryId'].astype(str).str.lstrip('#')
    if 'Pricebook2Id' in df.columns:
        df['Pricebook2Id'] = df['Pricebook2Id'].astype(str).str.lstrip('#')
    if 'QuoteId' in df.columns:
        df['QuoteId'] = df['QuoteId'].astype(str).str.lstrip('#')
    if 'QuoteId' in df.columns:
        df['QuoteId'] = df['QuoteId'].astype(str)
# prepare quote line items with product and list price
qlis['UnitPrice'] = qlis['UnitPrice'].astype(float)
qlis['Quantity'] = qlis['Quantity'].astype(float)
qlis['Discount'] = qlis['Discount'].astype(float)
qlis['TotalPrice'] = qlis['TotalPrice'].astype(float)
merged = qlis.merge(pbes[['Id','UnitPrice','Pricebook2Id']], left_on='PricebookEntryId', right_on='Id', how='left', suffixes=('','_pbe'))
merged = merged.merge(prods[['Id','Name','Description']], left_on='Product2Id', right_on='Id', how='left', suffixes=('','_prod'))
merged = merged.merge(pricebooks[['Id','Name','IsActive']], left_on='Pricebook2Id', right_on='Id', how='left', suffixes=('','_pb'))
# compute expected total price applying discount
merged['ComputedTotal'] = merged['Quantity'] * merged['UnitPrice'] * (1 - merged['Discount']/100)
# Compare with recorded TotalPrice and find discrepancies
merged['Diff'] = (merged['ComputedTotal'] - merged['TotalPrice']).round(4)
# round UnitPrice and list price
merged['UnitPrice'] = merged['UnitPrice'].round(2)
merged['ListUnitPrice'] = merged['UnitPrice_pbe'].astype(float).round(2)
# attach quote info
merged['QuoteId'] = merged['QuoteId'].str.lstrip('#')
quote_id = quote.at[0,'Id'].lstrip('#')
# gather summary
summary = {
    'QuoteId': quote_id,
    'Account': account.at[0,'Name'] if not account.empty else None,
    'NumLineItems': int(len(merged)),
    'LineItems': merged[['Id','Product2Id','Name','Quantity','UnitPrice','Discount','ListUnitPrice','TotalPrice','ComputedTotal','Diff','Name_pb']].rename(columns={'Name':'ProductName','Name_pb':'PricebookName'}).to_dict(orient='records')
}
print("__RESULT__:")
print(json.dumps(summary))"""

env_args = {'var_call_GQfncz0p0sYKyMWBTLXSzTqd': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_call_Zxg3MN2WVt7fVGt5SX5gbx0k': [{'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HavbIAC', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HXg4IAG', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HL76IAG', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}], 'var_call_m0iTOYSArcqoeFnjOsdpTBbZ': [{'Id': '01tWt000006hV57IAE', 'Name': 'PulseSim Pro', 'Description': 'Advanced simulation and verification software for optimizing circuit designs.'}], 'var_call_wAehBl62H4wdhYI0zffGADqH': [{'Id': '01uWt0000027P3lIAE', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hV57IAE', 'UnitPrice': '499.99'}, {'Id': '01uWt0000027PVBIA2', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVQ5IAM', 'UnitPrice': '339.99'}], 'var_call_OXHW8QHWshnvv9yJS6MVtNCP': [{'Id': '01sWt000000imiTIAQ', 'Name': 'Standard Price Book', 'IsActive': '1'}], 'var_call_NQaEDjgPepsag7VcKeqWVPGk': 'file_storage/call_NQaEDjgPepsag7VcKeqWVPGk.json', 'var_call_7n6AKYg6TAoRxY5iFFyvfJqn': [{'id': 'ka0Wt000000Eq0MIAS', 'title': 'Volume-Based Discounts', 'summary': 'Volume-Based Discounts'}, {'id': '#ka0Wt000000EpSUIA0', 'title': 'TechPulse Solution Volume-Based Installation Timeline Policy', 'summary': 'TechPulse Solution Volume-Based Installation Timeline Policy'}, {'id': 'ka0Wt000000EorOIAS', 'title': 'Automating Development Processes with AutoGen IDE', 'summary': 'Discussing the benefits of automation in accelerating coding and project setup using AutoGen IDE.'}, {'id': 'ka0Wt000000EoJWIA0', 'title': 'Streamlined Development with AutoGen IDE', 'summary': 'An overview of how AutoGen IDE supports rapid coding and project setup through automation.'}, {'id': 'ka0Wt000000Em4zIAC', 'title': 'Navigating Installation Challenges: Solutions for Seamless Setup of TechPulse EDA Tools', 'summary': "TechPulse Solutions clients sometimes face software installation errors, which can be an obstacle during the initial setup of the company's powerful electronic design automation tools. This article delves into the two main solutions designed to address these challenges effectively. The 'Priority Support Upgrade' offers customers the advantage of faster response times to installation issues, ensuring minimal disruption and timely resolution. Additionally, 'Comprehensive Training Access' equips users with the necessary skills and confidence to handle potential roadblocks in the installation process, fostering a deeper understanding of the product's intricacies. These strategies, together with TechPulse Solutions' commitment to innovation and customer satisfaction, reinforce the seamless integration of their AI-powered solutions into existing workflows, ensuring clients maximize their investment."}, {'id': 'ka0Wt000000EnthIAC', 'title': 'Competing Offers', 'summary': 'Policy for price adjustments based on competing offers'}], 'var_call_18WYZPZBGIyWyUf1kLiiNm4V': 'file_storage/call_18WYZPZBGIyWyUf1kLiiNm4V.json', 'var_call_TXKmIIFbm49xzlYbTHw6T0Cf': 'file_storage/call_TXKmIIFbm49xzlYbTHw6T0Cf.json', 'var_call_kOitzp1VJUXYca3Kw2uj6Ag9': [{'Id': '#001Wt00000PGXrKIAX', 'Name': 'InnovateX Solutions'}], 'var_call_5wpIZFYPZudG1zZlbRQXw56X': [{'Id': '00kWt000002HL76IAG', 'OpportunityId': '006Wt000007BHHfIAO', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'TotalPrice': '2260.9335'}, {'Id': '00kWt000002HavbIAC', 'OpportunityId': '#006Wt000007BHHfIAO', 'Product2Id': '01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'TotalPrice': '2379.932'}]}

exec(code, env_args)
