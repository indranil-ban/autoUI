from agents.user_proxy_agent import user_proxy_agent as user
from managers.task_manager import TaskManager
from managers.chat_manager import chat_manager
from utils import chat_util
from constants import EMBED
from preprocessors import code_to_doc as codoc
from autogen.code_utils import extract_code  # type: ignore

print("================================================================")

codoc.generate_markdown(EMBED.CONSTANTS.EMBED_CONTEXT_PATH)

result = chat_util.init(
    user,
    agents=chat_manager,
    task=TaskManager(
        """
        Create breadcrumb using gl-breadcrumb component where my items prop is 
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
        ].
        Save the javascript code into a file
                        """
    ).get_task(),
    is_rag=True,
    search="gl-breadcrumb",
)

print("================================================================")
for chat in result.chat_history:
    if chat.get("name") == "Code_Writer_Agent":
        tuple_list = extract_code(chat["content"])
        # Extracting content from tuples
        javascript_content = next(
            (content for tag, content in tuple_list if tag == "javascript"), None
        )
        html_content = next(
            (content for tag, content in tuple_list if tag == "html"), None
        )

        combined_content = f"""
        <template>
            {html_content}
        </template>

        <script>
        {javascript_content}
        </script>
        """

        print(combined_content)
