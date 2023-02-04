## Sent Pattern
This package categorizes English sentences into one of five basic sentence patterns and identifies the subject, verb, object, and other components. The five basic sentence patterns are based on C. T. Onions's Advanced English Syntax and are frequently used when teaching English in Japan.<br>
[Influence of His Grammar on English Language Education in Japan ](https://www.intcul.tohoku.ac.jp/ronshu/vol17/12.pdf)
#### [Universe Project](https://spacy.io/universe/project/sent-pattern)

## Quick Start
### [fastapi docker Example Code](./examples/docker_poetry_fastapi/)

## How To Use

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



## Cases without pipeline
If you want to know the sentence pattern without using components, we recommend using method of tags module.
The following three methods must be followed in order.
 `create_dep_list`, `create_elements`, `create_sent_pattern`.
execute in order to generate the sentpattern class.<br>
**merit**: can get sentpattern type


```py
import spacy
from sent_pattern import tags
nlp = spacy.load("en_core_web_lg")
doc = nlp("he gives me something")
dep_list = tags.create_dep_list(doc)
elements  = tags.create_elements(dep_list=dep_list)
p  = tags.create_sent_pattern(elements=elements)
pattern = p.pattern_type
# FourthSentencePattern(class)
print(pattern.subject.root.text)
# he (string)
print(pattern.verb.root)
# gives(spacy.Token)
print(dep_list)
# {'ROOT': [gives], 'dative': [me], 'dobj': [something], 'nsubj': [he]}
print(pattern.abbreviation)
# SVO (str)

```

how to get prep phrase
```py
nlp = spacy.load("en_core_web_lg")

text = "The Eureka client handles all aspects of service instance registration and deregistration"
doc =  nlp(text)
dep_list = tags.create_dep_list(doc)
custom = ElementsFactory.make_custom_elements(dep_list, doc=doc, option="prep")
phrase = custom.option

print(phrase.prep_groups)
# [of service instance registration and deregistration]
```


### License
Distributed under the terms of the MIT license, "sent-pattern" is free and open source software


