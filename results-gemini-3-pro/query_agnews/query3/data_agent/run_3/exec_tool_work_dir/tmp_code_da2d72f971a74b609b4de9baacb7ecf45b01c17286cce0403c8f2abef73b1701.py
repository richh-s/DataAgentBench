code = """import json
import re

# Load metadata
with open(locals()['var_function-call-7230959688738805590'], 'r') as f:
    metadata_list = json.load(f)

# Load articles
with open(locals()['var_function-call-16295593414804423020'], 'r') as f:
    articles_list = json.load(f)

articles_dict = {str(item['article_id']): item for item in articles_list}

# Keywords
business_keywords = [
    'market', 'markets', 'stock', 'stocks', 'trade', 'trading', 'economy', 'economic', 'business', 
    'company', 'companies', 'profit', 'profits', 'bank', 'banks', 'financial', 'finance', 'invest', 
    'investment', 'investor', 'investors', 'fund', 'funds', 'dollar', 'euro', 'yen', 'currency', 
    'oil', 'price', 'prices', 'cost', 'costs', 'rate', 'rates', 'inflation', 'fed', 'federal reserve', 
    'wall st', 'wall street', 'nasdaq', 'dow', 'ipo', 'revenue', 'revenues', 'deal', 'merger', 
    'acquisition', 'ceo', 'cfo', 'manager', 'corporate', 'share', 'shares', 'dividend', 'bond', 
    'bonds', 'debt', 'loan', 'credit', 'budget', 'tax', 'taxes', 'sales', 'retail', 'spending', 
    'growth', 'forecast', 'analyst', 'analysts', 'sector', 'industry'
]
sports_keywords = [
    'sport', 'sports', 'game', 'games', 'team', 'teams', 'match', 'matches', 'cup', 'win', 'wins', 
    'winner', 'loss', 'lost', 'score', 'scores', 'player', 'players', 'coach', 'olympic', 'olympics', 
    'medal', 'football', 'soccer', 'basketball', 'baseball', 'hockey', 'tennis', 'golf', 'race', 
    'racing', 'prix', 'champion', 'championship', 'league', 'tournament', 'athlete', 'athletes', 
    'stadium', 'club', 'nfl', 'nba', 'mlb', 'nhl', 'fifa', 'uefa', 'season', 'playoff', 'final'
]
tech_keywords = [
    'technology', 'tech', 'science', 'computer', 'computers', 'software', 'hardware', 'internet', 
    'web', 'website', 'online', 'digital', 'mobile', 'phone', 'phones', 'cellphone', 'smartphone', 
    'chip', 'chips', 'processor', 'server', 'wireless', 'network', 'networks', 'space', 'nasa', 
    'satellite', 'virus', 'malware', 'microsoft', 'google', 'intel', 'apple', 'linux', 'windows', 
    'gadget', 'device', 'research', 'scientist', 'scientists', 'lab', 'browser', 'search engine', 
    'cyber', 'robot', 'robotics', 'broadband', 'telecom', 'carrier'
]
world_keywords = [
    'world', 'government', 'governments', 'president', 'minister', 'ministers', 'prime minister', 
    'election', 'elections', 'vote', 'voters', 'war', 'wars', 'military', 'army', 'troops', 'soldier', 
    'soldiers', 'police', 'killed', 'kill', 'dead', 'death', 'bomb', 'bombing', 'attack', 'attacks', 
    'blast', 'iraq', 'iraqi', 'iran', 'afghanistan', 'palestin', 'palestinian', 'israel', 'israeli', 
    'un', 'united nations', 'treaty', 'nuclear', 'protest', 'protests', 'court', 'law', 'legal', 
    'crime', 'criminal', 'disaster', 'storm', 'hurricane', 'quake', 'earthquake', 'tsunami', 'flood', 
    'hostage', 'terror', 'terrorism', 'terrorist', 'rebel', 'rebels', 'politic', 'politics', 'party'
]

# Compile regexes with double backslash for word boundary
def compile_regex(keywords):
    pattern = r'\\b(?:' + '|'.join(map(re.escape, keywords)) + r')\\b'
    return re.compile(pattern)

re_business = compile_regex(business_keywords)
re_sports = compile_regex(sports_keywords)
re_tech = compile_regex(tech_keywords)
re_world = compile_regex(world_keywords)

counts_per_year = {y: 0 for y in range(2010, 2021)}

for entry in metadata_list:
    aid = str(entry['article_id'])
    if aid in articles_dict:
        art = articles_dict[aid]
        text = (art.get('title', '') + " " + art.get('description', '')).lower()
        
        c_biz = len(re_business.findall(text))
        c_sport = len(re_sports.findall(text))
        c_tech = len(re_tech.findall(text))
        c_world = len(re_world.findall(text))
        
        counts = {'business': c_biz, 'sports': c_sport, 'tech': c_tech, 'world': c_world}
        max_c = max(counts.values())
        
        if max_c > 0:
            candidates = [k for k, v in counts.items() if v == max_c]
            if 'business' in candidates:
                final_cat = 'business'
            else:
                final_cat = candidates[0]
            
            if final_cat == 'business':
                pub_date = entry['publication_date']
                try:
                    year = int(pub_date.split('-')[0])
                    if 2010 <= year <= 2020:
                        counts_per_year[year] += 1
                except:
                    pass

total_biz = sum(counts_per_year.values())
avg_biz = total_biz / 11.0

print("__RESULT__:")
print(json.dumps({
    "counts": counts_per_year,
    "total": total_biz,
    "average": avg_biz
}))"""

env_args = {'var_function-call-7230959688738805590': 'file_storage/function-call-7230959688738805590.json', 'var_function-call-10820393096766796138': {'count': 14860, 'sample_ids': [3, 9, 13, 14, 21, 27, 43, 60, 62, 63], 'file_path_used': 'file_storage/function-call-7230959688738805590.json'}, 'var_function-call-1252885495403344339': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-7038289333483106192': 5, 'var_function-call-15983958513975732915': ['articles'], 'var_function-call-7425021987037564653': [{'_id': '6944c26316c3efdda9fc9184', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944c26316c3efdda9fc918a', 'article_id': '9', 'title': 'Wall St. Bears Claw Back Into the Black', 'description': " NEW YORK (Reuters) - Short-sellers, Wall Street's dwindling  band of ultra-cynics, are seeing green again."}, {'_id': '6944c26316c3efdda9fc918e', 'article_id': '13', 'title': 'Google IPO Auction Off to Rocky Start', 'description': " WASHINGTON/NEW YORK (Reuters) - The auction for Google  Inc.'s highly anticipated initial public offering got off to a  rocky start on Friday after the Web search company sidestepped  a bullet from U.S. securities regulators."}], 'var_function-call-14402555524284394332': {'min': 3, 'max': 127583, 'count': 14860}, 'var_function-call-16295593414804423020': 'file_storage/function-call-16295593414804423020.json', 'var_function-call-7439365376240442064': {'counts_per_year': {}, 'total': 0, 'average': 0.0}, 'var_function-call-7434129476837696971': [{'id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'found': True}, {'id': '9', 'title': 'Wall St. Bears Claw Back Into the Black', 'found': True}, {'id': '13', 'title': 'Google IPO Auction Off to Rocky Start', 'found': True}, {'id': '14', 'title': 'Dollar Falls Broadly on Record Trade Gap', 'found': True}, {'id': '21', 'title': 'Eurozone economy keeps growing', 'found': True}], 'var_function-call-5706828954881185857': {'counts': {'2010': 0, '2011': 0, '2012': 0, '2013': 0, '2014': 0, '2015': 0, '2016': 0, '2017': 0, '2018': 0, '2019': 0, '2020': 0}, 'total': 0, 'average': 0.0}, 'var_function-call-3449678831547945563': [{'id': '3', 'text': 'iraq halts oil exports from main southern pipeline (reuters) reuters - authorities have halted oil export\\flows from the main pipeline in southern iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on saturday.', 'matches': [], 'pattern': '\x08(?:wall\\ st|market|oil|stock)\x08'}, {'id': '9', 'text': "wall st. bears claw back into the black  new york (reuters) - short-sellers, wall street's dwindling  band of ultra-cynics, are seeing green again.", 'matches': [], 'pattern': '\x08(?:wall\\ st|market|oil|stock)\x08'}, {'id': '13', 'text': "google ipo auction off to rocky start  washington/new york (reuters) - the auction for google  inc.'s highly anticipated initial public offering got off to a  rocky start on friday after the web search company sidestepped  a bullet from u.s. securities regulators.", 'matches': [], 'pattern': '\x08(?:wall\\ st|market|oil|stock)\x08'}, {'id': '14', 'text': "dollar falls broadly on record trade gap  new york (reuters) - the dollar tumbled broadly on friday  after data showing a record u.s. trade deficit in june cast  fresh doubts on the economy's recovery and its ability to draw  foreign capital to fund the growing gap.", 'matches': [], 'pattern': '\x08(?:wall\\ st|market|oil|stock)\x08'}, {'id': '21', 'text': 'eurozone economy keeps growing official figures show the 12-nation eurozone economy continues to grow, but there are warnings it may slow down later in the year.', 'matches': [], 'pattern': '\x08(?:wall\\ st|market|oil|stock)\x08'}]}

exec(code, env_args)
