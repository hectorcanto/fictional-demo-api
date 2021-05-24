import json


def render_payload(response):
    response.render()
    return json.loads(response.rendered_content)
