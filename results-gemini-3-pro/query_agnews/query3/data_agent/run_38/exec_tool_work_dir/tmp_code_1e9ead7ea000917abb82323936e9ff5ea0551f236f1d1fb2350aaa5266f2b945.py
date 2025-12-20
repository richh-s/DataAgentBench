code = """import json
import re

# Load data
with open(locals()['var_function-call-7027072809545360369'], 'r') as f:
    metadata = json.load(f)
meta_dict = {str(r['article_id']): str(r['year']) for r in metadata}
target_ids = set(meta_dict.keys())

with open(locals()['var_function-call-2863100870777153422'], 'r') as f:
    articles_data = json.load(f)

# Keyword sets
kw_business = {
    'business', 'economy', 'economic', 'financial', 'finance', 'market', 'stock', 'trade', 
    'investment', 'investor', 'corporate', 'industry', 'bank', 'banking', 'money', 
    'rates', 'profit', 'revenue', 'wall', 'street', 'share', 'shares', 'inflation', 'capital', 
    'debt', 'ceo', 'cfo', 'fed', 'treasury', 'imf', 'wto', 'sales', 'deal', 'merger', 
    'acquisition', 'earnings', 'quarterly', 'dividend', 'oil', 'gold', 'price', 'prices',
    'bond', 'bonds', 'loan', 'recession', 'growth', 'budget', 'deficit', 'euro', 'dollar', 'yen',
    'currency', 'exchange', 'nasdaq', 'dow', 'index', 'commodity', 'futures', 'asx', 
    'nyse', 'lse', 'stocks', 'markets', 'trading', 'company', 'firm', 'crude'
}

kw_sports = {
    'sport', 'sports', 'game', 'games', 'match', 'matches', 'team', 'teams', 'cup', 'league', 
    'coach', 'player', 'players', 'olympic', 'olympics', 'championship', 'tournament', 
    'score', 'scores', 'football', 'baseball', 'basketball', 'tennis', 'cricket', 'soccer', 
    'racing', 'athlete', 'athletes', 'medal', 'medals', 'stadium', 'club', 'winner', 'loser',
    'nfl', 'nba', 'mlb', 'nhl', 'fifa', 'uefa', 'wimbledon', 'rugby', 'golf', 'hockey'
}

kw_scitech = {
    'technology', 'tech', 'science', 'computer', 'computers', 'software', 'hardware', 'internet', 
    'web', 'digital', 'space', 'nasa', 'research', 'study', 'scientist', 'scientists', 
    'biology', 'physics', 'chemistry', 'health', 'medical', 'medicine', 'phone', 'mobile', 
    'chip', 'chips', 'google', 'microsoft', 'apple', 'intel', 'linux', 'windows', 'browser',
    'server', 'network', 'wireless', 'broadband', 'online', 'robot', 'galaxy', 'planet', 
    'virus', 'cancer', 'drug', 'treatment', 'disease', 'experiment', 'launch', 'orbit'
}

kw_world = {
    'world', 'international', 'war', 'peace', 'government', 'election', 'elections', 
    'president', 'minister', 'police', 'attack', 'attacks', 'bomb', 'bombing', 'kill', 
    'killed', 'protest', 'protests', 'court', 'law', 'legal', 'treaty', 'united', 'nations', 
    'un', 'eu', 'official', 'officials', 'politics', 'political', 'military', 'army', 
    'troops', 'iraq', 'iran', 'afghanistan', 'china', 'russia', 'usa', 'palestinian', 
    'israel', 'nuclear', 'weapon', 'security', 'terror', 'terrorism', 'rebel', 'insurgent',
    'crisis', 'human', 'rights', 'diplomat', 'embassy', 'vote', 'voters', 'parliament'
}

counts = {str(y): 0 for y in range(2010, 2021)}
category_counts = {'Business': 0, 'Sports': 0, 'SciTech': 0, 'World': 0, 'Unclassified': 0}

for a in articles_data:
    aid = str(a.get('article_id'))
    if aid in target_ids:
        title = a.get('title', '')
        desc = a.get('description', '')
        text = (title + " " + desc).lower()
        tokens = re.findall(r'\w+', text)
        token_set = set(tokens)
        
        # Count matches
        # Using intersection length
        s_bus = len(token_set.intersection(kw_business))
        s_spo = len(token_set.intersection(kw_sports))
        s_sci = len(token_set.intersection(kw_scitech))
        s_wor = len(token_set.intersection(kw_world))
        
        scores = {'Business': s_bus, 'Sports': s_spo, 'SciTech': s_sci, 'World': s_wor}
        
        # Determine max
        max_score = max(scores.values())
        
        if max_score > 0:
            # Find categories with max score
            best_cats = [k for k, v in scores.items() if v == max_score]
            # Tie breaking:
            # If Business is in best_cats, prioritize it?
            # Or prioritize World?
            # Actually, "Oil prices" -> Business=2 (oil, prices, business?), World=0?
            # "War in Iraq affects oil prices" -> World (War, Iraq) = 2, Business (Oil, prices) = 2.
            # This is tricky.
            # Let's assume the question implies dominant category.
            # If tie, maybe default to Business if Business is one of them?
            # Or use a hierarchy.
            
            # Simple heuristic: Just pick the first one or prioritize.
            # Let's prioritize: Sports > SciTech > Business > World (World is catch-all often).
            # But "Business" is what we want.
            # If Business is tied with World, it might be Business news about World events (e.g. trade war). count as Business.
            # If Business is tied with Sports (e.g. team sold), it's Business of Sports? Usually Sports section.
            # If Business tied with SciTech (e.g. Apple stock), it's Business.
            
            final_cat = best_cats[0]
            if 'Business' in best_cats:
                final_cat = 'Business'
            elif 'Sports' in best_cats:
                final_cat = 'Sports'
            # else pick random
            
            category_counts[final_cat] += 1
            
            if final_cat == 'Business':
                y = meta_dict[aid]
                if y in counts:
                    counts[y] += 1
        else:
            category_counts['Unclassified'] += 1
            # Check if it looks like business?
            # If unclassified, maybe our keywords were insufficient.
            pass

print(f"Category breakdown: {category_counts}")
print(f"Business counts per year: {counts}")

avg = sum(counts.values()) / 11.0
print(f"Average: {avg}")

print("__RESULT__:")
print(json.dumps(avg))"""

env_args = {'var_function-call-7027072809545360369': 'file_storage/function-call-7027072809545360369.json', 'var_function-call-13493351497379091720': 14860, 'var_function-call-658368012291302324': [{'_id': '6944e048b48ecdbf132e20a9', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944e048b48ecdbf132e20aa', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944e048b48ecdbf132e20ab', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944e048b48ecdbf132e20ac', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944e048b48ecdbf132e20ad', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-3157074696120618017': [{'_id': '6944e048b48ecdbf132e20a9', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944e048b48ecdbf132e20aa', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944e048b48ecdbf132e20ab', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944e048b48ecdbf132e20ac', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944e048b48ecdbf132e20ad', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-1866068854374072169': {'min': 3, 'max': 127583}, 'var_function-call-2595205932566337217': [{'_id': '6944e048b48ecdbf132e20ac', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}], 'var_function-call-5404317657608827314': [{'_id': '6944e048b48ecdbf132e20a9', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944e048b48ecdbf132e20aa', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944e048b48ecdbf132e20ab', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944e048b48ecdbf132e20ac', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944e048b48ecdbf132e20ad', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-17892153534094417851': [{'_id': '6944e049b48ecdbf132ebce9', 'article_id': '40000', 'title': 'Into the danger zone', 'description': 'AUSTRALIA #39;S involvement in Iraq and terrorism strikes in Southeast Asia have made defence and national security potentially decisive issues for voters as polling day nears.'}, {'_id': '6944e049b48ecdbf132ebcea', 'article_id': '40001', 'title': 'US ends its final drought', 'description': 'The US swept into the Davis Cup final for the first time in seven years when Bob and Mike Bryan crushed Max Mirnyi and Vladimir Voltchkov of Belarus to give the host an unassailable 3-0 lead in the semi-final.'}, {'_id': '6944e049b48ecdbf132ebceb', 'article_id': '40002', 'title': 'Windies discover a sting in the tail', 'description': 'Ian Bradshaw, left, and Courtney Browne celebrate their matchwinning 71-run ninth-wicket stand. Photo: Reuters. Brian Lara #39;s West Indies held their nerve in near darkness to beat England by '}, {'_id': '6944e049b48ecdbf132ebcec', 'article_id': '40003', 'title': 'Los Angeles Dodgers Team Report - September 26', 'description': '(Sports Network) - The Dodgers will try to win their three-game series against arch-rival San Francisco and increase their narrow 1 1/2-contest lead in the standings today at SBC Park.'}, {'_id': '6944e049b48ecdbf132ebced', 'article_id': '40004', 'title': 'Forest say farewell to legend Clough', 'description': ' #39;Ol #39; Blue Eyes #39; provided an emotional musical tribute to  #39;Old Big  #39;Ead #39; as Nottingham Forest celebrated the remarkable life of Brian Clough ahead of today #39;s game with West Ham.'}], 'var_function-call-8000977932169438302': [{'_id': '6944e04ab48ecdbf132f5929', 'article_id': '80000', 'title': 'Filmmaker Who Criticized Islam Slain', 'description': 'A filmmaker who was the great-grandnephew of the painter Vincent Van Gogh was shot and stabbed to death on an Amsterdam street Tuesday after receiving death threats over a movie he made criticizing the treatment of women under Islam.'}, {'_id': '6944e04ab48ecdbf132f592a', 'article_id': '80001', 'title': 'Iran Considers EU Compromise Proposal', 'description': 'Representatives from France, Germany, and the United Kingdom met with Iranian officials twice in October in an effort to head off a possible diplomatic showdown over its nuclear program.'}, {'_id': '6944e04ab48ecdbf132f592b', 'article_id': '80002', 'title': 'RPT-UPDATE 2-Slot machine maker IGT beats estimates', 'description': 'Slot machine maker International Game Technology (IGT.N: Quote, Profile, Research) on Tuesday posted better-than-expected quarterly earnings, as casinos bought '}, {'_id': '6944e04ab48ecdbf132f592c', 'article_id': '80003', 'title': 'Bayer Drug Can Be Combined With Others', 'description': 'German drug maker Bayer AG said Tuesday that early-stage trials of an experimental cancer treatment showed no significant safety concerns when used in combination with other drugs.'}, {'_id': '6944e04ab48ecdbf132f592d', 'article_id': '80004', 'title': 'Yahoo Moving on Desktop Search; Semel Says He Will Stay', 'description': 'Yahoo is ready to engage in combat with rival Google by offering a new desktop search tool to help people find information on their computer hard drives.'}], 'var_function-call-6364193371803783738': 'done', 'var_function-call-6050460174566706300': {'type_v1': "<class 'list'>", 'len_v1': 5}, 'var_function-call-2863100870777153422': 'file_storage/function-call-2863100870777153422.json', 'var_function-call-2471553235075418555': 409.09090909090907}

exec(code, env_args)
