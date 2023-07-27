
from ...rust import make_enum, make_struct, make_tuple, get_class, SelfResolvingTypeVar, Dict
import typing
            
PredicateBox = make_enum("PredicateBox", [("And", get_class(list)), ("Or", get_class(list)), ("Not", get_class("iroha_data_model.predicate.PredicateBox")), ("Raw", get_class("iroha_data_model.predicate.value.Predicate"))], typing.Union[get_class(list), get_class(list), get_class("iroha_data_model.predicate.PredicateBox"), get_class("iroha_data_model.predicate.value.Predicate")])

SelfResolvingTypeVar.resolve_all()
