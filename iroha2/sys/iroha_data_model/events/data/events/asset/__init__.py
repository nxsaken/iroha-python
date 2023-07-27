
from ......rust import make_enum, make_struct, make_tuple, get_class, SelfResolvingTypeVar, Dict
import typing
            
AssetDefinitionEvent = make_enum("AssetDefinitionEvent", [("Created", get_class("iroha_data_model.asset.DefinitionId")), ("MintabilityChanged", get_class("iroha_data_model.asset.DefinitionId")), ("Deleted", get_class("iroha_data_model.asset.DefinitionId")), ("MetadataInserted", get_class("iroha_data_model.asset.DefinitionId")), ("MetadataRemoved", get_class("iroha_data_model.asset.DefinitionId"))], typing.Union[get_class("iroha_data_model.asset.DefinitionId"), get_class("iroha_data_model.asset.DefinitionId"), get_class("iroha_data_model.asset.DefinitionId"), get_class("iroha_data_model.asset.DefinitionId"), get_class("iroha_data_model.asset.DefinitionId")])

AssetDefinitionEventFilter = make_enum("AssetDefinitionEventFilter", [("ByCreated", get_class(type(None))), ("ByMintabilityChanged", get_class(type(None))), ("ByDeleted", get_class(type(None))), ("ByMetadataInserted", get_class(type(None))), ("ByMetadataRemoved", get_class(type(None)))], typing.Union[get_class(type(None)), get_class(type(None)), get_class(type(None)), get_class(type(None)), get_class(type(None))])

AssetDefinitionFilter = make_struct("AssetDefinitionFilter", [("origin_filter", "iroha_data_model.events.data.filters.FilterOpt"), ("event_filter", "iroha_data_model.events.data.filters.FilterOpt")])

AssetEvent = make_enum("AssetEvent", [("Created", get_class("iroha_data_model.asset.Id")), ("Deleted", get_class("iroha_data_model.asset.Id")), ("Added", get_class("iroha_data_model.asset.Id")), ("Removed", get_class("iroha_data_model.asset.Id")), ("MetadataInserted", get_class("iroha_data_model.asset.Id")), ("MetadataRemoved", get_class("iroha_data_model.asset.Id"))], typing.Union[get_class("iroha_data_model.asset.Id"), get_class("iroha_data_model.asset.Id"), get_class("iroha_data_model.asset.Id"), get_class("iroha_data_model.asset.Id"), get_class("iroha_data_model.asset.Id"), get_class("iroha_data_model.asset.Id")])

AssetEventFilter = make_enum("AssetEventFilter", [("ByCreated", get_class(type(None))), ("ByDeleted", get_class(type(None))), ("ByAdded", get_class(type(None))), ("ByRemoved", get_class(type(None))), ("ByMetadataInserted", get_class(type(None))), ("ByMetadataRemoved", get_class(type(None)))], typing.Union[get_class(type(None)), get_class(type(None)), get_class(type(None)), get_class(type(None)), get_class(type(None)), get_class(type(None))])

AssetFilter = make_struct("AssetFilter", [("origin_filter", "iroha_data_model.events.data.filters.FilterOpt"), ("event_filter", "iroha_data_model.events.data.filters.FilterOpt")])

SelfResolvingTypeVar.resolve_all()
