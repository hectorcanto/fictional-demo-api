from pathlib import Path

from diagrams import Diagram, Edge
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS, Dynamodb
from diagrams.aws.network import APIGateway
from diagrams.aws.security import Cognito

BASE_DIR = Path(__file__).resolve().parent

with Diagram("Fictional Motor Co\nDiagram 1",
             filename=str(BASE_DIR / "architecture1"),
             show=False, direction="BT", outformat="png",
             graph_attr=dict(labelloc="t")):

    db = RDS("Operational DB cluster")
    backend = EC2("Core backend")
    cache = Dynamodb("cache")
    gw = APIGateway("AWS API GW")

    db >> Edge(reverse=True) >> backend << gw << Cognito("Auth")
    backend >> Edge(reverse=True) >> cache
