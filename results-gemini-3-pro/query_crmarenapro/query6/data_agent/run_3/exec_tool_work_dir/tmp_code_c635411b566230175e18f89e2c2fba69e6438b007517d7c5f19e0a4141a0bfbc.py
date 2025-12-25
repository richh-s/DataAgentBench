code = """import json

target_ids = ["#ka0Wt000000EnwvIAC", "ka0Wt000000EnvJIAS", "ka0Wt000000EnwvIAC"] # Include both with and without # just in case

with open(locals()['var_function-call-3392226514804622973'], 'r') as f:
    articles = json.load(f)

found_articles = []
for art in articles:
    if art['id'] in target_ids:
        found_articles.append(art)

print("__RESULT__:")
print(json.dumps(found_articles))"""

env_args = {'var_function-call-3392226514804621660': [{'Id': '0QLWt0000022j3GOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HUwhIAG', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0', 'TotalPrice': '1049.97'}, {'Id': '0QLWt0000022j81OAA', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HHRkIAO', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0', 'TotalPrice': '1059.98'}, {'Id': '0QLWt0000022n8TOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJYIA4', 'Product2Id': '#01tWt000006hPffIAE', 'PricebookEntryId': '01uWt0000027PADIA2', 'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0', 'TotalPrice': '1199.96'}, {'Id': '#0QLWt0000022oAvOAI', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJZIA4', 'Product2Id': '01tWt000006hVczIAE', 'PricebookEntryId': '01uWt0000027Pi5IAE', 'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0', 'TotalPrice': '11899.7025'}], 'var_function-call-3392226514804622973': 'file_storage/function-call-3392226514804622973.json', 'var_function-call-4947644945305673138': [{'Id': '01tWt000006hPffIAE', 'Name': 'DevVision IDE'}, {'Id': '01tWt000006hV6jIAE', 'Name': 'EcoPCB Creator   '}, {'Id': '01tWt000006hV8LIAU', 'Name': 'AI Cirku-Tech'}, {'Id': '01tWt000006hVczIAE', 'Name': 'CollabDesign Studio'}], 'var_function-call-6085294866981528523': [{'id': '#ka0Wt000000EoUoIAK', 'title': 'Enhancing User Experience in DevVision IDE', 'summary': 'Examine the user-friendly features of DevVision IDE that foster an efficient coding and debugging environment, aiding developers in mastering EDA tools.', 'matched_products': ['DevVision IDE']}, {'id': '#ka0Wt000000EqGTIA0', 'title': 'Integrating AI-Powered Circuit Design with AI Cirku-Tech', 'summary': 'Exploring the competitive edge and innovative features brought by AI Cirku-Tech in the circuit design landscape.', 'matched_products': ['AI Cirku-Tech']}, {'id': 'ka0Wt000000EpQtIAK', 'title': 'Intelligent Power Management with OptiPower and EcoPCB', 'summary': 'Balance environmental goals with performance using OptiPower Manager and EcoPCB Creator.', 'matched_products': ['EcoPCB Creator']}, {'id': 'ka0Wt000000EpM1IAK', 'title': 'Enhancing Teamwork with CollabDesign Studio', 'summary': 'Utilizing real-time editing features of CollabDesign Studio to improve team productivity and design outcomes.', 'matched_products': ['CollabDesign Studio']}, {'id': 'ka0Wt000000Ep4IIAS', 'title': 'Power Optimization Insights with EcoPCB Creator', 'summary': 'Maximizing efficiency with EcoPCB Creator’s power optimization features.', 'matched_products': ['EcoPCB Creator']}, {'id': '#ka0Wt000000EnwvIAC', 'title': 'Product Quantity Limits   ', 'summary': 'Product Quantity Limits', 'matched_products': ['CollabDesign Studio']}, {'id': 'ka0Wt000000EnvJIAS', 'title': 'Product Exclusion Constraints', 'summary': 'Product Exclusion Constraints', 'matched_products': ['DevVision IDE']}]}

exec(code, env_args)
