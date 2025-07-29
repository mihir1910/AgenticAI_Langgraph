from src.langgraphagenticai.state.state import State



class BasicChatBotNode:
    """
    Basic chatbot node
    """
    def __init__(self,model):
        self.llm=model

    def process(self,state:State)->dict:
        """
            Process the state and return the response
        """
        return {"messages":self.llm.invoke(state["messages"])}
