OK_FORMAT = True
test = {   'name': 'q3_11',
    'points': 1,
    'suites': [   {   'cases': [   {'code': '>>> len(differences) == 5000\nTrue', 'hidden': False, 'locked': False,
                                    "failure_message":"""The length of `differences` is incorrect!."""},
                                   {'code': '>>> abs(np.average(differences)) < 1\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> all(differences == differences.item(0)) == False\nTrue', 'hidden': False, 'locked': False,
                                    "failure_message":"""The value of `differences` is incorrect! Check again!""",
                                    "success_message":"""All answers provided are correct!"""}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
