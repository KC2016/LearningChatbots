bot_template = "BOT : {0}"
user_template = "USER : {0}"

# Define a function that responds to a user's message: respond
def respond(message):
    # Concatenate the user's message to the end of a standard bot respone
    bot_message = 'I can hear you! You said: ' + message
    # Return the result
    return bot_message

# Test function
print(respond("hello!"))

# EchoBot II
# Having written your respond() function, you'll now define a function called send_message() with a single parameter message which logs the message and the bot's response.

# Instructions
# 100 XP
# Use the user_template string's .format() method to include the user's message into the user template, and print the result.
# Call the respond() function with the message passed in and save the result as response.
# Log the bot's response using the bot_template string's .format() method.
# Send the message "hello" to the bot.


# Create templates
bot_template = "BOT : {0}"
user_template = "USER : {0}"

# Define a function that sends a message to the bot: send_message
def send_message(message):
    # Print user_template including the user_message
    print(user_template.format(message))
    # Get the bot's response to the message
    response = respond(message)
    # Print the bot template including the bot's response.
    print(bot_template.format(response))

# Send a message to the bot
send_message("hello")