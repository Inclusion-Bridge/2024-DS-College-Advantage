OK_FORMAT = True
test = {   'name': 'q1_1',
    'points': 1,
    'suites': [   {   'cases': [   {'code': '>>> # Did you add Career Length Column?;\n>>> nfl.num_columns == 6\nTrue', 'hidden': False, 'locked': False},
                                   {   'code': '>>> # Check that the first 10 rows are correct;\n>>> nfl.take(np.arange(10)).column(0).item(0) == "Baker Mayfield"\nTrue',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}