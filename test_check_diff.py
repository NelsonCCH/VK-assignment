import unittest

from check_diff import count_new_tickets, count_price_updated_tickets, count_removed_tickets

#testing data
t1 = {'1': 1.0, '2': 2.0, '3': 3.0 }
t2 = {'1': 1.0, '2': 200.0, '3': 3.0, '4': 400.0 }
t3 = {'1': 1.0, '2': 2.0, '3': 3.0 }
t4 = {'1': 100.0, '2': 200.0, '5': 5.0}
            

class TestCheckDiff (unittest.TestCase):

    def test_count_new_tickets(self):

        self.assertEqual(count_new_tickets(t1, t2), 1)
        self.assertEqual(count_new_tickets(t1, t3), 0)
        self.assertEqual(count_new_tickets(t1, t4), 1)

    def test_count_removed_tickets(self):

        self.assertEqual(count_removed_tickets(t1, t2), 0)
        self.assertEqual(count_removed_tickets(t1, t3), 0)
        self.assertEqual(count_removed_tickets(t1, t4), 1)
    
    def test_count_price_updated_tickets(self):

        self.assertEqual(count_price_updated_tickets(t1, t2), 1)
        self.assertEqual(count_price_updated_tickets(t1, t3), 0)
        self.assertEqual(count_price_updated_tickets(t1, t4), 2)


if __name__ == '__main__':
    unittest.main()