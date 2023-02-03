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


FirstSpanDictType: TypeAlias = Dict[str, Union[Token, List[Token]]]
FirstSpanDictTypeStr: TypeAlias = Dict[str, Optional[str]]


SecondSpanDictType: TypeAlias = Dict[str, List[Optional[Union[Token, str, List[Token]]]]]
SecondSpanDictTypeStr: TypeAlias = Dict[str, Optional[str]]

ThirdSpanDictType: TypeAlias = Dict[str, List[Optional[Union[Token, str, List[Token]]]]]
ThirdSpanDictTypeStr: TypeAlias = Dict[str, Optional[str]]

FourthSpanDictType: TypeAlias = Dict[str, Optional[List[Union[List[Token], Token]]]]
FourthSpanDictTypeStr: TypeAlias = Dict[str, Optional[str]]

FifthSpanDictType: TypeAlias = Dict[str, Optional[List[Union[List[Token], Token]]]]
FifthSpanDictTypeStr: TypeAlias = Dict[str, Optional[str]]