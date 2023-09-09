OK_FORMAT = True
test = {   'name': 'q24',
    'points': 1,
    'suites': [   {   'cases': [   {'code': '>>> convert_pay_string_to_number("$100 ") == 100000000.0\nTrue', 'hidden': False, 'locked': False,
                                    "failure_message":"""Check your ``convert_pay_string_to_number`` function again. The function you defined fails case:\n/
                                    >>> convert_pay_string_to_number("$100 ")"""},
                                   {'code': '>>> convert_pay_string_to_number("$23 ") == 23000000.0\nTrue', 'hidden': False, 'locked': False,
                                    "success_message":"""All answers provided are correct!"""}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
