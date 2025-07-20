from mlxtend.frequent_patterns import apriori, association_rules
import pandas as pd

def perform_apriori(transactions):
    all_items = sorted(set(item for t in transactions for item in t))
    df = pd.DataFrame([{item: (item in t) for item in all_items} for t in transactions])
    frequent = apriori(df, min_support=0.25, use_colnames=True)
    rules = association_rules(frequent, metric="lift", min_threshold=1.0)
    rules = rules.round({'lift' : 4, 'confidence' : 4})
    rules['antecedents'] = rules['antecedents'].apply(lambda x: sorted(list(x)))
    rules['consequents'] = rules['consequents'].apply(lambda x: sorted(list(x)))
    rules['conf_category'] = rules['confidence'].apply(conf_category)
    rules['lift_category'] = rules['lift'].apply(lift_category)
    
    return rules[['antecedents', 'consequents', 'support', 'confidence', 'lift', 'conf_category', 'lift_category']].to_dict('records')

def conf_category(conf):
    if conf >= 0.9:
        return 'High'
    elif conf >= 0.7:
        return 'Medium'
    else:
        return 'Low'
    
def lift_category(lift):
    if lift >= 2:
        return 'Strong'
    elif lift >= 1:
        return 'Moderate'
    else:
        return 'Weak'