# talking-assistant-with-openai-api

This project is a talking assistant that uses OpenAI's GPT-3 API to provide natural language processing capabilities. The assistant can understand and respond to text-based queries, making it a powerful tool for a variety of applications.


## Usage

```py
git clone https://github.com/divyansh10100/talking-assistant-with-openai-api.git
cd talking-assistant-with-openai-api
```

Go to the `openai` website to get your personal API token and paste it in the code.
```bash
openai.api_key=<your_api_key>
```
After cloning the repo, install the requirements.
## Install requirements

```bash
pip install -r requirements.txt
```
After the requirements are successfully installed run the code.
```bash
$ python -m assistant.py
#or
$ assistant.py
```
The assistant should now be available to talk to.

To use the assistant, simply speak to the bot, and the assistant will use OpenAI's API to generate a response. The response is then spoken using `playsound` library, allowing for easy interaction and communication. Additionally the text input and output is also visible in the CLI for reference.

The assistant can be customized to suit your needs by adjusting the parameters of the OpenAI API, such as the response length, the language model used, and more. This makes it a flexible tool that can be adapted to a wide range of use cases.

In addition to its natural language processing capabilities, the assistant also includes a variety of features to enhance its functionality. For example, it can provide information on the weather, news, and more, making it a valuable resource for daily use.
