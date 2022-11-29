import alerter

from pytest import MonkeyPatch
from alerter import alert_in_celcius, alert_failure_count, network_alert
from alerter_constants import alert_threshold_in_celcius



def nertwork_alert_stub(temperature_reading_in_celcius):
    if temperature_reading_in_celcius > alert_threshold_in_celcius:
        return 500
    return 200
    

def test_alert_in_celcius(monkeypatch):
    monkeypatch.setattr(alerter, "network_alert", nertwork_alert_stub)

    alert_in_celcius(100)
    assert(alert_failure_count == 0)

    alert_in_celcius(500)
    assert(alert_failure_count == 1)