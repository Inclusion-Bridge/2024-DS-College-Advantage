OK_FORMAT = True
test = {   'name': 'q211',
    'points': 1,
    'suites': [   {   'cases': [   {'code': '>>> type(interesting_numbers) == np.ndarray\nTrue', 'hidden': False, 'locked': False,
                                    "failure_message":""""The data type for ``interesting_numbers`` is incorrect. Expected numpy array."""},
                                   {'code': '>>> len(interesting_numbers) == 5\nTrue', 'hidden': False, 'locked': False,
                                    "failure_message":""""The length of ``interesting_numbers`` is incorrect. Expected five elements."""},
                                   {'code': '>>> all(interesting_numbers == np.array([0, 1, -1, math.pi, math.e]))\nTrue', 'hidden': False, 'locked': False,
                                    "failure_message":""""The provided answer for ``interesting_numbers`` is incorrect. """,
                                                            "success_message":"""All answers provided are correct!"""}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
