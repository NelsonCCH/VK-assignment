I decided to do it without libraries, I think it would be more interesting and better assessing my knowledge


To run: run check_diff.py, since I don't know how this will be called and how should I return the values, I simply print the answers to console for your reference

To test: run test_check_diff, I have drafted a few test cases for each functions

Time and space complexity analysis:

Let's say there are N entries in tickets1 and M entries in tickets2,
Time complexity: O(N+M): since populaing a dictionary for comparison takes one loop for each file, and another loop to execute the counting methods, worst case would walking through both files for once

Space complexity: O(N+M) , the two extracted dictionaries from original json files, which contains TicketID and its prices only


