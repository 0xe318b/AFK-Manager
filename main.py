import pymongo,disnake
from disnake.ext import commands

# Connect to the MongoDB instance
MONGO = pymongo.MongoClient("")



client = commands.Bot(command_prefix=commands.when_mentioned)


@client.slash_command()
async def afk(inter, reason: str):
    await inter.response.defer(ephemeral=True)
    if not collection.find_one({"UserID": str(str(inter.author.id))}):
        db = MONGO.mydatabase
        collection = db.mycollection

        # Create a document to insert
        document = {
            "UserID": str(inter.author.id),
            "Reason": reason,
        }

        collection.insert_one(document)
        await inter.edit_original_message("You are now afk!")
        return
    await inter.edit_original_message("You are already afk!")

# Message event handler
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    db = MONGO.mydatabase
    collection = db.mycollection
    if collection.find_one({"UserID": str(message.author.id)}):
        collection.delete_many({"UserID": str(message.author.id)})

        await message.reply("You are no longer afk!")
    for user in message.mentions:
        if collection.find_one({"UserID": str(user.id)}):
            await message.reply(f"{user.mention} is AFK and may not be able to respond to your message.")

@client.event
async def on_ready():
    print("---------")
    print("Ready!")
    print("Username: ", client.user.name)
    print("ID: ", client.user.id)
    print("---------")


client.run("")
