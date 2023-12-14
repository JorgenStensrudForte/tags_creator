# openai.api_key = "5a90b85ba420469c9b36438e238d70fe"
# openai.api_base = "https://da-openai-test.openai.azure.com/"  # your endpoint should look like the following https://YOUR_RESOURCE_NAME.openai.azure.com/
# openai.api_type = "azure"
# openai.api_version = "2023-05-15"  # this might change in the future


import os
from openai import OpenAI
from openai import AzureOpenAI


deployment_name = "gpt-4-turbo-1106-preview"  # This will correspond to the custom name you chose for your deployment when you deployed a model.


client = AzureOpenAI(
    azure_endpoint="https://da-openai-test.openai.azure.com/",
    api_key="5a90b85ba420469c9b36438e238d70fe",
    api_version="2023-05-15",
)

chat_completion = client.chat.completions.create(
    model=deployment_name,
    messages=[
        {"role": "system", "content": "You are a helpful assistant. return Json"},
        {"role": "user", "content": start_phrase},
    ],
    response_format={"type": "json_object"},
    temperature=0.1,
    top_p=0.1,
)

print(chat_completion.choices[0].message.content)
