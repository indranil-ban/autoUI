
from agents.user_proxy_agent import user_proxy_agent as user
from managers.task_manager import TaskManager
from managers.chat_manager import chat_manager


result = user.initiate_chat(
    chat_manager,
    message=TaskManager(
        """Access the repository url https://gitlab.com/gitlab-org/gitlab-ui. 
        It does not required username or password.
        Give me vue js code by using gl-breadcrumb component where my items prop is 
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
    summary_method="reflection_with_llm"
)
print(result.summary)
