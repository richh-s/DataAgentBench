code = """import re
import json

# Access the previous query results stored in variables
lead = var_call_GWYcQSQTjMj3V9CaJjxBMgdi[0]
transcripts = var_call_CWDHd4yHHuOxPJ1qUl7olHxR
knowledge = var_call_4H3qalUhqWeXxqlAKSNzcrOz

body = transcripts[0].get('Body__c','')
qa = knowledge[0]

failing = []
reasons = {}

# Check Authority: look for phrases indicating lead cannot decide
if re.search(r"don't have the final say|need to consult|consult with|not the final decision|will need approval|i'll need to consult", body, re.IGNORECASE):
    failing.append('Authority')
    reasons['Authority'] = 'Lead stated they need to consult with finance / do not have final approval.'

# Extract budget, unit price, quantity from transcript if present
budget = None
unit_price = None
quantity = None

m_budget = re.search(r"budget is \$?([0-9,]+(?:\.[0-9]{2})?)", body, re.IGNORECASE)
if m_budget:
    budget = float(m_budget.group(1).replace(',',''))

m_unit = re.search(r"Each .*unit is priced at \$?([0-9,]+(?:\.[0-9]{2})?)", body, re.IGNORECASE)
if m_unit:
    unit_price = float(m_unit.group(1).replace(',',''))

m_qty = re.search(r"interested in (?:four|4) units|we want to (?:purchase|buy) (?:four|4) units", body, re.IGNORECASE)
if m_qty:
    # handle spoken 'four' or '4'
    if re.search(r"four", m_qty.group(0), re.IGNORECASE):
        quantity = 4
    else:
        quantity = 4

# Also capture explicit "for four units" pattern
m_qty2 = re.search(r"for (?:four|4) units", body, re.IGNORECASE)
if m_qty2:
    quantity = 4

# Fallback: look for total price mentioned
m_total = re.search(r"it will come to \$?([0-9,]+(?:\.[0-9]{2})?)", body, re.IGNORECASE)
if m_total and not (unit_price and quantity):
    total = float(m_total.group(1).replace(',',''))
else:
    total = None

if unit_price and quantity:
    total = unit_price * quantity

# Check budget feasibility
budget_issue = False
if budget is not None and total is not None:
    margin = budget - total
    # Check knowledge article for mandatory bundles for PulseSim Pro
    bundles_required = 'PulseSim Pro' in qa.get('title','') or 'PulseSim Pro' in qa.get('faq_answer__c','') or 'PulseSim Pro' in qa.get('summary','')
    # If bundles are required and margin is small (<500), consider budget failing because agent didn't include bundles
    if bundles_required and margin <= 500:
        failing.append('Budget')
        reasons['Budget'] = 'Knowledge article indicates mandatory bundles for PulseSim Pro; the quoted price in call did not include bundles and remaining budget margin is small.'
    else:
        # If margin negative, definitely budget fails
        if margin < 0:
            failing.append('Budget')
            reasons['Budget'] = 'Quoted total exceeds stated budget.'

# If no budget info, mark Budget as unknown but do not fail automatically

# Need: check if lead expressed interest and problem to solve
if re.search(r"interested to learn more|we want to enhance|that fits|i'd like to move forward|interested", body, re.IGNORECASE):
    need_present = True
else:
    need_present = False

if not need_present:
    failing.append('Need')
    reasons['Need'] = 'No clear expressed need in latest transcript.'

# Timeline: look for mention of timeline concerns
if re.search(r"tight timeline|timeline", body, re.IGNORECASE):
    # Agent confirmed install within a day -> timeline likely ok
    if re.search(r"complete installations within a day|within a day", body, re.IGNORECASE):
        timeline_ok = True
    else:
        timeline_ok = False
else:
    timeline_ok = True

if not timeline_ok:
    failing.append('Timeline')
    reasons['Timeline'] = 'Timeline constraints not addressed.'

# Deduplicate failing list and preserve order Budget, Authority, Need, Timeline as possible
ordered = [f for f in ['Budget','Authority','Need','Timeline'] if f in failing]

output = {'failing_factors': ordered, 'reasons': reasons}
print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_GWYcQSQTjMj3V9CaJjxBMgdi': [{'Id': '00QWt0000089AekMAE', 'FirstName': 'Ali', 'LastName': 'Hussein', 'Email': 'ali.hussein@baghdadhtechhub.com', 'Phone': '555-452-7654', 'Company': 'Baghdad Tech Hub', 'Status': 'Converted', 'ConvertedContactId': 'None', 'ConvertedAccountId': 'None', 'Title': 'Head of Emerging Technologies', 'CreatedDate': '2023-08-18T15:35:50.000+0000', 'ConvertedDate': 'None', 'IsConverted': '0', 'OwnerId': '005Wt000003NErnIAG'}], 'var_call_CWDHd4yHHuOxPJ1qUl7olHxR': [{'Id': 'a05Wt000003SukEIAS', 'OpportunityId__c': 'None', 'LeadId__c': '00QWt0000089AekMAE', 'Body__c': "[2023-10-21T10:02:00] Ava Sullivan: Hi Ali, this is Ava Sullivan from TechSolutions. How are you today?\n[2023-10-21T10:02:10] Ali Hussein: Hi Ava, I'm doing well, thank you. How about you?\n[2023-10-21T10:02:20] Ava Sullivan: I'm great, thank you for asking! I'm glad we could connect. I was looking over the details you provided about your interest in the PulseSim Pro. Is now a good time to discuss?\n[2023-10-21T10:02:30] Ali Hussein: Yes, now works for me. I'm interested to learn more and see how it fits with what we need.\n[2023-10-21T10:02:40] Ava Sullivan: Fantastic! From what you’ve mentioned, you’re interested in four units of the PulseSim Pro, correct?\n[2023-10-21T10:02:50] Ali Hussein: That's right. We want to enhance our simulation capabilities, and the PulseSim Pro seems like a great fit.\n[2023-10-21T10:03:05] Ava Sullivan: Absolutely. The PulseSim Pro is one of our top products for high precision simulation. It offers advanced analytics and seamless integration with existing systems, which is great for boosting efficiency.\n[2023-10-21T10:03:15] Ali Hussein: Those features sound beneficial. We do have a tight timeline for installation, though. Could you tell me more about that?\n[2023-10-21T10:03:30] Ava Sullivan: Certainly. We understand the importance of meeting tight schedules. We usually aim to complete installations within a day and ensure everything runs smoothly. Our technical team is very efficient.\n[2023-10-21T10:03:40] Ali Hussein: That’s reassuring. And as for the budget, how does it look for four units?\n[2023-10-21T10:03:55] Ava Sullivan: Considering your budget is $2,261, I think we can work something out. Each PulseSim Pro unit is priced at $500. For four units, it will come to $2,000. This is below your budget, leaving room for additional services if you wish.\n[2023-10-21T10:04:10] Ali Hussein: That fits really well. I'd like to move forward, but I'll need to consult with the finance team here since I don’t have the final say.\n[2023-10-21T10:04:20] Ava Sullivan: I completely understand, Ali. Would you like me to send over a detailed proposal and pricing information so you can present it to your team?\n[2023-10-21T10:04:25] Ali Hussein: Yes, please. That would be very helpful.\n[2023-10-21T10:04:35] Ava Sullivan: Great! I'll have that to you by the end of the day. Is there anything else you would need from my side?\n[2023-10-21T10:04:40] Ali Hussein: No, that sounds good for now. Thank you, Ava.\n[2023-10-21T10:04:50] Ava Sullivan: You're welcome, Ali. If any questions come up, feel free to reach out. Have a wonderful day!\n[2023-10-21T10:04:55] Ali Hussein: Thanks, Ava. You too!", 'CreatedDate': '2023-10-21T10:02:00.000+0000', 'EndTime__c': '2023-10-21'}], 'var_call_4H3qalUhqWeXxqlAKSNzcrOz': [{'id': 'ka0Wt000000Ens5IAC', 'title': 'Mandatory Bundles for Quotes', 'faq_answer__c': "In the fast-paced world of technological solutions, understanding mandatory product bundles is crucial for securing the best performance and compatibility. At TechPulse Solution, we have streamlined our product offerings, ensuring optimal functionality through specific bundled requirements. This guide provides a comprehensive overview of the mandatory bundles required for quoting our top-tier products.\n\n1. PulseSim Pro Bundle: When purchasing PulseSim Pro, customers must also include the CircuitMaster Analyzer and VeriSim Express in their package. This bundling is designed to enhance your simulation experience, providing unparalleled accuracy and efficiency. CircuitMaster Analyzer works to deliver precise circuit analysis, while VeriSim Express complements it by facilitating swift verification processes. Together, these tools enhance the functionalities of PulseSim Pro, resulting in top-notch simulation capabilities.\n\n2. CloudLink Designer Bundle: To acquire the CloudLink Designer, it's essential to purchase DesignEdge Pro and AI DesignShift as well. This trio creates a robust design platform ideally suited for cloud-based operations. DesignEdge Pro offers advanced design capabilities, ensuring top-quality outcomes, while AI DesignShift incorporates artificial intelligence for intelligent design adaptability and innovation. By combining these products with CloudLink Designer, you achieve a seamless integration that improves performance and design fluidity on the cloud.\n\n3. AI Cirku-Tech Bundle: Customers interested in AI Cirku-Tech must also consider acquiring CircuitAI Innovator and AI DesignShift. Partnered with CircuitAI Innovator, AI Cirku-Tech brings artificial intelligence enhancements to circuit design, optimizing both creativity and efficiency. AI DesignShift, on the other hand, introduces advanced AI-driven design shifts, facilitating a broader scope of design possibilities. This bundle offers a significant leap forward in circuit technology, fully realizing the potential of AI integration.\n\n4. OptiPower Manager Bundle: Purchasing OptiPower Manager necessitates the inclusion of the OptiEnergy Suite and PowerPro Optimize. This comprehensive power management bundle ensures users can effectively monitor and optimize power usage. OptiEnergy Suite offers robust tools for energy management and efficiency, while PowerPro Optimize provides critical power optimization features. Combined with OptiPower Manager, these tools help in achieving significant energy savings and power control.\n\n5. AIOptics Vision Bundle: Lastly, AIOptics Vision requires the Workflow Genius and AI DesignShift as part of its package. This requirement ensures customers have access to superior workflow management tools and AI capabilities. Workflow Genius enhances project management and operational workflows, while AI DesignShift contributes AI-enhanced design innovations. Together with AIOptics Vision, these products deliver a powerful platform for optical analysis and design.\n\nUnderstanding these mandatory bundles helps ensure you receive the full potential of each product offered by TechPulse Solution. By purchasing these curated packages, customers benefit from enhanced functionality, superior performance, and seamless integration, providing an unparalleled technological advantage.", 'summary': 'Mandatory Bundles for Quotes'}]}

exec(code, env_args)
