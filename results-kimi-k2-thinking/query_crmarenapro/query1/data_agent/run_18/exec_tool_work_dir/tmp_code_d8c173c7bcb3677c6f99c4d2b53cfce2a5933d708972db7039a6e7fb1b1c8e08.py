code = """import json
import re

# Retrieve the voice call transcript for the lead
transcript_data = locals().get('var_functions.query_db:2', [])

# Extract the conversation text
if transcript_data and len(transcript_data) > 0:
    transcript_text = transcript_data[0]['Body__c']
    
    # Analyze BANT factors based on the transcript
    
    # BUDGET CHECK
    budget_mentioned = re.search(r'\$([0-9.,]+)', transcript_text)
    budget_match = 'Yes' if budget_mentioned and int(budget_mentioned.group(1).replace(',', '').replace('.', '')) >= 200000 else 'Budget discussed and fits'
    
    # AUTHORITY CHECK
    authority_indicators = ["final say", "need to consult", "finance team", "need approval", "can't decide", "need to check", "get back to you"]
    authority_not_met = any(phrase.lower() in transcript_text.lower() for phrase in authority_indicators)
    
    # NEED CHECK
    need_indicators = ["simulation capabilities", "enhance", "interested", "need", "want", "fits", "beneficial"]
    need_met = any(phrase.lower() in transcript_text.lower() for phrase in need_indicators)
    
    # TIMELINE CHECK
    timeline_indicators = ["timeline", "installation", "schedule", "deadline", "complete installations within"]
    timeline_met = any(phrase.lower() in transcript_text.lower() for phrase in timeline_indicators)
    
    # Detailed analysis
    analysis = {
        "Budget": {
            "met": True,
            "evidence": "Prospect has budget of $2,261. Cost is $2,000 (4 units @ $500 each), which is within budget"
        },
        "Authority": {
            "met": not authority_not_met,
            "evidence": "Ali states 'I'll need to consult with the finance team here since I don't have the final say' - does not have decision-making authority"
        },
        "Need": {
            "met": need_met,
            "evidence": "Prospect wants to 'enhance our simulation capabilities' and finds features 'beneficial'"
        },
        "Timeline": {
            "met": timeline_met,
            "evidence": "Discussed 'tight timeline for installation' and Ava confirmed 'complete installations within a day'"
        }
    }
    
    # Determine which factors are NOT met
    factors_not_met = [factor for factor, details in analysis.items() if not details['met']]
    
    result = {
        "can_be_qualified": len(factors_not_met) == 0,
        "factors_not_met": factors_not_met,
        "analysis": analysis
    }
    
    print("__RESULT__:")
    print(json.dumps(result, indent=2))
else:
    print("__RESULT__:")
    print(json.dumps({"error": "No transcript found for this lead"}))"""

env_args = {'var_functions.list_db:0': ['Event', 'Task', 'VoiceCallTranscript__c'], 'var_functions.query_db:2': [{'Id': 'a05Wt000003SukEIAS', 'OpportunityId__c': 'None', 'LeadId__c': '00QWt0000089AekMAE', 'Body__c': "[2023-10-21T10:02:00] Ava Sullivan: Hi Ali, this is Ava Sullivan from TechSolutions. How are you today?\n[2023-10-21T10:02:10] Ali Hussein: Hi Ava, I'm doing well, thank you. How about you?\n[2023-10-21T10:02:20] Ava Sullivan: I'm great, thank you for asking! I'm glad we could connect. I was looking over the details you provided about your interest in the PulseSim Pro. Is now a good time to discuss?\n[2023-10-21T10:02:30] Ali Hussein: Yes, now works for me. I'm interested to learn more and see how it fits with what we need.\n[2023-10-21T10:02:40] Ava Sullivan: Fantastic! From what you’ve mentioned, you’re interested in four units of the PulseSim Pro, correct?\n[2023-10-21T10:02:50] Ali Hussein: That's right. We want to enhance our simulation capabilities, and the PulseSim Pro seems like a great fit.\n[2023-10-21T10:03:05] Ava Sullivan: Absolutely. The PulseSim Pro is one of our top products for high precision simulation. It offers advanced analytics and seamless integration with existing systems, which is great for boosting efficiency.\n[2023-10-21T10:03:15] Ali Hussein: Those features sound beneficial. We do have a tight timeline for installation, though. Could you tell me more about that?\n[2023-10-21T10:03:30] Ava Sullivan: Certainly. We understand the importance of meeting tight schedules. We usually aim to complete installations within a day and ensure everything runs smoothly. Our technical team is very efficient.\n[2023-10-21T10:03:40] Ali Hussein: That’s reassuring. And as for the budget, how does it look for four units?\n[2023-10-21T10:03:55] Ava Sullivan: Considering your budget is $2,261, I think we can work something out. Each PulseSim Pro unit is priced at $500. For four units, it will come to $2,000. This is below your budget, leaving room for additional services if you wish.\n[2023-10-21T10:04:10] Ali Hussein: That fits really well. I'd like to move forward, but I'll need to consult with the finance team here since I don’t have the final say.\n[2023-10-21T10:04:20] Ava Sullivan: I completely understand, Ali. Would you like me to send over a detailed proposal and pricing information so you can present it to your team?\n[2023-10-21T10:04:25] Ali Hussein: Yes, please. That would be very helpful.\n[2023-10-21T10:04:35] Ava Sullivan: Great! I'll have that to you by the end of the day. Is there anything else you would need from my side?\n[2023-10-21T10:04:40] Ali Hussein: No, that sounds good for now. Thank you, Ava.\n[2023-10-21T10:04:50] Ava Sullivan: You're welcome, Ali. If any questions come up, feel free to reach out. Have a wonderful day!\n[2023-10-21T10:04:55] Ali Hussein: Thanks, Ava. You too!", 'CreatedDate': '2023-10-21T10:02:00.000+0000', 'EndTime__c': '2023-10-21'}]}

exec(code, env_args)
