code = """# Retrieve the voice call transcript analysis result from storage
# Need to access it properly using the locals() function
import json

transcript_data = locals()['var_functions.query_db:0']
transcript_text = transcript_data[0]['Body__c']

# Initialize BANT factors
budget_met = False
authority_met = False
need_met = False
timeline_met = False

# Budget analysis - Check if budget is sufficient
if '$2,261' in transcript_text and '$2,000' in transcript_text and 'below your budget' in transcript_text:
    budget_met = True

# Authority analysis - Check if lead has decision-making authority
if "don't have the final say" in transcript_text or 'consult with the finance team' in transcript_text:
    authority_met = False
else:
    authority_met = True

# Need analysis - Check if there's a clear business need
if 'enhance our simulation capabilities' in transcript_text and 'great fit' in transcript_text:
    need_met = True

# Timeline analysis - Check if timeline is acceptable
if 'tight timeline' in transcript_text and 'complete installations within a day' in transcript_text:
    timeline_met = True

# Determine which BANT factors are NOT met
unmet_factors = []
if not budget_met:
    unmet_factors.append('Budget')
if not authority_met:
    unmet_factors.append('Authority')
if not need_met:
    unmet_factors.append('Need')
if not timeline_met:
    unmet_factors.append('Timeline')

print('__RESULT__:')
print(json.dumps(unmet_factors))"""

env_args = {'var_functions.query_db:0': [{'Id': 'a05Wt000003SukEIAS', 'OpportunityId__c': 'None', 'LeadId__c': '00QWt0000089AekMAE', 'Body__c': "[2023-10-21T10:02:00] Ava Sullivan: Hi Ali, this is Ava Sullivan from TechSolutions. How are you today?\n[2023-10-21T10:02:10] Ali Hussein: Hi Ava, I'm doing well, thank you. How about you?\n[2023-10-21T10:02:20] Ava Sullivan: I'm great, thank you for asking! I'm glad we could connect. I was looking over the details you provided about your interest in the PulseSim Pro. Is now a good time to discuss?\n[2023-10-21T10:02:30] Ali Hussein: Yes, now works for me. I'm interested to learn more and see how it fits with what we need.\n[2023-10-21T10:02:40] Ava Sullivan: Fantastic! From what you’ve mentioned, you’re interested in four units of the PulseSim Pro, correct?\n[2023-10-21T10:02:50] Ali Hussein: That's right. We want to enhance our simulation capabilities, and the PulseSim Pro seems like a great fit.\n[2023-10-21T10:03:05] Ava Sullivan: Absolutely. The PulseSim Pro is one of our top products for high precision simulation. It offers advanced analytics and seamless integration with existing systems, which is great for boosting efficiency.\n[2023-10-21T10:03:15] Ali Hussein: Those features sound beneficial. We do have a tight timeline for installation, though. Could you tell me more about that?\n[2023-10-21T10:03:30] Ava Sullivan: Certainly. We understand the importance of meeting tight schedules. We usually aim to complete installations within a day and ensure everything runs smoothly. Our technical team is very efficient.\n[2023-10-21T10:03:40] Ali Hussein: That’s reassuring. And as for the budget, how does it look for four units?\n[2023-10-21T10:03:55] Ava Sullivan: Considering your budget is $2,261, I think we can work something out. Each PulseSim Pro unit is priced at $500. For four units, it will come to $2,000. This is below your budget, leaving room for additional services if you wish.\n[2023-10-21T10:04:10] Ali Hussein: That fits really well. I'd like to move forward, but I'll need to consult with the finance team here since I don’t have the final say.\n[2023-10-21T10:04:20] Ava Sullivan: I completely understand, Ali. Would you like me to send over a detailed proposal and pricing information so you can present it to your team?\n[2023-10-21T10:04:25] Ali Hussein: Yes, please. That would be very helpful.\n[2023-10-21T10:04:35] Ava Sullivan: Great! I'll have that to you by the end of the day. Is there anything else you would need from my side?\n[2023-10-21T10:04:40] Ali Hussein: No, that sounds good for now. Thank you, Ava.\n[2023-10-21T10:04:50] Ava Sullivan: You're welcome, Ali. If any questions come up, feel free to reach out. Have a wonderful day!\n[2023-10-21T10:04:55] Ali Hussein: Thanks, Ava. You too!", 'CreatedDate': '2023-10-21T10:02:00.000+0000', 'EndTime__c': '2023-10-21'}]}

exec(code, env_args)
