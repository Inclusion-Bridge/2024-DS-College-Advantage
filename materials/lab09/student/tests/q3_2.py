OK_FORMAT = True
test = {   'name': 'q3_2',
    'points': 1,
    'suites': [   {   'cases': [   {'code': ">>> set(faithful_predictions.labels) == set(['duration', 'wait', 'predicted wait'])\nTrue", 'hidden': False, 'locked': False,
                                    "failure_message":"""Incorrect: Check the labels in the `faithful_predictions` column. Ensure that they align with the requirements of question 3.2""",},
                                   {'code': '>>> abs(1 - np.mean(faithful_predictions.column(2))/100) <= 0.35\nTrue', 'hidden': False, 'locked': False,
                                    "failure_message":"""The value of `faithful_predictions` is incorrect!""",
                                     "success_message":"""All answers provided are correct!"""}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
