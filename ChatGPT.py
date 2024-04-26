#this is a chatgpt api

#first pip install openai
#then importopenai

import openai

#next we will get the api key from openai
#to get this ai key go on api chatgpt then sign up then make the secret key and it will work
#copy and paste your api key into below
openai.api_key = "get your own code"

#create a function when we ask the ai a question
def chat_with_gpt(prompt):
    #right here we will generate a response
    response = openai.ChatCompletion.create(
        #right here we will give them the model 
        model = "gpt-3.5-turbo",
        #now we will do the messages
        #inside the array we will pass object which role is user and the content is the prompt
        messages = [{"role": "user", "content": prompt}],
    )
    #here we will return the completed response and we want it back to the user and the strip will remove any white space 
    return response.choices[0].message.content.strip()

#now this is our main function
if __name__ == "__main__":
    #we will have a while true here beacause we want the gpt to keep asking us questions so we use a simple while loop
    while True:
        #first ask for the user input
        user_input = input("You: ")
        #here we use a if else statement in case they want to exit the chat
        if user_input.lower() == "exit":
            #if they do exit then we will print goodbye and then break out of it
            print("Goodbye!")
            break

        #or we can also do this up to you:
        """
        if user_input.lower() in ["exit", "quit", "bye"]:
            break
        we can do this because if our response is any of those three it also breaks
        """
        #now we will generate a response from the gpt
        response = chat_with_gpt(user_input)
        #now we will print what it said
        print("Chatbot:", response)
