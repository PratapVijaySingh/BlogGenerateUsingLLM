import streamlit as streamlit
from langchain.prompts import PromptTemplate

from langchain_community.llms import CTransformers

#method to get response from llama2 model 
def getLLamaRes(input_text,no_words,blog_style):
    ##call local model
    llm=CTransformers(model='models/llama-2-7b-chat.ggmlv3.q8_0.bin',
    model_type='llama',
    config={'max_new_tokens':256,'temperature':0.01} )

    ##write prompt template
    template="""
    Write a blog for {blog_style} job profile for a topic {input_text} within  {no_words} words.
    """
    prompt=PromptTemplate(input_variables=["blog_style","input_text",'no_words'],template=template)
    ## get response
    response=llm(prompt.format(blog_style=blog_style,input_text=input_text,no_words=no_words))
    print(response)
    return response
streamlit.set_page_config(page_title="vijay",
page_icon='',
layout='centered',
initial_sidebar_state='collapsed')
streamlit.header("generate blogs ")
input_text=streamlit.text_input("enter the blog topic")

##additional fields

col1,col2=streamlit.columns([5,5])
with col1:
    no_words=streamlit.text_input('No of words')
with col2:
    blog_style=streamlit.selectbox('Writing the blog for',('DataScientist','Individuals'),index=0)
submit=streamlit.button("Generate")

if submit:
    streamlit.write(getLLamaRes(input_text,no_words,blog_style))
