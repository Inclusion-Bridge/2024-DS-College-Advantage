OK_FORMAT = True
test = {   'name': 'q14',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> # One or more of the reaction results could be incorrect;;\n'
                                               ">>> np.count_nonzero(ten_nachos_reactions.column('Reactions') == make_array('Meh.', 'Cheesy!', 'Wow!', 'Wow!', 'Cheesy!', 'Spicy!', 'Wow!', 'Meh.', "
                                               "'Cheesy!', 'Wow!')) == 10\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False,
                                       "failure_message":"""One or more of the reaction results could be incorrect. Check again!""",
                                    "success_message":"""All answers provided are correct!"""}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
