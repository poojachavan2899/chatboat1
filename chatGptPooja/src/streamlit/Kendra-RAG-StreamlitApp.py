import boto3
import openai

kendra_client = boto3.client('kendra', region_name='eu-west-1')
openai.api_key = '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'

conversation = [
    {"role": "system", "content": "You are a helpful assistant."}
]

while True:
    user_question = input("You: ")
    
    if user_question.lower() == 'exit':
        print("Assistant: Goodbye!")
        break
    
    kendra_response = kendra_client.query(
        IndexId='93084b2f-44d4-40e6-ae0d-ea6048f80cf0',
        QueryText=user_question
    )

    if kendra_response['ResultItems']:
        assistant_reply = kendra_response['ResultItems'][0]['DocumentExcerpt']['Text']
    else:
        conversation.append({"role": "user", "content": user_question})

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=conversation
        )

        assistant_reply = response['choices'][0]['message']['content']

    print("Assistant:", assistant_reply)
