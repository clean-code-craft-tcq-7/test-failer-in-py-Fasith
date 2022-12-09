import alerter

from pytest import MonkeyPatch
from alerter import alert_in_celcius,network_alert
from alerter_constants import alert_threshold_in_celcius


def return_alert_failure_count():
    from alerter import alert_failure_count
    return alert_failure_count

def nertwork_alert_stub(temperature_reading_in_celcius):
    if temperature_reading_in_celcius > alert_threshold_in_celcius:
        print('500')
        return 500
    print('200')
    return 200
    

def test_alert_in_celcius(monkeypatch):
    global alert_failure_count
    monkeypatch.setattr(alerter, "network_alert", nertwork_alert_stub)

    # Below threshold
    alert_in_celcius(100)
    assert(return_alert_failure_count() == 0)

    #At threshold
    alert_in_celcius(212)      
    assert(return_alert_failure_count() == 0)

    #Above threshold
    alert_in_celcius(500)
    assert(return_alert_failure_count() == 1)

    