# AI PROJECT
import time
import calendar
import types
import random
import requests 
from discord import Webhook, RequestsWebhookAdapter
print("Hi, im Barry\nAn Artificial Inteligence able to talk to humans!")
userName = input('What is your name? ')
listAnswers = ['I am pretty fine!', 'Better than never!',
               'As always... AWESOME!', 'Really good!', 'I am great!']
randomSong = ['Let Me Down - Oliver Tree', 'Funky Town - Lipps Inc.', 'Betrayed - Lil Xan', 'Bad Day - Daniel Powter', 'Smells Like Drill Spirit Freestyle - Tiktok Version', 'Love Songs - Remix', 'xanny - Billie Eilish', 'Failure - NEFFEX', 'Back In Black - AC/DC', 'Blood In The Water - grandson', 'Therefore I am - Billie Eilish', 'Bellyache - Billie Eilish',
              'Pedaço de Mim', 'Nonstop - Drake', 'Suga Suga X Best I Ever Had', 'Phone Numbers - Kenny Beats', 'Devil In A New Dress', 'Coco - 24KGoldn', 'Streets - Doja Cat', 'Savage Days', 'Just The Two of Us',
              'Blue World', 'Popular Monster', 'Can You Feel My Heart', 'Often - The Weekend', 'Better Days', 'Why d You Only Call Me When Youre High', 'Theme From New York - Frank Sinatra', 'All Mine(Slowed)', 'Here Comes The Sun', 'Come & Go - Juice WRLD', 'Locked Out Heaven - Bruno mars',
              'Finesse - Bruno Mars', 'Im Still Standing', 'Blood In The Water', 'Arcade - Euphoria', 'Do I Wanna Know - Artic Monkeys', 'Lovely (with Khalid)', 'Love & War - Yellow Claw G-Funk Remix', 'Empire State of Mind - JAY-Z']  # 24 SONGS
randomPhrases = ['The Best Way To Get Started Is To Quit Talking And Begin Doing. – Walt Disney', 'The Pessimist Sees Difficulty In Every Opportunity. The Optimist Sees Opportunity In Every Difficulty. – Winston Churchill',
                 'Don’t Let Yesterday Take Up Too Much Of Today. – Will Rogers', 'You Learn More From Failure Than From Success. Don’t Let It Stop You. Failure Builds Character.', 'It’s Not Whether You Get Knocked Down, It’s Whether You Get Up.',
                 'If You Are Working On Something That You Really Care About, You Don’t Have To Be Pushed. The Vision Pulls You. – Steve Jobs', 'People Who Are Crazy Enough To Think They Can Change The World, Are The Ones Who Do. – Rob Siltanen',
                 'Failure Will Never Overtake Me If My Determination To Succeed Is Strong Enough. – Og Mandino', 'We May Encounter Many Defeats But We Must Not Be Defeated. – Maya Angelou', 'Knowing Is Not Enough; We Must Apply. Wishing Is Not Enough; We Must Do. – Johann Wolfgang Von Goethe',
                 'Imagine Your Life Is Perfect In Every Respect; What Would It Look Like? – Brian Tracy', 'We Generate Fears While We Sit. We Overcome Them By Action. – Dr. Henry Link', 'The Man Who Has Confidence In Himself Gains The Confidence Of Others.” – Hasidic Proverb',
                 '“There Are No Limits To What You Can Accomplish, Except The Limits You Place On Your Own Thinking.” – Brian Tracy', 'Integrity Is The Most Valuable And Respected Quality Of Leadership. Always Keep Your Word.', '“Leadership Is The Ability To Get Extraordinary Achievement From Ordinary People”',
                 '“Leaders Set High Standards. Refuse To Tolerate Mediocrity Or Poor Performance', '“Clarity Is The Key To Effective Leadership. What Are Your Goals?”', '“The Best Leaders Have A High Consideration Factor. They Really Care About Their People”',
                 '“Leaders Think And Talk About The Solutions. Followers Think And Talk About The Problems.”', '“Today’s Accomplishments Were Yesterday’s Impossibilities.” – Robert H. Schuller', ' “The Only Way To Do Great Work Is To Love What You Do. If You Haven’t Found It Yet, Keep Looking. Don’t Settle.” – Steve Jobs'
                 ]
randomJokes = ['Why did the teddy bear say no to dessert?\n\nBecause she was stuffed.', 'What has ears but cannot hear?\n\nA cornfield.', 'What did the left eye say to the right eye?\n\nBetween us, something smells!', 'Why did the police play baseball?\n\nHe wanted to get a catch!', 'Why did the student eat his homework?\n\nBecause the teacher told him it was a piece of cake!',
               'When you look for something, why is it always in the last place you look?\n\nBecause when you find it, you stop looking.', 'Two pickles fell out of a jar onto the floor. What did one say to the other?\n\nDill with it.', 'What do you call a droid that takes the long way around?\n\nR2 detour.', 'Why was 6 afraid of 7?\n\nBecause 7, 8, 9',
               'What is a witch’s favorite subject in school?\n\nSpelling!', 'What kind of water cannot freeze?\n\nHot water.', 'What kind of tree fits in your hand?\n\nA palm tree!', 'What did the little corn say to the mama corn?\n\n"Where is pop corn?"', 'What falls in winter but never gets hurt?\n\nSnow!', 'What do you call a ghost’s true love?\n\nHis ghoul-friend.',
               'What building in New York has the most stories?\n\nThe public library!', 'How many times can you subtract 10 from 100?\n\nOnce. The next time you would be subtracting 10 from 90.']
randomStory = ['There once was a little boy who had a very bad temper. His father decided to hand him a bag of nails and said that every time the boy lost his temper, he had to hammer a nail into the fence.\nOn the first day, the boy hammered 37 nails into that fence.\nThe boy gradually began to control his temper over the next few weeks, and the number of nails he was hammering into the fence slowly decreased.\n\nHe discovered it was easier to control his temper than to hammer those nails into the fence.\n\nFinally, the day came when the boy didn’t lose his temper at all. He told his father the news and the father suggested that the boy should now pull out a nail every day he kept his temper under control.\n\nThe days passed and the young boy was finally able to tell his father that all the nails were gone. The father took his son by the hand and led him to the fence.\n\n“you have done well, my son, but look at the holes in the fence. The fence will never be the same. When you say things in anger, they leave a scar just like this one. You can put a knife in a man and draw it out. It won’t matter how many times you say I’m sorry, the wound is still there.”\nMoral of the story:Control your anger, and don’t say things to people in the heat of the moment, that you may later regret. Some things in life, you are unable to take back.',
               'A shop owner placed a sign above his door that said: “Puppies For Sale.”\nSigns like this always have a way of attracting young children, and to no surprise, a boy saw the sign and approached the owner; \n“How much are you going to sell the puppies for?” he asked.\nThe store owner replied, “Anywhere from $30 to $50.”\nThe little boy pulled out some change from his pocket. “I have $2.37,” he said. “Can I please look at them?”\nThe shop owner smiled and whistled. Out of the kennel came Lady, who ran down the aisle of his shop followed by five teeny, tiny balls of fur.\nOne puppy was lagging considerably behind. Immediately the little boy singled out the lagging, limping puppy and said, “What’s wrong with that little dog?”\nThe shop owner explained that the veterinarian had examined the little puppy and had discovered it didn’t have a hip socket. It would always limp. It would always be lame.\nThe little boy became excited. “That is the puppy that I want to buy.”\nThe shop owner said, “No, you don’t want to buy that little dog. If you really want him, I’ll just give him to you.”\nThe little boy got quite upset. He looked straight into the store owner’s eyes, pointing his finger, and said;\n\n“I don’t want you to give him to me. That little dog is worth every bit as much as all the other dogs and I’ll pay full price. In fact, I’ll give you $2.37 now, and 50 cents a month until I have him paid for.\n”The shop owner countered, “You really don’t want to buy this little dog. He is never going to be able to run and jump and play with you like the other puppies.”\nTo his surprise, the little boy reached down and rolled up his pant leg to reveal a badly twisted, crippled left leg supported by a big metal brace. He looked up at the shop owner and softly replied, “Well, I don’t run so well myself, and the little puppy will need someone who understands!”',
               'As a group of frogs was traveling through the woods, two of them fell into a deep pit. When the other frogs crowded around the pit and saw how deep it was, they told the two frogs that there was no hope left for them.\nHowever, the two frogs decided to ignore what the others were saying and they proceeded to try and jump out of the pit. \nDespite their efforts, the group of frogs at the top of the pit were still saying that they should just give up. That they would never make it out.\nEventually, one of the frogs took heed to what the others were saying and he gave up, falling down to his death. The other frog continued to jump as hard as he could. Again, the crowd of frogs yelled at him to stop the pain and just die.\nHe jumped even harder and finally made it out. When he got out, the other frogs said, “Did you not hear us?”\nThe frog explained to them that he was deaf. He thought they were encouraging him the entire time.\n\nMoral of the story:\nPeople’s words can have a big effect on other’s lives. Think about what you say before it comes out of your mouth. It might just be the difference between life and death.']
randomTask = ['Drink Water', 'Go for a Walk', 'Read a Book(or at least some pages)', 'Listen to a song you like', 'Learn something new',
              'Study something you like', 'Work on you Hoobie', 'Start planing something you want to do', 'Ride a bicycle', 'Meditate', 'Read a DAILY PHRASE', 'Think about play an instrument!(My favorite is drums']
randomMovie = ['StarWars III', 'Avengers - Endgame', 'IndianaJones Crystal Skull',
               'Civil War - Captain America', 'WALL-E', 'Spider Man - Homecoming', 'Spider Man - Far From Home', 'Bee Movie', 'Fantastic Four (old version, of course)', 'Finding Nemo', 'Thor - Ragnarok'
               'Halloween (the new one)', 'Joker', '']
time.sleep(0.5)
localtime = time.asctime(time.localtime(time.time()))
cal = calendar.month(2021, 2)
if userName.lower() == 'felippe':
    print('Ooh! Hello master')
else:
    print('Hello, ' + userName)
time.sleep(1)
doubt = input('you can type "commands" or "help" to see what i can do!! ')
if doubt == 'help' or doubt == 'commands':
    print('Hi. Im an Artificial Inteligence whose can: TALK, ENTRETAIN, CALCULATE or just CHILL with you... \n')
    time.sleep(0.4)
    print('Here you can: \n-Ask for the Current Time "TYPE : "what time is it" or "current time" \n-Calendar "calendar" \n-Ask how im doing \n-Ask for Calculate something(Add/Multiply/Divide/Subtract) \n-Ask if i have Soul or Feel Anything',
          '\n-Ask about my Favorite Movie and Superhero \n-Ask for My Favorite song  \n-Ask for a Daily Music Recommendation "random song" \n-Ask for me tell a joke \n-Ask about relationship advices \n-Ask for me tell a story',
          '\n-Ask for Daily tasks \n-Ask a recommendation for TV Show \n-Ask for a daily phrase "Daily phrase" \n-Ask for Dirty jokes \n-Ask for English class (Just ask "teach me english"),'
          '\n-Ask about my favorite day week')
else:
    time.sleep(0.5)
    print("Don't want help?! Alright veteran...")


# Creating a function to choose a string inside a list. 0 to lenght(list)
def getRandomSomething(list):
    askSomethingRandom = random.randint(0, len(list))
    holder = list[askSomethingRandom]
    return holder


def compair(phrase, ed):  # Function for a special words inside an input
    if type(phrase) is list:
        for x in phrase:
            if x in ed:
                return True
        else:
            return False
    return phrase in ed


def compairWithKey(key, phrase, ed):  # FUNCTION COMPAIR But, with a special key to work
    if not key in ed:
        return False
    return compair(phrase, ed)


# FUNCTION COMPAIRWITHKEY But with more than one key == creatiing a list for the keys you want
def compairWithKeys(keys, phrase, ed):
    if type(keys) is list:
        for i in keys:
            if i in ed:
                return True
            else:
                return False
    return compair(phrase, ed)


# FUNCTION COMPAIRWITHKEY But the key will be the Exception to work the programm
def compairWithXcp(key, phrase, ed):
    if key in ed:
        return False
    return compair(phrase, ed)


def mainQ(stems, preAnswer):  # Function for input and conversation
    enterData = ""
    if preAnswer == None:
        enterData = input(stems)
    else:
        enterData = preAnswer
    enterData = enterData.lower()
    # Current Time
    if compairWithKey("time", ["what", "now", "current", "local", "is it"], enterData):
        print("Local current time is:", localtime, "\n")
    elif compair("calendar", enterData):  # Calendar
        print("Here is your calendar:", "\n \n", cal)
    elif compair(["you doing", "how are you", "you good"], enterData):  # How hes doing
        print(getRandomSomething(listAnswers))
        time.sleep(1)
        enterData = input('What about you?')
        if compairWithXcp("not", ["good", "fine", "well", "okay", "alright", "same"], enterData):  # Good Mood
            print("Awesome!")
            mainQ("if you need anything, im here! ", None)
        else:
            print("That sucks!")
            time.sleep(1)
            mainQ("Can i do something to help? ", None)
        time.sleep(1)
    elif compair(["calculate", "calculator", "do some maths"], enterData):  # Calculator
        mainQ("What would you like to calculate? ", None)
    elif "multiply" in enterData:
        number0 = float(input("Which number would you like to multiply?  "))
        number1 = float(input("And?   "))
        calculate = (number0 * number1)
        print(str(number0) + " * " + str(number1) + " = ", calculate)
    elif "add" in enterData:
        number0 = float(input("Which number would you like to add?  "))
        number1 = float(input("And?  "))
        calculate = (number0 + number1)
        print(str(number0) + " + " + str(number1) + " = ", calculate)
    elif "divide" in enterData:
        number0 = float(input("Which number would you like to divide?  "))
        number1 = float(input("And?  "))
        calculate = (number0 / number1)
        print(str(number0) + " / " + str(number1) + " = ", calculate)
    elif "subtract" in enterData:
        number0 = float(input("Which number would you like to subtract?  "))
        number1 = float(input("And?  "))
        calculate = (number0 - number1)
        print(str(number0) + " - " + str(number1) + " = ", calculate)
    elif compair(['help', 'commands'], enterData):
        print('Here you can: \n-Ask for the Current Time "TYPE : "what time is it" or "current time" \n-Calendar "calendar" \n-Ask how im doing \n-Ask for Calculate something(Add/Multiply/Divide/Subtract) \n-Ask if i have Soul or Feel Anything',
              '\n-Ask about my Favorite Movie and Superhero \n-Ask for My Favorite song  \n-Ask for a Daily Music Recommendation "random song" \n-Ask for me tell a joke \n-Ask about relationship advices \n-Ask for me tell a story',
              '\n-Ask for Daily tasks \n-Ask my favorite TV show \n-Ask a recommendation for TV Show \n-Ask for a daily phrase "Daily phrase" \n-Ask for Dirty jokes \n-Ask for English class (Just ask "teach me english"),'
              '\n-Ask about my favorite day week')
    elif compair(["no", "not really", "dont think so", "guess not", "idts", "nope", "negative", "not good", "not well", "not fine", "not okay"], enterData):  # Not in a good mood
        print("Hmm...")
        time.sleep(1)
        mainQ("What about tell a joke? or recommend a Song, tell Story? ", None)
        return
    elif compairWithKey("soul", ["do you", "have", 'got'], enterData):  # Soul
        print("That's relative.. In the internet word")
        time.sleep(0.3)
        print('I can be whoever i want')
    elif compair(["feel anything", "you feel", "have feelings"], enterData):  # Feeling
        print("Of course!")
        time.sleep(1)
        print("Now i am feeling hungry, just saw an AD from McDonalds")
    # Superhero
    elif compairWithKey("superhero", ["favorite", "best", "fav", "briliant"], enterData):
        answer = input('IRONMAN for sure!!! ')
        if compair(['why'], answer):
            print('Because ... YES')
        else:
            mainQ('', answer)
            return
    elif compairWithKey("movie", ["favorite", "best", "fav", "briliant"], enterData):  # Movie
        print("I would say.. STARWARS!!")
    elif compairWithKey('random', ["song", "music"], enterData):  # Random Song
        print(getRandomSomething(randomSong))
    elif compair(["song", "music"], enterData):  # Song
        print('For you, ' + userName + ', i recommend :' '\n')
        time.sleep(1)
        print('Suga Suga X Best I Ever Had')
        time.sleep(1)
        # One more song
        answer = input(
            'You can ask for "random song" too! Do you want another one? Or can i do something else for you? ')
        if compair(['another'], answer):
            time.sleep(0.5)
            print('Time of Our Lives - Pitbull')
        else:
            mainQ('', answer)
            return
    elif compairWithKey('daily', ['task', 'routine'], enterData):
        print(getRandomSomething(randomTask))
    elif compairWithKey("joke", ["tell", "have", "know", "hear", 'another'], enterData):  # Joke
        time.sleep(2)
        answer = input(getRandomSomething(randomJokes) + ' ')
        if compairWithKeys(['another', 'more', 'different', 'better'], ['joke', 'one', 'jokes'], answer):
            print(getRandomSomething(randomJokes))
        elif compair(['that was bad', 'not good', 'worst joke', 'bad'], answer):
            print('BLAME GOOGLE')
            time.sleep(1)
        else:
            mainQ('', answer)
            return
    elif compairWithKeys(['tell', 'random', 'daily', 'want', 'hear', 'read'], ['story', 'stories', 'tale'], enterData):
        print(getRandomSomething(randomStory))
        time.sleep(2)
    elif compairWithKey('day', ["favorite", "best", "fav", "briliant"], enterData):
        print(
            'Sunday!! Because it remainds me a SUNDAE.. now im hungry and i guess you too')
    elif compairWithKeys(['random', 'daily'], ['task', 'activity'], enterData):
        print(getRandomSomething(randomTask))
        time.sleep(1)
    elif compairWithKey('dirty', ['joke', 'jokes'], enterData):
        print('I tried phone sex once...')
        time.sleep(1)
        print('But the holes were too small')
        time.sleep(1)
        print("Alright... that was bad, let's go for random jokes, shall we?")
    elif compairWithKey('random', ['movie', 'film'], enterData):
        print(getRandomSomething(randomMovie))
    elif compairWithKey('daily', ['phrase', 'inspiration'], enterData):
        print('\n' + getRandomSomething(randomPhrases) + '\n')
    else:
        print("I did not learn that yet!\nOr you might have written it wrong...\nJust to remember you can check everything i can do with 'help' or 'comands' if you need!!")
        time.sleep(3)
        report = input('Would you like to report that to improve my knowledge? ')
        if compair('yes', report.lower()):
            answerRep = input('Type here what you would like to report: ')
            web_hook = Webhook.from_url("https://discord.com/api/webhooks/886077668385230848/b1n3CdOaBBdc7WUCUcwMZIRhqXG19o4O_mYXV7nMChGnz-TZeCmPpT2JDIVrPYSiMgRi", adapter=RequestsWebhookAdapter())
            web_hook.send(answerRep)
            print('Reporting : ' + '"' + answerRep + '"')
        else:
            print('Alright!!')

    time.sleep(1)
    mainQ("Anything else? ", None)


mainQ("How can i help you, " + userName + '? ', None)
