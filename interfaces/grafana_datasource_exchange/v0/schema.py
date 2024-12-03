from typing import List

from interface_tester.schema_base import DataBagSchema
from pydantic import Json, BaseModel, Field


class GrafanaDatasource(BaseModel):
    type: str = Field(description="Type of the datasource.",
                      examples=['tempo', 'loki', 'prometheus'])
    uid: str = Field(description="Grafana datasource UID, as assigned by Grafana.")


class GrafanaSourceAppData(BaseModel):
    """Application databag model for the requirer side of this interface."""
    datasources: Json[List[GrafanaDatasource]]


class ProviderSchema(DataBagSchema):
    """The schemas for the requirer side of this interface."""
    app: GrafanaSourceAppData


class RequirerSchema(DataBagSchema):
    """The schemas for the provider side of this interface."""
    app: GrafanaSourceAppData
