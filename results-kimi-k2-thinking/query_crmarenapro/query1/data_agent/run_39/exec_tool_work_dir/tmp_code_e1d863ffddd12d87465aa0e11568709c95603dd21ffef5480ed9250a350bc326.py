code = """# Review the voice call transcript stored in var_functions.query_db:0
import json
import re

# Access the transcript
transcript_data = locals()['var_functions.query_db:0']

if not transcript_data:
    print('__RESULT__:')
    print('[]')
else:
    transcript = transcript_data[0]
    body = transcript['Body__c']
    
    # Analyze BANT factors
    bant_factors = {
        'Budget': False,
        'Authority': False,
        'Need': False,
        'Timeline': False
    }
    
    # Budget analysis
    budget_pattern = r'\$?\d[\d,]*(?:\.\d{2})?'
    budget_matches = re.findall(budget_pattern, body)
    # Check for budget mention and if product cost fits
    if '$2,261' in body and '$2,000' in body:
        bant_factors['Budget'] = True
    
    # Authority analysis  
    authority_indicators = [
        "don't have the final say",
        "need to consult",
        "finance team",
        "get approval"
    ]
    for indicator in authority_indicators:
        if indicator.lower() in body.lower():
            # These indicate LACK of authority
            bant_factors['Authority'] = False
            break
    else:
        # If no indicators of lacking authority, assume authority is met
        if any(word in body.lower() for word in ["i can decide", "i have the authority", "i can approve"]):
            bant_factors['Authority'] = True
    
    # Need analysis
    need_indicators = [
        "enhance our simulation capabilities",
        "great fit",
        "interested to learn more"
    ]
    for indicator in need_indicators:
        if indicator.lower() in body.lower():
            bant_factors['Need'] = True
            break
    
    # Timeline analysis
    timeline_indicators = [
        "tight timeline",
        "complete installations within",
        "deadline",
        "need it by"
    ]
    timeline_found = False
    for indicator in timeline_indicators:
        if indicator.lower() in body.lower():
            timeline_found = True
            break
    
    # Check if actual date/commitment exists
    if timeline_found:
        # If only general mention but no specific commitment, treat as not met
        if "within a day" in body.lower() or "tight timeline" in body.lower():
            # This is not a committed timeline, just a general statement
            bant_factors['Timeline'] = False
        else:
            bant_factors['Timeline'] = True
    else:
        bant_factors['Timeline'] = False
    
    # Determine which factors are NOT met
    failed_factors = []
    if not bant_factors['Budget']:
        failed_factors.append('Budget')
    if not bant_factors['Authority']:
        failed_factors.append('Authority')  
    if not bant_factors['Need']:
        failed_factors.append('Need')
    if not bant_factors['Timeline']:
        failed_factors.append('Timeline')
    
    print('__RESULT__:')
    print(json.dumps(failed_factors))"""

env_args = {'var_functions.query_db:0': [{'Id': 'a05Wt000003SukEIAS', 'OpportunityId__c': 'None', 'LeadId__c': '00QWt0000089AekMAE', 'Body__c': "[2023-10-21T10:02:00] Ava Sullivan: Hi Ali, this is Ava Sullivan from TechSolutions. How are you today?\n[2023-10-21T10:02:10] Ali Hussein: Hi Ava, I'm doing well, thank you. How about you?\n[2023-10-21T10:02:20] Ava Sullivan: I'm great, thank you for asking! I'm glad we could connect. I was looking over the details you provided about your interest in the PulseSim Pro. Is now a good time to discuss?\n[2023-10-21T10:02:30] Ali Hussein: Yes, now works for me. I'm interested to learn more and see how it fits with what we need.\n[2023-10-21T10:02:40] Ava Sullivan: Fantastic! From what you’ve mentioned, you’re interested in four units of the PulseSim Pro, correct?\n[2023-10-21T10:02:50] Ali Hussein: That's right. We want to enhance our simulation capabilities, and the PulseSim Pro seems like a great fit.\n[2023-10-21T10:03:05] Ava Sullivan: Absolutely. The PulseSim Pro is one of our top products for high precision simulation. It offers advanced analytics and seamless integration with existing systems, which is great for boosting efficiency.\n[2023-10-21T10:03:15] Ali Hussein: Those features sound beneficial. We do have a tight timeline for installation, though. Could you tell me more about that?\n[2023-10-21T10:03:30] Ava Sullivan: Certainly. We understand the importance of meeting tight schedules. We usually aim to complete installations within a day and ensure everything runs smoothly. Our technical team is very efficient.\n[2023-10-21T10:03:40] Ali Hussein: That’s reassuring. And as for the budget, how does it look for four units?\n[2023-10-21T10:03:55] Ava Sullivan: Considering your budget is $2,261, I think we can work something out. Each PulseSim Pro unit is priced at $500. For four units, it will come to $2,000. This is below your budget, leaving room for additional services if you wish.\n[2023-10-21T10:04:10] Ali Hussein: That fits really well. I'd like to move forward, but I'll need to consult with the finance team here since I don’t have the final say.\n[2023-10-21T10:04:20] Ava Sullivan: I completely understand, Ali. Would you like me to send over a detailed proposal and pricing information so you can present it to your team?\n[2023-10-21T10:04:25] Ali Hussein: Yes, please. That would be very helpful.\n[2023-10-21T10:04:35] Ava Sullivan: Great! I'll have that to you by the end of the day. Is there anything else you would need from my side?\n[2023-10-21T10:04:40] Ali Hussein: No, that sounds good for now. Thank you, Ava.\n[2023-10-21T10:04:50] Ava Sullivan: You're welcome, Ali. If any questions come up, feel free to reach out. Have a wonderful day!\n[2023-10-21T10:04:55] Ali Hussein: Thanks, Ava. You too!", 'CreatedDate': '2023-10-21T10:02:00.000+0000', 'EndTime__c': '2023-10-21'}], 'var_functions.query_db:2': [], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
