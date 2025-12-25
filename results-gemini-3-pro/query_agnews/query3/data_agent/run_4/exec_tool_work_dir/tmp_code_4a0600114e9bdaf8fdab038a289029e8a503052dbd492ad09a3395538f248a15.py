code = """import json
import re

# Load metadata
with open(locals()['var_function-call-12916141909924863267'], 'r') as f:
    metadata_list = json.load(f)

meta_dict = {}
for item in metadata_list:
    aid = str(item['article_id'])
    date = item['publication_date']
    year = int(date.split('-')[0])
    meta_dict[aid] = year

# Load articles
with open(locals()['var_function-call-8892273225730457980'], 'r') as f:
    articles_list = json.load(f)

# Business Keywords (regex friendly)
keywords = [
    'business', 'markets?', 'stocks?', 'trade', 'economy', 'economics?', 'financial', 
    'banks?', 'investments?', 'investors?', 'money', 'profits?', 'loss(es)?', 'shares?', 
    'wall street', 'oil prices?', 'inflation', 'fed', 'federal reserve', 'interest rates?', 
    'dollars?', 'euro', 'currency', 'currenc(y|ies)', 'compan(y|ies)', 'corporations?', 
    'corporate', 'mergers?', 'acquisitions?', 'earnings?', 'revenues?', 'debt', 'recession', 
    'tax(es)?', 'jobs?', 'hiring', 'ceo', 'cfo', 'ipo', 'nasdaq', 'dow jones', 's&p', 
    'crude', 'prices?', 'spending', 'deals?', 'sales?', 'retail', 'growth', 'deficit', 
    'budget', 'consumers?', 'labor', 'strikes?', 'unions?', 'contracts?', 'executives?', 
    'managers?', 'industry', 'sectors?', 'commercial', 'assets?', 'funds?', 'equity', 
    'bonds?', 'dividends?', 'shareholders?'
]

# Construct regex pattern
# \b matches word boundary.
pattern = re.compile(r'\b(' + '|'.join(keywords) + r')\b', re.IGNORECASE)

yearly_counts = {y: 0 for y in range(2010, 2021)}
matched_count = 0
business_count = 0

for art in articles_list:
    aid = str(art['article_id'])
    if aid in meta_dict:
        matched_count += 1
        text = (art.get('title', '') + " " + art.get('description', ''))
        if pattern.search(text):
            y = meta_dict[aid]
            if 2010 <= y <= 2020:
                yearly_counts[y] += 1
                business_count += 1

print(f"Matched: {matched_count}")
print(f"Business: {business_count}")
print(f"Counts: {yearly_counts}")

avg = business_count / 11
print("__RESULT__:")
print(json.dumps(avg))"""

env_args = {'var_function-call-2923091366904016682': ['authors', 'article_metadata'], 'var_function-call-12916141909924863267': 'file_storage/function-call-12916141909924863267.json', 'var_function-call-9166120240192453384': 'file_storage/function-call-9166120240192453384.json', 'var_function-call-17718603129355737146': [{'_id': '6944c3322ea32ad80cdb93a3', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944c3322ea32ad80cdb93a4', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944c3322ea32ad80cdb93a5', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944c3322ea32ad80cdb93a6', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944c3322ea32ad80cdb93a7', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-8892273225730457980': 'file_storage/function-call-8892273225730457980.json', 'var_function-call-742056741586345338': [{'_id': '6944c3322ea32ad80cdb93a3', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944c3322ea32ad80cdb9407', 'article_id': '100', 'title': 'Comets, Asteroids and Planets around a Nearby Star (SPACE.com)', 'description': 'SPACE.com - A nearby star thought to harbor comets and asteroids now appears to be home to planets, too. The presumed worlds are smaller than Jupiter and could be as tiny as Pluto, new observations suggest.'}, {'_id': '6944c3322ea32ad80cdb9597', 'article_id': '500', 'title': 'Kerry Campaign Helping With Fla. Recovery (AP)', 'description': "AP - Democratic presidential candidate John Kerry does not plan to visit Florida in the aftermath of Hurricane Charley because he's concerned his campaign entourage could distract from recovery efforts, he said Saturday."}, {'_id': '6944c3322ea32ad80cdb978b', 'article_id': '1000', 'title': 'European Union Extends Microsoft-Time Warner Review', 'description': 'BRUSSELS, Belgium (AP) -- European antitrust regulators said Monday they have extended their review of a deal between Microsoft Corp. (MSFT) and Time Warner Inc...'}, {'_id': '6944c3322ea32ad80cdb9b73', 'article_id': '2000', 'title': 'Applied Materials Reports Profit in 3Q', 'description': 'Applied Materials Inc., the world #39;s largest supplier of machines that make computer chips, Tuesday said surging sales in its latest quarter surpassed its own and Wall Street estimates. '}, {'_id': '6944c3322ea32ad80cdba72b', 'article_id': '5000', 'title': 'Cyberonics #39; Shares Jumps on Stock Buy', 'description': 'Advanced Neuromodulation Systems Inc. reported Friday that it purchased 3.5 million shares of Cyberonics Inc., taking a 14.9 percent stake in the Houston-based medical device maker, and expressed an interest in combining the two companies. '}, {'_id': '6944c3322ea32ad80cdbaefb', 'article_id': '7000', 'title': 'Virgin Blue Increases Surcharge as Fuel Prices Soar (Update1)', 'description': 'Virgin Blue Holdings Ltd., Australia #39;s second-biggest airline, increased a surcharge on all tickets as the cost of jet fuel soars.'}], 'var_function-call-17430149432680249704': 82.81818181818181}

exec(code, env_args)
