## Sent Pattern
This package categorizes English sentences into one of five basic sentence patterns and identifies the subject, verb, object, and other components. The five basic sentence patterns are based on C. T. Onions's Advanced English Syntax and are frequently used when teaching English in Japan.<br>
[Influence of His Grammar on English Language Education in Japan ](https://www.intcul.tohoku.ac.jp/ronshu/vol17/12.pdf)

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

### [Universe Project](https://spacy.io/universe/project/sent-pattern)