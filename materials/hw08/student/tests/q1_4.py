OK_FORMAT = True
test = {   'name': 'q1_4',
    'points': 1,
    'suites': [   {   'cases': [{'code': '>>> type(one_resampled_difference(votes)) in set([float, np.float64])\nTrue', 'hidden': False, 'locked': False},
                                {'code': ">>> votes = Table.read_table('votes.csv');\n>>> np.random.seed(123);\n>>> -6 <= float(one_resampled_difference(votes)) <= 15\nTrue", 'hidden': False, 'locked': False,
                                "failure_message":"""The ``one_resampled_difference`` function you defined is incorrect. Kindly check the information provided in the function description to make sure you are using the right formula.""",
                                "success_message": "The ``one_resampled_difference`` function is correct!"}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}