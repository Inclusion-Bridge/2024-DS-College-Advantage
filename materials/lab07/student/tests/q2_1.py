OK_FORMAT = True
test = {   'name': 'q2_1',
    'points': 1,
    'suites': [   {   'cases': [   {'code': '>>> ak_mn.num_rows == 44\nTrue', 'hidden': False, 'locked': False,
                                    "failure_message":"""The shape of `ak_mn` is incorrect! Expected number of rows should be 44."""},
                                   {'code': '>>> ak_mn.column("Murder rate in Alaska").item(0) == 10.19999981\nTrue', 'hidden': False, 'locked': False,
                                    "failure_message":"""The table `ak_mn` is incorrect! Check again!"""},
                                   {'code': '>>> ak_mn.column("Murder rate in Minnesota").item(0) == 1.200000048\nTrue', 'hidden': False, 'locked': False,
                                    "failure_message":"""The table `ak_mn` is incorrect! Check again!""",
                                     "success_message":"""All answers provided are correct!"""}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
