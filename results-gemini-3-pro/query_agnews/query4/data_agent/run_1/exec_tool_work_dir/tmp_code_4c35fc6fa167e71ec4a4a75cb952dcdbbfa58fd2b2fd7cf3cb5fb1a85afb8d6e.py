code = """import json
import re
import string

# Load 2015 metadata
with open(locals()['var_function-call-6414145257666997456'], 'r') as f:
    metadata_list = json.load(f)

# Load articles
with open(locals()['var_function-call-490337090254977264'], 'r') as f:
    articles_1 = json.load(f)
with open(locals()['var_function-call-17060646393931628735'], 'r') as f:
    articles_2 = json.load(f)
with open(locals()['var_function-call-13111836206336045727'], 'r') as f:
    articles_3 = json.load(f)

articles_map = {}
for a in articles_1: articles_map[int(a['article_id'])] = a
for a in articles_2: articles_map[int(a['article_id'])] = a
for a in articles_3: articles_map[int(a['article_id'])] = a

world_keywords = [
    "president", "minister", "prime minister", "official", "government", "parliament", "senate", "congress", 
    "election", "vote", "poll", "war", "troop", "soldier", "army", "military", "attack", "bomb", "blast", 
    "kill", "killed", "dead", "injured", "wound", "rebel", "militia", "guerrilla", "terrorist", "hostage", "kidnap", 
    "peace", "talks", "treaty", "agreement", "summit", "meeting", "nuclear", "weapon", "sanction", "storm", 
    "hurricane", "typhoon", "earthquake", "flood", "disaster", "crash", "police", "court", "judge", "trial", 
    "prison", "arrest", "protest", "demonstration", "strike", "union", "law", "bill", "pope", "vatican", 
    "un", "united nations", "eu", "european union", "nato", "palestinian", "israeli", "iraqi", "afghan", 
    "syrian", "russian", "chinese", "ukraine", "korea", "iran", "saudi", "sudan", "darfur", "nepal", 
    "indonesia", "pakistan", "india", "baghdad", "kabul", "jerusalem", "gaza", "cairo", "damascus", "beirut",
    "moscow", "beijing", "washington", "london", "paris", "berlin", "tokyo", "politics", "political", "diplomat", 
    "ambassador", "embassy", "border", "security", "refugee", "crisis", "conflict",
    "isis", "isil", "islamic state", "boko haram", "al shabaab", "taliban", "al qaeda", "hezbollah", "hamas",
    "coup", "dictator", "regime", "human rights", "genocide", "massacre"
]

# Keep others same
business_keywords = [
    "stock", "market", "wall street", "dow", "nasdaq", "share", "profit", "earning", "quarter", "dividend", 
    "revenue", "sale", "deal", "merger", "acquisition", "buyout", "ipo", "investor", "analyst", "rate", 
    "fed", "federal reserve", "bank", "central bank", "economy", "economic", "dollar", "euro", "yen", "yuan", 
    "currency", "oil", "price", "barrel", "gold", "silver", "company", "corp", "corporation", "inc", "ltd", 
    "firm", "business", "industry", "trade", "deficit", "surplus", "budget", "tax", "inflation", "recession", 
    "job", "unemployment", "hire", "layoff", "ceo", "cfo", "executive", "manager", "boeing", "airbus", 
    "wal-mart", "general motors", "ford", "toyota", "microsoft", "google", "apple", "ibm", "intel", "oracle",
    "financial", "finance", "bond", "fund", "equity", "asset", "capital"
]
sports_keywords = [
    "sport", "game", "match", "team", "player", "coach", "manager", "score", "win", "loss", "defeat", 
    "victory", "draw", "tie", "season", "league", "cup", "championship", "tournament", "olympic", "medal", 
    "gold", "silver", "bronze", "record", "world cup", "super bowl", "nba", "nfl", "mlb", "nhl", "fifa", 
    "uefa", "tennis", "golf", "soccer", "football", "baseball", "basketball", "hockey", "cricket", "rugby", 
    "boxing", "racing", "f1", "nascar", "athlete", "stadium", "club", "round", "final", "semi-final"
]
scitech_keywords = [
    "science", "technology", "tech", "computer", "software", "hardware", "internet", "web", "online", "net", 
    "cyber", "virus", "worm", "hacker", "security", "space", "nasa", "shuttle", "mission", "launch", "orbit", 
    "planet", "mars", "moon", "astronomy", "telescope", "physics", "chemistry", "biology", "gene", "dna", 
    "stem cell", "clone", "medical", "medicine", "drug", "health", "disease", "cancer", "aids", "hiv", 
    "study", "research", "survey", "report", "device", "gadget", "phone", "mobile", "wireless", "broadband", 
    "satellite", "robot", "engine", "motor", "battery", "chip", "processor", "server", "network", "microsoft", 
    "google", "apple", "intel", "linux", "windows", "browser", "search engine", "digital", "electronic"
]

def classify(title, description):
    text = (title + " " + description).lower()
    for char in string.punctuation:
        text = text.replace(char, ' ')
    tokens = set(text.split())
    
    scores = {"World": 0, "Business": 0, "Sports": 0, "SciTech": 0}
    
    for word in tokens:
        if word in world_keywords: scores["World"] += 1
        if word in business_keywords: scores["Business"] += 1
        if word in sports_keywords: scores["Sports"] += 1
        if word in scitech_keywords: scores["SciTech"] += 1
            
    # Check for multi-word keywords (simple check)
    text_raw = (title + " " + description).lower()
    if "prime minister" in text_raw: scores["World"] += 1
    if "united nations" in text_raw: scores["World"] += 1
    if "islamic state" in text_raw: scores["World"] += 1
    if "boko haram" in text_raw: scores["World"] += 1
    if "al qaeda" in text_raw: scores["World"] += 1
    if "human rights" in text_raw: scores["World"] += 1
    if "wall street" in text_raw: scores["Business"] += 1
    
    max_score = -1
    best_cat = None
    for cat, score in scores.items():
        if score > max_score:
            max_score = score
            best_cat = cat
        elif score == max_score:
            if cat == "World": best_cat = "World"
            elif cat == "Sports" and best_cat != "World": best_cat = "Sports"
            
    if max_score == 0: return "Unknown"
    return best_cat

region_counts = {}

for meta in metadata_list:
    aid = int(meta['article_id'])
    region = meta['region']
    
    if aid in articles_map:
        article = articles_map[aid]
        category = classify(article['title'], article['description'])
        
        if category == "World":
            region_counts[region] = region_counts.get(region, 0) + 1

print("__RESULT__:")
print(json.dumps(region_counts))"""

env_args = {'var_function-call-6414145257666997456': 'file_storage/function-call-6414145257666997456.json', 'var_function-call-17387279326264468321': 'file_storage/function-call-17387279326264468321.json', 'var_function-call-10428291813963926827': 6696, 'var_function-call-4939086114809291303': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-13401999490339433067': 5, 'var_function-call-2594177708310146329': ['articles'], 'var_function-call-1080993007468921455': [{'_id': '6944e918a831038495320111', 'article_id': '13', 'title': 'Google IPO Auction Off to Rocky Start', 'description': " WASHINGTON/NEW YORK (Reuters) - The auction for Google  Inc.'s highly anticipated initial public offering got off to a  rocky start on Friday after the Web search company sidestepped  a bullet from U.S. securities regulators."}], 'var_function-call-490337090254977264': 'file_storage/function-call-490337090254977264.json', 'var_function-call-13608484779050026561': {}, 'var_function-call-7396373676834293089': 'Debug done', 'var_function-call-264186479689831389': {'meta_count': 6696, 'art_count': 50000, 'common_count': 2606, 'samples': [{'id': 13, 'title': 'Google IPO Auction Off to Rocky Start', 'desc': " WASHINGTON/NEW YORK (Reuters) - The auction for Google  Inc.'s highly anticipated initial public offering got off to a  rocky start on Friday after the Web search company sidestepped  a bullet from U.S. securities regulators."}, {'id': 18, 'title': 'US trade deficit swells in June', 'desc': 'The US trade deficit has exploded 19 to a record \\$55.8bn as oil costs drove imports higher, according to a latest figures.'}, {'id': 26, 'title': 'Google auction begins on Friday', 'desc': 'An auction of shares in Google, the web search engine which could be floated for as much as \\$36bn, takes place on Friday.'}, {'id': 51, 'title': 'Delightful Dell', 'desc': "The company's results show that it's not grim all over tech world. Just all of it that isn't Dell."}, {'id': 52, 'title': "Chrysler's Bling King", 'desc': "After a tough year, Detroit's troubled carmaker is back -- thanks to a maverick designer and a car that is dazzling the hip-hop crowd"}]}, 'var_function-call-17577238825078641661': {'max': 127570, 'min': 13}, 'var_function-call-6615796554866923446': {'c1': 2606, 'c2': 2620, 'c3': 1470}, 'var_function-call-2135196166811878855': {'max': 49999, 'min': 0}, 'var_function-call-4794802073798709164': [{'article_id': '50000', 'title': 'David Hare Sees How War Plays on World Stage', 'description': '  LONDON -- "Stuff happens!" Donald Rumsfeld once exclaimed in response to a reporter\'s question about the looting of Baghdad after the U.S. invasion of Iraq in 2003. "Freedom\'s untidy," he went on to explain, "and free people are free to make mistakes and commit crimes and do bad things. They\'re also free to love their lives and do wonderful things, and that\'s what\'s going to happen here."'}, {'article_id': '50001', 'title': 'Bremer Criticizes Lack of Troops in Iraq', 'description': 'The U.S. official said Monday that the United States made two major mistakes: not deploying enough troops and then not containing the violence immediately after the ouster of Saddam Hussein.'}, {'article_id': '50002', 'title': 'SpaceShipOne Wins \\$10 Mln X Prize With Today #39;s Flight (Update2)', 'description': 'The rocket plane SpaceShipOne, built by aviation pioneer Burt Rutan and financed by Microsoft Corp. co- founder Paul Allen, won the \\$10 million competition aimed at creating a space tourism '}, {'article_id': '50003', 'title': 'Tennis: Harel Levy beats Yen-Hsun Lu at Japan Open', 'description': 'Israeli Harel Levy defeated Yen-Hsun Lu of Chinese Taipei 7-6 (7-1), 7-6 (7-1) on Monday in the first round of the \\$860,000 ATP/WTA Tour #39;s Japan Open.'}, {'article_id': '50004', 'title': ' #39;Grinders #39; turn up pressure in postseason', 'description': 'Like the autumn leaves, baseball changes in October. Pitchers dominate, and hitters desperately look for ways to score runs. By Andre Pichette, AP.'}], 'var_function-call-16347106118032338340': [{'article_id': '100000', 'title': 'Venezuelan Car-Bomb Suspect Killed, Weapons Found', 'description': " CARACAS, Venezuela (Reuters) - A Venezuelan lawyer  suspected in last week's bombing murder of a top state  prosecutor was killed in a gunfight with police on Tuesday  after he tried to ram detectives with his car and opened fire  on them, officials said."}, {'article_id': '100001', 'title': 'British Muslims push to integrate', 'description': 'They are working to repair an image tattered by homegrown radicals - and to find a place in mainstream society.'}, {'article_id': '100002', 'title': 'Ukraine set for talks on crisis', 'description': "Ukraine's president and opposition agree to hold talks, as huge protests over disputed elections continue."}, {'article_id': '100003', 'title': 'Smoking killing millions globally', 'description': '\\Smoking killed almost 5 million people around the world in 2000, researchers have calculated.'}, {'article_id': '100004', 'title': 'Outsource that reporter!', 'description': 'Reuters journalists are said to be close to striking over the outsourcing of reporting jobs to India.'}], 'var_function-call-17060646393931628735': 'file_storage/function-call-17060646393931628735.json', 'var_function-call-13111836206336045727': 'file_storage/function-call-13111836206336045727.json', 'var_function-call-15731376188537317951': {'counts': {}, 'coverage': 6696, 'total_meta': 6696}, 'var_function-call-17463734382494246623': 'Done', 'var_function-call-14511347728020974839': {'title': 'David Hare Sees How War Plays on World Stage', 'desc': '  LONDON -- "Stuff happens!" Donald Rumsfeld once exclaimed in response to a reporter\'s question about the looting of Baghdad after the U.S. invasion of Iraq in 2003. "Freedom\'s untidy," he went on to explain, "and free people are free to make mistakes and commit crimes and do bad things. They\'re also free to love their lives and do wonderful things, and that\'s what\'s going to happen here."', 'tokens_sample': [], 'found': [], 'war_in_keywords': True}, 'var_function-call-7514730158527600338': {'South America': 439, 'Asia': 435, 'North America': 444, 'Africa': 446, 'Europe': 434}, 'var_function-call-1676993166136189007': {'Europe': 1357, 'South America': 1332, 'Africa': 1345, 'Asia': 1333, 'North America': 1329}}

exec(code, env_args)
