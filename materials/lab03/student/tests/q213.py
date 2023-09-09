OK_FORMAT = True
test = {   'name': 'q213',
    'points': 1,
    'suites': [   {   'cases': [   {'code': '>>> type(multiples_of_99) == np.ndarray\nTrue', 'hidden': False, 'locked': False,
                                    "failure_message":"""The data type for ``multiples_of_99`` is incorrect. Expected numpy array. """},
                                   {'code': '>>> len(multiples_of_99) == 102\nTrue', 'hidden': False, 'locked': False,
                                    "failure_message":""""The length of ``multiples_of_99`` is incorrect. Expected 102 elements."""},
                                   {'code': '>>> all(multiples_of_99 == np.arange(0, 9999+99, 99))\nTrue', 'hidden': False, 'locked': False,
                                     "failure_message":""""The provided answer for ``multiples_of_99`` is incorrect. """,
                                                            "success_message":"""All answers provided are correct!"""}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
