import allure
import pytest


# Тестирование

@allure.id("Low_cost")
def test_lowcost_status_code(resp):
    response = resp.low_cost_com()
    assert response.status_code == 200, f"Status code should be 200, got {response.status_code}"
    assert "success" in response.text, "Response does not contain 'success'"

    json_data = response.json()
    print(json_data['data'])
    assert json_data["success"], "JSON data does not indicate success"


@allure.id("direct")
def test_direct_status_code(resp):
    response = resp.direct_tickets()
    assert response.status_code == 200, f"Status code should be 200, got {response.status_code}"


@allure.id("direct")
def test_direct_response_contains_success(resp):
    response = resp.direct_tickets()
    assert "flight_number" in response.text, "Response does not contain 'flight_number'"


@allure.id("direct")
def test_direct_json_data_success(resp):
    response = resp.direct_tickets()
    json_data = response.json()
    print(json_data['data'])
    assert json_data["success"], "JSON data does not indicate success"