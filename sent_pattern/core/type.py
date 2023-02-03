from typing import TypeAlias, Dict, List, Optional,Union
from spacy.tokens import Token

DepLemmaListType: TypeAlias = Dict[str, List[Optional[Token]]]
AdjectiveSpanType: TypeAlias = Optional[List[Token]]
AdjectiveSpanStrType: TypeAlias = Optional[str]
AdjectiveRootType: TypeAlias = Union[Token, str]
SubjectSpanType: TypeAlias = List[Token]
SubjectRootType: TypeAlias = Token
ObjectRootType: TypeAlias = List[Optional[Token]]
ObjectSpanType: TypeAlias = Optional[List[Union[List[Token], Token]]]
