OK_FORMAT = True
test = {   'name': 'q1_2',
    'points': 1,
    'suites': [   {   'cases': [   {'code': '>>> mean_based_estimator(np.array([1,2,3])) is not None\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> int(np.round(mean_based_estimator(make_array([1,2,3])))) == 4\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> np.isclose(mean_based_estimate, 122.47058823529412)\nTrue', 'hidden': True, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}