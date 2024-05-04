
from agents.user_proxy_agent import user_proxy_agent as user
from managers.task_manager import TaskManager
from managers.chat_manager import chat_manager
from utils import chat_util
from constants import EMBED
from preprocessors import code_to_doc as codoc

print("================================================================")

codoc.generate_markdown(EMBED.CONSTANTS.EMBED_CONTEXT_PATH)

result =chat_util.init(user, 
    agents=chat_manager,
    task=TaskManager(
        """
        Give me vue.js code by using gl-breadcrumb component where my items prop is 
        [
            {
                "text": "First item",
                "href": "#",
                "avatarPath": "2f644f9f852c9a6703f3.png"
            },
            {
                "text": "Second item",
                "href": "#"
            },
            {
                "text": "Third item",
                "href": "#",
                "avatarPath": "2853f51cf3def4d20cb1.png"
            },
            {
                "text": "Fourth item",
                "to": {
                "name": "fourth-item"
                }
            }
        ]
                        """
    ).get_task(),
    is_rag=True,
    search="gl-breadcrumb"
)

print("================================================================")
print(result)
