import pytest

from fictional.vehicles.views import ModelsViewSet, collection_conf, detail_conf
from fictional.vehicles.models import Model
from .aux import render_payload
from .factories import ModelFactory, PartsFactory


pytestmark = [pytest.mark.models, pytest.mark.api, pytest.mark.django_db]

view = ModelsViewSet.as_view(collection_conf)
detail_view = ModelsViewSet.as_view(detail_conf)


@pytest.mark.current
def test_model_list(rf):
    ModelFactory(model_parts=[part.id for part in PartsFactory.create_batch(5)])
    request = rf.get("/models/")
    response = view(request)

    assert response.status_code == 200
    payload = render_payload(response)
    assert len(payload) == 1

    assert len(payload[0]["model_parts"]) == 5, payload


@pytest.mark.current
def test_model_delete(rf):
    model = ModelFactory()

    request = rf.delete("/model/{pk}")
    response = detail_view(request, pk=model.id)

    assert response.status_code == 204
    assert Model.objects.count() == 0
