OK_FORMAT = True
test = {   'name': 'q41',
    'points': 1,
    'suites': [   {   'cases': [   {'code': '>>> type(above_eight) == tables.Table\nTrue', 'hidden': False, 'locked': False,
                                     "failure_message":""""The data type of the ``above_eight`` variable is incorrect. Make sure that ``above_eight`` is a table!"""},
                                   {'code': '>>> above_eight.num_rows == 20\nTrue', 'hidden': False, 'locked': False},
                                   {   'code': '>>> # Make sure your columns are in the right order!;\n'
                                               ">>> # First column should be 'Title', second column should be 'Rating';\n"
                                               '>>> print(above_eight.sort(0).take([17]))\n'
                                               'Title       | Rating\n'
                                               'Toy Story 3 | 8.3\n',
                                       'hidden': False,
                                       'locked': False,
                                        "failure_message":""""The provided answer for ``above_eight`` is incorrect. Make sure your columns are in the right order! \n/
                                        First column should be 'Title', second column should be 'Rating'. """,
                                        "success_message":"""All answers provided are correct!"""}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
