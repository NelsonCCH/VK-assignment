# for N entries in tickets1 and M entries in tickets2:
# Time complexity: O(N+M), 
#   since populaing a dictionary for comparison takes one loop for each file, 
#   and DeepDiff runs for near-linear time
# Space complexity: O(N+M) , the two extracted dictionaries from original json files

import json
from deepdiff import DeepDiff

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

# DeepDiff returns a dictionary of differences, 
# I can return with the specifics if needed,
# but for now, we are only interested in the counts
diff = DeepDiff(Inventory1, Inventory2)

# Since I don't know how this functionality will be called, I will only print the answers out for now
print(f"No. of new tickets : {len(diff['dictionary_item_added'])}")
print(f"No. of removed tickets : {len(diff['dictionary_item_removed'])}")
print(f"No. of price changed tickets : {len(diff['values_changed'])}")
