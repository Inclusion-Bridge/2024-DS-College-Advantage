OK_FORMAT = True
test = {   'name': 'q1_6',
    'points': 1,
    'suites': [   {   'cases': [   {'code': ">>> pter_over_time.take(0).column(0).item(0) == '1994-01-01'\nTrue", 'hidden': False, 'locked': False},
                                   {'code': '>>> np.all(pter_over_time.column("PTER")== pter)\nTrue', 'hidden': True, 'locked': False},
                                   {'code': '>>> np.all(pter_over_time.column("Year")== year)\nTrue', 'hidden': True, 'locked': False},
                                   {'code': ">>> pter_over_time.labels\n('Date', 'NEI', 'NEI-PTER', 'Year', 'PTER')", 'hidden': True, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}