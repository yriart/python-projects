flashcards_master=[
    ("rmdir","remove directory"),
    ("apropos","find an appropriate manual page"),
    ("chown","change ownership"),
    ("mkdir","make directory"),
    ("less","page through a file"),
    ("xargs","execute arguments"),
    ("cat","print the whole file"),
    ("cd","change directory"),
    ("exit","exit the shell"),
    ("env","view your environment"),
    ("pwd","print working directory"),
    ("man","view manual page for a command"),
    ("sudo","excute command as super-user with root access - DANGER"),
    ("chmod","change permission modifiers"),
    ("echo","print whatever you type after it"),
    ("export","export/set a new environment variable"),
    ("grep","find things inside files",("options","pattern","location")),
    ("hostname","my computer's network name"),
    ("popd","pop directory - remove from bookmarked directories"),
    ("pushd","push directory - bookmark a directory or go to the last bookmarked directory"),
    ("touch","create a blank file"),
    ("find","find a file"),
    ("mv","move a file or directory"),
    ("ls","list directory"),
    ("cp","copy a file or directory"),
    (">","take output of command on left, write it to the file on the right"),
    ("|","pipe: takes output from command on left and pipes it to the command on the right"),
    ("*","wildcard"),
    ("<","takes and sends contents of file on the right to the program/command on the left"),
    (">>","takes output of the command on the left, appends it to the file on the right"),
    ("grep -A","search that prints matched line and the nth line after it"),
    ("grep -B","search that prints matched line and the nth line before it"),
    ("grep -C","search that prints nth line before, matched line, and nth line after"),
    ("grep -v","inverted search: find what does NOT patch the pattern"),
    ("grep -i","search that is case insensitive"),
    ("grep -l","search filenames, not file contents"),
    ("grep -r","recursively search through all files in current dir and subdirs"),
    ("grep -c","search and count the number of matches"),
    ("grep -w","search with full word match - not substrings"),
    ("grep -e","search and match ALL the given patterns"),
    ("grep -o","search that returns only the matched string, not the whole line it's on"),
    ("grep -n","search that returns line number of matches")
]

def randomizer(input_deck):
    import random
    random.shuffle(input_deck)
    return input_deck

def score_calculator(count, wrong_answers):
    total_answers=len(flashcards_random)
    total_incorrect=len(wrong_answers)
    score=count-total_incorrect

    if total_answers != count:
        print "You only completed " + str(count) + "/" + str(total_answers) + " total questions."
    print "Your score: " + str(score) + "/" + str(total_answers)

    if total_incorrect>0:
        print ""
        print "Here are the ones you got wrong: "
        for item in wrong_answers:
            print item[0]
        #offer to start playing again but only with the wrong answers
        #also offer to play through from start, not with only wrong answers
        
    elif score==total_answers:
        print "Congrats, you got a perfect score!"
        #reponse=raw_input("Want to go again? [y] [n] ")
        #if response=="y":
            #finish the function and restart it - but don't start it again inside itself
        #elif response=="n":
            #print "Goodbye!"

def quiz_mode(flashcards_random):
    count=0
    wrong_answers=[]
    print "Welcome to the *nix Command Line Quiz."
    print "Type the name of the command that does what the prompt says."
    print "At any time, type q to quit.\n"
    for item in flashcards_random:
        print str(count+1)+")"
        print item[1]
        user_answer=raw_input("command is: ")

        #quiz answers loop
        if (user_answer == str(item[0])):
            print "Correct!\n"
        else:
            #save wrong answer without counting q as a wrong answer
            if (user_answer !="q") and (user_answer !=str(item[0])):
                wrong_answers.append(item)
                print "Incorrect. Correct answer is:\t" + str(item[0])

            while (user_answer !="q") and (user_answer !=str(item[0])):
                #making user review the right answer before moving on
                user_answer=raw_input("Review: correct answer is? ")
            if (user_answer == str(item[0])):
                print "Good. Study that one more.\n"
                
        #increment count but don't add a quit to the count
        if (user_answer !="q"):
            count+=1

        #quit check
        if user_answer =="q":
            print "Goodbye!"
            break
    print ""
        
    score_calculator(count, wrong_answers)
    return wrong_answers


#main 
flashcards_random=randomizer(flashcards_master)
keep_going="y"
while keep_going == "y":
    flashcards_random=quiz_mode(flashcards_random)
    if len(flashcards_random) > 0:
        keep_going=raw_input("Do you want to quiz the ones you got wrong? [y/n]: ") 
        if keep_going=="y":
            print "Ok, shuffling the ones you got wrong..."
            flashcards_random=randomizer(flashcards_random)
        else:
            print "Ok, good work today!"
    else:
        keep_going="n"

#bugz:
