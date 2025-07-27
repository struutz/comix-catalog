import strawberry
from strawberry.fastapi import GraphQLRouter

from app.interface.graphql.queries import Query
from app.interface.graphql.mutations import Mutation

schema = strawberry.Schema(query=Query, mutation=Mutation)
graphql_app = GraphQLRouter(schema)
