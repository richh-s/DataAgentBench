code = """import json
with open(locals()['var_function-call-16883777531300941153'], 'r') as f:
    knowledge_articles = json.load(f)

invalid_config_article_id = None
keywords = ["invalid config", "violation", "quantity limits", "price regulation", "pricing policy"]

for article in knowledge_articles:
    content = f"{article.get("title", "")} {article.get("summary", "")} {article.get("faq_answer__c", "")}".lower()
    if any(keyword in content for keyword in keywords):
        invalid_config_article_id = article.get("id")
        break

print("__RESULT__:")
print(json.dumps(invalid_config_article_id))"""

env_args = {'var_function-call-4619205259174174615': [{'Product2Id': '#01tWt000006hV6jIAE', 'Quantity': '3.0', 'UnitPrice': '349.99'}, {'Product2Id': '01tWt000006hV8LIAU', 'Quantity': '2.0', 'UnitPrice': '529.99'}, {'Product2Id': '#01tWt000006hPffIAE', 'Quantity': '4.0', 'UnitPrice': '299.99'}, {'Product2Id': '01tWt000006hVczIAE', 'Quantity': '35.0', 'UnitPrice': '399.99'}], 'var_function-call-3065481764562116538': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-16883777531300941153': 'file_storage/function-call-16883777531300941153.json'}

exec(code, env_args)
