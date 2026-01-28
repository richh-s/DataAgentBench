code = """import json
# Load the voice call transcript stored in var_call_NElokdVDE6DnQXSuSbvdEksr
transcripts = var_call_NElokdVDE6DnQXSuSbvdEksr
# Load the knowledge articles from the JSON file path stored in var_call_KkUUsHZKuA5BObcRkXptb6yR
with open(var_call_KkUUsHZKuA5BObcRkXptb6yR, 'r', encoding='utf-8') as f:
    knowledge = json.load(f)

# Analyze transcript for BANT cues
text = "\n".join([t.get('Body__c','') for t in transcripts])
text_lower = text.lower()

budget_ok = False
if 'budget' in text_lower:
    # check for explicit budget amount and price comparison
    if '$' in text or 'budget is' in text_lower or 'below your budget' in text_lower:
        budget_ok = True

need_ok = False
if any(phrase in text_lower for phrase in ['interested', 'want to', 'we need', 'we want', 'fit with what we need']):
    need_ok = True

authority_ok = True
if any(phrase in text_lower for phrase in ["i don't have the final say", "i don\'t have the final say", 'consult with the finance', 'consult with', 'need to consult']):
    authority_ok = False

# Timeline: check if lead expressed tight timeline and whether knowledge article contradicts rep's claim
timeline_ok = True
lead_mentions_tight = 'tight timeline' in text_lower or 'timeline' in text_lower
# find installation policy article
install_article = None
for a in knowledge:
    title = a.get('title','')
    body = a.get('faq_answer__c','')
    if 'installation timeline' in title.lower() or 'installation timeline' in body.lower() or 'volume-based installation' in title.lower():
        install_article = a
        break

# Determine timeline feasibility for 4 units
# From transcript, lead wants 4 units. Rep claimed installation within a day.
# From knowledge article, small batch (5 units) -> 3 days; single unit -> 1 day. 4 units falls between.
# This creates ambiguity; if lead has a tight timeline but no firm commitment, treat timeline as unclear but not failed.
if lead_mentions_tight:
    # if article exists and suggests >1 day for batches >=5, but 4 units not listed — we consider timeline as uncertain, not explicitly failing
    timeline_ok = True

# Determine failing BANT factors
failing = []
if not budget_ok:
    failing.append('Budget')
if not authority_ok:
    failing.append('Authority')
if not need_ok:
    failing.append('Need')
if not timeline_ok:
    failing.append('Timeline')

# If none failing, lead is qualified; but based on transcript authority failed, so failing=['Authority']
result = failing

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_NElokdVDE6DnQXSuSbvdEksr': [{'Id': 'a05Wt000003SukEIAS', 'OpportunityId__c': 'None', 'LeadId__c': '00QWt0000089AekMAE', 'Body__c': "[2023-10-21T10:02:00] Ava Sullivan: Hi Ali, this is Ava Sullivan from TechSolutions. How are you today?\n[2023-10-21T10:02:10] Ali Hussein: Hi Ava, I'm doing well, thank you. How about you?\n[2023-10-21T10:02:20] Ava Sullivan: I'm great, thank you for asking! I'm glad we could connect. I was looking over the details you provided about your interest in the PulseSim Pro. Is now a good time to discuss?\n[2023-10-21T10:02:30] Ali Hussein: Yes, now works for me. I'm interested to learn more and see how it fits with what we need.\n[2023-10-21T10:02:40] Ava Sullivan: Fantastic! From what you’ve mentioned, you’re interested in four units of the PulseSim Pro, correct?\n[2023-10-21T10:02:50] Ali Hussein: That's right. We want to enhance our simulation capabilities, and the PulseSim Pro seems like a great fit.\n[2023-10-21T10:03:05] Ava Sullivan: Absolutely. The PulseSim Pro is one of our top products for high precision simulation. It offers advanced analytics and seamless integration with existing systems, which is great for boosting efficiency.\n[2023-10-21T10:03:15] Ali Hussein: Those features sound beneficial. We do have a tight timeline for installation, though. Could you tell me more about that?\n[2023-10-21T10:03:30] Ava Sullivan: Certainly. We understand the importance of meeting tight schedules. We usually aim to complete installations within a day and ensure everything runs smoothly. Our technical team is very efficient.\n[2023-10-21T10:03:40] Ali Hussein: That’s reassuring. And as for the budget, how does it look for four units?\n[2023-10-21T10:03:55] Ava Sullivan: Considering your budget is $2,261, I think we can work something out. Each PulseSim Pro unit is priced at $500. For four units, it will come to $2,000. This is below your budget, leaving room for additional services if you wish.\n[2023-10-21T10:04:10] Ali Hussein: That fits really well. I'd like to move forward, but I'll need to consult with the finance team here since I don’t have the final say.\n[2023-10-21T10:04:20] Ava Sullivan: I completely understand, Ali. Would you like me to send over a detailed proposal and pricing information so you can present it to your team?\n[2023-10-21T10:04:25] Ali Hussein: Yes, please. That would be very helpful.\n[2023-10-21T10:04:35] Ava Sullivan: Great! I'll have that to you by the end of the day. Is there anything else you would need from my side?\n[2023-10-21T10:04:40] Ali Hussein: No, that sounds good for now. Thank you, Ava.\n[2023-10-21T10:04:50] Ava Sullivan: You're welcome, Ali. If any questions come up, feel free to reach out. Have a wonderful day!\n[2023-10-21T10:04:55] Ali Hussein: Thanks, Ava. You too!", 'CreatedDate': '2023-10-21T10:02:00.000+0000', 'EndTime__c': '2023-10-21'}], 'var_call_KkUUsHZKuA5BObcRkXptb6yR': 'file_storage/call_KkUUsHZKuA5BObcRkXptb6yR.json'}

exec(code, env_args)
