OK_FORMAT = True
test = {   'name': 'q233',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': ">>> # It looks like you're not making an array.  You shouldn't need to;\n"
                                               '>>> # use .item anywhere in your solution.;\n'
                                               '>>> type(more_total_charges) == np.ndarray\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False,
                                       "failure_message":""""The data type for ``more_total_charges`` is incorrect. It looks like you're not making an array.  You shouldn't need to use `.item` anywhere in your solution."""},
                                   {   'code': ">>> # You made an array, but it doesn't have the right numbers in it.;\n>>> sum(abs(more_total_charges - 1.2 * more_restaurant_bills)) < 1e-6\nTrue",
                                       'hidden': False,
                                       'locked': False,
                                       "failure_message":""""The provided answer for ``more_total_charges`` is incorrect. You made an array, but it doesn't have the right numbers in it.""",
                                                            "success_message":"""All answers provided are correct!"""}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
