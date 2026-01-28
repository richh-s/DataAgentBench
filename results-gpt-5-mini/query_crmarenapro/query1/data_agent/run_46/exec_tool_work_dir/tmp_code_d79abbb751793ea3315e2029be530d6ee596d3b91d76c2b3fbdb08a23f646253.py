code = """import json, re
# load stored variables
leads = var_call_JpE3StquwDffdTD7ipnqYsTz
calls = var_call_LrPLzqJfkyHGBAMx7TUe9M55
kb = var_call_r5Wx60lxyJd1Lr0enF3GY5yY
products = var_call_7UYiVKaU7Ckp7Km7hwsPbCqK
pricebook = var_call_gjIGUKlxCvfnzAeGAmP38SfR

transcript = calls[0].get('Body__c','') if calls else ''
transcript_lower = transcript.lower()

# Authority: look for lack of final decision phrases
authority_issues = False
authority_phrases = ["i don't have the final say", "i do not have the final say", "need to consult with", "consult with the finance", "i'll need to consult", "i will need to consult", "i need to consult"]
for ph in authority_phrases:
    if ph in transcript_lower:
        authority_issues = True
        break

# Need: look for clear statements of interest or intent to move forward
need_ok = False
need_phrases = ["i'm interested", "im interested", "we want to enhance", "interested to learn", "would like to move forward", "i'd like to move forward", "i would like to move forward", "we want to"]
for ph in need_phrases:
    if ph in transcript_lower:
        need_ok = True
        break

# Timeline: check for timeline mention and vendor's reassurance
timeline_issue = False
if 'tight timeline' in transcript_lower or 'tight timeline for installation' in transcript_lower:
    # vendor reassurance phrases
    if 'complete installations within a day' in transcript_lower or 'aim to complete installations within a day' in transcript_lower:
        timeline_issue = False
    else:
        timeline_issue = True

# Budget: parse mentioned budget and check mandatory bundles pricing
budget_issue = False
budget_mentioned = None
m = re.search(r'budget is \$([0-9,]+(?:\.[0-9]{2})?)', transcript_lower)
if m:
    try:
        budget_mentioned = float(m.group(1).replace(',',''))
    except:
        budget_mentioned = None

# Find product ids/prices
pulse_id = None
veri_id = None
circuit_id = None
for p in products:
    name = p.get('Name','').strip().lower()
    if name == 'pulsesim pro':
        pulse_id = p.get('Id')
    elif name == 'verisim express':
        veri_id = p.get('Id')
    elif name == 'circuitmaster analyzer':
        circuit_id = p.get('Id')

pulse_price = None
veri_price = None
circuit_price = None
for pb in pricebook:
    pid = pb.get('Product2Id')
    try:
        price = float(pb.get('UnitPrice'))
    except:
        continue
    if pid == pulse_id:
        pulse_price = price
    if pid == veri_id:
        veri_price = price
    if pid == circuit_id:
        circuit_price = price

# KB indicates mandatory bundles for PulseSim Pro: must include CircuitMaster Analyzer and VeriSim Express
bundles_mandatory = False
if kb and len(kb) > 0:
    # assume the KB entry refers to mandatory bundles including PulseSim
    bundles_mandatory = True

# Compute total cost if possible
total_cost = None
if pulse_price is not None and veri_price is not None and circuit_price is not None:
    total_cost = 4 * pulse_price + veri_price + circuit_price
else:
    # partial known
    partial = 0.0
    known = False
    if pulse_price is not None:
        partial += 4 * pulse_price
        known = True
    if veri_price is not None:
        partial += veri_price
        known = True
    if circuit_price is not None:
        partial += circuit_price
        known = True
    total_cost = partial if known else None

# Decide budget issue
if budget_mentioned is not None and total_cost is not None and total_cost > 0:
    if total_cost > budget_mentioned:
        budget_issue = True
    else:
        budget_issue = False
else:
    # If mandatory bundles exist and any mandatory bundle price missing, mark budget issue due to uncertainty
    if bundles_mandatory and (circuit_price is None or veri_price is None):
        budget_issue = True
    else:
        budget_issue = False

# Compile failing factors
failing = []
if budget_issue:
    failing.append('Budget')
if authority_issues:
    failing.append('Authority')
if not need_ok:
    failing.append('Need')
if timeline_issue:
    failing.append('Timeline')

print('__RESULT__:')
print(json.dumps(failing))"""

env_args = {'var_call_JpE3StquwDffdTD7ipnqYsTz': [{'Id': '00QWt0000089AekMAE', 'FirstName': 'Ali', 'LastName': 'Hussein', 'Email': 'ali.hussein@baghdadhtechhub.com', 'Phone': '555-452-7654', 'Company': 'Baghdad Tech Hub', 'Status': 'Converted', 'ConvertedContactId': 'None', 'ConvertedAccountId': 'None', 'Title': 'Head of Emerging Technologies', 'CreatedDate': '2023-08-18T15:35:50.000+0000', 'ConvertedDate': 'None', 'IsConverted': '0', 'OwnerId': '005Wt000003NErnIAG'}], 'var_call_LrPLzqJfkyHGBAMx7TUe9M55': [{'Id': 'a05Wt000003SukEIAS', 'OpportunityId__c': 'None', 'LeadId__c': '00QWt0000089AekMAE', 'Body__c': "[2023-10-21T10:02:00] Ava Sullivan: Hi Ali, this is Ava Sullivan from TechSolutions. How are you today?\n[2023-10-21T10:02:10] Ali Hussein: Hi Ava, I'm doing well, thank you. How about you?\n[2023-10-21T10:02:20] Ava Sullivan: I'm great, thank you for asking! I'm glad we could connect. I was looking over the details you provided about your interest in the PulseSim Pro. Is now a good time to discuss?\n[2023-10-21T10:02:30] Ali Hussein: Yes, now works for me. I'm interested to learn more and see how it fits with what we need.\n[2023-10-21T10:02:40] Ava Sullivan: Fantastic! From what you’ve mentioned, you’re interested in four units of the PulseSim Pro, correct?\n[2023-10-21T10:02:50] Ali Hussein: That's right. We want to enhance our simulation capabilities, and the PulseSim Pro seems like a great fit.\n[2023-10-21T10:03:05] Ava Sullivan: Absolutely. The PulseSim Pro is one of our top products for high precision simulation. It offers advanced analytics and seamless integration with existing systems, which is great for boosting efficiency.\n[2023-10-21T10:03:15] Ali Hussein: Those features sound beneficial. We do have a tight timeline for installation, though. Could you tell me more about that?\n[2023-10-21T10:03:30] Ava Sullivan: Certainly. We understand the importance of meeting tight schedules. We usually aim to complete installations within a day and ensure everything runs smoothly. Our technical team is very efficient.\n[2023-10-21T10:03:40] Ali Hussein: That’s reassuring. And as for the budget, how does it look for four units?\n[2023-10-21T10:03:55] Ava Sullivan: Considering your budget is $2,261, I think we can work something out. Each PulseSim Pro unit is priced at $500. For four units, it will come to $2,000. This is below your budget, leaving room for additional services if you wish.\n[2023-10-21T10:04:10] Ali Hussein: That fits really well. I'd like to move forward, but I'll need to consult with the finance team here since I don’t have the final say.\n[2023-10-21T10:04:20] Ava Sullivan: I completely understand, Ali. Would you like me to send over a detailed proposal and pricing information so you can present it to your team?\n[2023-10-21T10:04:25] Ali Hussein: Yes, please. That would be very helpful.\n[2023-10-21T10:04:35] Ava Sullivan: Great! I'll have that to you by the end of the day. Is there anything else you would need from my side?\n[2023-10-21T10:04:40] Ali Hussein: No, that sounds good for now. Thank you, Ava.\n[2023-10-21T10:04:50] Ava Sullivan: You're welcome, Ali. If any questions come up, feel free to reach out. Have a wonderful day!\n[2023-10-21T10:04:55] Ali Hussein: Thanks, Ava. You too!", 'CreatedDate': '2023-10-21T10:02:00.000+0000', 'EndTime__c': '2023-10-21'}], 'var_call_r5Wx60lxyJd1Lr0enF3GY5yY': [{'id': 'ka0Wt000000Ens5IAC', 'title': 'Mandatory Bundles for Quotes', 'faq_answer__c': "In the fast-paced world of technological solutions, understanding mandatory product bundles is crucial for securing the best performance and compatibility. At TechPulse Solution, we have streamlined our product offerings, ensuring optimal functionality through specific bundled requirements. This guide provides a comprehensive overview of the mandatory bundles required for quoting our top-tier products.\n\n1. PulseSim Pro Bundle: When purchasing PulseSim Pro, customers must also include the CircuitMaster Analyzer and VeriSim Express in their package. This bundling is designed to enhance your simulation experience, providing unparalleled accuracy and efficiency. CircuitMaster Analyzer works to deliver precise circuit analysis, while VeriSim Express complements it by facilitating swift verification processes. Together, these tools enhance the functionalities of PulseSim Pro, resulting in top-notch simulation capabilities.\n\n2. CloudLink Designer Bundle: To acquire the CloudLink Designer, it's essential to purchase DesignEdge Pro and AI DesignShift as well. This trio creates a robust design platform ideally suited for cloud-based operations. DesignEdge Pro offers advanced design capabilities, ensuring top-quality outcomes, while AI DesignShift incorporates artificial intelligence for intelligent design adaptability and innovation. By combining these products with CloudLink Designer, you achieve a seamless integration that improves performance and design fluidity on the cloud.\n\n3. AI Cirku-Tech Bundle: Customers interested in AI Cirku-Tech must also consider acquiring CircuitAI Innovator and AI DesignShift. Partnered with CircuitAI Innovator, AI Cirku-Tech brings artificial intelligence enhancements to circuit design, optimizing both creativity and efficiency. AI DesignShift, on the other hand, introduces advanced AI-driven design shifts, facilitating a broader scope of design possibilities. This bundle offers a significant leap forward in circuit technology, fully realizing the potential of AI integration.\n\n4. OptiPower Manager Bundle: Purchasing OptiPower Manager necessitates the inclusion of the OptiEnergy Suite and PowerPro Optimize. This comprehensive power management bundle ensures users can effectively monitor and optimize power usage. OptiEnergy Suite offers robust tools for energy management and efficiency, while PowerPro Optimize provides critical power optimization features. Combined with OptiPower Manager, these tools help in achieving significant energy savings and power control.\n\n5. AIOptics Vision Bundle: Lastly, AIOptics Vision requires the Workflow Genius and AI DesignShift as part of its package. This requirement ensures customers have access to superior workflow management tools and AI capabilities. Workflow Genius enhances project management and operational workflows, while AI DesignShift contributes AI-enhanced design innovations. Together with AIOptics Vision, these products deliver a powerful platform for optical analysis and design.\n\nUnderstanding these mandatory bundles helps ensure you receive the full potential of each product offered by TechPulse Solution. By purchasing these curated packages, customers benefit from enhanced functionality, superior performance, and seamless integration, providing an unparalleled technological advantage.", 'summary': 'Mandatory Bundles for Quotes', 'urlname': '1745269013-flbrj'}], 'var_call_7UYiVKaU7Ckp7Km7hwsPbCqK': [{'Id': '01tWt000006hV57IAE', 'Name': 'PulseSim Pro', 'Description': 'Advanced simulation and verification software for optimizing circuit designs.'}, {'Id': '#01tWt000006hVDBIA2', 'Name': 'CircuitMaster Analyzer', 'Description': 'Sophisticated simulation software ensuring precise verification and testing.'}, {'Id': '01tWt000006hVQ6IAM', 'Name': 'VeriSim Express  ', 'Description': 'Express verification software focusing on speed and precision for circuit testing.'}], 'var_call_zN27C2qEoTC92nWP2NRObMM7': [{'id': 'ka0Wt000000Ens5IAC', 'title': 'Mandatory Bundles for Quotes', 'faq_answer__c': "In the fast-paced world of technological solutions, understanding mandatory product bundles is crucial for securing the best performance and compatibility. At TechPulse Solution, we have streamlined our product offerings, ensuring optimal functionality through specific bundled requirements. This guide provides a comprehensive overview of the mandatory bundles required for quoting our top-tier products.\n\n1. PulseSim Pro Bundle: When purchasing PulseSim Pro, customers must also include the CircuitMaster Analyzer and VeriSim Express in their package. This bundling is designed to enhance your simulation experience, providing unparalleled accuracy and efficiency. CircuitMaster Analyzer works to deliver precise circuit analysis, while VeriSim Express complements it by facilitating swift verification processes. Together, these tools enhance the functionalities of PulseSim Pro, resulting in top-notch simulation capabilities.\n\n2. CloudLink Designer Bundle: To acquire the CloudLink Designer, it's essential to purchase DesignEdge Pro and AI DesignShift as well. This trio creates a robust design platform ideally suited for cloud-based operations. DesignEdge Pro offers advanced design capabilities, ensuring top-quality outcomes, while AI DesignShift incorporates artificial intelligence for intelligent design adaptability and innovation. By combining these products with CloudLink Designer, you achieve a seamless integration that improves performance and design fluidity on the cloud.\n\n3. AI Cirku-Tech Bundle: Customers interested in AI Cirku-Tech must also consider acquiring CircuitAI Innovator and AI DesignShift. Partnered with CircuitAI Innovator, AI Cirku-Tech brings artificial intelligence enhancements to circuit design, optimizing both creativity and efficiency. AI DesignShift, on the other hand, introduces advanced AI-driven design shifts, facilitating a broader scope of design possibilities. This bundle offers a significant leap forward in circuit technology, fully realizing the potential of AI integration.\n\n4. OptiPower Manager Bundle: Purchasing OptiPower Manager necessitates the inclusion of the OptiEnergy Suite and PowerPro Optimize. This comprehensive power management bundle ensures users can effectively monitor and optimize power usage. OptiEnergy Suite offers robust tools for energy management and efficiency, while PowerPro Optimize provides critical power optimization features. Combined with OptiPower Manager, these tools help in achieving significant energy savings and power control.\n\n5. AIOptics Vision Bundle: Lastly, AIOptics Vision requires the Workflow Genius and AI DesignShift as part of its package. This requirement ensures customers have access to superior workflow management tools and AI capabilities. Workflow Genius enhances project management and operational workflows, while AI DesignShift contributes AI-enhanced design innovations. Together with AIOptics Vision, these products deliver a powerful platform for optical analysis and design.\n\nUnderstanding these mandatory bundles helps ensure you receive the full potential of each product offered by TechPulse Solution. By purchasing these curated packages, customers benefit from enhanced functionality, superior performance, and seamless integration, providing an unparalleled technological advantage."}], 'var_call_gjIGUKlxCvfnzAeGAmP38SfR': [{'Id': '01uWt0000027P3lIAE', 'Product2Id': '01tWt000006hV57IAE', 'UnitPrice': '499.99'}, {'Id': '#01uWt0000027PWnIAM', 'Product2Id': '01tWt000006hVQ6IAM', 'UnitPrice': '429.99'}]}

exec(code, env_args)
