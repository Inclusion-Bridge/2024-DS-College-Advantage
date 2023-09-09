OK_FORMAT = True
test = {   'name': 'q1_9',
    'points': 1,
    'suites': [   {   'cases': [   {'code': '>>> 0 <= proportion_greater_or_equal <= 1\nTrue', 'hidden': False, 'locked': False,
                                    "failure_message":"""Value of `proportion_greater_or_equal` expect to lie between 0 and 1.""",},
                                   {'code': '>>> proportion_greater_or_equal*1000 == np.count_nonzero(simulated_statistics >= observed_statistic)\nTrue', 'hidden': False, 'locked': False,
                                    "failure_message":"""The value of `proportion_greater_or_equal` is incorrect!""",
                                     "success_message":"""All answers provided are correct!"""}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
