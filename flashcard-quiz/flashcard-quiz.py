#let user decide which set of cards to quiz
def choose_cardset():
    print "Welcome to the Program Syntax Quiz."
    print "Type the name of the command or call that does what the prompt says."
    print "At any time, type q to quit.\n"
    print "Which flashcard set would you like to quiz?"
    print "    [m]ongodb"
    print "    [u]nix"
    print "    [g]rep"
    chosen_cardset = raw_input()

    #quit check
    if chosen_cardset == "q":
        print "Goodbye!"
        raise SystemExit

    #catch bad input
    while chosen_cardset != "q" and chosen_cardset != "m" and chosen_cardset != "u" and chosen_cardset != "g":
        chosen_cardset = raw_input("Not a valid cardset, choose again: ")
        
    if chosen_cardset == "m":
        print "Quizzing on MongoDB syntax."
        return "mongo_cards.txt"
    elif chosen_cardset == "u":
        print "Quizzing on Unix command-line syntax."
        return "unix_cards.txt"
    elif chosen_cardset == "g":
        print "Quizzing on grep syntax."
        return "grep_cards.txt"

#open source file and create deck of cards
def create_deck(filename):
    f = open(filename, "r")
    deck = []
    for line in f:
        stripped = line.rstrip("\n")
        deck.append(stripped.split(":"))
    return deck

#shuffle the deck
def randomizer(input_deck):
    import random
    random.shuffle(input_deck)
    return input_deck

#quiz the flashcards
def quiz_mode(deck_random):
    count=0
    wrong_answers=[]
    for item in deck_random:
        print str(count+1)+")"
        print item[1]
        user_answer = raw_input("command is: ")

        #quiz answers loop
        if (user_answer == str(item[0]) ):
            print "Correct!\n"
        else:
            #save wrong answer without counting q as a wrong answer
            if (user_answer != "q") and (user_answer != str(item[0]) ):
                wrong_answers.append(item)
                print "Incorrect. Correct answer is:\t" + str(item[0])

            while (user_answer != "q") and (user_answer != str(item[0]) ):
                #making user review the right answer before moving on
                user_answer = raw_input("Review: correct answer is? ")
            if (user_answer == str(item[0]) ):
                print "Good. Study that one more.\n"
                
        #increment count but don't add a quit to the count
        if (user_answer != "q"):
            count += 1

        #quit check
        if user_answer == "q":
            print "Goodbye!"
            break
    print ""
        
    score_calculator(count, wrong_answers)
    return wrong_answers

#calculate the user's score
def score_calculator(count, wrong_answers):
    total_answers = len(deck_random)
    total_incorrect = len(wrong_answers)
    score = count - total_incorrect

    if total_answers != count:
        print "You only completed " + str(count) + "/" + str(total_answers) + " total questions."
    print "Your score: " + str(score) + "/" + str(total_answers)

    if total_incorrect > 0:
        print ""
        print "Here are the ones you got wrong: "
        for item in wrong_answers:
            print item[0]
        #idea: offer to start playing again but only with the wrong answers
        #also offer to play through from start, not with only wrong answers
        
    elif score == total_answers:
        print "Congrats, you got a perfect score!"
        #reponse = raw_input("Want to go again? [y] [n] ")
        #if response == "y":
            #finish the function and restart it - but don't start it again inside itself
        #elif response == "n":
            #print "Goodbye!"

#loop to quiz through flashcards and do stuff - controlled by main control
def main_loop():
    

#main
deck_ordered = create_deck( choose_cardset() )
deck_random = randomizer(deck_ordered)
keep_going = "y"
while keep_going == "y":
    deck_random = quiz_mode(deck_random)
    if len(deck_random) > 0:
        keep_going = raw_input("Do you want to quiz the ones you got wrong? [y/n]: ") 
        if keep_going == "y":
            print "Ok, shuffling the ones you got wrong..."
            deck_random = randomizer(deck_random)
        else:
            print "Ok, good work today!"
    else:
        keep_going="n"



#bugz:
    #should review_mode be its own function separate from main? seems like it should.
    
    #I don't know how to stop the function and start it again. would that be in a separate function maybe?
    #the issue is I don't know how to tell, based on the last time that it ran, whether or not to use only wrong answers or all the answers
    #I'd have to pass something different to the quiz function depending on which I want it to go through.
