code = """import json
import re
import os
from collections import Counter

# Load data
m_file = locals()['var_function-call-16836183799483844241']
a_file = locals()['var_function-call-1990041759778261395']

if isinstance(m_file, str):
    with open(m_file, 'r') as f: metadata = json.load(f)
else: metadata = m_file

if isinstance(a_file, str):
    with open(a_file, 'r') as f: articles = json.load(f)
else: articles = a_file

articles_map = {str(a['article_id']): a for a in articles}

# Categories (same as before)
raw_categories = {
    "Business": [
        "market", "stock", "stocks", "economy", "trade", "profit", "loss", "bank", "banks", "finance", 
        "invest", "investment", "rate", "rates", "inflation", "company", "companies", "corp", "ipo", 
        "oil", "price", "prices", "business", "dollar", "euro", "yen", "wall st", "nasdaq", "dow", 
        "fed", "federal reserve", "sales", "revenue", "deal", "merger", "acquisition", "ceo"
    ],
    "Sports": [
        "sport", "sports", "game", "games", "team", "teams", "match", "matches", "player", "players", 
        "score", "scores", "win", "won", "lose", "lost", "cup", "league", "season", "champion", 
        "championship", "olympic", "olympics", "medal", "football", "soccer", "baseball", "basketball", 
        "tennis", "golf", "hockey", "club", "coach", "f1", "racing", "stadium"
    ],
    "Sci_Tech": [
        "technology", "tech", "science", "computer", "computers", "software", "internet", "web", 
        "google", "apple", "microsoft", "ibm", "nasa", "space", "research", "study", "device", 
        "phone", "mobile", "app", "apps", "virus", "hacker", "cyber", "robot", "digital", "chip", 
        "network", "online", "browser"
    ],
    "World": [
        "world", "international", "government", "govt", "president", "minister", "parliament", "congress", 
        "senate", "election", "vote", "war", "peace", "military", "army", "troop", "troops", "attack", 
        "attacks", "bomb", "bombing", "kill", "killed", "dead", "died", "police", "crisis", "conflict", 
        "refugee", "migrant", "un", "united nations", "nato", "eu", "european union", "isis", "syria", 
        "iraq", "iran", "afghanistan", "pakistan", "china", "russia", "ukraine", "israel", "palestine", 
        "gaza", "egypt", "saudi", "yemen", "turkey", "greece", "nepal", "earthquake", "storm", "hurricane", 
        "flood", "disaster", "climate", "treaty", "nuclear", "diplomacy", "foreign", "official", 
        "authorities", "security", "boko haram", "taliban", "premier", "chancellor"
    ]
}

# Process keywords
cat_config = {}
for cat, kws in raw_categories.items():
    singles = set()
    phrases = []
    for kw in kws:
        if ' ' in kw:
            phrases.append(kw)
        else:
            singles.add(kw)
    cat_config[cat] = {'singles': singles, 'phrases': phrases}

def classify(text):
    clean = re.sub(r'[^a-z0-9]', ' ', text.lower())
    words = set(clean.split())
    
    scores = {k: 0 for k in raw_categories}
    
    for cat, config in cat_config.items():
        match_count = 0
        for w in config['singles']:
            if w in words:
                match_count += 1
        scores[cat] += match_count
        for p in config['phrases']:
            if f" {p} " in f" {clean} ":
                scores[cat] += 1
                
    max_cat = max(scores, key=scores.get)
    if scores[max_cat] == 0:
        return "Unknown"
    return max_cat

unknowns = []
count = 0
for m in metadata:
    aid = str(m['article_id'])
    if aid in articles_map:
        art = articles_map[aid]
        content = (art.get('title', '') + " " + art.get('description', ''))
        cat = classify(content)
        if cat == "Unknown":
            unknowns.append(content)
            count += 1
            if count >= 10: break

print("__RESULT__:")
print(json.dumps(unknowns))"""

env_args = {'var_function-call-4087601676422552917': ['authors', 'article_metadata'], 'var_function-call-4087601676422553258': ['articles'], 'var_function-call-16836183799483844241': 'file_storage/function-call-16836183799483844241.json', 'var_function-call-11996756743093828097': 'file_storage/function-call-11996756743093828097.json', 'var_function-call-8460452426655104065': {'min': 13, 'max': 127570, 'count': 6696}, 'var_function-call-17656108898543788620': [{'article_id': '13', 'title': 'Google IPO Auction Off to Rocky Start', 'description': " WASHINGTON/NEW YORK (Reuters) - The auction for Google  Inc.'s highly anticipated initial public offering got off to a  rocky start on Friday after the Web search company sidestepped  a bullet from U.S. securities regulators."}, {'article_id': '14', 'title': 'Dollar Falls Broadly on Record Trade Gap', 'description': " NEW YORK (Reuters) - The dollar tumbled broadly on Friday  after data showing a record U.S. trade deficit in June cast  fresh doubts on the economy's recovery and its ability to draw  foreign capital to fund the growing gap."}, {'article_id': '15', 'title': 'Rescuing an Old Saver', 'description': "If you think you may need to help your elderly relatives with their finances, don't be shy about having the money talk -- soon."}, {'article_id': '16', 'title': 'Kids Rule for Back-to-School', 'description': 'The purchasing power of kids is a big part of why the back-to-school season has become such a huge marketing phenomenon.'}, {'article_id': '17', 'title': 'In a Down Market, Head Toward Value Funds', 'description': "There is little cause for celebration in the stock market these days, but investors in value-focused mutual funds have reason to feel a bit smug -- if only because they've lost less than the folks who stuck with growth."}], 'var_function-call-6556494366233684975': [{'region': 'Europe', 'title': 'Google IPO Auction Off to Rocky Start', 'description': " WASHINGTON/NEW YORK (Reuters) - The auction for Google  Inc.'s highly anticipated initial public offering got off to a  rocky start on Friday after the Web search company sidestepped  a bullet from U.S. securities regulators."}], 'var_function-call-11690996527890362772': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-1990041759778261395': 'file_storage/function-call-1990041759778261395.json', 'var_function-call-2316604512931417648': {'world_counts': {}, 'sample': []}, 'var_function-call-5023701990922176121': [{'id': '13', 'content': "Google IPO Auction Off to Rocky Start  WASHINGTON/NEW YORK (Reuters) - The auction for Google  Inc.'s highly anticipated initial public offering got off to a  rocky start on Friday after the Web search company sidestepped  a bullet from U.S. securities regulators."}, {'id': '18', 'content': 'US trade deficit swells in June The US trade deficit has exploded 19 to a record \\$55.8bn as oil costs drove imports higher, according to a latest figures.'}, {'id': '26', 'content': 'Google auction begins on Friday An auction of shares in Google, the web search engine which could be floated for as much as \\$36bn, takes place on Friday.'}, {'id': '51', 'content': "Delightful Dell The company's results show that it's not grim all over tech world. Just all of it that isn't Dell."}, {'id': '52', 'content': "Chrysler's Bling King After a tough year, Detroit's troubled carmaker is back -- thanks to a maverick designer and a car that is dazzling the hip-hop crowd"}, {'id': '67', 'content': 'IT Myth 5: Most IT projects fail Do most IT projects fail? Some point to the number of giant consultancies such as IBM Global Services, Capgemini, and Sapient, who feed off bad experiences encountered by enterprises. Sapient is a company founded on the realization that IT projects are not successful, says Sapient CTO Ben Gaucherin.'}, {'id': '70', 'content': "U.K.'s NHS taps Gartner to help plan \\$9B IT overhaul LONDON -- The U.K.'s National Health Service (NHS) has tapped IT researcher Gartner Inc. to provide market intelligence services as the health organization forges ahead with a mammoth, 5 billion (\\$9.2 billion) project to upgrade its information technology infrastructure."}, {'id': '74', 'content': 'HP to Buy Synstar Hewlett-Packard will pay \\$297 million for the British company. Also: TiVo goes all out to attract customers   hellip;. Sprint offers service guarantees for business wireless subscribers   hellip;. and more.'}, {'id': '86', 'content': "Oracle Sales Data Seen Being Released (Reuters) Reuters - Oracle Corp. sales documents\\detailing highly confidential information, such as which\\companies receive discounts on Oracle's business software\\products and the size of the discounts, are likely to be made\\public, a federal judge said on Friday."}, {'id': '97', 'content': "What's in a Name? Well, Matt Is Sexier Than Paul (Reuters) Reuters - As Shakespeare said, a rose by any other\\name would smell as sweet. Right?"}], 'var_function-call-17495019835124794378': {'category_counts': {'Business': 1779, 'Sci_Tech': 914, 'Unknown': 288, 'World': 2330, 'Sports': 1385}, 'world_region_counts': {'North America': 479, 'Asia': 446, 'South America': 470, 'Europe': 465, 'Africa': 470}}, 'var_function-call-10644385359616107151': {'counts': {'Unknown': 6696}, 'world_region_counts': {}}, 'var_function-call-10015373596397977800': {'counts': {'Business': 1602, 'Sci_Tech': 971, 'Unknown': 1110, 'World': 1627, 'Sports': 1386}, 'world_region_counts': {'Asia': 318, 'Europe': 314, 'South America': 334, 'North America': 331, 'Africa': 330}}}

exec(code, env_args)
