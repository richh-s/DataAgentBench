code = """import json
# Access stored query results
lead = var_call_FOXjirGk1b4zaJkVOZ4T56Yh[0] if isinstance(var_call_FOXjirGk1b4zaJkVOZ4T56Yh, list) and len(var_call_FOXjirGk1b4zaJkVOZ4T56Yh)>0 else {}
transcripts = var_call_b2KKtCLEdANNPkiBt3dmnWhm if isinstance(var_call_b2KKtCLEdANNPkiBt3dmnWhm, list) else []
kb_mandatory = var_call_UAkO1Lvli0nIBf9ewmZUL3XC if isinstance(var_call_UAkO1Lvli0nIBf9ewmZUL3XC, list) else []
# var_call_m3VAyxmHZ9u2wZYJudiI6B7t may be a file path (large result)
timeline_policy_text = None
if isinstance(var_call_m3VAyxmHZ9u2wZYJudiI6B7t, str):
    try:
        with open(var_call_m3VAyxmHZ9u2wZYJudiI6B7t, 'r', encoding='utf-8') as f:
            content = f.read()
            timeline_policy_text = content
    except Exception as e:
        timeline_policy_text = None

# Simple extraction from transcript to decide BANT factors
budget_ok = False
authority_ok = False
need_ok = False
timeline_ok = False

if transcripts:
    body = transcripts[0].get('Body__c','')
    lower = body.lower()
    # Budget: look for budget and pricing statements
    if 'budget' in lower and '$' in lower:
        # crude parse: find budget amount and price per unit
        try:
            # find budget value after 'budget is'
            import re
            m = re.search(r'budget is \$?([0-9,]+)', body, re.IGNORECASE)
            budget_val = None
            if m:
                budget_val = int(m.group(1).replace(',',''))
            # find per unit price
            m2 = re.search(r'priced at \$?([0-9,]+)', body, re.IGNORECASE)
            unit_price = None
            if m2:
                unit_price = int(m2.group(1).replace(',',''))
            # find quantity
            m3 = re.search(r'(?:interested in|interested in four units|interested in (\d+) units|we want to .* (\d+) units)', body, re.IGNORECASE)
            qty = None
            if 'four units' in lower:
                qty = 4
            elif m3 and (m3.group(1) or m3.group(2)):
                qty = int(m3.group(1) or m3.group(2))
            if budget_val is not None and unit_price is not None and qty is not None:
                total = unit_price * qty
                if total <= budget_val:
                    budget_ok = True
        except Exception:
            budget_ok = False
    # Authority: look for needing to consult
    if 'need to consult' in lower or 'consult with' in lower or 'i don\'t have the final say' in lower or 'need to consult with the finance' in lower or 'consult with the finance team' in lower:
        authority_ok = False
    else:
        # if explicit "i'll approve" or "i have final say"
        if 'final say' in lower or 'approve' in lower:
            authority_ok = True
        else:
            # default to False unless clear
            authority_ok = True
    # Need: expressions of fit
    if 'interested' in lower or 'fits' in lower or 'want to' in lower or 'need' in lower:
        need_ok = True
    # Timeline: lead said tight timeline, agent promised quick install; check policy
    if 'tight timeline' in lower or 'tight' in lower:
        # check policy text for timelines for volumes
        timeline_ok = False
        if timeline_policy_text:
            if 'Small Batch Purchase (Volume: 5)' in timeline_policy_text and '3 days' in timeline_policy_text:
                # for 4 units, likely 3 days; agent said 1 day in call which conflicts
                # Without explicit required deadline from lead, we mark timeline as uncertain; since lead said tight timeline, mark as not met
                timeline_ok = False
        else:
            timeline_ok = True
    else:
        timeline_ok = True

# Based on above, determine failed BANT factors
failed = []
if not budget_ok:
    failed.append('Budget')
if not authority_ok:
    failed.append('Authority')
if not need_ok:
    failed.append('Need')
if not timeline_ok:
    failed.append('Timeline')

# However, the authority parsing above defaulted to True; override using explicit transcript phrase
# Check explicitly for phrases indicating lack of authority
body_lower = transcripts[0].get('Body__c','').lower() if transcripts else ''
if 'consult with the finance' in body_lower or 'i don\'t have the final say' in body_lower or 'i will need to consult' in body_lower:
    if 'Authority' not in failed:
        failed.append('Authority')

# Budget: ensure if transcript clearly showed budget covered price
if 'budget is' in body_lower and 'priced at' in body_lower:
    # we attempted to set budget_ok earlier; if budget_ok True remove Budget from failed
    if budget_ok and 'Budget' in failed:
        failed.remove('Budget')

# Ensure uniqueness and consistent ordering as per BANT order
order = ['Budget','Authority','Need','Timeline']
failed_sorted = [f for f in order if f in failed]

print("__RESULT__:")
print(json.dumps(failed_sorted))"""

env_args = {'var_call_FOXjirGk1b4zaJkVOZ4T56Yh': [{'Id': '00QWt0000089AekMAE', 'FirstName': 'Ali', 'LastName': 'Hussein', 'Email': 'ali.hussein@baghdadhtechhub.com', 'Phone': '555-452-7654', 'Company': 'Baghdad Tech Hub', 'Status': 'Converted', 'ConvertedContactId': 'None', 'ConvertedAccountId': 'None', 'Title': 'Head of Emerging Technologies', 'CreatedDate': '2023-08-18T15:35:50.000+0000', 'ConvertedDate': 'None', 'IsConverted': '0', 'OwnerId': '005Wt000003NErnIAG'}], 'var_call_b2KKtCLEdANNPkiBt3dmnWhm': [{'Id': 'a05Wt000003SukEIAS', 'OpportunityId__c': 'None', 'LeadId__c': '00QWt0000089AekMAE', 'Body__c': "[2023-10-21T10:02:00] Ava Sullivan: Hi Ali, this is Ava Sullivan from TechSolutions. How are you today?\n[2023-10-21T10:02:10] Ali Hussein: Hi Ava, I'm doing well, thank you. How about you?\n[2023-10-21T10:02:20] Ava Sullivan: I'm great, thank you for asking! I'm glad we could connect. I was looking over the details you provided about your interest in the PulseSim Pro. Is now a good time to discuss?\n[2023-10-21T10:02:30] Ali Hussein: Yes, now works for me. I'm interested to learn more and see how it fits with what we need.\n[2023-10-21T10:02:40] Ava Sullivan: Fantastic! From what you’ve mentioned, you’re interested in four units of the PulseSim Pro, correct?\n[2023-10-21T10:02:50] Ali Hussein: That's right. We want to enhance our simulation capabilities, and the PulseSim Pro seems like a great fit.\n[2023-10-21T10:03:05] Ava Sullivan: Absolutely. The PulseSim Pro is one of our top products for high precision simulation. It offers advanced analytics and seamless integration with existing systems, which is great for boosting efficiency.\n[2023-10-21T10:03:15] Ali Hussein: Those features sound beneficial. We do have a tight timeline for installation, though. Could you tell me more about that?\n[2023-10-21T10:03:30] Ava Sullivan: Certainly. We understand the importance of meeting tight schedules. We usually aim to complete installations within a day and ensure everything runs smoothly. Our technical team is very efficient.\n[2023-10-21T10:03:40] Ali Hussein: That’s reassuring. And as for the budget, how does it look for four units?\n[2023-10-21T10:03:55] Ava Sullivan: Considering your budget is $2,261, I think we can work something out. Each PulseSim Pro unit is priced at $500. For four units, it will come to $2,000. This is below your budget, leaving room for additional services if you wish.\n[2023-10-21T10:04:10] Ali Hussein: That fits really well. I'd like to move forward, but I'll need to consult with the finance team here since I don’t have the final say.\n[2023-10-21T10:04:20] Ava Sullivan: I completely understand, Ali. Would you like me to send over a detailed proposal and pricing information so you can present it to your team?\n[2023-10-21T10:04:25] Ali Hussein: Yes, please. That would be very helpful.\n[2023-10-21T10:04:35] Ava Sullivan: Great! I'll have that to you by the end of the day. Is there anything else you would need from my side?\n[2023-10-21T10:04:40] Ali Hussein: No, that sounds good for now. Thank you, Ava.\n[2023-10-21T10:04:50] Ava Sullivan: You're welcome, Ali. If any questions come up, feel free to reach out. Have a wonderful day!\n[2023-10-21T10:04:55] Ali Hussein: Thanks, Ava. You too!", 'CreatedDate': '2023-10-21T10:02:00.000+0000', 'EndTime__c': '2023-10-21'}], 'var_call_m3VAyxmHZ9u2wZYJudiI6B7t': 'file_storage/call_m3VAyxmHZ9u2wZYJudiI6B7t.json', 'var_call_UAkO1Lvli0nIBf9ewmZUL3XC': [{'id': 'ka0Wt000000Ens5IAC', 'title': 'Mandatory Bundles for Quotes', 'faq_answer__c': "In the fast-paced world of technological solutions, understanding mandatory product bundles is crucial for securing the best performance and compatibility. At TechPulse Solution, we have streamlined our product offerings, ensuring optimal functionality through specific bundled requirements. This guide provides a comprehensive overview of the mandatory bundles required for quoting our top-tier products.\n\n1. PulseSim Pro Bundle: When purchasing PulseSim Pro, customers must also include the CircuitMaster Analyzer and VeriSim Express in their package. This bundling is designed to enhance your simulation experience, providing unparalleled accuracy and efficiency. CircuitMaster Analyzer works to deliver precise circuit analysis, while VeriSim Express complements it by facilitating swift verification processes. Together, these tools enhance the functionalities of PulseSim Pro, resulting in top-notch simulation capabilities.\n\n2. CloudLink Designer Bundle: To acquire the CloudLink Designer, it's essential to purchase DesignEdge Pro and AI DesignShift as well. This trio creates a robust design platform ideally suited for cloud-based operations. DesignEdge Pro offers advanced design capabilities, ensuring top-quality outcomes, while AI DesignShift incorporates artificial intelligence for intelligent design adaptability and innovation. By combining these products with CloudLink Designer, you achieve a seamless integration that improves performance and design fluidity on the cloud.\n\n3. AI Cirku-Tech Bundle: Customers interested in AI Cirku-Tech must also consider acquiring CircuitAI Innovator and AI DesignShift. Partnered with CircuitAI Innovator, AI Cirku-Tech brings artificial intelligence enhancements to circuit design, optimizing both creativity and efficiency. AI DesignShift, on the other hand, introduces advanced AI-driven design shifts, facilitating a broader scope of design possibilities. This bundle offers a significant leap forward in circuit technology, fully realizing the potential of AI integration.\n\n4. OptiPower Manager Bundle: Purchasing OptiPower Manager necessitates the inclusion of the OptiEnergy Suite and PowerPro Optimize. This comprehensive power management bundle ensures users can effectively monitor and optimize power usage. OptiEnergy Suite offers robust tools for energy management and efficiency, while PowerPro Optimize provides critical power optimization features. Combined with OptiPower Manager, these tools help in achieving significant energy savings and power control.\n\n5. AIOptics Vision Bundle: Lastly, AIOptics Vision requires the Workflow Genius and AI DesignShift as part of its package. This requirement ensures customers have access to superior workflow management tools and AI capabilities. Workflow Genius enhances project management and operational workflows, while AI DesignShift contributes AI-enhanced design innovations. Together with AIOptics Vision, these products deliver a powerful platform for optical analysis and design.\n\nUnderstanding these mandatory bundles helps ensure you receive the full potential of each product offered by TechPulse Solution. By purchasing these curated packages, customers benefit from enhanced functionality, superior performance, and seamless integration, providing an unparalleled technological advantage.", 'summary': 'Mandatory Bundles for Quotes', 'urlname': '1745269013-flbrj'}]}

exec(code, env_args)
