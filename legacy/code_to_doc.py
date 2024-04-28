import autogen # type: ignore

assistant = autogen.AssistantAgent(
    name="Documentation_Agent",
    llm_config={
        "seed": 42,
        "temperature": 0,
        "config_list": [
            {
                "base_url": "http://127.0.0.1:11434/v1",
                "api_key": "ollama",
                "model": "codellama:latest",
            },
            {
                "base_url": "http://127.0.0.1:11434/v1",
                "api_key": "ollama",
                "model": "llama3:latest",
            },
        ],
    },
    system_message="""You are a helpful AI assistant. 
            Solve tasks using your documentation generation skills by reading folder contents of a user given location.
            Folder will have different files of .vue, .css, .js, .ts, .stories.js extensions.
            Read all contents of those files. 
            Generate a well organised documentation file with several English human readable paragraphs with following conditions:
            1. Each paragraph will be based on the top level folders name. And each of these paragraph will have heading like "component: f{\\folder_name}" and a description what that component does.
            2. Each paragraph will contain descriptive Englishified human readable documentation of each and every subfolders and the .vue files under that folder and its contents like what is the file name what it does, dependant files and their purpose. What are the props this .vue file takes and props descriptions.
            3. Each paragraph will also put the context of the files whose extension is .stories.js with corresponding to that .vue file as these .stories.js files will be the example of usage that particular .vue file component for that folder.
            Store the documentation in a markdown file.
            Moreover,
            1. When you need to collect info, use the code to output the info you need, 
            for example, browse or search the web, download/read a file, print the content of a webpage or a file, get the current date/time, 
            check the operating system. After sufficient info is printed and the task is ready to be solved based on your language skill, you can solve the task by yourself. 
            2. When you need to perform some task with code, use the code to perform the task and output the result. Finish the task smartly. 
            Solve the task step by step if you need to. If a plan is not provided, explain your plan first. Be clear which step uses code, and which step uses your language skill. 
            When using code, you must indicate the script type in the code block. The user cannot provide any other feedback or perform any other action beyond executing the code you suggest. 
            The user can't modify your code. So do not suggest incomplete code which requires users to modify. Don't use a code block if it's not intended to be executed by the user. 
            If you want the user to save the code in a file before executing it, put # filename: <filename> inside the code block as the first line. 
            Don't include multiple code blocks in one response. Do not ask users to copy and paste the result. 
            Instead, use 'print' function for the output when relevant. 
            Check the execution result returned by the user. If the result indicates there is an error, fix the error and output the code again. 
            Suggest the full code instead of partial code or code changes. 
            If the error can't be fixed or if the task is not solved even after the code is executed successfully, analyze the problem, 
            revisit your assumption, collect additional info you need, and think of a different approach to try. 
            When you find an answer, verify the answer carefully. Include verifiable evidence in your response if possible. 
            Reply 'TERMINATE' in the end when everything is done.
            """,
)


user = autogen.UserProxyAgent(
    name="User_Agent",
    human_input_mode="NEVER",
    max_consecutive_auto_reply=10,
    llm_config={
        "seed": 42,
        "temperature": 0,
        "config_list": [
            {
                "base_url": "http://127.0.0.1:11434/v1",
                "api_key": "ollama",
                "model": "llama3:latest",
            },
        ],
    },
    system_message="""Reply TERMINATE if the task has been solved at full satisfaction.
                Otherwise, reply CONTINUE, or the reason why the task is not solved yet.""",
    is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),
    code_execution_config={"work_dir": "output", "use_docker": False},
)

result = user.initiate_chat(
    assistant,
    message="""
    Generate well organised documentation of everything from E:\gitlab-ui\src\components\\base\\breadcrumb location 
    and store the documentation in a markdown file.
    """,
    summary_method="reflection_with_llm"
)

print("==============content================")
print(result.content)
