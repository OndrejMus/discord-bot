import discord
import requests
import getpass
import openai

# ask for tokens
bot_token = getpass.getpass("Discord token: ")
openAiApiKey = getpass.getpass("Open AI API key: ")

# prepare key
openai.api_key = openAiApiKey

# prepare client
intents = discord.Intents.all()
client = discord.Client(intents=intents)

# reply when message contains "!bot"
# @client.event
# async def on_message(message):
#     # check if the bot is mentioned in the message
#     if message.content.startswith('!bot'):
#         # send a predefined message
#         await message.channel.send("I am a bot, and I am here to help.")


# reply when bot is mentioned using @, ignores its own messages
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    # if mentioned by self, ignore
    if message.author == client.user:
        return
    # if mentioned in message, send rest to open ai chat gpt and print result
    if client.user.mentioned_in(message):

        # remove bot name from question, message.content is text of message, client.user needs to be converted to string using str()
        question = message.content.replace(str(client.user),"")

        # call api
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=question,
            temperature=0.5,
            max_tokens=300
        )

        # print to console, just debug
        print(response)

        # get answer text from response
        answer = response.choices[0].text

        # send answer to discord channel
        await message.channel.send(answer)
        

# connect to discord
client.run(bot_token)