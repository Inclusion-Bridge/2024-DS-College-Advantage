OK_FORMAT = True
test = {   'name': 'q1_1',
    'points': 1,
    'suites': [   {   'cases': [   {'code': '>>> len(ab_test_order) == 6\nTrue', 'hidden': False, 'locked': False,
                                    "failure_message":"""The length of `ab_test_order` is incorrect! Expected number of elements should be 6."""},
                                   {'code': '>>> correct_order = make_array(5, 1, 3, 2, 4, 6);\n>>> all(correct_order == ab_test_order)\nTrue', 'hidden': False, 'locked': False,
                                    "failure_message":""""The order of A/B tests in ``correct_order`` is incorrect.""",
                                    "success_message":"""All answers provided are correct!"""}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
