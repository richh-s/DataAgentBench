code = """import json
import pandas as pd

# Load metadata IDs and dates
# metadata file contains list of dicts: [{"article_id": "...", "publication_date": "..."}]
file_path_meta = locals()['var_function-call-12916141909924863267']
with open(file_path_meta, 'r') as f:
    metadata_list = json.load(f)

# Create a dictionary mapping article_id -> year
# Ensure article_id matches the type in articles DB (string)
meta_dict = {}
for item in metadata_list:
    aid = str(item['article_id'])
    date = item['publication_date'] # YYYY-MM-DD
    year = int(date.split('-')[0])
    meta_dict[aid] = year

# Load articles
# articles file contains list of dicts: [{"article_id": "...", "title": "...", "description": "..."}]
file_path_articles = locals()['var_function-call-8892273225730457980']
with open(file_path_articles, 'r') as f:
    articles_list = json.load(f)

# Business Keywords
business_keywords = [
    'business', 'market', 'stock', 'trade', 'economy', 'economic', 'finance', 'financial', 
    'bank', 'investment', 'investor', 'money', 'profit', 'loss', 'share', 'shares', 
    'wall street', 'oil price', 'inflation', 'fed', 'federal reserve', 'interest rate', 
    'dollar', 'euro', 'currency', 'company', 'corporation', 'corporate', 'merger', 
    'acquisition', 'earning', 'revenue', 'debt', 'recession', 'tax', 'job', 'hiring', 
    'ceo', 'cfo', 'ipo', 'nasdaq', 'dow jones', 's&p', 'crude', 'prices', 'spending',
    'deal', 'sales', 'retail', 'growth', 'deficit', 'budget', 'consumer', 'labor', 
    'strike', 'union', 'contract', 'executive', 'manager', 'industry', 'sector', 
    'commercial', 'asset', 'fund', 'equity', 'bond', 'dividend', 'shareholder'
]

# Helper to check if text is business
def is_business(text):
    text_lower = text.lower()
    for kw in business_keywords:
        # Simple substring match (could be improved with tokenization, but simple is often enough)
        # Add spaces to avoid partial matches like "market" in "supermarket" if desired, 
        # but "supermarket" is also business-related often.
        # Let's trust substrings for now or use word boundaries if I had regex.
        if kw in text_lower:
            return True
    return False

# Count business articles per year
yearly_counts = {y: 0 for y in range(2010, 2021)}

business_article_count = 0
total_matched = 0

for art in articles_list:
    aid = str(art['article_id'])
    if aid in meta_dict:
        total_matched += 1
        # Check category
        # Combine title and description
        text = (art.get('title', '') + " " + art.get('description', ''))
        if is_business(text):
            y = meta_dict[aid]
            if 2010 <= y <= 2020:
                yearly_counts[y] += 1
                business_article_count += 1

print(f"Total matched articles: {total_matched}")
print(f"Total business articles found: {business_article_count}")
print(f"Yearly counts: {yearly_counts}")

# Calculate average
total_business = sum(yearly_counts.values())
num_years = 11
average = total_business / num_years

print("__RESULT__:")
print(json.dumps(average))"""

env_args = {'var_function-call-2923091366904016682': ['authors', 'article_metadata'], 'var_function-call-12916141909924863267': 'file_storage/function-call-12916141909924863267.json', 'var_function-call-9166120240192453384': 'file_storage/function-call-9166120240192453384.json', 'var_function-call-17718603129355737146': [{'_id': '6944c3322ea32ad80cdb93a3', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944c3322ea32ad80cdb93a4', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944c3322ea32ad80cdb93a5', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944c3322ea32ad80cdb93a6', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944c3322ea32ad80cdb93a7', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-8892273225730457980': 'file_storage/function-call-8892273225730457980.json', 'var_function-call-742056741586345338': [{'_id': '6944c3322ea32ad80cdb93a3', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944c3322ea32ad80cdb9407', 'article_id': '100', 'title': 'Comets, Asteroids and Planets around a Nearby Star (SPACE.com)', 'description': 'SPACE.com - A nearby star thought to harbor comets and asteroids now appears to be home to planets, too. The presumed worlds are smaller than Jupiter and could be as tiny as Pluto, new observations suggest.'}, {'_id': '6944c3322ea32ad80cdb9597', 'article_id': '500', 'title': 'Kerry Campaign Helping With Fla. Recovery (AP)', 'description': "AP - Democratic presidential candidate John Kerry does not plan to visit Florida in the aftermath of Hurricane Charley because he's concerned his campaign entourage could distract from recovery efforts, he said Saturday."}, {'_id': '6944c3322ea32ad80cdb978b', 'article_id': '1000', 'title': 'European Union Extends Microsoft-Time Warner Review', 'description': 'BRUSSELS, Belgium (AP) -- European antitrust regulators said Monday they have extended their review of a deal between Microsoft Corp. (MSFT) and Time Warner Inc...'}, {'_id': '6944c3322ea32ad80cdb9b73', 'article_id': '2000', 'title': 'Applied Materials Reports Profit in 3Q', 'description': 'Applied Materials Inc., the world #39;s largest supplier of machines that make computer chips, Tuesday said surging sales in its latest quarter surpassed its own and Wall Street estimates. '}, {'_id': '6944c3322ea32ad80cdba72b', 'article_id': '5000', 'title': 'Cyberonics #39; Shares Jumps on Stock Buy', 'description': 'Advanced Neuromodulation Systems Inc. reported Friday that it purchased 3.5 million shares of Cyberonics Inc., taking a 14.9 percent stake in the Houston-based medical device maker, and expressed an interest in combining the two companies. '}, {'_id': '6944c3322ea32ad80cdbaefb', 'article_id': '7000', 'title': 'Virgin Blue Increases Surcharge as Fuel Prices Soar (Update1)', 'description': 'Virgin Blue Holdings Ltd., Australia #39;s second-biggest airline, increased a surcharge on all tickets as the cost of jet fuel soars.'}]}

exec(code, env_args)
