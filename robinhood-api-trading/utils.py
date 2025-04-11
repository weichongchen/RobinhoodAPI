import json
from pprint import pprint

def display(data):
    """
    Clean the data by removing the account number
    """
    if 'account_number' in data:
        del data['account_number']
    
    print(json.dumps(data, indent=4))
    #pprint(data)

    return data