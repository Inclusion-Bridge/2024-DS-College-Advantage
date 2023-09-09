OK_FORMAT = True
test = {   'name': 'q3_3_2',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> # Fill in the line that currently says;\n>>> #   predicted_distance_m = ...;\n>>> # in the cell above.;\n>>> predicted_distance_m != ...\nTrue',
                                       'hidden': False,
                                       'locked': False,
                                       "failure_message":"""It looks like you didn't change the cell to define ``predicted_distance_m``. Fill in the line that currently says;\n>>> #   predicted_distance_m = ...;\n."""},
                                   {   'code': '>>> # Compute predicted_distance_m using the formula in the text;\n'
                                               '>>> # above.  Hint: it should start with something like this:;\n'
                                               '>>> #   predicted_distance_m = (1/2) * gravity_constant ...;\n'
                                               '>>> round(predicted_distance_m, 5) == 1.17022\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False,
                                       "failure_message":"""The value of ``predicted_distance_m`` resulting from your solution is incorrect."""},
                                   {'code': '>>> round(difference, 5)  == 0.04022\nTrue', 'hidden': False, 'locked': False,
                                    "failure_message":"""The value of ``difference`` resulting from your solution is incorrect.""",
                                    "success_message":"""All answers provided are correct!"""}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
