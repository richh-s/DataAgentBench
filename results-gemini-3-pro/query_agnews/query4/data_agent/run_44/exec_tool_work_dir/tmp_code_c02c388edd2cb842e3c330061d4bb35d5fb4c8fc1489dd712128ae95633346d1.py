code = """import json
import re

# Load data
with open(locals()['var_function-call-1914971640396700157'], 'r') as f:
    meta_list = json.load(f)

with open(locals()['var_function-call-13503504558976548684'], 'r') as f:
    articles_list = json.load(f)

meta_map = {str(item['article_id']): item['region'] for item in meta_list}

# Keywords
world_keywords = {
    "iraq", "iraqi", "baghdad", "iran", "tehran", "nuclear", "palestinian", "gaza", "israel", "jerusalem",
    "peace", "troops", "forces", "military", "army", "war", "rebel", "insurgent", "attack", "kill", "dead", "blast", "bomb", "suicide",
    "president", "minister", "prime", "official", "leader", "government", "parliament", "senate", "election", "vote", "poll",
    "darfur", "sudan", "africa", "chavez", "venezuela", "russia", "putin", "china", "beijing", "korea", "afghanistan", "kabul",
    "un", "united nations", "nato", "eu", "european", "treaty", "sanction", "diplomat", "envoy", "talks", "meeting", "summit",
    "hostage", "kidnap", "terror", "qaeda", "bin laden", "militant", "clash", "violence", "security", "police", "court", "trial", "judge",
    "hurricane", "storm", "typhoon", "tsunami", "earthquake", "disaster", "relief", "aid", "crash", "plane", "zimbabwe", "pakistan", "musharraf", "arafat", "sharon", "bush", "kerry"
    # Removed "usa", "us"
}

sports_keywords = {
    "sport", "sports", "game", "match", "cup", "league", "tournament", "championship", "champion", "title",
    "win", "won", "winner", "victory", "loss", "lost", "defeat", "beat", "score", "result", "standings",
    "team", "squad", "club", "coach", "manager", "player", "athlete", "medal", "olympic", "athens", "gold", "silver", "bronze",
    "football", "soccer", "basketball", "nba", "baseball", "mlb", "red sox", "yankees", "hockey", "nhl", "tennis", "golf", "tiger woods",
    "racing", "f1", "formula one", "schumacher", "ferrari", "cricket", "rugby", "boxing", "nfl", "super bowl", "quarterback"
}

business_keywords = {
    "business", "company", "companies", "firm", "corp", "corporation", "inc", "ltd", "industry", "sector",
    "market", "stock", "share", "wall st", "dow", "nasdaq", "s&p", "index", "price", "rate", "value",
    "economy", "economic", "growth", "inflation", "recession", "deficit", "budget", "finance", "financial", "bank", "banking",
    "profit", "loss", "earnings", "quarter", "revenue", "sales", "deal", "merger", "acquisition", "bid", "buy", "sell",
    "invest", "investor", "investment", "fund", "dollar", "euro", "yen", "currency", "oil", "crude", "barrel", "energy", "gas",
    "airline", "airways", "boeing", "airbus", "delta", "fed", "greenspan", "wto", "imf", "job", "unemployment", "labor", "strike"
}

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

for article in articles_list:
    aid = str(article.get('article_id', ''))
    if aid in meta_map:
        text = (article.get('title', '') + " " + article.get('description', '')).lower()
        words = set(re.findall(r'\w+', text))
        
        scores = {
            'World': sum(1 for w in words if w in world_keywords),
            'Sports': sum(1 for w in words if w in sports_keywords),
            'Business': sum(1 for w in words if w in business_keywords),
            'Tech': sum(1 for w in words if w in tech_keywords)
        }
        
        if all(s == 0 for s in scores.values()):
            continue

        best_cat = max(scores, key=scores.get)
        
        # Tie-breaking logic refined
        if list(scores.values()).count(scores[best_cat]) > 1:
            # There is a tie for the max score
            # Prioritize: Tech > Sports > Business > World? No.
            # Use specific indicators.
            
            is_world_tie = (scores['World'] == scores[best_cat])
            is_biz_tie = (scores['Business'] == scores[best_cat])
            is_sport_tie = (scores['Sports'] == scores[best_cat])
            
            if is_world_tie and is_biz_tie:
                # World vs Business tie
                if any(w in words for w in ["iraq", "war", "troops", "bomb", "kill", "nuclear", "terror", "palestinian", "gaza", "israel", "darfur", "sudan"]):
                    best_cat = 'World'
                elif any(w in words for w in ["company", "profit", "stock", "market", "sales", "earnings", "deal", "oil", "price"]):
                    best_cat = 'Business'
                else:
                    # Default to Business (conservative for World)
                    best_cat = 'Business'
            
            elif is_world_tie and is_sport_tie:
                # World vs Sports tie (e.g. "Election win")
                # "Win" -> Sports. "Election" -> World.
                if any(w in words for w in ["game", "match", "cup", "league", "team", "score", "olympic", "medal"]):
                    best_cat = 'Sports'
                else:
                    best_cat = 'World'

        if best_cat == 'World':
            region = meta_map[aid]
            region_counts[region] = region_counts.get(region, 0) + 1

max_region = max(region_counts, key=region_counts.get) if region_counts else "None"

print("__RESULT__:")
print(json.dumps(region_counts))"""

env_args = {'var_function-call-1914971640396700157': 'file_storage/function-call-1914971640396700157.json', 'var_function-call-10479132233513005664': 6696, 'var_function-call-8989729352298864404': [{'_id': '6945236d71e5a520afd3711f', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6945236d71e5a520afd37120', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6945236d71e5a520afd37121', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6945236d71e5a520afd37122', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6945236d71e5a520afd37123', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-17645446409733323876': [{'_id': '6945236d71e5a520afd3711f', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6945236d71e5a520afd37120', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6945236d71e5a520afd37121', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6945236d71e5a520afd37122', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6945236d71e5a520afd37123', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-7763971529073008408': [], 'var_function-call-306862715966043572': [{'_id': '6945236d71e5a520afd3712c', 'article_id': '13', 'title': 'Google IPO Auction Off to Rocky Start', 'description': " WASHINGTON/NEW YORK (Reuters) - The auction for Google  Inc.'s highly anticipated initial public offering got off to a  rocky start on Friday after the Web search company sidestepped  a bullet from U.S. securities regulators."}, {'_id': '6945236d71e5a520afd37131', 'article_id': '18', 'title': 'US trade deficit swells in June', 'description': 'The US trade deficit has exploded 19 to a record \\$55.8bn as oil costs drove imports higher, according to a latest figures.'}, {'_id': '6945236d71e5a520afd37139', 'article_id': '26', 'title': 'Google auction begins on Friday', 'description': 'An auction of shares in Google, the web search engine which could be floated for as much as \\$36bn, takes place on Friday.'}], 'var_function-call-9887750109441631916': 5, 'var_function-call-13503504558976548684': 'file_storage/function-call-13503504558976548684.json', 'var_function-call-17053250052862343729': {'region_counts': {'Europe': 374, 'Asia': 381, 'North America': 393, 'Africa': 393, 'South America': 388}, 'max_region': 'North America', 'matched_articles': 6696}, 'var_function-call-10104289256948113553': {'North America': ['s', '39', 'iraq', 'minister', 'president', 'bush', 'over', 'his', 'two', 'government', 'prime', 'after', 'court', 'leader', 'security', 'more', 'their', 'people', 'lt'], 'Africa': ['s', '39', 'iraq', 'u', 'his', 'president', 'after', 'bush', 'minister', 'over', 'quot', 'talks', 'police', 'military', 'baghdad', 'government', 'up', 'not', 'killed', 'attack']}}

exec(code, env_args)
