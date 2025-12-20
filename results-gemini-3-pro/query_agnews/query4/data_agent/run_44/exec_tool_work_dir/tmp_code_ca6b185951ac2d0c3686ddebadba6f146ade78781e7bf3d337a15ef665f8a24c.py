code = """import json
import re

# Load data
with open(locals()['var_function-call-1914971640396700157'], 'r') as f:
    meta_list = json.load(f)

with open(locals()['var_function-call-17645446409733323876'], 'r') as f:
    articles_list = json.load(f)

# Build metadata map
# Check id type. The previous output showed strings.
meta_map = {str(item['article_id']): item['region'] for item in meta_list}

# Keywords
# World (Politics, War, International Relations)
world_keywords = {
    "iraq", "iraqi", "baghdad", "iran", "tehran", "nuclear", "palestinian", "gaza", "israel", "jerusalem",
    "peace", "troops", "forces", "military", "army", "war", "rebel", "insurgent", "attack", "kill", "dead", "blast", "bomb", "suicide",
    "president", "minister", "prime", "official", "leader", "government", "parliament", "senate", "election", "vote", "poll",
    "darfur", "sudan", "africa", "chavez", "venezuela", "russia", "putin", "china", "beijing", "korea", "afghanistan", "kabul",
    "un", "united nations", "nato", "eu", "european", "treaty", "sanction", "diplomat", "envoy", "talks", "meeting", "summit",
    "hostage", "kidnap", "terror", "qaeda", "bin laden", "militant", "clash", "violence", "security", "police", "court", "trial", "judge",
    "hurricane", "storm", "typhoon", "tsunami", "earthquake", "disaster", "relief", "aid", "crash", "plane"
}

# Sports
sports_keywords = {
    "sport", "sports", "game", "match", "cup", "league", "tournament", "championship", "champion", "title",
    "win", "won", "winner", "victory", "loss", "lost", "defeat", "beat", "score", "result", "standings",
    "team", "squad", "club", "coach", "manager", "player", "athlete", "medal", "olympic", "athens", "gold", "silver", "bronze",
    "football", "soccer", "basketball", "nba", "baseball", "mlb", "red sox", "yankees", "hockey", "nhl", "tennis", "golf", "tiger woods",
    "racing", "f1", "formula one", "schumacher", "ferrari", "cricket", "rugby", "boxing", "nfl", "super bowl", "quarterback"
}

# Business
business_keywords = {
    "business", "company", "companies", "firm", "corp", "corporation", "inc", "ltd", "industry", "sector",
    "market", "stock", "share", "wall st", "dow", "nasdaq", "s&p", "index", "price", "rate", "value",
    "economy", "economic", "growth", "inflation", "recession", "deficit", "budget", "finance", "financial", "bank", "banking",
    "profit", "loss", "earnings", "quarter", "revenue", "sales", "deal", "merger", "acquisition", "bid", "buy", "sell",
    "invest", "investor", "investment", "fund", "dollar", "euro", "yen", "currency", "oil", "crude", "barrel", "energy", "gas",
    "airline", "airways", "boeing", "airbus", "delta", "fed", "greenspan", "wto", "imf", "job", "unemployment", "labor", "strike"
}

# Sci/Tech
tech_keywords = {
    "technology", "tech", "science", "scientific", "research", "study", "discovery", "new", "innovation",
    "computer", "software", "hardware", "internet", "web", "online", "net", "cyber", "digital",
    "google", "yahoo", "microsoft", "windows", "linux", "apple", "ipod", "mac", "ibm", "intel", "amd", "oracle", "cisco",
    "mobile", "phone", "wireless", "cell", "network", "broadband", "telecom", "nokia", "motorola",
    "space", "nasa", "shuttle", "mission", "launch", "orbit", "mars", "moon", "saturn", "cassini", "astronomy", "universe",
    "virus", "worm", "spam", "security", "hacker", "patch", "browser", "search", "engine", "blog",
    "game", "video game", "sony", "nintendo", "xbox", "playstation", "doom", "halo"
}

region_counts = {}

# Check IDs in filtering
filtered_count = 0
world_count = 0

for article in articles_list:
    aid = str(article['article_id'])
    if aid in meta_map:
        filtered_count += 1
        text = (article.get('title', '') + " " + article.get('description', '')).lower()
        
        # Tokenize (simple split)
        words = set(re.findall(r'\w+', text))
        
        scores = {
            'World': sum(1 for w in words if w in world_keywords),
            'Sports': sum(1 for w in words if w in sports_keywords),
            'Business': sum(1 for w in words if w in business_keywords),
            'Tech': sum(1 for w in words if w in tech_keywords)
        }
        
        # Find max category
        # If all 0, default? 
        # AG News is well separated. 
        # Tie breaking: World > Business > Sports > Tech?
        # Let's pick max.
        
        best_cat = max(scores, key=scores.get)
        
        if scores[best_cat] == 0:
            # If no keywords matched, ignore or try heuristics?
            # With rich keywords, 0 should be rare.
            pass
        elif best_cat == 'World':
            region = meta_map[aid]
            region_counts[region] = region_counts.get(region, 0) + 1
            world_count += 1

result = {
    "filtered_articles": filtered_count,
    "world_articles": world_count,
    "region_counts": region_counts
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-1914971640396700157': 'file_storage/function-call-1914971640396700157.json', 'var_function-call-10479132233513005664': 6696, 'var_function-call-8989729352298864404': [{'_id': '6945236d71e5a520afd3711f', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6945236d71e5a520afd37120', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6945236d71e5a520afd37121', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6945236d71e5a520afd37122', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6945236d71e5a520afd37123', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-17645446409733323876': [{'_id': '6945236d71e5a520afd3711f', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6945236d71e5a520afd37120', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6945236d71e5a520afd37121', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6945236d71e5a520afd37122', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6945236d71e5a520afd37123', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-7763971529073008408': [], 'var_function-call-306862715966043572': [{'_id': '6945236d71e5a520afd3712c', 'article_id': '13', 'title': 'Google IPO Auction Off to Rocky Start', 'description': " WASHINGTON/NEW YORK (Reuters) - The auction for Google  Inc.'s highly anticipated initial public offering got off to a  rocky start on Friday after the Web search company sidestepped  a bullet from U.S. securities regulators."}, {'_id': '6945236d71e5a520afd37131', 'article_id': '18', 'title': 'US trade deficit swells in June', 'description': 'The US trade deficit has exploded 19 to a record \\$55.8bn as oil costs drove imports higher, according to a latest figures.'}, {'_id': '6945236d71e5a520afd37139', 'article_id': '26', 'title': 'Google auction begins on Friday', 'description': 'An auction of shares in Google, the web search engine which could be floated for as much as \\$36bn, takes place on Friday.'}]}

exec(code, env_args)
