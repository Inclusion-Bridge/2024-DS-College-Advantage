OK_FORMAT = True
test = {   'name': 'q35',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> # Make sure to remove the "(No previous year)" CEOs;\n>>> "(No previous year)" not in with_previous_compensation.column("% Change")\nTrue',
                                       'hidden': False,
                                       'locked': False,
                                       "failure_message":"""Incorrect! Make sure to remove the "(No previous year)" CEOs."""},
                                   {   'code': '>>> import math;\n'
                                               '>>> # You have the column, but some of ;\n'
                                               '>>> # your values may be wrong.;\n'
                                               '>>> t = with_previous_compensation.sort("2014 Total Pay ($)", descending = True);\n'
                                               '>>> value = t.column("2014 Total Pay ($)").item(0);\n'
                                               '>>> math.isclose(value, 67700000.0, rel_tol = 1000)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False,
                                       "failure_message":"""Incorrect! You have the `2014 Total Pay ($)` column, but some of your values may be wrong."""},
                                   {'code': '>>> # You have the column, but your number of rows is off;\n>>> with_previous_compensation.num_rows==81\nTrue', 'hidden': False, 'locked': False,
                                    "failure_message":"""Incorrect! You have the `2014 Total Pay ($)` column, but your number of rows is off.""",
                                    "success_message":"""All answers provided are correct!"""}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
