
from ....rust import make_enum, make_struct, make_tuple, get_class, SelfResolvingTypeVar, Dict
import typing
            
BlockPublisherMessage = make_enum("BlockPublisherMessage", [("SubscriptionAccepted", get_class(type(None))), ("Block", get_class("iroha_core.block.VersionedCommittedBlock"))], typing.Union[get_class(type(None)), get_class("iroha_core.block.VersionedCommittedBlock")])

BlockSubscriberMessage = make_enum("BlockSubscriberMessage", [("SubscriptionRequest", get_class(int)), ("BlockReceived", get_class(type(None)))], typing.Union[get_class(int), get_class(type(None))])

VersionedBlockPublisherMessage = make_enum("VersionedBlockPublisherMessage", [("V1", get_class("iroha_core.block.stream.BlockPublisherMessage"))], typing.Union[get_class("iroha_core.block.stream.BlockPublisherMessage")])

VersionedBlockSubscriberMessage = make_enum("VersionedBlockSubscriberMessage", [("V1", get_class("iroha_core.block.stream.BlockSubscriberMessage"))], typing.Union[get_class("iroha_core.block.stream.BlockSubscriberMessage")])

SelfResolvingTypeVar.resolve_all()
