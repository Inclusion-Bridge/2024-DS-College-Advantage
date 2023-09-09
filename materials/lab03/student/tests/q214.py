OK_FORMAT = True
test = {   'name': 'q214',
    'points': 1,
    'suites': [   {   'cases': [   {'code': '>>> type(collection_times) == np.ndarray\nTrue', 'hidden': False, 'locked': False,
                                       "failure_message":"""The data type for ``collection_times`` is incorrect. Expected numpy array. """},
                                   {'code': '>>> len(collection_times) == 744\nTrue', 'hidden': False, 'locked': False,
                                    "failure_message":""""The length of ``collection_times`` is incorrect. Expected 744 elements."""},
                                   {'code': '>>> all(collection_times == np.arange(0, 31*24*60*60, 60*60))\nTrue', 'hidden': False, 'locked': False,
                                    "failure_message":""""The provided answer for ``collection_times`` is incorrect. """,
                                                            "success_message":"""All answers provided are correct!"""}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
