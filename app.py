from preprocessors import code_to_doc as codoc
from constants import EMBED
print("================================================================")

codoc.generate_markdown(EMBED.CONSTANTS.EMBED_CONTEXT_PATH, EMBED.CONSTANTS.EMBED_CONTEXT_OUTPUT_PATH)


from agents.user_proxy_agent import user_proxy_agent as user
from managers.task_manager import TaskManager
from managers.chat_manager import chat_manager
from utils import chat_util
from autogen.code_utils import extract_code  # type: ignore

result = chat_util.init(
    user,
    agents=chat_manager,
    task=TaskManager(
        """
        create table using gl-table component where items are [{"column_one":"test","col_2":"ABC","col_three":1234},{"column_one":"test2","col_2":"DEF","col_three":5678},{"column_one":"test3","col_2":"GHI","col_three":9101}], fields are 
        [{"key":"column_one","label":"First column","variant":"secondary","sortable":true,"isRowHeader":false},{"key":"col_2","label":"Second column"},{"key":"col_three","sortable":true,"label":"Third column","thClass":"gl-text-right","tdClass":"gl-text-right"}], selected variant is primary, sort direction is desc and sort by col_three. Keep other props with default value
        """
    ).get_task(),
    is_rag=True,
    search="gl-table",
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
