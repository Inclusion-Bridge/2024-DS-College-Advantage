OK_FORMAT = True
test = {   'name': 'q3_1_2',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': ">>> # It looks like you didn't give anything the name;\n"
                                               ">>> # seconds_in_a_decade. Maybe there's a typo, or maybe you ;\n"
                                               '>>> # just need to run the cell below Question 3.2 where you defined ;\n'
                                               '>>> # seconds_in_a_decade. Click that cell and then click the "run;\n'
                                               '>>> # cell" button in the menu bar above.);\n'
                                               ">>> 'seconds_in_a_decade' in vars()\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False,
                                       "failure_message":"""It looks like you didn't give anything the name: ``seconds_in_a_decade``.\n Maybe there's a typo, or maybe you\
                                        just need to run the cell below Question 3.2 where you defined ``seconds_in_a_decade``.\n Click that cell and then click the "run\
                                            cell" button in the menu bar above."""},
                                   {   'code': ">>> # It looks like you didn't change the cell to define;\n"
                                               '>>> # seconds_in_a_decade appropriately.  It should be a number,;\n'
                                               ">>> # computed using Python's arithmetic.  For example, this is;\n"
                                               '>>> # almost right:;\n'
                                               '>>> #   seconds_in_a_decade = 10*365*24*60*60;\n'
                                               '>>> seconds_in_a_decade != ...\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False,
                                       "failure_message":"""It looks like you didn't change the cell to define ``seconds_in_a_decade``. It should be a number,\
                                        computed using Python's arithmetic.  For example, this is almost right:\n ``seconds_in_a_decade = 10*365*24*60*60.``"""},
                                   {   'code': ">>> # It looks like you didn't account for leap years.;\n"
                                               '>>> # There were 2 leap years and 8 non-leap years in this period.;\n'
                                               '>>> # Leap years have 366 days instead of 365.;\n'
                                               '>>> (seconds_in_a_decade != 315360000) & (seconds_in_a_decade != ...)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False,
                                       "failure_message":"""It looks like you didn't account for leap years.\n There were 2 leap years and 8 non-leap years in this period. \
                                         Leap years have 366 days instead of 365.For example, this is almost right:\n ``seconds_in_a_decade = 10*365*24*60*60.``"""},
                                 {   'code': '>>> seconds_in_a_decade == 315532800\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False,
                                       "failure_message":"""The provided value for ``seconds_in_a_decade`` is incorrect. Kindly check the information provided in the previous cell.""",
                                       "success_message": "The provided answer is correct!"}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
