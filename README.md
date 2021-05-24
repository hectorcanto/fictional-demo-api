# Fictional Motor CO system

In this document we will explain how to setup the project and work with it.

- Set up the Docker environment
- Launch the backend
- Make API calls using Postman
- Launch tests per type (unitary and non=unitary)

Also, we will introduce the ___ documentation we've build for this project

For the implementation we will combine:
- API Model View Controller (MVC) (or MVVM Model View ViewModel)
  - Where Views are the endpoints 
- HTTP REST, especially
  - We also consider HATEOAS, #TODO json:api hyperlink 
    but we will not implement a Level 4 maturity REST API for this prototype
- Domain Driven Design to some degree, it is not advisable to _fight_ the framework architecture, but
  we will split some `domain` and `infrastructure` out of the framework artifacts that are bound to be
  separated in to transversal code - specifications, common constants and libraries
  
## Structure

.
├── config: general configuration, Django settings and urls config
├── docs
│   └── diagrams
├── fictional: Django project with each context
|   ├── core
│   ├── domain
│   ├── infra
│   ├── sales
│   ├── users
│   └── vehicles
├── scripts: scripts to set up the system
├── staticfiles
└── tests: Unitary and API test


## Setup

1. Create a virtualenv
1. Install the dependencies
```bash
pip install -r requirments
```

## Launch test

```bash
pytest
```

It should prompt code coverage and test resulta

## Documentation

Further information will be in the folder `docs` including:

- [Domain research](docs/domain_resarch.md)
- [Api design](docs/api_design.md)
- [Architecture description](docs/architecture.md)
- [Architecture decisions](docs/adr/)
- [Implementation details](docs/process.md)

## Future work

This being a prototype, it lacks a lot of features that are advisable, both on the architecture and microcode side.
To list a few:
- Add Authenticantion
  
- Add Django-Admin, to have a nice backoffice
- Use a Filter Backend for query_params
- Add cache
- Add a JSON:API renderer

## References

Here are the reference I used the most

- [Django docs](https://docs.djangoproject.com/en/3.2/ref/)
- [Django Rest Framework](https://www.django-rest-framework.org)
- [pytest documentation](https://docs.pytest.org/en/6.2.x/contents.html)
- [Factory Boy documentation](https://factoryboy.readthedocs.io/en/stable/index.html)
- [Architecture Decission Records template](https://gist.github.com/hectorcanto/1276e41fc24e8c4ee1427cd5d02bf82a#file-adr-template-md)


### Diagrams

- [Diagrams library docs](https://diagrams.mingrammer.com/)
- [AWS components](https://diagrams.mingrammer.com/docs/nodes/aws)