OK_FORMAT = True
test = {   'name': 'q1_5',
    'points': 1,
    'suites': [   {   'cases': [   {'code': '>>> int(round(statistic(.5,.5) + statistic(.4,.1),1)) == 30\nTrue', 'hidden': False, 'locked': False,
                                     "failure_message":"""Test case failed. Ensure that your `statistic` function computes the absolute difference between the expected percent correct and the actual percent correct.\n/
                                     Additionally, it must return a percentage and not proportion!"""},
                                   {'code': '>>> int(statistic(.4,.1) - statistic(.1,.4)) == 0\nTrue', 'hidden': False, 'locked': False,
                                    "failure_message":"""Test case failed. Ensure that your `statistic` function computes the absolute difference between the expected percent correct and the actual percent correct.\n/
                                     Additionally, it must return a percentage and not proportion!""",
                                    "success_message":"""All answers provided are correct!"""}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
