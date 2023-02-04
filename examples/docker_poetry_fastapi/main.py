import spacy
from sent_pattern import tags
from fastapi import FastAPI
from pydantic import BaseModel

nlp = spacy.load("en_core_web_sm")

app = FastAPI()

class SentPatternReq(BaseModel):
    text: str
    
class SentPatternRes(BaseModel):
    pattern: str
    abbreviation: str
    
@app.get("/")
async def ping():
    return {"message": "pong"}

@app.post("/sentpattern")
async def sentpattern(req: SentPatternReq):
    text = req.text
    doc = nlp(text)
    dep_list = tags.create_dep_list(doc)
    elements  = tags.create_elements(dep_list=dep_list)
    p  = tags.create_sent_pattern(elements=elements)
    pattern = p.pattern_type
    return SentPatternRes(pattern=pattern.__class__.__name__, abbreviation=pattern.abbreviation)
    