## Sent Pattern
this is open source project that returns which sentence type the input sentence is. returns which is the subject, verb, object, and adjective so on.
The reason for English interpretation is to develop the ability to read English sentences correctly.


## Quick Start

### Installation
```bash
pip install sent-pattern
```

### Usage

```py
import spacy

nlp = spacy.load("en_core_web_lg")

nlp.add_pipe("span_noun")
nlp.add_pipe("sent_pattern")
text = "he gives me something"

doc = nlp(text)

pattern = doc._.sentpattern
print(pattern) 
# FourthSentencePattern (class)
print(pattern.subject.root)
# he (Token)
print(pattern.verb.root)
# give (Token)
```

#### If you want to know the sentence pattern without using components, we recommend using method directly

```py
import spacy
from sent_pattern import tags

nlp = spacy.load("en_core_web_lg")
text = "he gives me something"
doc = nlp(text)


dep_list = tags.create_dep_list(doc)
lemma_list = tags.create_lemma_list(doc)
elements = tags.create_elements(dep_list, lemma_list)
pattern = tags.create_sent_pattern(elements)

print(pattern.subject.root.text)
# he (string)
print(dep_list)
# {'ROOT': [gives], 'dative': [me], 'dobj': [something], 'nsubj': [he]}
print(pattern.abbreviation)
# "SVOO"
```


### License
Distributed under the terms of the MIT license, "sent-pattern" is free and open source software