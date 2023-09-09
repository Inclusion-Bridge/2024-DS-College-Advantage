OK_FORMAT = True
test = {   'name': 'q41',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> # Oops, your name is assigned to the wrong data type!;\n'
                                               '>>> type(year_population_crossed_6_billion) == int or type(year_population_crossed_6_billion) == np.int32\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False,
                                        "failure_message":""""The data type of ``year_population_crossed_6_billion`` is incorrect. Your answer must be an integer."""},
                                   {'code': '>>> year_population_crossed_6_billion == 1999\nTrue', 'hidden': False, 'locked': False,
                                    "failure_message":""""The provided answer for ``year_population_crossed_6_billion`` is incorrect. Population crossed 6 billion in 1999.""",
                                    "success_message":"""All answers provided are correct!"""}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
