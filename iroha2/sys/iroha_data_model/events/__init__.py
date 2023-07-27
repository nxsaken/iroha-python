
from ...rust import make_enum, make_struct, make_tuple, get_class, SelfResolvingTypeVar, Dict
import typing
            
Event = make_enum("Event", [("Pipeline", get_class("iroha_data_model.events.pipeline.Event")), ("Data", get_class("iroha_data_model.events.data.events.Event")), ("Time", get_class("iroha_data_model.events.time.Event")), ("ExecuteTrigger", get_class("iroha_data_model.events.execute_trigger.Event"))], typing.Union[get_class("iroha_data_model.events.pipeline.Event"), get_class("iroha_data_model.events.data.events.Event"), get_class("iroha_data_model.events.time.Event"), get_class("iroha_data_model.events.execute_trigger.Event")])

EventPublisherMessage = make_enum("EventPublisherMessage", [("SubscriptionAccepted", get_class(type(None))), ("Event", get_class("iroha_data_model.events.Event"))], typing.Union[get_class(type(None)), get_class("iroha_data_model.events.Event")])

EventSubscriberMessage = make_enum("EventSubscriberMessage", [("SubscriptionRequest", get_class("iroha_data_model.events.FilterBox")), ("EventReceived", get_class(type(None)))], typing.Union[get_class("iroha_data_model.events.FilterBox"), get_class(type(None))])

FilterBox = make_enum("FilterBox", [("Pipeline", get_class("iroha_data_model.events.pipeline.EventFilter")), ("Data", get_class("iroha_data_model.events.data.filters.FilterOpt")), ("Time", get_class("iroha_data_model.events.time.EventFilter")), ("ExecuteTrigger", get_class("iroha_data_model.events.execute_trigger.EventFilter"))], typing.Union[get_class("iroha_data_model.events.pipeline.EventFilter"), get_class("iroha_data_model.events.data.filters.FilterOpt"), get_class("iroha_data_model.events.time.EventFilter"), get_class("iroha_data_model.events.execute_trigger.EventFilter")])

VersionedEventPublisherMessage = make_enum("VersionedEventPublisherMessage", [("V1", get_class("iroha_data_model.events.EventPublisherMessage"))], typing.Union[get_class("iroha_data_model.events.EventPublisherMessage")])

VersionedEventSubscriberMessage = make_enum("VersionedEventSubscriberMessage", [("V1", get_class("iroha_data_model.events.EventSubscriberMessage"))], typing.Union[get_class("iroha_data_model.events.EventSubscriberMessage")])

SelfResolvingTypeVar.resolve_all()
