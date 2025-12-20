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

# Categories (previous expanded list + strict additions)
categories = {
    "Business": [
        "market", "markets", "stock", "stocks", "share", "shares", "equity", "equities", "bond", "bonds", 
        "currency", "currencies", "dollar", "euro", "yen", "yuan", "pound", "exchange", "trading", "trader", 
        "broker", "wall street", "dow jones", "nasdaq", "economy", "economic", "economist", "finance", 
        "financial", "bank", "banking", "banker", "central bank", "fed", "federal reserve", "interest rate", 
        "inflation", "deflation", "gdp", "growth", "recession", "recovery", "trade", "deficit", "surplus", 
        "tariff", "export", "import", "company", "companies", "firm", "firms", "corporation", "corporate", 
        "business", "biz", "industry", "industrial", "sector", "profit", "earnings", "revenue", "sales", 
        "loss", "losses", "debt", "loan", "credit", "mortgage", "deal", "merger", "acquisition", "buyout", 
        "takeover", "bid", "ipo", "ceo", "cfo", "executive", "manager", "management", "oil", "crude", "gas", 
        "energy", "petroleum", "price", "pricing", "cost", "consumer", "retail", "spending", "shopper", 
        "store", "shop", "job", "employment", "unemployment", "hiring", "layoff", "wage", "salary", "tax", 
        "taxation", "budget", "imf", "world bank", "wto", "treasury", "chrysler", "gm", "ford", "toyota", 
        "honda", "nissan", "automaker", "airline", "boeing", "airbus", "walmart"
    ],
    "Sports": [
        "sport", "sports", "game", "games", "match", "matches", "tournament", "tourney", "championship", 
        "champion", "title", "cup", "league", "season", "playoff", "final", "semifinal", "quarterfinal", 
        "team", "club", "squad", "roster", "player", "athlete", "coach", "manager", "referee", "umpire", 
        "score", "result", "win", "winner", "victory", "lose", "loser", "defeat", "draw", "tie", "goal", 
        "point", "run", "touchdown", "basket", "home run", "homer", "medal", "gold", "silver", "bronze", 
        "record", "olympic", "olympics", "football", "soccer", "baseball", "basketball", "hockey", "tennis", 
        "golf", "cricket", "rugby", "boxing", "wrestling", "racing", "driver", "f1", "nascar", "stadium", 
        "arena", "field", "pitch", "court", "nfl", "nba", "mlb", "nhl", "fifa", "uefa", "red sox", "yankees"
    ],
    "Sci_Tech": [
        "science", "scientist", "scientific", "research", "researcher", "study", "studies", "experiment", 
        "lab", "laboratory", "discovery", "tech", "technology", "technological", "computer", "computing", 
        "software", "hardware", "program", "app", "application", "code", "coding", "developer", "internet", 
        "web", "online", "net", "cyber", "digital", "data", "database", "server", "cloud", "network", 
        "wireless", "mobile", "phone", "smartphone", "tablet", "device", "gadget", "electronics", "chip", 
        "processor", "semiconductor", "robot", "robotics", "ai", "artificial intelligence", "space", 
        "universe", "galaxy", "planet", "star", "astronomy", "nasa", "esa", "mission", "shuttle", "rocket", 
        "launch", "satellite", "orbit", "mars", "moon", "earth", "biology", "biological", "genetics", "gene", 
        "dna", "medical", "medicine", "health", "healthcare", "disease", "virus", "bacteria", "infection", 
        "cancer", "aids", "hiv", "drug", "pharmaceutical", "treatment", "therapy", "patient", "doctor", 
        "physician", "surgeon", "hospital", "google", "apple", "microsoft", "ibm", "facebook", "amazon", 
        "twitter", "intel", "dell", "hp", "oracle", "sap", "linux", "windows", "browser", "firefox", 
        "explorer", "mozilla"
    ],
    "World": [
        "world", "international", "government", "govt", "president", "minister", "parliament", "congress", 
        "senate", "representative", "legislation", "law", "bill", "vote", "election", "poll", "campaign", 
        "candidate", "voter", "party", "democrat", "republican", "conservative", "labour", "liberal", 
        "socialist", "war", "civil war", "battle", "fight", "fighting", "clash", "conflict", "crisis", 
        "attack", "bomb", "blast", "explosion", "suicide", "terror", "terrorist", "militant", "insurgent", 
        "rebel", "guerrilla", "army", "navy", "air force", "marine", "soldier", "troop", "military", 
        "defense", "defence", "weapon", "arms", "nuclear", "atomic", "missile", "drone", "airstrike", 
        "peace", "treaty", "ceasefire", "deal", "talks", "diplomat", "diplomacy", "ambassador", "foreign", 
        "global", "refugee", "migrant", "immigration", "border", "police", "arrest", "detain", "jail", 
        "prison", "prisoner", "human rights", "protest", "demonstration", "rally", "riot", "strike", 
        "court", "trial", "judge", "justice", "supreme court", "verdict", "sentence", "official", 
        "authority", "spokesman", "leader", "chief", "head", "director", "secretary", "premier", 
        "chancellor", "king", "queen", "prince", "pope", "vatican", "german", "germany", "french", 
        "france", "spanish", "spain", "italian", "italy", "britain", "british", "uk", "united kingdom", 
        "london", "europe", "european", "asia", "asian", "africa", "african", "middle east", 
        "latin america", "south america", "north america", "australia", "australian", "canada", 
        "canadian", "japan", "japanese", "china", "chinese", "india", "indian", "pakistan", 
        "pakistani", "afghan", "afghanistan", "iraq", "iraqi", "iran", "iranian", "syria", "syrian", 
        "israel", "israeli", "palestine", "palestinian", "gaza", "egypt", "egyptian", "russia", 
        "russian", "ukraine", "ukrainian", "crimea", "putin", "obama", "biden", "bush", "clinton", 
        "trump", "merkel", "hollande", "cameron", "blair", "modi", "xi jinping", "kim jong", "un", 
        "united nations", "nato", "eu", "commission", "boko haram", "taliban", "isis", "al qaeda",
        "united states", "white house", "pentagon", "state department", "african union", "asean"
    ]
}

cat_config = {}
for cat, kws in categories.items():
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
    
    scores = {k: 0 for k in categories}
    
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

debug_counts = Counter()
world_region_counts = Counter()

for m in metadata:
    aid = str(m['article_id'])
    if aid in articles_map:
        art = articles_map[aid]
        content = (art.get('title', '') + " " + art.get('description', ''))
        cat = classify(content)
        debug_counts[cat] += 1
        
        if cat == "World":
            world_region_counts[m['region']] += 1

print("__RESULT__:")
print(json.dumps({
    "counts": dict(debug_counts),
    "world_region_counts": dict(world_region_counts)
}))"""

env_args = {'var_function-call-4087601676422552917': ['authors', 'article_metadata'], 'var_function-call-4087601676422553258': ['articles'], 'var_function-call-16836183799483844241': 'file_storage/function-call-16836183799483844241.json', 'var_function-call-11996756743093828097': 'file_storage/function-call-11996756743093828097.json', 'var_function-call-8460452426655104065': {'min': 13, 'max': 127570, 'count': 6696}, 'var_function-call-17656108898543788620': [{'article_id': '13', 'title': 'Google IPO Auction Off to Rocky Start', 'description': " WASHINGTON/NEW YORK (Reuters) - The auction for Google  Inc.'s highly anticipated initial public offering got off to a  rocky start on Friday after the Web search company sidestepped  a bullet from U.S. securities regulators."}, {'article_id': '14', 'title': 'Dollar Falls Broadly on Record Trade Gap', 'description': " NEW YORK (Reuters) - The dollar tumbled broadly on Friday  after data showing a record U.S. trade deficit in June cast  fresh doubts on the economy's recovery and its ability to draw  foreign capital to fund the growing gap."}, {'article_id': '15', 'title': 'Rescuing an Old Saver', 'description': "If you think you may need to help your elderly relatives with their finances, don't be shy about having the money talk -- soon."}, {'article_id': '16', 'title': 'Kids Rule for Back-to-School', 'description': 'The purchasing power of kids is a big part of why the back-to-school season has become such a huge marketing phenomenon.'}, {'article_id': '17', 'title': 'In a Down Market, Head Toward Value Funds', 'description': "There is little cause for celebration in the stock market these days, but investors in value-focused mutual funds have reason to feel a bit smug -- if only because they've lost less than the folks who stuck with growth."}], 'var_function-call-6556494366233684975': [{'region': 'Europe', 'title': 'Google IPO Auction Off to Rocky Start', 'description': " WASHINGTON/NEW YORK (Reuters) - The auction for Google  Inc.'s highly anticipated initial public offering got off to a  rocky start on Friday after the Web search company sidestepped  a bullet from U.S. securities regulators."}], 'var_function-call-11690996527890362772': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-1990041759778261395': 'file_storage/function-call-1990041759778261395.json', 'var_function-call-2316604512931417648': {'world_counts': {}, 'sample': []}, 'var_function-call-5023701990922176121': [{'id': '13', 'content': "Google IPO Auction Off to Rocky Start  WASHINGTON/NEW YORK (Reuters) - The auction for Google  Inc.'s highly anticipated initial public offering got off to a  rocky start on Friday after the Web search company sidestepped  a bullet from U.S. securities regulators."}, {'id': '18', 'content': 'US trade deficit swells in June The US trade deficit has exploded 19 to a record \\$55.8bn as oil costs drove imports higher, according to a latest figures.'}, {'id': '26', 'content': 'Google auction begins on Friday An auction of shares in Google, the web search engine which could be floated for as much as \\$36bn, takes place on Friday.'}, {'id': '51', 'content': "Delightful Dell The company's results show that it's not grim all over tech world. Just all of it that isn't Dell."}, {'id': '52', 'content': "Chrysler's Bling King After a tough year, Detroit's troubled carmaker is back -- thanks to a maverick designer and a car that is dazzling the hip-hop crowd"}, {'id': '67', 'content': 'IT Myth 5: Most IT projects fail Do most IT projects fail? Some point to the number of giant consultancies such as IBM Global Services, Capgemini, and Sapient, who feed off bad experiences encountered by enterprises. Sapient is a company founded on the realization that IT projects are not successful, says Sapient CTO Ben Gaucherin.'}, {'id': '70', 'content': "U.K.'s NHS taps Gartner to help plan \\$9B IT overhaul LONDON -- The U.K.'s National Health Service (NHS) has tapped IT researcher Gartner Inc. to provide market intelligence services as the health organization forges ahead with a mammoth, 5 billion (\\$9.2 billion) project to upgrade its information technology infrastructure."}, {'id': '74', 'content': 'HP to Buy Synstar Hewlett-Packard will pay \\$297 million for the British company. Also: TiVo goes all out to attract customers   hellip;. Sprint offers service guarantees for business wireless subscribers   hellip;. and more.'}, {'id': '86', 'content': "Oracle Sales Data Seen Being Released (Reuters) Reuters - Oracle Corp. sales documents\\detailing highly confidential information, such as which\\companies receive discounts on Oracle's business software\\products and the size of the discounts, are likely to be made\\public, a federal judge said on Friday."}, {'id': '97', 'content': "What's in a Name? Well, Matt Is Sexier Than Paul (Reuters) Reuters - As Shakespeare said, a rose by any other\\name would smell as sweet. Right?"}], 'var_function-call-17495019835124794378': {'category_counts': {'Business': 1779, 'Sci_Tech': 914, 'Unknown': 288, 'World': 2330, 'Sports': 1385}, 'world_region_counts': {'North America': 479, 'Asia': 446, 'South America': 470, 'Europe': 465, 'Africa': 470}}, 'var_function-call-10644385359616107151': {'counts': {'Unknown': 6696}, 'world_region_counts': {}}, 'var_function-call-10015373596397977800': {'counts': {'Business': 1602, 'Sci_Tech': 971, 'Unknown': 1110, 'World': 1627, 'Sports': 1386}, 'world_region_counts': {'Asia': 318, 'Europe': 314, 'South America': 334, 'North America': 331, 'Africa': 330}}, 'var_function-call-17883424521961616688': ["Chrysler's Bling King After a tough year, Detroit's troubled carmaker is back -- thanks to a maverick designer and a car that is dazzling the hip-hop crowd", "What's in a Name? Well, Matt Is Sexier Than Paul (Reuters) Reuters - As Shakespeare said, a rose by any other\\name would smell as sweet. Right?", "Saturn's Moon Titan: Prebiotic Laboratory by Harry Bortman    In this second and final part of the interview, Lunine explains how Huygens may help scientists understand the origin of life on Earth, even if it doesn't detect life on Titan.    Astrobiology Magazine -- Titan is the only moon in our solar system with an atmosphere, and it is the organic chemistry that has been detected in that atmosphere that has sparked the imagination of planetary scientists like Lunine...", "He #146;s not short on confidence It's a case he could have made more convincingly with something other than a half-swing tapper to the pitcher for the final out of yet another in a seemingly endless series of one-run losses for the Red Sox. But Orlando Cabrera wants fans to believe this: For all the futile swings he has made in his two-week incarnation as a ...", 'Exercise -- the Real Fountain of Youth Want to age gracefully? Keep moving. Regular exercise can reduce the risk of chronic disease -- such as heart trouble, diabetes, even cancer -- and keep you feeling and looking younger as you age.', 'Suspected Militants Kidnap Iraqi Officer-Jazeera  DUBAI (Reuters) - Suspected militants have kidnapped an  Iraqi intelligence officer in response to the fighting in the  holy city of Najaf, Al Jazeera television reported on Tuesday.', "Marlins Defeat Dodgers 4-2 (AP) AP - Miguel Cabrera homered and Mike Lowell singled home the go-ahead run, helping the Florida Marlins beat the Dodgers 4-2 on Monday night in Paul Lo Duca's return to Los Angeles.", "BOFH takes a hit from Cupid's arrow &lt;strong&gt;Episode 26&lt;/strong&gt; Shall I compare thee to an OS2-free Intel box?", 'German welfare rallies escalate Eastern Germany sees more mass protests over welfare cuts, with smaller rallies in western cities.', 'Migrants #39; ordeal ugly side of paradise Pleasant visions of fun in the sun in the Dominican Republic are being shattered by sad images of residents being smuggled away on wooden boats, only to perish at sea. '], 'var_function-call-1539849633491697580': {'counts': {'Unknown': 6696}, 'world_region_counts': {}}, 'var_function-call-4762272999924423397': {'counts': {'Business': 1722, 'Sci_Tech': 1120, 'Unknown': 418, 'Sports': 1464, 'World': 1972}, 'world_region_counts': {'North America': 401, 'Asia': 384, 'Africa': 392, 'Europe': 398, 'South America': 397}}}

exec(code, env_args)
