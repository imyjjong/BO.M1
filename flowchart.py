from time import sleep

def Start():
    print("You wake up")
    sleep(1)
    decision1()

def decision1():
    print('''a) You're just gonna wake up and get ready
b) You're gonna check your phone and fall back asleep''')

    answer = input()

    if answer == "a":
        decision1a()
    elif answer == "b":
        print("You wake up again and you see that you're way to late now")
        sleep(1)
        decision1b()

def decision1a():
    print('''a) You're gonna take the train and come on school early
b) You're gonna take the bus and be late''')

    answer = input()

    if answer == "a":
        print("You arrive at school but once you get there you see a lot of black, expensive cars")
        sleep(1)
        decision3b()
    elif answer == "b":
        print("Once you arrive you hear a lots of shootings, you decide to leave and go home")
        sleep(1)
        decision2b()
        sleep(1)
        decision3a()

def decision1b():
    print('''a) You're gonna sleep again and just skip school
b) You're finally waking up and get to school''')

    answer=input()

    if answer=="a":
        print("While you're sleeping your mother sees that you're skipping school and she is so disappointed in you that she just stabs you. She never really wanted you anyways🌈")
        sleep(3)
        decision9a()
    elif answer=="b":
        print("When you arrive at school you see that the whole school is burned down")
        sleep(1)
        decision2a()

def decision2a():
    print('''You started to dance and just be happy for the first time in your life and then someone shoots you thru your skull. You may rest in peace now🌈''')

def decision2b():
    print('''Once you're almost home someone in a van asks you if you want a candy''')

def decision3a():
    print('''a) You say yes, cuz yeah candy
b) You say "No mister, this is wrong:(" ''')

    answer=input()

    if answer=="a":
        print("You eat the candy and feel very dizzy suddenly, you passed away a few minutes later. Silly goose, didn't your mom thought you to never take candy from strangers😔")
    elif answer=="b":
        print("If you chose this, we all know that you're lying, how can you say no to candy, so silly of you")
        sleep(1)
        print("You're still gonna eat the candy, because you're a child. That's just how it works")
        sleep(1)
        print("You end up dying anyways, NEVER TAKE CANDY FROM STRANGERS🚩")

def decision3b():
    print('''a) You're gonna approach the cars to see what's going on
b) You see that it's not safe for you to go there so you turn around and go home''')

    answer=input()

    if answer=="a":
        print("Once you get there you see a lot of men with guns")
        sleep(1)
        decision4a()
    elif answer=="b":
        print("Because of your pussy move, the devil visits you and brings you with him to hell🌈")
        sleep(1)
        print("You become friends with the devil and kill random people just for fun.")
        sleep(1)
        print("But because you're a stupid mf, you piss off the devil by calling yourself god of hell")
        sleep(1)
        print("The devil gets mad at you and tries to kill you by stabbing you with his fire sword")
        decision6b()

def decision4a():
    print('''a) You're gonna run away
b) You're gonna try to be a hero''')

    answer=input()

    if answer=="a":
        print("While you're running away one of the guys sees you and shoots you thru your skull🌈")
    elif answer=="b":
        print("While you're trying to save people a guy comes up to you and points a gun at you, you're screwed bestie")
        sleep(1)
        print("Suddenly the man gets distracted")
        sleep(1)
        decision4b()

def decision4b():
    print('''a) Are you gonna run away?
b) Are you gonna try to take the gun?''')

    answer=input()

    if answer=="a":
        print("You ran away and hid from the guy, you're waiting in fear till the guy goes inside of the school")
        sleep(1)
        print("The man goes away and you secretly run away. You wanna go home and just sleep")
        sleep(1)
        print("But guess what, suddenly Voldemort appears and he Avada Kedavras you and there you are. Lying on the ground. Dead af🌈")
    elif answer=="b":
        print("You somehow managed to really take the gun and point it at the guy")
        sleep(1)
        print("The man looks at you in fear and he suddenly he said, 'Please listen to me, don't shoot me. If you don't shoot me, i will give you something really special.'")
        sleep(1)
        decision5a()

def decision5a():
    print('''a) Are you gonna listen to him?
b) Are you gonna shoot him like a real boss😎?''')

    answer=input()

    if answer=="a":
        print("You put the gun down, he started to talk again 'Trust me, give me the gun. Please trust me")
        sleep(1)
        print("Once you hand him the gun, he points it at you and he shoots you right thru your skull🌈")
    elif answer=="b":
        print("You shoot him right in his chest and the moment you shot him everything went blank.")
        sleep(1)
        print("You look around in confusion, you're standing in a white room. The walls, the door, the floor, everything is white")
        sleep(1)
        print("You walk to the door and open it. When you open the door you suddenly feel ice cold.")
        sleep(1)
        print("You start to run and suddenly you're home again")
        sleep(1)
        decision5b()

def decision5b():
    print('''a) You're gonna jump of a building
b) You're gonna try figure it out''')

    answer=input()

    if answer=="a":
        print("While you're falling of the building, you get a call from your mom. She tells you that you were a big mistake and she wishes you dead.")
        sleep(1)
        print("Damn bestie, sucks to be you😔")
    elif answer=="b":
        print("You're really trying to be smart huh, silly goose. Just give up🤠")
        sleep(1)
        print("While you're walking through your room and try to search for directions or something that could lead to an answer, you see an book you have never seen bofore")
        sleep(1)
        decision6a()

def decision6a():
    print('''a) Are you gonna look in that book?
b) Are you gonna jump out of your window?''')

    answer=input()

    if answer=="a":
        print("When you open the book you suddenly see a flashlight and you close your eyes. When you open them you see your ceilling. It was all a dream after all")
        sleep(1)
        print("But before you know it your house explodes because you didn't check the oven and let the explosives in it while the oven is on")
        sleep(1)
        print("Silly you, so disappointing of you😔")
        sleep(1)
        print("Bestie ur dead af🌈")
    elif answer=="b":
        print("You simply just die😌")
        sleep(3)
        print("But you still have a choice")
        sleep(2)
        print("Yeah, I know. I'm very nice")
        sleep(1)
        print("You can choose between hell and heaven")
        decision7a()

def decision6b():
    print('''a) You tried to fight him which is just useless but okay
b) You give up and let him stab you to death''')

    answer=input()

    if answer=="a":
        print("Istg why would you think this was smart to do, well yeah you and up dying🌈")
    elif answer=="b":
        print("He actually has a little bit of emphathy in him and he lets you go")
        sleep(2)
        print("But then you get attacked by an alligator that the devil send to murder you")
        sleep(1)
        print("You really thought you could survive, haha cute🌈")
        sleep(2)
        decision10a()

def decision7a():
    print('''a) Hell
b) Heaven''')

    answer=input()
    if answer=="a":
        print("You go burn in hell and just yeah suffer")
        sleep(2)
        print("Or...")
        sleep(3)
        print("...you choose to be reincarnated")
        sleep(2)
        decision7b()
    elif answer=="b":
        print("You go do boring stuff with yeah idk angels")
        sleep(2)
        print("Or...")
        print("...you choose to be reincarnated")
        sleep(2)
        decision7b()

def decision7b():
    print('''a) Wanna reincarnate?
b) That's actually pretty lame, so no thank you''') 

    answer=input()
    
    if answer=="a":
        print("You really thought you can ust reincarnate like that, you silly goose. But because you were so desperate to get reincarnate you just stay dead and stay stuck in your coffin😁")
    elif answer=="b":
        print("Go choose again, you can't say no to me. I am basically god😌")
        sleep(3)
        decision8a()

def decision8a():
    print('''a) Wanna reincarnate?
b) That's actually pretty lame, so no thank you''')

    answer=input()
    
    if answer=="a":
        print("You really thought you can ust reincarnate like that, you silly goose. But because you were so desperate to get reincarnate you just stay dead and stay stuck in your coffin😁")
    elif answer=="b":
        print("You're like pissing me off right now, choose again")
        sleep(3)
        decision8b()

def decision8b():
    print('''a) Wanna reincarnate?
b) Yes, you can't choose no anymore''')

    answer=input()
    
    if answer=="a":
        print("You really thought you can ust reincarnate like that, you silly goose. But because you were so desperate to get reincarnate you just stay dead and stay stuck in your coffin😁")
    elif answer=="b":
        print("You really thought you can ust reincarnate like that, you silly goose. But because you were so desperate to get reincarnate you just stay dead and stay stuck in your coffin😁")

def decision9a():
    print('''a) Want to survive your moms stabbing?
b) Do you wanna rest in peace?''')

    answer=input()

    if answer=="a":
        print("Do you think you deserve to stay alive?")
        sleep(1)
        decision9b()
    elif answer=="b":
        print("Good choice my brother😔🤝")

def decision9b():
    print('''a) Yes😌
b) No😔''')

    answer=input()

    if answer=="a":
        print("I don't think so boo. Your mother wanted to get rid of you for a reason, so you better be honest now")
        sleep(1)
        decision11b()
    elif answer=="b":
        print("I'm glad that you're aware of that")

def decision10a():
    print('''a) I'm funny right?🤠
b) No like not at all☹️''')

    answer=input()

    if answer=="a":
        print("Thank you boo, so sweet of you. But yeah I am very aware of that🌈")
    elif answer=="b":
        print("Hope you rot in hell🥺")
        sleep(3)
        print("You're so mean to me, you better choose again before I stab you in the eye🤭")
        sleep(1)
        decision10b()

def decision10b():
    print('''a) I am extremely funny
b) No, ur still very lame''')

    answer=input()

    if answer=="a":
        print("Awww so sweet🌈")
    elif answer=="b":
        print("You're gonna regret this babygirl")
        sleep(2)
        print("I am gonna send a big dog to your house and let him eat your mother🤭")
        decision11a()

def decision11a():
    print('''a) u sad now?
b) Gonna cry?''')

    answer=input()

    if answer=="a":
        print("Go cry about it, baby")
        sleep(1)
        print("I really couldn't care less")
        sleep(1)
        print("It doesn't really matter anyways, cuz ur dead as hell")
    elif answer=="b":
        print("Melanie named her album after you")
        sleep(1)
        print("I really couldn't care less")
        sleep(1)
        print("It doesn't really matter anyways, cuz ur dead as hell")

def decision11b():
    print('''a) Yes, I'm sure I deserve it
b) You're right, I don't deserve it''')

    answer=input()

    if answer=="a":
        print("You're still a lying lil baby I see")
        sleep(2)
        print("Here, do it again")
        sleep(1)
        decision11b()
    elif answer=="b":
        print("Yes indeed, you deserve to die and rot in hell😌")

Start()