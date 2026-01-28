code = """import json
import re

order_items = [
    {"Id": "802Wt0000078wz5IAA"}, {"Id": "802Wt0000078xAAIAY"}, {"Id": "802Wt0000078yXiIAI"}, 
    {"Id": "#802Wt00000790WEIAY"}, {"Id": "802Wt00000792gDIAQ"}, {"Id": "802Wt00000792zTIAQ"}, 
    {"Id": "#802Wt0000079315IAA"}, {"Id": "802Wt00000793sTIAQ"}, {"Id": "802Wt00000794F3IAI"}, 
    {"Id": "802Wt00000794F4IAI"}, {"Id": "#802Wt00000794JmIAI"}, {"Id": "#802Wt00000794YFIAY"}, 
    {"Id": "802Wt00000794YJIAY"}, {"Id": "802Wt000007959OIAQ"}, {"Id": "802Wt00000795akIAA"}, 
    {"Id": "802Wt00000795ywIAA"}, {"Id": "802Wt000007962JIAQ"}, {"Id": "802Wt000007968hIAA"}, 
    {"Id": "802Wt000007968iIAA"}, {"Id": "802Wt00000796F5IAI"}, {"Id": "#802Wt00000796N7IAI"}, 
    {"Id": "802Wt00000796NAIAY"}, {"Id": "802Wt00000796RzIAI"}, {"Id": "802Wt00000796S0IAI"}, 
    {"Id": "802Wt00000796S1IAI"}, {"Id": "802Wt00000796VDIAY"}, {"Id": "802Wt00000796YPIAY"}, 
    {"Id": "802Wt00000796YQIAY"}, {"Id": "802Wt00000796a1IAA"}, {"Id": "802Wt00000796dFIAQ"}, 
    {"Id": "#802Wt00000796dIIAQ"}, {"Id": "#802Wt00000796jiIAA"}, {"Id": "802Wt00000796myIAA"}, 
    {"Id": "802Wt00000796oaIAA"}, {"Id": "802Wt00000796rlIAA"}, {"Id": "802Wt00000796tTIAQ"}, 
    {"Id": "802Wt00000796v0IAA"}, {"Id": "802Wt00000796wbIAA"}, {"Id": "802Wt00000796wcIAA"}, 
    {"Id": "802Wt00000797FxIAI"}, {"Id": "802Wt00000797MQIAY"}, {"Id": "#802Wt00000797O5IAI"}, 
    {"Id": "#802Wt00000797axIAA"}, {"Id": "802Wt00000797e9IAA"}, {"Id": "802Wt00000797hNIAQ"}, 
    {"Id": "802Wt00000797j0IAA"}, {"Id": "#802Wt00000797mDIAQ"}, {"Id": "802Wt00000797nsIAA"}, 
    {"Id": "#802Wt00000797pSIAQ"}, {"Id": "802Wt00000797sfIAA"}, {"Id": "802Wt00000797z8IAA"}, 
    {"Id": "802Wt000007982LIAQ"}, {"Id": "802Wt00000798IUIAY"}, {"Id": "802Wt00000798IVIAY"}, 
    {"Id": "802Wt00000798NKIAY"}, {"Id": "#802Wt00000798S9IAI"}, {"Id": "#802Wt00000798nBIAQ"}, 
    {"Id": "802Wt00000798rxIAA"}, {"Id": "802Wt00000798wpIAA"}, {"Id": "802Wt000007991dIAA"}, 
    {"Id": "802Wt0000079987IAA"}, {"Id": "802Wt00000799EZIAY"}, {"Id": "802Wt00000799HoIAI"}, 
    {"Id": "#802Wt00000799JPIAY"}, {"Id": "802Wt00000799T3IAI"}, {"Id": "802Wt00000799ckIAA"}, 
    {"Id": "#802Wt00000799fxIAA"}, {"Id": "802Wt00000799srIAA"}, {"Id": "802Wt00000799w5IAA"}, 
    {"Id": "#802Wt0000079A0wIAE"}, {"Id": "802Wt0000079A2aIAE"}, {"Id": "802Wt0000079A49IAE"}, 
    {"Id": "802Wt0000079AU1IAM"}, {"Id": "802Wt0000079AgrIAE"}, {"Id": "802Wt0000079AqXIAU"}, 
    {"Id": "802Wt0000079As9IAE"}
]

order_item_ids = [item['Id'] for item in order_items]

# Clean the IDs (remove leading #) and create a string for the SQL query
clean_ids = [re.sub(r'^#', '', oid) for oid in order_item_ids]

# Create a comma-separated string for SQL IN clause
in_clause = "'" + "','".join(clean_ids) + "'"

print("__RESULT__:")
print(in_clause)"""

env_args = {'var_functions.list_db:0': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_functions.query_db:2': [{'id': '#500Wt00000DDDfwIAH', 'priority': 'Medium', 'subject': 'Feature Update Notifications Lack', 'description': "Without regular update notifications, we are unable to fully utilize CollabCircuit Hub's latest features.", 'status': 'Waiting on Customer', 'contactid': '003Wt00000JqxKSIAZ', 'createddate': '2023-07-02T11:00:00.000+0000', 'closeddate': 'None', 'orderitemid__c': '802Wt00000797r4IAA', 'issueid__c': 'a03Wt00000JqzSfIAJ', 'accountid': '001Wt00000PFttwIAD', 'ownerid': '005Wt000003NJ0DIAW'}, {'id': '500Wt00000DDDtTIAX', 'priority': 'Medium', 'subject': 'Missing Feature Update Alerts', 'description': 'I have noticed that I am not consistently receiving notifications about new feature updates for the SecureFlow Suite, which affects my ability to use the software to its full potential.', 'status': 'Waiting on Customer   ', 'contactid': '003Wt00000Jqp3WIAR', 'createddate': '2020-12-29T08:36:00.000+0000', 'closeddate': 'None', 'orderitemid__c': '802Wt00000798aDIAQ', 'issueid__c': 'a03Wt00000JqzSfIAJ', 'accountid': '001Wt00000PHVkAIAX', 'ownerid': '#005Wt000003NJWTIA4'}, {'id': '500Wt00000DDNYoIAP', 'priority': 'Medium', 'subject': 'Delayed Support Response ', 'description': 'I am experiencing delays in getting timely responses from TechPulse support during busy periods, which is affecting our project timelines.', 'status': 'Closed', 'contactid': '#003Wt00000JqqVtIAJ', 'createddate': '2023-09-30T11:30:00.000+0000', 'closeddate': '2023-09-30T16:03:45.000+0000', 'orderitemid__c': '802Wt00000792tiIAA', 'issueid__c': 'a03Wt00000JqtOtIAJ', 'accountid': '001Wt00000PGZZoIAP', 'ownerid': '005Wt000003NIc3IAG'}, {'id': '500Wt00000DDPIsIAP', 'priority': 'Medium', 'subject': 'AI Feature Malfunction', 'description': 'Some of the AI-powered features in CloudLink Designer are intermittently failing to operate, leading to reduced efficiency and user frustration.', 'status': 'Closed ', 'contactid': '003Wt00000JqlkjIAB', 'createddate': '2022-08-05T14:30:00.000+0000', 'closeddate': '2022-08-05T14:39:32.000+0000', 'orderitemid__c': '802Wt00000797r3IAA', 'issueid__c': 'a03Wt00000JqxVjIAJ', 'accountid': '#001Wt00000PGRnYIAX', 'ownerid': '#005Wt000003NEzqIAG'}, {'id': '500Wt00000DDPM6IAP', 'priority': 'High', 'subject': 'Access Issues with Training Module', 'description': "I am experiencing difficulty accessing the online training modules which are crucial for my team's smooth adoption of the SecureFlow Suite.", 'status': 'Closed', 'contactid': '#003Wt00000Jqv14IAB', 'createddate': '2020-09-01T10:30:00.000+0000', 'closeddate': '2020-09-01T14:08:55.000+0000', 'orderitemid__c': '802Wt00000797r5IAA', 'issueid__c': 'a03Wt00000JqvNUIAZ', 'accountid': '001Wt00000PGzSaIAL', 'ownerid': '005Wt000003NISLIA4'}], 'var_functions.query_db:5': [{'Id': '01tWt000006hV8LIAU', 'Name': 'AI Cirku-Tech', 'Description': 'AI-driven circuit design platform offering rapid prototyping and innovation support.', 'IsActive': '1', 'External_ID__c': 'AI-Powered Circuit Design Tools,Customizable Workflow Automation_5'}], 'var_functions.query_db:6': [{'Id': '802Wt0000078wz5IAA'}, {'Id': '802Wt0000078xAAIAY'}, {'Id': '802Wt0000078yXiIAI'}, {'Id': '#802Wt00000790WEIAY'}, {'Id': '802Wt00000792gDIAQ'}, {'Id': '802Wt00000792zTIAQ'}, {'Id': '#802Wt0000079315IAA'}, {'Id': '802Wt00000793sTIAQ'}, {'Id': '802Wt00000794F3IAI'}, {'Id': '802Wt00000794F4IAI'}, {'Id': '#802Wt00000794JmIAI'}, {'Id': '#802Wt00000794YFIAY'}, {'Id': '802Wt00000794YJIAY'}, {'Id': '802Wt000007959OIAQ'}, {'Id': '802Wt00000795akIAA'}, {'Id': '802Wt00000795ywIAA'}, {'Id': '802Wt000007962JIAQ'}, {'Id': '802Wt000007968hIAA'}, {'Id': '802Wt000007968iIAA'}, {'Id': '802Wt00000796F5IAI'}, {'Id': '#802Wt00000796N7IAI'}, {'Id': '802Wt00000796NAIAY'}, {'Id': '802Wt00000796RzIAI'}, {'Id': '802Wt00000796S0IAI'}, {'Id': '802Wt00000796S1IAI'}, {'Id': '802Wt00000796VDIAY'}, {'Id': '802Wt00000796YPIAY'}, {'Id': '802Wt00000796YQIAY'}, {'Id': '802Wt00000796a1IAA'}, {'Id': '802Wt00000796dFIAQ'}, {'Id': '#802Wt00000796dIIAQ'}, {'Id': '#802Wt00000796jiIAA'}, {'Id': '802Wt00000796myIAA'}, {'Id': '802Wt00000796oaIAA'}, {'Id': '802Wt00000796rlIAA'}, {'Id': '802Wt00000796tTIAQ'}, {'Id': '802Wt00000796v0IAA'}, {'Id': '802Wt00000796wbIAA'}, {'Id': '802Wt00000796wcIAA'}, {'Id': '802Wt00000797FxIAI'}, {'Id': '802Wt00000797MQIAY'}, {'Id': '#802Wt00000797O5IAI'}, {'Id': '#802Wt00000797axIAA'}, {'Id': '802Wt00000797e9IAA'}, {'Id': '802Wt00000797hNIAQ'}, {'Id': '802Wt00000797j0IAA'}, {'Id': '#802Wt00000797mDIAQ'}, {'Id': '802Wt00000797nsIAA'}, {'Id': '#802Wt00000797pSIAQ'}, {'Id': '802Wt00000797sfIAA'}, {'Id': '802Wt00000797z8IAA'}, {'Id': '802Wt000007982LIAQ'}, {'Id': '802Wt00000798IUIAY'}, {'Id': '802Wt00000798IVIAY'}, {'Id': '802Wt00000798NKIAY'}, {'Id': '#802Wt00000798S9IAI'}, {'Id': '#802Wt00000798nBIAQ'}, {'Id': '802Wt00000798rxIAA'}, {'Id': '802Wt00000798wpIAA'}, {'Id': '802Wt000007991dIAA'}, {'Id': '802Wt0000079987IAA'}, {'Id': '802Wt00000799EZIAY'}, {'Id': '802Wt00000799HoIAI'}, {'Id': '#802Wt00000799JPIAY'}, {'Id': '802Wt00000799T3IAI'}, {'Id': '802Wt00000799ckIAA'}, {'Id': '#802Wt00000799fxIAA'}, {'Id': '802Wt00000799srIAA'}, {'Id': '802Wt00000799w5IAA'}, {'Id': '#802Wt0000079A0wIAE'}, {'Id': '802Wt0000079A2aIAE'}, {'Id': '802Wt0000079A49IAE'}, {'Id': '802Wt0000079AU1IAM'}, {'Id': '802Wt0000079AgrIAE'}, {'Id': '802Wt0000079AqXIAU'}, {'Id': '802Wt0000079As9IAE'}]}

exec(code, env_args)
