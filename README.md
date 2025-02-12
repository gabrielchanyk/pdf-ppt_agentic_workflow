# document_searcher_agent

This agent is built to read multiple documents and create a powerpoint template based on the information in the documentations

Setup

1. Install python on workstation
2. Install python dependecies in requirements.txt
   `pip install -r requirements.txt`
3. Create an open ai account and generate a ssh key
4. Ensure you have at the minimum $5 USD in your account

Execution
To execute script use following command:
`python main.py`

Setup to run locally
Install ollama
https://ollama.com/

Pull models that you want to use in this case we are using phi3
https://ollama.com/library/phi3

`ollama pull phi3:3.8b`
`ollama list`

uncomment code for local run
comment code for api run
