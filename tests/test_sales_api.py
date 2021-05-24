import pytest

from fictional.sales.views import SalesViewSet, collection_conf, Sale
from .aux import render_payload
from .factories import ModelFactory, OfficeFactory, VehicleFactory, SalesFactory


pytestmark = [pytest.mark.sales, pytest.mark.api, pytest.mark.django_db]

view = SalesViewSet.as_view(collection_conf)


def test_list(rf):
    SalesFactory()
    request = rf.get("/sales/")
    response = view(request)

    assert response.status_code == 200
    payload = render_payload(response)
    assert len(payload) == 1


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
