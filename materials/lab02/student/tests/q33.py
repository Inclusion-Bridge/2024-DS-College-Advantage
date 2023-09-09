OK_FORMAT = True
test = {   'name': 'q33',
    'points': 1,
    'suites': [   {   'cases': [   {'code': ">>> sorted(farmers_markets_locations.labels) == ['MarketName', 'State', 'city', 'x', 'y']\nTrue",
                                     'hidden': False, 'locked': False,
                                     "failure_message":""""The table ``farmers_markets_locations`` doesn't have the specified number of columns. Make sure the table only contains the following columns: \n['MarketName', 'State', 'city', 'x', 'y']"""},
                                   {'code': '>>> farmers_markets_locations.num_rows == 8546\nTrue',
                                     'hidden': False, 'locked': False,
                                    "failure_message":""""The provided table is incorrect. Check the instructions provided in question 3.3 again.""",
                                    "success_message":"""All answers provided are correct!"""}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
