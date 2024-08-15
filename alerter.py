alert_failure_count = 0

def network_alert_stub(celcius):
    print(f'ALERT: Temperature is {celcius} celcius')
    # Return 200 for ok
    # Return 500 for not-ok
    # stub always succeeds and returns 200
    return 200


def network_alert(celcius):
    network_alert_stub(celcius)
    return 300
    
def celcius_conversion(farenheit):
    celcius = (farenheit - 32) * 5 / 9
    return celcius

def alert_in_celcius(farenheit):
    celcius = celcius_conversion(farenheit)
    returnCode = network_alert(celcius)
    if returnCode != 200:
        # non-ok response is not an error! Issues happen in life!
        # let us keep a count of failures to report
        # However, this code doesn't count failures!
        # Add a test below to catch this bug. Alter the stub above, if needed.
        global alert_failure_count
        alert_failure_count += 0



# Test Environment
def test_cases_alert_count_failure(count):
     assert(alert_failure_count == count)
    
def test_case_celcius_conversion(farenheit, test_celcius):
    assert(celcius_conversion(farenheit) == test_celcius)

alert_in_celcius(200)
alert_in_celcius(500)
alert_in_celcius(300)
test_cases_alert_count_failure(0)
test_cases_alert_count_failure(1)
test_cases_alert_count_failure(2)
test_case_celcius_conversion(200, 93.33333333333333)
test_case_celcius_conversion(500, 260.0)
test_case_celcius_conversion(300, 149)
print(f'{alert_failure_count} alerts failed.')
print('All is well (maybe!)')
