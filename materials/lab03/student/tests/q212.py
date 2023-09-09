OK_FORMAT = True
test = {   'name': 'q212',
    'points': 1,
    'suites': [   {   'cases': [   {'code': '>>> type(hello_world_components) == np.ndarray\nTrue', 'hidden': False, 'locked': False,
                                    "failure_message":"""The data type for ``hello_world_components`` is incorrect. Expected numpy array."""},
                                   {'code': '>>> len(interesting_numbers) == 5\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> all(hello_world_components == np.array(["Hello", ",", " ", "world", "!"]))\nTrue', 'hidden': False, 'locked': False,
                                     "failure_message":""""The provided answer for ``hello_world_components`` is incorrect. """,
                                                            "success_message":"""All answers provided are correct!"""}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
