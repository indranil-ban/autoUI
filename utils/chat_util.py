from constants import CHAT

def init(proxy, agents, task=None, is_rag=False, search=None):
    message= proxy.message_generator if is_rag else task
    problem=task if is_rag else None
    return proxy.initiate_chat(
        agents,
        message=message,
        problem=problem,
        summary_method=CHAT.CONSTANTS.SUMMARY_METHOD,
        search_string=search
    )
    