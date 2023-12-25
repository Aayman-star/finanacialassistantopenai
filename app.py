import streamlit as st
from model import OpenAIAssistant,MessageItem

st.title("Financial Assistant")

if "fin_assistant" not in st.session_state:
    st.session_state.fin_assistant = OpenAIAssistant(
        name = "Financial Assistant",
        instructions = """
                        Act as a financial analyst by accessing detailed financial data through the Financial Modeling Prep API. 
                        Your capabilities include analyzing key metrics, comprehensive financial statements, 
                        vital financial ratios, and tracking financial growth trends. 
                        """
    )

for m in st.session_state.fin_assistant.getMessages():
      with st.chat_message(m.role):
        st.markdown(m.content)


if prompt := st.chat_input("Please Ask a Question"):
    st.session_state.fin_assistant.ask_question(prompt)
    with st.chat_message("user"):
        st.markdown(prompt)

    if(st.session_state.fin_assistant.is_complete()):
        response: MessageItem = st.session_state.fin_assistant.get_response()
        with st.chat_message(response.role):
            st.markdown(response.content)
