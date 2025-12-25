code = """import json
import re

# Load metadata
with open(locals()['var_function-call-7027072809545360369'], 'r') as f:
    metadata = json.load(f)

# Metadata to dict: article_id (str) -> year (str)
meta_dict = {str(r['article_id']): str(r['year']) for r in metadata}
target_ids = set(meta_dict.keys())

# Load articles
with open(locals()['var_function-call-2863100870777153422'], 'r') as f:
    articles_data = json.load(f)

# Keywords for Business
keywords = {
    'business', 'economy', 'economic', 'financial', 'finance', 'market', 'stock', 'trade', 
    'investment', 'investor', 'corporate', 'industry', 'bank', 'banking', 'money', 
    'rates', 'profit', 'revenue', 'wall st', 'share', 'shares', 'inflation', 'capital', 
    'debt', 'ceo', 'cfo', 'fed', 'treasury', 'imf', 'wto', 'sales', 'deal', 'merger', 
    'acquisition', 'earnings', 'quarterly', 'dividend', 'oil', 'gold', 'price', 'prices',
    'bonds', 'loan', 'recession', 'growth', 'budget', 'deficit', 'euro', 'dollar', 'yen',
    'currency', 'exchange', 'nasdaq', 'dow', 'index', 'commodity', 'futures', 'asx', 
    'nyse', 'lse', 'stocks', 'markets', 'trading'
}

# Counters
counts = {str(y): 0 for y in range(2010, 2021)}

filtered_count = 0
business_count = 0

for a in articles_data:
    aid = str(a.get('article_id'))
    if aid in target_ids:
        filtered_count += 1
        # Classify
        title = a.get('title', '')
        desc = a.get('description', '')
        text = (title + " " + desc).lower()
        
        # Check keywords
        # Tokenize
        tokens = re.findall(r'\w+', text)
        if not keywords.isdisjoint(tokens):
            y = meta_dict[aid]
            if y in counts:
                counts[y] += 1
                business_count += 1

print(f"Total articles filtered: {filtered_count}")
print(f"Total Business articles: {business_count}")
print(f"Counts per year: {counts}")

total_business = sum(counts.values())
avg = total_business / 11.0

print(f"Average: {avg}")

print("__RESULT__:")
print(json.dumps(avg))"""

env_args = {'var_function-call-7027072809545360369': 'file_storage/function-call-7027072809545360369.json', 'var_function-call-13493351497379091720': 14860, 'var_function-call-658368012291302324': [{'_id': '6944e048b48ecdbf132e20a9', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944e048b48ecdbf132e20aa', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944e048b48ecdbf132e20ab', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944e048b48ecdbf132e20ac', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944e048b48ecdbf132e20ad', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-3157074696120618017': [{'_id': '6944e048b48ecdbf132e20a9', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944e048b48ecdbf132e20aa', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944e048b48ecdbf132e20ab', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944e048b48ecdbf132e20ac', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944e048b48ecdbf132e20ad', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-1866068854374072169': {'min': 3, 'max': 127583}, 'var_function-call-2595205932566337217': [{'_id': '6944e048b48ecdbf132e20ac', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}], 'var_function-call-5404317657608827314': [{'_id': '6944e048b48ecdbf132e20a9', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944e048b48ecdbf132e20aa', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944e048b48ecdbf132e20ab', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944e048b48ecdbf132e20ac', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944e048b48ecdbf132e20ad', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-17892153534094417851': [{'_id': '6944e049b48ecdbf132ebce9', 'article_id': '40000', 'title': 'Into the danger zone', 'description': 'AUSTRALIA #39;S involvement in Iraq and terrorism strikes in Southeast Asia have made defence and national security potentially decisive issues for voters as polling day nears.'}, {'_id': '6944e049b48ecdbf132ebcea', 'article_id': '40001', 'title': 'US ends its final drought', 'description': 'The US swept into the Davis Cup final for the first time in seven years when Bob and Mike Bryan crushed Max Mirnyi and Vladimir Voltchkov of Belarus to give the host an unassailable 3-0 lead in the semi-final.'}, {'_id': '6944e049b48ecdbf132ebceb', 'article_id': '40002', 'title': 'Windies discover a sting in the tail', 'description': 'Ian Bradshaw, left, and Courtney Browne celebrate their matchwinning 71-run ninth-wicket stand. Photo: Reuters. Brian Lara #39;s West Indies held their nerve in near darkness to beat England by '}, {'_id': '6944e049b48ecdbf132ebcec', 'article_id': '40003', 'title': 'Los Angeles Dodgers Team Report - September 26', 'description': '(Sports Network) - The Dodgers will try to win their three-game series against arch-rival San Francisco and increase their narrow 1 1/2-contest lead in the standings today at SBC Park.'}, {'_id': '6944e049b48ecdbf132ebced', 'article_id': '40004', 'title': 'Forest say farewell to legend Clough', 'description': ' #39;Ol #39; Blue Eyes #39; provided an emotional musical tribute to  #39;Old Big  #39;Ead #39; as Nottingham Forest celebrated the remarkable life of Brian Clough ahead of today #39;s game with West Ham.'}], 'var_function-call-8000977932169438302': [{'_id': '6944e04ab48ecdbf132f5929', 'article_id': '80000', 'title': 'Filmmaker Who Criticized Islam Slain', 'description': 'A filmmaker who was the great-grandnephew of the painter Vincent Van Gogh was shot and stabbed to death on an Amsterdam street Tuesday after receiving death threats over a movie he made criticizing the treatment of women under Islam.'}, {'_id': '6944e04ab48ecdbf132f592a', 'article_id': '80001', 'title': 'Iran Considers EU Compromise Proposal', 'description': 'Representatives from France, Germany, and the United Kingdom met with Iranian officials twice in October in an effort to head off a possible diplomatic showdown over its nuclear program.'}, {'_id': '6944e04ab48ecdbf132f592b', 'article_id': '80002', 'title': 'RPT-UPDATE 2-Slot machine maker IGT beats estimates', 'description': 'Slot machine maker International Game Technology (IGT.N: Quote, Profile, Research) on Tuesday posted better-than-expected quarterly earnings, as casinos bought '}, {'_id': '6944e04ab48ecdbf132f592c', 'article_id': '80003', 'title': 'Bayer Drug Can Be Combined With Others', 'description': 'German drug maker Bayer AG said Tuesday that early-stage trials of an experimental cancer treatment showed no significant safety concerns when used in combination with other drugs.'}, {'_id': '6944e04ab48ecdbf132f592d', 'article_id': '80004', 'title': 'Yahoo Moving on Desktop Search; Semel Says He Will Stay', 'description': 'Yahoo is ready to engage in combat with rival Google by offering a new desktop search tool to help people find information on their computer hard drives.'}], 'var_function-call-6364193371803783738': 'done', 'var_function-call-6050460174566706300': {'type_v1': "<class 'list'>", 'len_v1': 5}, 'var_function-call-2863100870777153422': 'file_storage/function-call-2863100870777153422.json'}

exec(code, env_args)
