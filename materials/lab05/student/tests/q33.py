OK_FORMAT = True
test = {   'name': 'q33',
    'points': 1,
    'suites': [   {   'cases': [   {'code': '>>> len(convenience_stats) == 2\nTrue', 'hidden': False, 'locked': False,
                                    "failure_message":"""The length of `convenience_sample` is incorrect! Expected number of elements should be 2."""},
                                   {'code': '>>> round(float(convenience_stats[0]), 2) == 20.36\nTrue', 'hidden': False, 'locked': False,
                                    "failure_message":"""The content of `convenience_sample` is incorrect! Check the elements of the `convenience_sample`."""},
                                   {'code': '>>> round(float(convenience_stats[1]), 2) == 2383533.82\nTrue', 'hidden': False, 'locked': False,
                                    "failure_message":"""The content of `convenience_sample` is incorrect! Check the elements of the `convenience_sample`.""",
                                    "success_message":"""All answers provided are correct!"""}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
