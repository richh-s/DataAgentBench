code = """import json
import re

# Quote line items from the query
quote_items = [
    {"Product2Id": "#01tWt000006hV6jIAE", "Name": "EcoPCB Creator", "Quantity": 3.0, "UnitPrice": 349.99, "TotalPrice": "1049.97"},
    {"Product2Id": "01tWt000006hV8LIAU", "Name": "AI Cirku-Tech", "Quantity": 2.0, "UnitPrice": 529.99, "TotalPrice": "1059.98"},
    {"Product2Id": "#01tWt000006hPffIAE", "Name": "DevVision IDE", "Quantity": 4.0, "UnitPrice": 299.99, "TotalPrice": "1199.96"},
    {"Product2Id": "01tWt000006hVczIAE", "Name": "CollabDesign Studio", "Quantity": 35.0, "UnitPrice": 399.99, "Discount": "15.0", "TotalPrice": "11899.7025"}
]

# Product quantity limits from knowledge article
quantity_limits_text = """
1. **AIOptics Vision** - Customers can purchase up to 20 units per order. Designed for advanced visual analytics, AIOptics Vision empowers businesses with insightful image and video processing capabilities.

2. **CloudLink Designer** - A maximum of 15 units can be ordered at once. This product facilitates seamless networking and connectivity solutions within cloud environments, ideal for optimizing digital architecture.

3. **CollabDesign Studio** - Each order is limited to 25 units. CollabDesign Studio specializes in collaborative workspace solutions, enhancing team productivity and interaction through innovative design features.

4. **CryptGuard Module** - For enhanced data encryption and protection needs, customers can order up to 10 units per purchase. CryptGuard Module provides robust security measures to safeguard sensitive information.

5. **EduFlow Academy** - This educational platform is available for purchase in bundles of up to 5 units per order, perfect for institutions looking to integrate comprehensive e-learning solutions.

6. **SecuManage Pro** - Orders can include up to 30 units. SecuManage Pro offers extensive management tools for cybersecurity operations, enabling businesses to streamline their security protocols effectively.

7. **SecureAnalytics Pro** - Limited to 12 units per order, SecureAnalytics Pro assists in delivering accurate data analysis and reporting within secure environments, supporting informed decision-making.

8. **IntegrGuard Secure** - Users can order up to 8 units. Known for integration security, IntegrGuard Secure is essential for ensuring secure data transfers and connectivity between diverse systems.

9. **CloudInnovate Space** - This dynamic product is available in quantities of up to 18 units per order, designed to spur innovation within cloud technologies through versatile and adaptive solutions.

10. **AI DesignShift** - Clients may order a maximum of 7 units per order. AI DesignShift drives creativity through AI-driven design tools, enabling rapid development of innovative digital solutions.
"""

# Extract quantity limits
quantity_limits = {}
for line in quantity_limits_text.split('\n'):
    if '**' in line and 'up to' in line:
        # Extract product name and limit
        match = re.search(r'\*\*(.*?)\*\*.*?up to (\d+) units', line)
        if match:
            product_name = match.group(1).strip()
            limit = int(match.group(2))
            quantity_limits[product_name] = limit

print("Product Quantity Limits:")
for name, limit in quantity_limits.items():
    print(f"  {name}: {limit}")

print("\nChecking quote items against quantity limits:")
violations = []
for item in quote_items:
    product_name = item['Name']
    quantity = item['Quantity']
    
    # Check for exact match
    if product_name in quantity_limits:
        limit = quantity_limits[product_name]
        if quantity > limit:
            violations.append({
                'product': product_name,
                'quantity': quantity,
                'limit': limit,
                'violation': f'Exceeds quantity limit of {limit} units'
            })
            print(f"  VIOLATION: {product_name} - Ordered: {quantity}, Limit: {limit}")
        else:
            print(f"  OK: {product_name} - Ordered: {quantity}, Limit: {limit}")
    else:
        # Check for partial match (case insensitive)
        found = False
        for limit_name, limit in quantity_limits.items():
            if product_name.lower() in limit_name.lower() or limit_name.lower() in product_name.lower():
                if quantity > limit:
                    violations.append({
                        'product': product_name,
                        'quantity': quantity,
                        'limit': limit,
                        'violation': f'Exceeds quantity limit of {limit} units'
                    })
                    print(f"  VIOLATION: {product_name} (matches {limit_name}) - Ordered: {quantity}, Limit: {limit}")
                else:
                    print(f"  OK: {product_name} (matches {limit_name}) - Ordered: {quantity}, Limit: {limit}")
                found = True
                break
        
        if not found:
            print(f"  NOT FOUND: {product_name} - No quantity limit defined")

print(f"\nTotal violations found: {len(violations)}")
for v in violations:
    print(f"  - {v['product']}: {v['violation']}")"""

env_args = {'var_functions.query_db:0': [], 'var_functions.query_db:2': [{'Id': '#0Q0Wt000001WRAzKAO', 'OpportunityId': '006Wt000007BGgXIAW', 'AccountId': '001Wt00000PHVsDIAX', 'ContactId': '#003Wt00000JqyI6IAJ', 'Name': 'NeoGreen EDA Expansion Quote', 'Description': 'Quote for expanding EDA solutions including AI-powered tools to enhance energy system analytics.', 'Status': 'Needs Review', 'CreatedDate': '2021-05-15T10:30:00.000+0000', 'ExpirationDate': '2021-06-15'}], 'var_functions.query_db:4': [], 'var_functions.list_db:6': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_functions.query_db:8': [], 'var_functions.query_db:10': [{'Id': '0QLWt0000022j3GOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HUwhIAG', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0', 'TotalPrice': '1049.97'}, {'Id': '0QLWt0000022j81OAA', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HHRkIAO', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0', 'TotalPrice': '1059.98'}, {'Id': '0QLWt0000022n8TOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJYIA4', 'Product2Id': '#01tWt000006hPffIAE', 'PricebookEntryId': '01uWt0000027PADIA2', 'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0', 'TotalPrice': '1199.96'}, {'Id': '#0QLWt0000022oAvOAI', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJZIA4', 'Product2Id': '01tWt000006hVczIAE', 'PricebookEntryId': '01uWt0000027Pi5IAE', 'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0', 'TotalPrice': '11899.7025'}], 'var_functions.query_db:12': [{'id': '#ka0Wt000000EqRlIAK', 'title': 'Competitor: NanoDesign Systems   ', 'summary': "NanoDesign Systems is a prominent player in the electronic design automation industry, hailed for its strong vendor stability and partnership model, ensuring reliable, long-term collaborations with its clients. The company places significant emphasis on its roadmap and future enhancements, continually striving to align with emerging market demands and technological advancements. However, it faces challenges in offering highly customizable and flexible solutions, sometimes falling short of catering to specific and unique client workflows. Additionally, NanoDesign's support and service level agreements could be more responsive, with their pricing strategy occasionally seen as less transparent compared to competitors like TechPulse Solutions. Despite these challenges, NanoDesign remains a formidable entity with a focus on vendor reliability and technological growth.", 'urlname': '1745269013-qccav'}, {'id': 'ka0Wt000000Eq0MIAS', 'title': 'Volume-Based Discounts', 'summary': 'Volume-Based Discounts', 'urlname': '1745269013-mq1zw'}, {'id': 'ka0Wt000000EqA3IAK', 'title': 'Customer Feedback and Improvement Initiatives at TechPulse', 'summary': "Learn about TechPulse Solutions' mechanisms for collecting customer feedback and how this valuable input is utilized to implement continuous service improvements and product enhancements.", 'urlname': '1745269013-sac67'}, {'id': 'ka0Wt000000Eq8QIAS', 'title': 'Revolutionizing Integrated Development Environments with AI', 'summary': "Explore how AI technologies transform TechPulse's IDEs to accommodate diverse coding and debugging needs, improving productivity and innovation.", 'urlname': '1745269013-swbjf'}, {'id': 'ka0Wt000000EorOIAS', 'title': 'Automating Development Processes with AutoGen IDE', 'summary': 'Discussing the benefits of automation in accelerating coding and project setup using AutoGen IDE.', 'urlname': '1745269013-bh7jy'}, {'id': 'ka0Wt000000EmklIAC', 'title': 'Advancing PCB Design with AI and Eco-Friendly Solutions', 'summary': "Enhance PCB design efficiency by integrating AI with TechPulse's eco-conscious product suite.", 'urlname': '1745269013-qw9zq'}, {'id': 'ka0Wt000000EpYvIAK', 'title': 'Optimizing Security and Compliance in EDA  ', 'summary': 'An exploration of how TechPulse Solutions maintains robust security and compliance across their EDA product lineup.', 'urlname': '1745269013-pekga'}, {'id': 'ka0Wt000000Ep4JIAS', 'title': 'Enhancing Debugging with DevVision IDE', 'summary': 'Techniques for leveraging DevVision IDE’s debugging capabilities for productive development cycles.', 'urlname': '1745269013-qw1d2'}, {'id': 'ka0Wt000000EpM1IAK', 'title': 'Enhancing Teamwork with CollabDesign Studio', 'summary': 'Utilizing real-time editing features of CollabDesign Studio to improve team productivity and design outcomes.', 'urlname': '1745269013-fdyt0'}, {'id': 'ka0Wt000000EoJWIA0', 'title': 'Streamlined Development with AutoGen IDE', 'summary': 'An overview of how AutoGen IDE supports rapid coding and project setup through automation.', 'urlname': '1745269013-6jrpo'}, {'id': 'ka0Wt000000EpInIAK', 'title': 'Collaborative Designing with CloudLink Designer   ', 'summary': 'How CloudLink Designer improves productivity through seamless cloud-based design collaboration.', 'urlname': '1745269013-vsyc1'}, {'id': 'ka0Wt000000EpAkIAK', 'title': 'Intuitive IDEs for Seamless Development', 'summary': "A guide to TechPulse's integrated development environments, focusing on enhancing developer productivity and workflow integration.", 'urlname': '1745269013-tcg98'}, {'id': 'ka0Wt000000Em4zIAC', 'title': 'Navigating Installation Challenges: Solutions for Seamless Setup of TechPulse EDA Tools', 'summary': "TechPulse Solutions clients sometimes face software installation errors, which can be an obstacle during the initial setup of the company's powerful electronic design automation tools. This article delves into the two main solutions designed to address these challenges effectively. The 'Priority Support Upgrade' offers customers the advantage of faster response times to installation issues, ensuring minimal disruption and timely resolution. Additionally, 'Comprehensive Training Access' equips users with the necessary skills and confidence to handle potential roadblocks in the installation process, fostering a deeper understanding of the product's intricacies. These strategies, together with TechPulse Solutions' commitment to innovation and customer satisfaction, reinforce the seamless integration of their AI-powered solutions into existing workflows, ensuring clients maximize their investment.", 'urlname': '1745269013-ubgtf'}, {'id': 'ka0Wt000000Eo50IAC', 'title': 'Streamlining License Renewal with Effective Training and Support Solutions at TechPulse Solutions', 'summary': 'TechPulse Solutions identifies a prevalent issue in its license renewal process: confusion leading to unexpected service disruptions. To address this, the company proposes two strategic solutions. First, granting clients access to a comprehensive suite of training modules ensures a thorough understanding of all product features, thus improving clarity in the renewal process. This solution, without a validity limit, promises to enhance user expertise consistently. Second, by offering a priority support upgrade valid for one year, TechPulse aims to expedite response times, thereby reducing potential delays and amplifying service efficiency. Together, these solutions not only mitigate the risk of service disruption but also reinforce TechPulse’s commitment to exceptional customer support and ongoing client success.', 'urlname': '1745269013-1g05a'}, {'id': 'ka0Wt000000Eo9pIAC', 'title': 'Resolving Billing Discrepancies: Enhancing Client Satisfaction with TechPulse Solutions', 'summary': "Billing discrepancies can create confusion and dissatisfaction among clients, impacting their overall experience with TechPulse Solutions' EDA products. This article explores effective solutions to address this issue, such as offering a Priority Support Upgrade and Comprehensive Training Access. By enhancing support response times and ensuring clients fully understand and utilize product features, TechPulse Solutions aims to improve client satisfaction and maintain its reputation for excellent customer service.", 'urlname': '1745269013-l1cnv'}, {'id': 'ka0Wt000000EnwwIAC', 'title': 'Enhancing Customization: Bridging the Gap for Niche Industry Needs with TechPulse Solutions', 'summary': "In the world of electronic design automation, the demand for highly customizable solutions is paramount. TechPulse Solutions, recognized for its innovative and AI-powered offerings, addresses the challenge some users face in meeting niche industry requirements. This article explores the company's proactive solutions to enhance customization capabilities. Through initiatives like the 'Custom Feature Workshop' and enhanced access to comprehensive training modules, TechPulse aims to empower clients with the tools and knowledge needed to fully leverage product features, ensuring adaptability and satisfaction across diverse industry landscapes.", 'urlname': '1745269013-i26sq'}, {'id': '#ka0Wt000000Eo3NIAS', 'title': 'Navigating Security Compliance with TechPulse Solutions: Effective Strategies for Clients', 'summary': "As a leader in electronic design automation, TechPulse Solutions recognizes the importance of security compliance in today's digital landscape. This article addresses clients' concerns about understanding and adhering to evolving security standards set by the company. Explore feasible solutions including a Security Compliance Audit to ensure adherence to industry benchmarks, a Priority Support Upgrade for enhanced service efficiency, and Comprehensive Training Access for in-depth knowledge of product features. Discover how these measures can provide peace of mind and bolster confidence in TechPulse Solutions' AI-powered tools.", 'urlname': '1745269013-rld4p'}, {'id': 'ka0Wt000000Eo4zIAC', 'title': 'Enhancing Access to Online Training Modules at TechPulse Solutions', 'summary': "This article explores the occasional challenges customers face in accessing TechPulse Solutions' online training modules. Identified as a crucial step in product adoption, access issues may impact the learning curve for new users. The article discusses two feasible solutions: upgrading to priority support for faster response times, ensuring efficient service delivery, and granting comprehensive training access to ensure all users fully utilize the product’s features. Implementing these solutions can significantly improve user experience and optimize the adoption process, aligning with TechPulse Solutions' commitment to user-friendly innovation and strategic partnership success.", 'urlname': '1745269013-swzlr'}, {'id': '#ka0Wt000000EnwvIAC', 'title': 'Product Quantity Limits   ', 'summary': 'Product Quantity Limits', 'urlname': '1745269013-cbwj9'}, {'id': 'ka0Wt000000Ens5IAC', 'title': 'Mandatory Bundles for Quotes', 'summary': 'Mandatory Bundles for Quotes', 'urlname': '1745269013-flbrj'}, {'id': 'ka0Wt000000EnvJIAS', 'title': 'Product Exclusion Constraints', 'summary': 'Product Exclusion Constraints', 'urlname': '1745269013-l7479'}], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': [{'Id': '01tWt000006hPffIAE', 'Name': 'DevVision IDE', 'Description': 'Integrated development environment with intuitive coding and debugging capabilities.'}, {'Id': '01tWt000006hV6jIAE', 'Name': 'EcoPCB Creator   ', 'Description': 'Environmentally-friendly PCB design solution with power utilization analytics.'}, {'Id': '01tWt000006hV8LIAU', 'Name': 'AI Cirku-Tech', 'Description': 'AI-driven circuit design platform offering rapid prototyping and innovation support.'}, {'Id': '01tWt000006hVczIAE', 'Name': 'CollabDesign Studio', 'Description': 'Enhanced design collaboration platform offering real-time editing and feedback.'}], 'var_functions.query_db:18': [{'id': '#ka0Wt000000EnwvIAC'}, {'id': 'ka0Wt000000Ens5IAC'}]}

exec(code, env_args)
