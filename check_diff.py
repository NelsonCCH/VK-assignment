# for N entries in tickets1 and M entries in tickets2:
# Time complexity: O(N+M), 
#   since populaing a dictionary for comparison takes one loop for each file, 
#   and DeepDiff runs for near-linear time
# Space complexity: O(N+M) , the two extracted dictionaries from original json files

import json

with open('tickets1.json', 'r') as tickets1:
    tickets1_data = json.load(tickets1)

with open('tickets2.json', 'r') as tickets2:
    tickets2_data = json.load(tickets2)

# First extract the TicketID and its price of each json file, 
# and put them into a dictionary, where TicketID being the key, and its price being the value.
# A less nested structure is better for comparison later and improved readability

# I took the B2BRetailPrice for comparison anyway, since the email didn't specify which price I should go for
Inventory1 = {ticket['TicketID']: ticket['B2BRetailPrice'] for ticket in tickets1_data['Inventories']}
Inventory2 = {ticket['TicketID']: ticket['B2BRetailPrice'] for ticket in tickets2_data['Inventories']}

# checking if ticket exists in new record but not in old record
def count_new_tickets(old_record, new_record):
    count = 0
    for ticket in new_record:
        if ticket not in old_record:
            count += 1
    return count

# checking if ticket exists in old record but not in new record
def count_removed_tickets(old_record, new_record):
    count = 0
    for ticket in old_record:
        if ticket not in new_record:
            count += 1
    return count
    
# checking if ticket exists in both records nd the price is also changed
def count_price_updated_tickets(old_record, new_record):
    count = 0
    for ticket in new_record:
        if ticket in old_record and old_record[ticket] != new_record[ticket]:
            count += 1
    return count

# Since I don't know how this functionality will be called, I will only print the answers out for now
print(f'No. of new tickets : {count_new_tickets(Inventory1, Inventory2)}')
print(f'No. of removed tickets : {count_removed_tickets(Inventory1, Inventory2)}')
print(f'No. of price updated tickets : {count_price_updated_tickets(Inventory1, Inventory2)}')