code = """import json
import re

debug_info = []

text = "Reuters - Short-sellers, Wall Street's dwindling band of ultra-cynics, are seeing green again."
keywords = ['wall street', 'market']
pattern = re.compile(r'\b(' + '|'.join(keywords) + r')\b', re.IGNORECASE)

debug_info.append(f"Test match: {bool(pattern.search(text))}")

with open(locals()['var_function-call-8892273225730457980'], 'r') as f:
    articles = json.load(f)[:5]

for art in articles:
    txt = art['title'] + " " + art['description']
    simple = 'Wall Street' in txt
    regex = bool(pattern.search(txt))
    debug_info.append({"txt_preview": txt[:50], "simple": simple, "regex": regex})

print("__RESULT__:")
print(json.dumps(debug_info))"""

env_args = {'var_function-call-2923091366904016682': ['authors', 'article_metadata'], 'var_function-call-12916141909924863267': 'file_storage/function-call-12916141909924863267.json', 'var_function-call-9166120240192453384': 'file_storage/function-call-9166120240192453384.json', 'var_function-call-17718603129355737146': [{'_id': '6944c3322ea32ad80cdb93a3', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944c3322ea32ad80cdb93a4', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944c3322ea32ad80cdb93a5', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944c3322ea32ad80cdb93a6', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944c3322ea32ad80cdb93a7', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-8892273225730457980': 'file_storage/function-call-8892273225730457980.json', 'var_function-call-742056741586345338': [{'_id': '6944c3322ea32ad80cdb93a3', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944c3322ea32ad80cdb9407', 'article_id': '100', 'title': 'Comets, Asteroids and Planets around a Nearby Star (SPACE.com)', 'description': 'SPACE.com - A nearby star thought to harbor comets and asteroids now appears to be home to planets, too. The presumed worlds are smaller than Jupiter and could be as tiny as Pluto, new observations suggest.'}, {'_id': '6944c3322ea32ad80cdb9597', 'article_id': '500', 'title': 'Kerry Campaign Helping With Fla. Recovery (AP)', 'description': "AP - Democratic presidential candidate John Kerry does not plan to visit Florida in the aftermath of Hurricane Charley because he's concerned his campaign entourage could distract from recovery efforts, he said Saturday."}, {'_id': '6944c3322ea32ad80cdb978b', 'article_id': '1000', 'title': 'European Union Extends Microsoft-Time Warner Review', 'description': 'BRUSSELS, Belgium (AP) -- European antitrust regulators said Monday they have extended their review of a deal between Microsoft Corp. (MSFT) and Time Warner Inc...'}, {'_id': '6944c3322ea32ad80cdb9b73', 'article_id': '2000', 'title': 'Applied Materials Reports Profit in 3Q', 'description': 'Applied Materials Inc., the world #39;s largest supplier of machines that make computer chips, Tuesday said surging sales in its latest quarter surpassed its own and Wall Street estimates. '}, {'_id': '6944c3322ea32ad80cdba72b', 'article_id': '5000', 'title': 'Cyberonics #39; Shares Jumps on Stock Buy', 'description': 'Advanced Neuromodulation Systems Inc. reported Friday that it purchased 3.5 million shares of Cyberonics Inc., taking a 14.9 percent stake in the Houston-based medical device maker, and expressed an interest in combining the two companies. '}, {'_id': '6944c3322ea32ad80cdbaefb', 'article_id': '7000', 'title': 'Virgin Blue Increases Surcharge as Fuel Prices Soar (Update1)', 'description': 'Virgin Blue Holdings Ltd., Australia #39;s second-biggest airline, increased a surcharge on all tickets as the cost of jet fuel soars.'}], 'var_function-call-17430149432680249704': 82.81818181818181, 'var_function-call-1724200924536633618': 0.0}

exec(code, env_args)
