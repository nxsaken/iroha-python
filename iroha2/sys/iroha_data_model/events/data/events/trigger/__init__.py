
from ......rust import make_enum, make_struct, make_tuple, get_class, SelfResolvingTypeVar, Dict
import typing
            
TriggerEvent = make_enum("TriggerEvent", [("Created", get_class("iroha_data_model.trigger.Id")), ("Deleted", get_class("iroha_data_model.trigger.Id")), ("Extended", get_class("iroha_data_model.trigger.Id")), ("Shortened", get_class("iroha_data_model.trigger.Id"))], typing.Union[get_class("iroha_data_model.trigger.Id"), get_class("iroha_data_model.trigger.Id"), get_class("iroha_data_model.trigger.Id"), get_class("iroha_data_model.trigger.Id")])

TriggerEventFilter = make_enum("TriggerEventFilter", [("ByCreated", get_class(type(None))), ("ByDeleted", get_class(type(None))), ("ByExtended", get_class(type(None))), ("ByShortened", get_class(type(None)))], typing.Union[get_class(type(None)), get_class(type(None)), get_class(type(None)), get_class(type(None))])

TriggerFilter = make_struct("TriggerFilter", [("origin_filter", "iroha_data_model.events.data.filters.FilterOpt"), ("event_filter", "iroha_data_model.events.data.filters.FilterOpt")])

SelfResolvingTypeVar.resolve_all()
