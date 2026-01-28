code = """import json
# Accessing previous query results
transcripts = var_call_6X89Ljnwv9iaFZxYbL4NMN9k
knowledge = var_call_DtFF6Xv4mX21Geoy4lIIuC7Z

# Basic text extraction
transcript_text = "".join([t.get('Body__c','') for t in transcripts])
knowledge_text = "".join([k.get('faq_answer__c','') for k in knowledge])

# Heuristics to determine BANT failures
failures = []

# Authority: Check if lead states they need to consult others or lack final decision
if any(phrase in transcript_text.lower() for phrase in ["i'll need to consult", "i need to consult", "i don't have the final say", "i do not have the final say", "need to consult with", "consult with the finance", "consult with the finance team", "need to check with", "need to discuss with"]):
    failures.append('Authority')

# Budget: Check if budget mentioned appears sufficient for product only, but knowledge article indicates mandatory bundles that could increase cost
budget_mentioned = False
budget_sufficient_for_units = False
if '$' in transcript_text:
    budget_mentioned = True
    # crude parse for budget and unit price
    # look for patterns like "$2,261" and "$500"
    import re
    budgets = re.findall(r"\$[0-9,]+", transcript_text)
    nums = [int(b.replace('$','').replace(',','')) for b in budgets]
    if len(nums) >= 2:
        # assume first is budget, second is unit price
        budget_val = nums[0]
        unit_price = nums[1]
        # transcript mentions 4 units explicitly
        if 'four units' in transcript_text.lower() or '4 units' in transcript_text.lower():
            total_price = 4 * unit_price
            if budget_val >= total_price:
                budget_sufficient_for_units = True

# Knowledge: check for mandatory bundles mentioning PulseSim Pro
if 'pulsesim pro' in knowledge_text.lower() and ('must also include' in knowledge_text.lower() or 'mandatory bundle' in knowledge_text.lower() or 'mandatory bundles' in knowledge_text.lower()):
    # If budget only covered base units, mandatory bundles may cause budget risk
    if budget_mentioned and budget_sufficient_for_units:
        failures.append('Budget')
    elif budget_mentioned and not budget_sufficient_for_units:
        failures.append('Budget')

# Need: Check if explicit need stated
if not any(phrase in transcript_text.lower() for phrase in ["interested", "want to", "need", "enhance", "looking to", "would like to move forward"]):
    failures.append('Need')

# Timeline: Check if lead expressed timeline concerns unresolved
# Transcript shows "tight timeline for installation" but vendor assured quick install
if any(phrase in transcript_text.lower() for phrase in ["tight timeline", "tight schedules", "timeline" , "installation" ]):
    # if vendor addresses and seems to satisfy timeline, assume timeline met
    if not any(phrase in transcript_text.lower() for phrase in ["aim to complete installations within a day", "complete installations within a day", "one day", "within a day", "we usually aim to complete installations within a day"]) :
        failures.append('Timeline')

# Ensure uniqueness and preserve the logical order Budget, Authority, Need, Timeline if present
order = ['Budget','Authority','Need','Timeline']
final_failures = [f for f in order if f in failures]

# Prepare result as JSON-serializable string (list)
result = json.dumps(final_failures)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_6X89Ljnwv9iaFZxYbL4NMN9k': [{'Id': 'a05Wt000003SukEIAS', 'OpportunityId__c': 'None', 'LeadId__c': '00QWt0000089AekMAE', 'Body__c': "[2023-10-21T10:02:00] Ava Sullivan: Hi Ali, this is Ava Sullivan from TechSolutions. How are you today?\n[2023-10-21T10:02:10] Ali Hussein: Hi Ava, I'm doing well, thank you. How about you?\n[2023-10-21T10:02:20] Ava Sullivan: I'm great, thank you for asking! I'm glad we could connect. I was looking over the details you provided about your interest in the PulseSim Pro. Is now a good time to discuss?\n[2023-10-21T10:02:30] Ali Hussein: Yes, now works for me. I'm interested to learn more and see how it fits with what we need.\n[2023-10-21T10:02:40] Ava Sullivan: Fantastic! From what you’ve mentioned, you’re interested in four units of the PulseSim Pro, correct?\n[2023-10-21T10:02:50] Ali Hussein: That's right. We want to enhance our simulation capabilities, and the PulseSim Pro seems like a great fit.\n[2023-10-21T10:03:05] Ava Sullivan: Absolutely. The PulseSim Pro is one of our top products for high precision simulation. It offers advanced analytics and seamless integration with existing systems, which is great for boosting efficiency.\n[2023-10-21T10:03:15] Ali Hussein: Those features sound beneficial. We do have a tight timeline for installation, though. Could you tell me more about that?\n[2023-10-21T10:03:30] Ava Sullivan: Certainly. We understand the importance of meeting tight schedules. We usually aim to complete installations within a day and ensure everything runs smoothly. Our technical team is very efficient.\n[2023-10-21T10:03:40] Ali Hussein: That’s reassuring. And as for the budget, how does it look for four units?\n[2023-10-21T10:03:55] Ava Sullivan: Considering your budget is $2,261, I think we can work something out. Each PulseSim Pro unit is priced at $500. For four units, it will come to $2,000. This is below your budget, leaving room for additional services if you wish.\n[2023-10-21T10:04:10] Ali Hussein: That fits really well. I'd like to move forward, but I'll need to consult with the finance team here since I don’t have the final say.\n[2023-10-21T10:04:20] Ava Sullivan: I completely understand, Ali. Would you like me to send over a detailed proposal and pricing information so you can present it to your team?\n[2023-10-21T10:04:25] Ali Hussein: Yes, please. That would be very helpful.\n[2023-10-21T10:04:35] Ava Sullivan: Great! I'll have that to you by the end of the day. Is there anything else you would need from my side?\n[2023-10-21T10:04:40] Ali Hussein: No, that sounds good for now. Thank you, Ava.\n[2023-10-21T10:04:50] Ava Sullivan: You're welcome, Ali. If any questions come up, feel free to reach out. Have a wonderful day!\n[2023-10-21T10:04:55] Ali Hussein: Thanks, Ava. You too!", 'CreatedDate': '2023-10-21T10:02:00.000+0000', 'EndTime__c': '2023-10-21'}], 'var_call_DtFF6Xv4mX21Geoy4lIIuC7Z': [{'id': 'ka0Wt000000Ens5IAC', 'title': 'Mandatory Bundles for Quotes', 'faq_answer__c': "In the fast-paced world of technological solutions, understanding mandatory product bundles is crucial for securing the best performance and compatibility. At TechPulse Solution, we have streamlined our product offerings, ensuring optimal functionality through specific bundled requirements. This guide provides a comprehensive overview of the mandatory bundles required for quoting our top-tier products.\n\n1. PulseSim Pro Bundle: When purchasing PulseSim Pro, customers must also include the CircuitMaster Analyzer and VeriSim Express in their package. This bundling is designed to enhance your simulation experience, providing unparalleled accuracy and efficiency. CircuitMaster Analyzer works to deliver precise circuit analysis, while VeriSim Express complements it by facilitating swift verification processes. Together, these tools enhance the functionalities of PulseSim Pro, resulting in top-notch simulation capabilities.\n\n2. CloudLink Designer Bundle: To acquire the CloudLink Designer, it's essential to purchase DesignEdge Pro and AI DesignShift as well. This trio creates a robust design platform ideally suited for cloud-based operations. DesignEdge Pro offers advanced design capabilities, ensuring top-quality outcomes, while AI DesignShift incorporates artificial intelligence for intelligent design adaptability and innovation. By combining these products with CloudLink Designer, you achieve a seamless integration that improves performance and design fluidity on the cloud.\n\n3. AI Cirku-Tech Bundle: Customers interested in AI Cirku-Tech must also consider acquiring CircuitAI Innovator and AI DesignShift. Partnered with CircuitAI Innovator, AI Cirku-Tech brings artificial intelligence enhancements to circuit design, optimizing both creativity and efficiency. AI DesignShift, on the other hand, introduces advanced AI-driven design shifts, facilitating a broader scope of design possibilities. This bundle offers a significant leap forward in circuit technology, fully realizing the potential of AI integration.\n\n4. OptiPower Manager Bundle: Purchasing OptiPower Manager necessitates the inclusion of the OptiEnergy Suite and PowerPro Optimize. This comprehensive power management bundle ensures users can effectively monitor and optimize power usage. OptiEnergy Suite offers robust tools for energy management and efficiency, while PowerPro Optimize provides critical power optimization features. Combined with OptiPower Manager, these tools help in achieving significant energy savings and power control.\n\n5. AIOptics Vision Bundle: Lastly, AIOptics Vision requires the Workflow Genius and AI DesignShift as part of its package. This requirement ensures customers have access to superior workflow management tools and AI capabilities. Workflow Genius enhances project management and operational workflows, while AI DesignShift contributes AI-enhanced design innovations. Together with AIOptics Vision, these products deliver a powerful platform for optical analysis and design.\n\nUnderstanding these mandatory bundles helps ensure you receive the full potential of each product offered by TechPulse Solution. By purchasing these curated packages, customers benefit from enhanced functionality, superior performance, and seamless integration, providing an unparalleled technological advantage.", 'summary': 'Mandatory Bundles for Quotes', 'urlname': '1745269013-flbrj'}]}

exec(code, env_args)
