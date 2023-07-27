
from ...rust import make_enum, make_struct, make_tuple, get_class, SelfResolvingTypeVar, Dict
import typing
            
BlockHeader = make_struct("BlockHeader", [("timestamp", int), ("consensus_estimation", int), ("height", int), ("previous_block_hash", "iroha_crypto.hash.HashOf"), ("transactions_hash", "iroha_crypto.hash.HashOf"), ("rejected_transactions_hash", "iroha_crypto.hash.HashOf"), ("genesis_topology", "iroha_core.sumeragi.network_topology.Topology")])

CommittedBlock = make_struct("CommittedBlock", [("header", "iroha_core.block.BlockHeader"), ("rejected_transactions", list), ("transactions", list), ("event_recommendations", list), ("signatures", "iroha_crypto.signature.SignaturesOf")])

ValidBlock = make_struct("ValidBlock", [("header", "iroha_core.block.BlockHeader"), ("rejected_transactions", list), ("transactions", list), ("signatures", list), ("event_recommendations", list)])

VersionedCommittedBlock = make_enum("VersionedCommittedBlock", [("V1", get_class("iroha_core.block.CommittedBlock"))], typing.Union[get_class("iroha_core.block.CommittedBlock")])

VersionedValidBlock = make_enum("VersionedValidBlock", [("V1", get_class("iroha_core.block.ValidBlock"))], typing.Union[get_class("iroha_core.block.ValidBlock")])

SelfResolvingTypeVar.resolve_all()
