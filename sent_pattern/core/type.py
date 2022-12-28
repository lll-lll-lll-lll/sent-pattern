from typing import TypeAlias, Dict, List, Optional
from spacy.tokens import Token

DepLemmaListType: TypeAlias = Dict[str, List[Optional[Token]]]
