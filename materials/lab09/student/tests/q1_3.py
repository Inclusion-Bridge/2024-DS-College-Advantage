OK_FORMAT = True
test = {   'name': 'q1_3',
    'points': 1,
    'suites': [   {   'cases': [   {'code': '>>> abs(sum(faithful_standard.column(0))) <= 1e-8\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> int(round(duration_std)) == 1\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> int(round(wait_std)) == 14\nTrue', 'hidden': False, 'locked': False,
                                     "failure_message":"""The value of `wait_std` is incorrect! Check again!""",
                                     "success_message":"""All answers provided are correct!"""}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
