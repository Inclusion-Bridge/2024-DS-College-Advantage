OK_FORMAT = True
test = {   'name': 'q3_3_1',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> # Fill in the row;\n'
                                               '>>> #   time = ...;\n'
                                               '>>> # with something like:;\n'
                                               '>>> #   time = 4.567;\n'
                                               '>>> # (except with the right number).;\n'
                                               '>>> time != ...\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False,
                                       "failure_message":"""It looks like you didn't change the cell to define ``time``. Fill in the cell above with the appropriate value for ``time``."""},
                                   {'code': '>>> # Read the text above the question to see what;\n>>> # time should be.;\n>>> round(time, 5) == 1.2\nTrue',
                                        'hidden': False,
                                        'locked': False,
                                        "failure_message":"""The provided value for ``time`` is incorrect. Kindly check the information provided in the previous cell."""},
                                   {   'code': '>>> # Fill in the row;\n'
                                               '>>> #   estimated_distance_m = ...;\n'
                                               '>>> # with something like:;\n'
                                               '>>> #   estimated_distance_m = 4.567;\n'
                                               '>>> # (except with the right number).;\n'
                                               '>>> estimated_distance_m != ...\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False,
                                       "failure_message":"""It looks like you didn't change the cell to define ``estimated_distance_m``. Fill in the cell above with the appropriate value for ``estimated_distance_m``."""},
                                   {'code': '>>> # Note that the units are meters, but the text used;\n>>> # centimeters.;\n>>> (estimated_distance_m != 113) & (estimated_distance_m != ...)\nTrue',
                                        'hidden': False,
                                        'locked': False,
                                        "failure_message":"""Note that the question expects ``estimated_distance_m`` in *meters*. It seems like you specified your answer as the centimeter value provided in the previous cell."""},
                                   {   'code': '>>> # Read the text above the question to see what;\n>>> # estimated_distance_m should be.;\n>>> round(estimated_distance_m, 5) == 1.13\nTrue',
                                       'hidden': False,
                                       'locked': False,
                                        "failure_message":"""The provided value for ``estimated_distance_m`` is incorrect. Kindly check the information provided in the previous cell.""",
                                       "success_message": "The provided answer is correct!"}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
