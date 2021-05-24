from datetime import datetime, timezone

import pytest

from fictional.vehicles.views import ModelSalesView, sales_conf
from .aux import render_payload
from .factories import ModelFactory, SalesFactory

pytestmark = [pytest.mark.sales, pytest.mark.api, pytest.mark.django_db]

view = ModelSalesView.as_view(sales_conf)


@pytest.fixture
def model_sales():
    model = ModelFactory()
    dt1 = datetime(2021, 2, 12, tzinfo=timezone.utc)
    dt2 = datetime(2021, 3, 10, tzinfo=timezone.utc)
    SalesFactory.create_batch(10, created_at=dt1)
    SalesFactory.create_batch(10, created_at=dt2)
    return model


@pytest.mark.current
def test_some_sales_since(rf, model_sales):

    since = "2021/01"
    request = rf.get(f"/models/{model_sales.id}/sales?since={since}&skip=1")
    response = view(request)
    payload = render_payload(response)

    assert response.status_code == 200, payload
    # assert len(payload) == 20
    assert payload["average"] == 4.2
    assert payload["count"] == 20


@pytest.mark.current
def test_some_sales_until(rf, model_sales):

    since = "2021/04"
    request = rf.get(f"/models/{model_sales.id}/sales?until={since}&skip=1")
    response = view(request)
    payload = render_payload(response)

    assert response.status_code == 200, payload
    # assert len(payload) == 20
    assert payload["average"] == 12.5, payload
    assert payload["count"] == 20


@pytest.mark.current
def test_all_model_sales(rf, model_sales):

    request = rf.get(f"/models/{model_sales.id}/sales?skip=1")
    response = view(request)
    payload = render_payload(response)

    assert response.status_code == 200, payload
    # assert len(payload) == 20
    assert payload["average"] == 5.94, payload
    assert payload["count"] == 20


@pytest.mark.parametrize("parameter, value", (
        ("since", "2021-01"),
        ("until", "anything"),
        ("average", "anything"),
))
def test_model_sales_bad_param(rf, parameter, value):
    model = ModelFactory()

    request = rf.get(f"/models/{model.id}/sales?{parameter}={value}")
    response = view(request)
    payload = render_payload(response)
    assert response.status_code == 400, payload



"""
def test_create(rf):
    model = ModelFactory()
    office = OfficeFactory()
    vehicle = VehicleFactory()
    sale_fixture = dict(model_id=model.id, office_id=office.id, vehicle_id=vehicle.chassis_number)

    request = rf.post("/sales/", sale_fixture)
    response = view(request)

    payload = render_payload(response)

    assert response.status_code == 201
    assert Sale.objects.count() == 1
    assert payload["model_id"] == sale_fixture["model_id"]
"""