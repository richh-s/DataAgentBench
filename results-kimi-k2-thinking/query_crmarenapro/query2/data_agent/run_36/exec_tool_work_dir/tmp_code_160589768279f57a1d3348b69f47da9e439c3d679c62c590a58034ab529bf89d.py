code = """import json

# The knowledge articles about policies were stored in var_functions.query_db:2
# Let's check what we have
knowledge_articles = [
  {
    "id": "ka0Wt000000EqQ9IAK",
    "title": "Understanding TechPulse's Return Policy for Purchased Items",
    "faq_answer__c": "...",
    "summary": "Details of TechPulse Solutions' return policy for purchased items...",
    "urlname": "1745269013-p6yto"
  },
  {
    "id": "#ka0Wt000000EpSUIA0",
    "title": "TechPulse Solution Volume-Based Installation Timeline Policy",
    "faq_answer__c": "...",
    "summary": "TechPulse Solution Volume-Based Installation Timeline Policy",
    "urlname": "1745269013-n1rg3"
  },
  {
    "id": "ka0Wt000000Ens5IAC",
    "title": "Mandatory Bundles for Quotes",
    "faq_answer__c": "In the fast-paced world of technological solutions, understanding mandatory product bundles is crucial for securing the best performance and compatibility. At TechPulse Solution, we have streamlined our product offerings, ensuring optimal functionality through specific bundled requirements. This guide provides a comprehensive overview of the mandatory bundles required for quoting our top-tier products.\n\n1. PulseSim Pro Bundle: When purchasing PulseSim Pro, customers must also include the CircuitMaster Analyzer and VeriSim Express in their package. This bundling is designed to enhance your simulation experience, providing unparalleled accuracy and efficiency. CircuitMaster Analyzer works to deliver precise circuit analysis, while VeriSim Express complements it by facilitating swift verification processes. Together, these tools enhance the functionalities of PulseSim Pro, resulting in top-notch simulation capabilities.\n\n2. CloudLink Designer Bundle: To acquire the CloudLink Designer, it's essential to purchase DesignEdge Pro and AI DesignShift as well. This trio creates a robust design platform ideally suited for cloud-based operations. DesignEdge Pro offers advanced design capabilities, ensuring top-quality outcomes, while AI DesignShift incorporates artificial intelligence for intelligent design adaptability and innovation. By combining these products with CloudLink Designer, you achieve a seamless integration that improves performance and design fluidity on the cloud.\n\n3. AI Cirku-Tech Bundle: Customers interested in AI Cirku-Tech must also consider acquiring CircuitAI Innovator and AI DesignShift. Partnered with CircuitAI Innovator, AI Cirku-Tech brings artificial intelligence enhancements to circuit design, optimizing both creativity and efficiency. AI DesignShift, on the other hand, introduces advanced AI-driven design shifts, facilitating a broader scope of design possibilities. This bundle offers a significant leap forward in circuit technology, fully realizing the potential of AI integration.\n\n4. OptiPower Manager Bundle: Purchasing OptiPower Manager necessitates the inclusion of the OptiEnergy Suite and PowerPro Optimize. This comprehensive power management bundle ensures users can effectively monitor and optimize power usage. OptiEnergy Suite offers robust tools for energy management and efficiency, while PowerPro Optimize provides critical power optimization features. Combined with OptiPower Manager, these tools help in achieving significant energy savings and power control.\n\n5. AIOptics Vision Bundle: Lastly, AIOptics Vision requires the Workflow Genius and AI DesignShift as part of its package. This requirement ensures customers have access to superior workflow management tools and AI capabilities. Workflow Genius enhances project management and operational workflows, while AI DesignShift contributes AI-enhanced design innovations. Together with AIOptics Vision, these products deliver a powerful platform for optical analysis and design.\n\nUnderstanding these mandatory bundles helps ensure you receive the full potential of each product offered by TechPulse Solution. By purchasi",
    "summary": "Provides a comprehensive overview of the mandatory bundles required for quoting our top-tier products.",
    "urlname": "ka0Wt000000Ens5IAC"
  }
]

# Find the article about mandatory bundles
mandatory_bundle_article = None
for article in knowledge_articles:
    if 'Mandatory Bundles' in article['title']:
        mandatory_bundle_article = article
        break

print('__RESULT__:')
print(json.dumps(mandatory_bundle_article['id'] if mandatory_bundle_article else None))"""

env_args = {'var_functions.query_db:0': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': [{'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HavbIAC', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HXg4IAG', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HL76IAG', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}], 'var_functions.query_db:6': [{'Id': '01tWt000006hV57IAE', 'Name': 'PulseSim Pro'}], 'var_functions.query_db:10': [{'Id': '01tWt000006hV57IAE', 'Name': 'PulseSim Pro'}], 'var_functions.query_db:12': [{'Id': '#01tWt000006hVDBIA2', 'Name': 'CircuitMaster Analyzer'}], 'var_functions.query_db:14': [], 'var_functions.query_db:16': [{'Id': '01tWt000006hV6jIAE', 'Name': 'EcoPCB Creator   '}, {'Id': '01tWt000006hVQ5IAM', 'Name': 'CircuitSync Pro'}]}

exec(code, env_args)
