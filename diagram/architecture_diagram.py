# diagram.py
from diagrams import Diagram, Cluster
from diagrams.aws.database import DB
from diagrams.aws.compute import Lambda
from diagrams.aws.general import Client
from diagrams.aws.network import Route53
from diagrams.aws.network import CF
from diagrams.aws.storage import S3
from diagrams.aws.general import User


with Diagram("cameroncarl-resume-website.com", show=True):

    visitor = User("User")

    with Cluster("AWS"):
        func = Lambda("Lambda")
        db = DB("DynamoDB")
        client = Client("Website")
        route = Route53("Route53")
        cf = CF("CloudFront")
        s3 = S3("S3")


        visitor >> client >> route >> cf >> s3
        client >> func >> db >> func >> client
