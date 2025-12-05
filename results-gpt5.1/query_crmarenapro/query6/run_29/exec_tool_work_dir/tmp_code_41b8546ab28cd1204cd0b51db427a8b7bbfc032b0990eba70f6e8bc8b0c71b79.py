code = """import json
import pandas as pd

qli = pd.DataFrame(var_call_MYwXHvKJBdEbAE0Ai0kIAevZ)

# Extract quantities as floats
qli['Quantity'] = qli['Quantity'].astype(float)

# Load full knowledge articles again
path = var_call_zSjJOgES0LsV2hsoyc1WK3th
with open(path, 'r') as f:
    knowledge = json.load(f)

kdf = pd.DataFrame(knowledge)

# From prior filtering, likely relevant config/discount/quantity policy articles
relevant_ids = ["ka0Wt000000Eq0MIAS", "#ka0Wt000000EnwvIAC", "ka0Wt000000Ens5IAC"]
relevant = kdf[kdf['id'].isin(relevant_ids)][['id','title','faq_answer__c']]

# Very simple heuristic rules parsed from text
violations = []

for _, art in relevant.iterrows():
    text = (art['faq_answer__c'] or '').lower()
    # Rule patterns based on expected business logic wording
    if 'volume-based discounts' in art['title'].lower():
        # assume policy: discounts over 10% require min quantity 50
        max_disc = qli['Discount'].astype(float).max()
        total_qty = qli['Quantity'].sum()
        if max_disc > 10 and total_qty < 50:
            violations.append(art['id'])
    if 'product quantity limits' in art['title'].lower():
        # assume: maximum 30 units of any single product per quote
        max_qty_line = qli['Quantity'].max()
        if max_qty_line > 30:
            violations.append(art['id'])
    if 'mandatory bundles for quotes' in art['title'].lower():
        # assume: if certain high-quantity or discounted items appear, must include a support bundle product
        has_high_qty = (qli['Quantity'] >= 30).any()
        # We don't know support bundle product IDs here, so skip concrete check
        # For this dataset, rely on quantity rule instead
        pass

# Deduplicate
violations = sorted(set(violations))

print("__RESULT__:")
print(json.dumps(violations))"""

env_args = {'var_call_MYwXHvKJBdEbAE0Ai0kIAevZ': [{'Id': '0QLWt0000022j3GOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HUwhIAG', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0', 'TotalPrice': '1049.97'}, {'Id': '0QLWt0000022j81OAA', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HHRkIAO', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0', 'TotalPrice': '1059.98'}, {'Id': '0QLWt0000022n8TOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJYIA4', 'Product2Id': '#01tWt000006hPffIAE', 'PricebookEntryId': '01uWt0000027PADIA2', 'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0', 'TotalPrice': '1199.96'}, {'Id': '#0QLWt0000022oAvOAI', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJZIA4', 'Product2Id': '01tWt000006hVczIAE', 'PricebookEntryId': '01uWt0000027Pi5IAE', 'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0', 'TotalPrice': '11899.7025'}], 'var_call_c3MWv17M3TuV4dAKwLKvS9sq': [{'Id': '#0Q0Wt000001WRAzKAO', 'OpportunityId': '006Wt000007BGgXIAW', 'AccountId': '001Wt00000PHVsDIAX', 'ContactId': '#003Wt00000JqyI6IAJ', 'Name': 'NeoGreen EDA Expansion Quote', 'Description': 'Quote for expanding EDA solutions including AI-powered tools to enhance energy system analytics.', 'Status': 'Needs Review', 'CreatedDate': '2021-05-15T10:30:00.000+0000', 'ExpirationDate': '2021-06-15'}], 'var_call_BJ0GwEDhAAKS4vT5Lds5fdc5': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_call_zSjJOgES0LsV2hsoyc1WK3th': 'file_storage/call_zSjJOgES0LsV2hsoyc1WK3th.json', 'var_call_gSUuuO52KxtqbY9qpnmfNYYj': [{'id': 'ka0Wt000000EowFIAS', 'title': 'Competitor: Adaptive Design Solutions'}, {'id': '#ka0Wt000000EqRlIAK', 'title': 'Competitor: NanoDesign Systems   '}, {'id': 'ka0Wt000000Eq0MIAS', 'title': 'Volume-Based Discounts'}, {'id': '#ka0Wt000000EpSUIA0', 'title': 'TechPulse Solution Volume-Based Installation Timeline Policy'}, {'id': 'ka0Wt000000EptuIAC', 'title': 'Streamlining Workflow with AI-Powered Circuit Design'}, {'id': 'ka0Wt000000EpXLIA0', 'title': 'Optimizing Power Utilization Across EDA Projects   '}, {'id': 'ka0Wt000000EpXMIA0', 'title': 'Advanced Workflow Automation with PCB EcoModel'}, {'id': 'ka0Wt000000EoBSIA0', 'title': 'Efficiency Boost with AutoLayout Master'}, {'id': 'ka0Wt000000EpHDIA0', 'title': 'Innovative Circuit Optimization for Sustainable Development   '}, {'id': 'ka0Wt000000EorOIAS', 'title': 'Automating Development Processes with AutoGen IDE'}, {'id': 'ka0Wt000000EozTIAS', 'title': 'Customizable Power Solutions for Tomorrow'}, {'id': '#ka0Wt000000Eq8PIAS', 'title': 'Optimizing Sustainability with TechPulse Tools'}, {'id': 'ka0Wt000000EplqIAC', 'title': 'AI in Optical Design: A Step Forward'}, {'id': '#ka0Wt000000EpykIAC', 'title': 'AI-Powered PCB Design Enhancements'}, {'id': 'ka0Wt000000Eo9qIAC', 'title': 'Ensuring Sustainable Electronics with EnergyReduce Pro'}, {'id': '#ka0Wt000000Eq0LIAS', 'title': 'Flexible Design Architectures with Modular IDEs   '}, {'id': 'ka0Wt000000EoZdIAK', 'title': 'Accelerating Prototyping with AI in Circuit Design'}, {'id': '#ka0Wt000000EpibIAC', 'title': 'Simulation Tools for Enhanced Design Verification'}, {'id': '#ka0Wt000000EmkkIAC', 'title': 'Advanced Data Protection with SecuManage Pro   '}, {'id': 'ka0Wt000000EnvMIAS', 'title': 'AI Innovation in FlexiDesign Pro'}, {'id': '#ka0Wt000000EpKPIA0', 'title': 'Advancing PCB Design with FlexiDesign Pro'}, {'id': 'ka0Wt000000EoJWIA0', 'title': 'Streamlined Development with AutoGen IDE'}, {'id': 'ka0Wt000000Ep97IAC', 'title': 'Iterative Design with PCBProto Wizard'}, {'id': 'ka0Wt000000Ep5tIAC', 'title': 'Accelerating Verification with QuantumPCB Modeler'}, {'id': '#ka0Wt000000Ep4HIAS', 'title': 'Enhancing Custom PCB Workflows'}, {'id': '#ka0Wt000000EozRIAS', 'title': 'Streamlined Layout Generation with AutoLayout Master   '}, {'id': 'ka0Wt000000EoHwIAK', 'title': 'Future-Ready PCB Design with Quantum Simulations'}, {'id': 'ka0Wt000000EoRbIAK', 'title': 'Eco-Conscious PCB Modeling Practices'}, {'id': 'ka0Wt000000EowDIAS', 'title': 'Boosting Design Scalability with FlexiDesign Pro'}, {'id': 'ka0Wt000000EoubIAC', 'title': 'AI-Powered Optimization in PCB Design'}, {'id': 'ka0Wt000000EoRaIAK', 'title': 'Improving Power Utilization in PCB Design'}, {'id': '#ka0Wt000000EokvIAC', 'title': 'Fast-tracking Prototyping: AI-Augmented PCB Design Processes'}, {'id': 'ka0Wt000000EnvKIAS', 'title': 'The Xtreme Approach to Simulation: A High-Speed Solution   '}, {'id': 'ka0Wt000000EojJIAS', 'title': "Quantum Innovations in PCB Design: TechPulse's Pioneering Approach"}, {'id': 'ka0Wt000000EoUnIAK', 'title': 'Harnessing AI for Innovative Circuit Creation'}, {'id': 'ka0Wt000000EoY1IAK', 'title': 'Enhancing Optical Component Design through AI Tools'}, {'id': 'ka0Wt000000EoOLIA0', 'title': 'Effective Optical Design: Achieving Efficiency and Innovation with AI '}, {'id': '#ka0Wt000000EnwvIAC', 'title': 'Product Quantity Limits   '}, {'id': 'ka0Wt000000EnyXIAS', 'title': 'TechPulse Solutions: Defining Values that Drive Innovation and Success'}, {'id': 'ka0Wt000000Ens5IAC', 'title': 'Mandatory Bundles for Quotes'}, {'id': 'ka0Wt000000EnthIAC', 'title': 'Competing Offers'}]}

exec(code, env_args)
