OK_FORMAT = True
test = {   'name': 'q1_2',
    'points': 1,
    'suites': [   {   'cases': [   {'code': '>>> sum(standard_units(make_array(1,2,3,4,5))) == 0\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> np.isclose(standard_units(make_array(1,2,3,4,5))[0], -1.41421356)\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> sum(standard_units(make_array(-3,-2,1,0,1,2,3))) == 0\nTrue', 'hidden': True, 'locked': False},
                                   {'code': '>>> np.isclose(standard_units(make_array(-3,-2,1,0,1,2,3))[0], -1.65988202)\nTrue', 'hidden': True, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
