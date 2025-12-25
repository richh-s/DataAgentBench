code = """import json
import re
import collections

# Load data
with open(locals()['var_function-call-14621584579191841765'], 'r') as f:
    meta_list = json.load(f)

target_ids = set()
id_to_region = {}
for m in meta_list:
    aid = int(m['article_id'])
    target_ids.add(aid)
    id_to_region[aid] = m['region']

with open(locals()['var_function-call-9425048213146947809'], 'r') as f:
    all_articles = json.load(f)

# Keywords setup
raw_keywords = {
    "World": [
        "iraq", "israel", "iran", "palestin", "afghan", "darfur", "sudan", "nigeria", "korea", "syria", "lebanon", "pakistan", "russia", "china", "japan", "indonesia", "bush", "kerry", "election", "president", "minister", "prime", "official", "leader", "govt", "government", "parliament", "senate", "troop", "soldier", "military", "army", "rebel", "guerrilla", "militant", "terror", "bomb", "blast", "attack", "kill", "dead", "wound", "injured", "peace", "war", "treaty", "talks", "negotiation", "diplomat", "un", "nations", "eu", "european union", "nato", "nuclear", "weapon", "atomic", "strike", "hostage", "kidnap", "politic", "poll", "vote", "voter", "campaign", "candidate", "party", "baghdad", "gaza", "cairo", "moscow", "beijing", "tokyo", "london", "paris", "berlin", "tehran", "jerusalem", "kabul", "baghdad", "fallujah", "najaf", "basra", "arafat", "sharon", "putin", "blair", "chirac", "schroeder", "powell", "rice", "rumsfeld", "annan", "al-qaeda", "qaeda", "terrorism", "terrorist", "security", "insurgent", "province", "border", "country", "international", "foreign", "state", "law", "court", "judge", "justice", "police", "arrest", "jail", "prison", "crime", "criminal", "murder", "rights", "human", "aid", "refugee", "disaster", "storm", "hurricane", "flood", "earthquake", "tsunami", "typhoon", "crash", "accident", "plane", "train", "ship", "ferry"
    ],
    "Business": [
        "oil", "gas", "price", "stock", "market", "share", "wall st", "exchange", "nasdaq", "dow", "index", "dollar", "euro", "yen", "currency", "bank", "economy", "economic", "finance", "financial", "rate", "interest", "fed", "federal reserve", "profit", "earning", "revenue", "loss", "quarter", "fiscal", "corp", "inc", "company", "firm", "business", "industry", "sector", "trade", "deal", "merger", "acquisition", "buyout", "bid", "offer", "sales", "retail", "consumer", "ceo", "cfo", "executive", "manager", "chairman", "job", "labor", "workforce", "unemployment", "forecast", "outlook", "growth", "recession", "boeing", "airbus", "ford", "gm", "microsoft", "google", "yahoo", "intel", "oracle", "earnings", "dividend", "invest", "investment", "investor", "fund", "mutual", "bond", "treasury", "commodity", "gold", "silver", "crude", "barrel", "opec", "energy", "power", "utility", "electric", "telecom", "airline", "auto", "car", "manufacturer", "producer", "retailer", "store", "shop", "mall"
    ],
    "Sports": [
        "sport", "game", "match", "play", "player", "team", "coach", "manager", "cup", "league", "championship", "tournament", "olympic", "medal", "gold", "silver", "bronze", "world cup", "euro 2004", "nfl", "nba", "mlb", "nhl", "football", "baseball", "basketball", "soccer", "hockey", "tennis", "golf", "cricket", "rugby", "racing", "f1", "formula one", "driver", "athlete", "win", "lose", "victory", "defeat", "score", "record", "season", "stadium", "club", "red sox", "yankees", "lakers", "pistons", "arsenal", "manchester", "real madrid", "barcelona", "milan", "juventus", "chelsea", "liverpool", "bayern", "ferrari", "schumacher", "armstrong", "phelps", "williams", "federer", "roddick", "agassi", "woods", "mickelson", "final", "semi", "quarter", "round", "playoff", "super bowl", "series", "open", "tour", "grand slam", "wimbledon", "french open", "us open", "australian open", "masters", "pga"
    ],
    "Sci_Tech": [
        "technology", "tech", "science", "space", "nasa", "shuttle", "mission", "orbit", "planet", "mars", "moon", "solar", "astronomy", "computer", "pc", "software", "hardware", "internet", "web", "online", "net", "search engine", "virus", "worm", "security", "hacker", "patch", "microsoft", "windows", "linux", "apple", "ipod", "mac", "google", "yahoo", "intel", "amd", "chip", "processor", "server", "network", "wireless", "wifi", "broadband", "mobile", "phone", "cellphone", "cellular", "telecom", "biotech", "biology", "gene", "genome", "stem cell", "cloning", "research", "study", "discovery", "drug", "pharmaceutical", "medicine", "health", "disease", "cancer", "aids", "hiv", "fda", "gadget", "device", "digital", "electronic", "robot", "laser", "nanotech", "physic", "chemist", "biologist", "scientist", "lab", "laboratory", "experiment", "test", "trial", "launch", "satellite", "telescope", "galaxy", "universe", "star"
    ]
}

single_words = {}
phrases = {}

for cat, klist in raw_keywords.items():
    s_set = set()
    p_list = []
    for k in klist:
        k = k.lower()
        if " " in k:
            p_list.append(k)
        else:
            s_set.add(k)
    single_words[cat] = s_set
    phrases[cat] = p_list

region_counts = collections.defaultdict(int)
total_world_count = 0

for art in all_articles:
    try:
        aid = int(art['article_id'])
    except:
        continue
    
    if aid in target_ids:
        raw_text = (art.get('title', '') + " " + art.get('description', '')).lower()
        # Clean text for tokenization
        # Replace non-alphanumeric with space
        clean_text = ""
        for char in raw_text:
            if char.isalnum() or char.isspace():
                clean_text += char
            else:
                clean_text += " "
        
        tokens = set(clean_text.split())
        
        scores = {}
        for cat in raw_keywords:
            score = 0
            # Single words
            score += len(tokens.intersection(single_words[cat]))
            # Phrases
            for p in phrases[cat]:
                if p in raw_text:
                    score += 1
            scores[cat] = score
            
        if not scores:
            continue
            
        max_s = max(scores.values())
        if max_s == 0:
            continue
            
        candidates = [c for c, s in scores.items() if s == max_s]
        
        final_cat = candidates[0]
        if "World" in candidates:
            final_cat = "World"
            
        if final_cat == "World":
            reg = id_to_region[aid]
            region_counts[reg] += 1
            total_world_count += 1

print("__RESULT__:")
print(json.dumps(region_counts))"""

env_args = {'var_function-call-14621584579191841765': 'file_storage/function-call-14621584579191841765.json', 'var_function-call-7803509644995873515': 6696, 'var_function-call-6632200024076563961': 'file_storage/function-call-6632200024076563961.json', 'var_function-call-11326914846194858501': [{'_id': '694520032ac3bd471d0e4d73', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '694520032ac3bd471d0e4d74', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '694520032ac3bd471d0e4d75', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '694520032ac3bd471d0e4d76', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '694520032ac3bd471d0e4d77', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-14573584342887086246': [{'_id': '694520032ac3bd471d0e4d73', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '694520032ac3bd471d0e4d74', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '694520032ac3bd471d0e4d75', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '694520032ac3bd471d0e4d76', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '694520032ac3bd471d0e4d77', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-9425048213146947809': 'file_storage/function-call-9425048213146947809.json', 'var_function-call-14825555218432229196': {'counts': {}, 'total_world': 0, 'debug': []}, 'var_function-call-10078567874978574508': [{'_id': '694520032ac3bd471d0e4d80', 'article_id': '13', 'title': 'Google IPO Auction Off to Rocky Start', 'description': " WASHINGTON/NEW YORK (Reuters) - The auction for Google  Inc.'s highly anticipated initial public offering got off to a  rocky start on Friday after the Web search company sidestepped  a bullet from U.S. securities regulators."}, {'_id': '694520032ac3bd471d0e4d85', 'article_id': '18', 'title': 'US trade deficit swells in June', 'description': 'The US trade deficit has exploded 19 to a record \\$55.8bn as oil costs drove imports higher, according to a latest figures.'}, {'_id': '694520032ac3bd471d0e4d8d', 'article_id': '26', 'title': 'Google auction begins on Friday', 'description': 'An auction of shares in Google, the web search engine which could be floated for as much as \\$36bn, takes place on Friday.'}, {'_id': '694520032ac3bd471d0e4da6', 'article_id': '51', 'title': 'Delightful Dell', 'description': "The company's results show that it's not grim all over tech world. Just all of it that isn't Dell."}, {'_id': '694520032ac3bd471d0e4da7', 'article_id': '52', 'title': "Chrysler's Bling King", 'description': "After a tough year, Detroit's troubled carmaker is back -- thanks to a maverick designer and a car that is dazzling the hip-hop crowd"}], 'var_function-call-8882535602425701108': [{'World': 0, 'Business': 0, 'Sports': 0, 'Sci_Tech': 0}, {'World': 0, 'Business': 0, 'Sports': 0, 'Sci_Tech': 0}], 'var_function-call-2372033351680194466': ["<re.Match object; span=(0, 6), match='google'>", 'None', 'None', 'None']}

exec(code, env_args)
