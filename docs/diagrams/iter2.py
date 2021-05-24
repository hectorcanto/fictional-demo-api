from pathlib import Path

from diagrams import Diagram, Edge, Cluster
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS, Dynamodb
from diagrams.aws.security import Cognito
from diagrams.aws.network import APIGateway


BASE_DIR = Path(__file__).resolve().parent


with Diagram("Fictional Motor Co\nDiagram 2",
             filename=str(BASE_DIR / "architecture2"),
             show=False, direction="BT", outformat="png",
             graph_attr=dict(labelloc="t", curvestyles="ortho")):

    gw = APIGateway("API GW")
    gw << Cognito("Auth")

    with Cluster("", graph_attr=dict(pencolor="#FFFFFF", bgcolor=None)):

        with Cluster("Core", direction="BT"):
            backend = EC2("Core backend")

            with Cluster("Operational DB cluster", direction="LR") as db:
                units = [
                    RDS("master RW"), RDS("read\nreplica 1"), RDS("read\nreplica 2")
                    ]
            units << Edge() >> backend << Edge(label="/models\n/sales") << gw

        with Cluster("SalesWindow µs", direction="BT"):
            be2 = EC2("BE")
            dynamo = Dynamodb("Sales\nTimeSeries")
            dynamo << Edge() >> be2 << Edge(label="/model/<pk>/sales") << gw

        # backend - Edge(label="materialize", style="dashed") - be2
