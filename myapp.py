import streamlit as st 
from gensim.summarization import summarize
from sumy.summarizers.lex_rank import LexRankSummarizer
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
import os
import spacy


def sumy(docx):
	parser = PlaintextParser.from_string(docx,Tokenizer("english"))
	lex_summarizer = LexRankSummarizer()
	summary = lex_summarizer(parser.document,3)
	summary_list = [str(sentence) for sentence in summary]
	result = ' '.join(summary_list)
	return result


def entity_analyzer(my_text):
	nlp = spacy.load('en')
	docx = nlp(my_text)
	tokens = [ token.text for token in docx]
	entities = [(entity.text,entity.label_)for entity in docx.ents]
	allData = ['"Token":{},\n"Entities":{}'.format(tokens,entities)]
	return allData
    
def main():
    st.title("Entity Extractor")
    st.subheader("Built by Muhammed Salih")
    

    st.subheader("Analyze Your Text")

    message = st.text_area("Enter Text","Type Here ..")
    if st.button("Extract"):
        entity_result = entity_analyzer(message)
        st.json(entity_result)

if __name__ == '__main__':
		main()
