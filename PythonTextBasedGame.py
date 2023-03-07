#Hunter Conway
#December 6 2021
#Final Project

#This program is a text based adventure game. The user will asked to input answers to questions
# inorder to create a pathway for the character.


#this function stores the rep for part 1
def part1(rep):
    rep = conditioning1(rep)
    if rep == 0:
        return 0
    rep = conditioning2(rep)
    if rep == 0:
        return 0
    rep = conditioning3(rep)
    if rep == 0:
        return 0
    return rep



#this function stores the rep for part 2
def part2(rep):
    rep = competitionGame1(rep)
    if rep == 0:
        return 0
    rep = competitionGame2(rep)
    if rep == 0:
        return 0
    rep = competitionGame3(rep)
    if rep == 0:
        return 0
    return rep

#this function stores the rep for part 3
def part3(rep):
    rep = combat(rep)
    if rep == 0:
        return 0
    return rep

#this function stores the rep for part 4
def part4(rep):
    rep = knighting(rep)
    if rep == 0:
        return 0
    return rep

def intro():
    print("Welcome to A Knight’s Way. This is a texted based adventure game of becoming a noble knight.")
    print("You will train and face many tasks in order to be deemed worthy to server for the king.")
    inp = input("Are you up for the challenge? (y/n): ").lower()
    return inp[0] == "y"


def conditioning1(rep):
    introConditioning1()
    storyWater()
    ans = question(["Do what Theo said and walk to the river", "Save time and get water from the pond"])
    if ans == 1:
        print(" ")
        print("**You return to Commander Theo very late. You are exhausted and ready to pass out.**")
        print("Commander Theo: 'Well done son, I am very pleased with your work today.")
        print("Now go take this water and wash up. We train again at sun rise.'")
        rep = rep + 2
        print("reputation:", rep)
        print(" ")
        return rep

    else:
        pond()
        ans = question(["Lie. 'No, I ran to the river. Fish had kicked up the dirt causing the water to be dirty." ,"Truth. 'Yes, I cheated, Im sorry and I realize I have dishonored you.'"])
        if ans == 1:
            print(" ")
            print("'Commander Theo: You are a liar! I know about that pool of water at the bottom of the mountain. Not only did you fail the task but you lied! ")
            print("You are not worthy of becoming a knight. Leave at once!'")
            print("**You have dishonored Commander Theo and all the royal family. You have been banished from serving the king.**")
            print(" ")
            rep = 0
            return rep
        else:
            print(" ")
            print("Commander Theo: 'Although you disobeyed my orders you have shown responsibility and ownership. Get some rest and we shall try again tomorrow.'")
            rep = rep + 1
            print("reputation:", rep)
            print(" ")
            return rep
    return conditioning1(rep)

def introConditioning1():
    print(" ")
    print("'Hello, I am Grand Commander Theo, sent to you by King Louis. I will oversee your training. Follow me.")
    print("Today you will begin your training. We will test your strength. ")
    print("You will run down the mountain and fill these two jugs with water from the river and bring them back.")
    print("The river is far and will take you till night fall. You must be on your way!'")
    print("**You start your journey toward the river**")

def storyWater():
    print(" ")
    print("You have reached the bottom of the mountain and see a pool of water. ")
    print("You know its not the water Theo asked for, but the river is 3 miles away and it is going to get dark soon.")
def pond():
    print(" ")
    print("** you make it as the sun is setting**")
    print("Commander Theo:'Hmm this water looks awfully dirty and your back so soon.")
    print("Did you actually go to the river, or have you found a puddle along the way?'")
    print("You can lie or tell the truth...")



def conditioning2(rep):
    introConditioning2()
    pillarStory()
    ans = question(["Give up and tell Theo you quit", "Take a break and try again later","Continue to try and conquer the pillars"])
    if ans == 1:
        rep = 0
        print(" ")
        print("Theo is furious, he calls you a lazy bum and tells you to leave and never come back.")
        print(" ")
        return rep
    elif ans == 2:
        print(" ")
        print("Theo catches you slacking, he whips you and tells you to get back on the pillars.")
        print("Once Theo is satisfied you return to the barracks.")
        rep = rep - 1
        print("reputation:", rep)
        print(" ")
        return rep
    elif ans == 3:
        print(" ")
        print("Theo comes back at dawn and sees you repeatedly jumping across the pillars.")
        print("Theo: 'Well Done! I am very pleased with your progress. Keep up the good work. We will continue training in the morning.")
        rep = rep + 1
        print("reputation:", rep)
        print(" ")
        return rep
    return conditioning2(rep)

def introConditioning2():
    print(" ")
    print("**the next day you meet Commander Theo outside of the barracks**")
    print("Theo: 'Good morning lad. Today we will work on balance and agility. Do you see those pillars over there?")
    print("First you will climb them, then learn to jump from one pillar to another. If you fall get up and do it again. See you later!'")
    print("**Theo leaves**")
def pillarStory():
    print(" ")
    print("You climb the first pillar but lose balance and fall. You get up and keep your balance, you try to jump to the next pillar and fall once again.")
    print("You have been at it for hours but you continue to fall and you’re getting frustrated. There are 10 pillars but the highest you got to was 3. You are tired and think about quitting. ")


def conditioning3(rep):
    introConditioning3()
    bullRunStory()
    ans = question(["Be disqualified and jump into the approaching ally.","Kick yourself into third gear and run for your life!","Do the impossible, slide on the ground below the bull then swing on his back using his tail."])
    if ans == 1:
        print(" ")
        print("You are disqualified from the race. Theo thinks you are a coward and is very disappointed in you.")
        rep = rep - 1
        print("reputation:", rep)
        print(" ")
        return rep
    elif ans == 2:
        print(" ")
        print("You get mowed down and badly hurt. Theo is proud of your efforts and lets you rest for a couple days.")
        rep = rep + 1
        print("reputation:", rep)
        print(" ")
        return rep
    elif ans == 3:
        print(" ")
        print("You win the race after riding the bull. You have become the talk of the town. Theo says you’re an idiot but is impressed by your courageous act.")
        rep = rep + 2
        print("reputation:", rep)
        print(" ")
        return rep
    return conditioning3(rep)

def introConditioning3():
    print(" ")
    print("Theo:'Today we will test your speed and endurance. I have volunteered you into the race against bulls.")
    print("You will start in the arena and follow the designed path while the bulls chase you and many others through the town.'")
    print("You are terrified on what is going to happen but you believe in Theo and his guidance.")
    print("**You enter the arena where the bulls will be released**")
def bullRunStory():
    print(" ")
    print("King Louis: 'Welcome participants of the bull race! I am proud to see so many have joined us today to participate in this traditional event. Good Luck!'")
    print("** the bulls are released and you begin to run**")
    print("You are surprisingly very fast and keeping pace with the front group. You look behind you and see a bull is approaching quickly. ")
    print("Many people are ditching and hiding in the alleyways to avoid the bull but have been disqualified from the race.")
    print("**the bull is now on your tail, you must think fast**")


def competitionGame1(rep):
    introCompetitionGame1()
    race()
    ans = question(["Run past him and win the race.", "Spit at him as you run past.","Help and carry him up the hill."])
    if ans == 1:
        print(" ")
        print("congrats you won the first part of the competition. Everyone is impressed that you left everyone in the dust.")
        rep = rep + 1
        print("reputation:", rep)
        print(" ")
        return rep
    elif ans == 2:
        print(" ")
        print("The boy was faking and planned on taking your container. He grabs your leg as you run by, you fall. You finish but lost the lead.")
        rep = rep - 2
        print("reputation:", rep)
        print(" ")
        return rep
    elif ans == 3:
        print(" ")
        print("You did not win the first competition but you have earned the respect of others. You have shown you are courageous and selfless.")
        rep = rep + 2
        print("reputation:", rep)
        print(" ")
        return rep
    return rep

def introCompetitionGame1():
    print(" ")
    print("** a couple months have passed and you have done an outstanding job training with Theo mastering everything he has taught you.**")
    print("Theo: 'Today is the big competition, you will put all our training to work and compete against other boys who have been training just like you.'")
    print("** King Louis enters from the top of the balcony**")
    print("King Louis:'Hello fellow competitors, you have all been training so well. Not all of you will make it through to the next step of becoming a knight.")
    print("Only the best of the best will make it through. These games will test your abilities, there will be three games today.")
    print("One is based on speed and agility, the second is based on strength and the third… well you will find that out.' ")
def race():
    print(" ")
    print("The first game begins. All participants must run down the mountain along the dirt path and reach the river and come back. While at the river you must fill up a container of water.")
    print("**You started the race and you a have already filled you container.**")
    print("On your way up the mountain you see a participant laying on the ground with a sprained ankle.")

def competitionGame2(rep):
    game2_pillars()
    ans = question(["Rush your way up and get into the top 5." , "Take your time, go one hand at a time."])
    if ans == 1:
        print(" ")
        print("You went too fast. You lost your grip and fell.")
        print("You look around and many more have finished the competition.")
        answer = input("Do you want to continue climbing? (y/n)").lower()
        if answer == "y":
            print("You reached the top of the pole and get to move on to the last game.")
            rep = rep + 1
            print("reputation:", rep)
            print(" ")
            return rep
        else:
            print(" ")
            print("You got disqualified from the competition.")
            print(" ")
            rep = 0
            return rep
    elif  ans == 2:
        print(" ")
        print("you mange to reach the top and make the top 5. You now move on to the final game.")
        rep = rep + 1
        print("reputation:", rep)
        print(" ")
        return rep
    return rep

def game2_pillars():
    print(" ")
    print("King Louis: 'This next competition will test your strength. You must use these metal rings to climb your designated pole. Those who complete it will move on to the final competition.'")
    print("**you go to your pole and attempt to climb. It is hard and you cannot get a grip**")
    print("After a couple attempts and watching others, you begin to get a hang of it. You begin to climb the pole. You’re a little more than halfway and you’re getting tired. Three of the contestants have reached the top.")

def competitionGame3(rep):
    game3_archerRun()
    ans = question(["Hug the wall below the archers. It is very risky but will be the fastest route.","Go through the ally ways. It is the safest but also the slowest route.","Run through the center of town. There are some parts covered by buildings, but a majority is exposed. It is a decent risk but is the most direct route."])
    if ans == 1:
        route1(rep)
    elif ans == 2:
        print(" ")
        print("You make it safely through the ally and into the safe zone, however when you get there your were one of the last.")
        rep = rep - 1
        print("reputation:", rep)
        print(" ")
        return rep
    elif ans == 3:
        print(" ")
        print("You made it through the city. You were able to dodge the archers using the cover from buildings. You were not the first but qualified to pass.")
        print(" ")
        rep = rep + 1
    return rep

def game3_archerRun():
    print(" ")
    print("'King Louis: Congratulations to all of you who have made it thus far! This final challenge will test to see if you are ready for the next segment of becoming a night.")
    print("You will run across the city into the safe zone as my best archers are mounted on the walls. If you are hit by a blunt arrow you will be disqualified.'")
    print("** The race has started and arrows begin to fly everywhere**")
    print("As you run through the city you think of three routes to take.")
def route1(rep):
    print(" ")
    print("You have dodged many arrows and are close to the safe zone. The wall is about to end, and you will be exposed.")
    ans = question(["You see a wooden board in the middle of the road, take it and use it as a shield.","Dig into the approaching ally."])
    if ans == 1:
        print(" ")
        print("You are a brave soul. You slide into the board, and block incoming arrows. You are the first to make it into the safe zone. Everyone is impressed with your performance. ")
        rep = rep + 2
        print("reputation:", rep)
        print(" ")
        return rep
    elif ans == 2:
        print(" ")
        print("You were so close but got shot in the back before you escaped. You lost the competition.")
        print(" ")
        return rep
        rep = 0
    return rep

def combat(rep):
    combatIntro()
    ans = question(["We have daggers, it is light but powerful. The weapon for an assassin.", "Next is the battle axe, the weapon of a brute. It is heavy but will demolish any opponent.","Lastly, we have the sword and shield. The classic combo of a sharp blade and sturdy shield."])
    if ans == 1:
        daggers()
        rep = hunt(rep)
        rep = assassin(rep)
    elif ans == 2:
        battleAxe()
        rep = training(rep)
        rep = villageAttack(rep)
    elif ans == 3:
        swordAndShield()
        rep = swordTraining(rep)
    return rep


def combatIntro():
    print(" ")
    print("After a days break after the competition you are introduced to the next part of becoming a knight. Theo explains the next part is combat training.")
    print("Commander Theo: Before we start your training, we must pick your weapon of choice.")
    print("**Theo takes you to the blacksmith**")
    print("We have three available weapons which you can choose from.")


def daggers():
    print(" ")
    print("Black Smith: Great choice! With this pristine weapon you will be quick and nimble. Mobility will be key along with stealth.")
    print("**Theo takes you to the training ground where you will meet your new instructor.**")
    print("Jon: 'Hello! I will be your new instructor, I will teach you the way of the daggers and how to become a sneaky assassin.'")
    print("Jon: 'Today I will teach you to be stealthy and how to approach your victims.  To be stealthy you must be quick, quiet, and smart. I will teach you through hunting.'")


def hunt(rep):
    print(" ")
    print("**Jon takes you to the woods where he shows you how to sneak up on animals.**")
    print("It is now your turn. You spot a dear ahead eating berries from a bush. Jon taught you two methods so far...")
    ans = question(["Climb the trees and stalk it from above." , "Creep through the bushes and attack from behind."])
    if ans == 1:
        huntTree(rep)
    elif ans == 2:
        huntBush(rep)
    return rep


def huntTree(rep):
    print(" ")
    answer = input("You are right above the deer. Do you wait for the perfect moment or tackle it now? (type: “wait” or “tackle”)").lower()
    if answer == "wait":
        print(" ")
        print("Now was your chance. The deer heard a noise and ran off, now you are without dinner and Jon is not happy.")
        print("**you return to your barrack for the night**")
        rep = rep - 1
        print("Reputation:", rep)
        print(" ")
        return rep
    elif answer == "tackle":
        print(" ")
        print("You successfully tackled the deer. You kill him and bring it back for dinner. Jon is very pleased with your quick learning.")
        rep = rep + 1
        print("Reputation:", rep)
        print(" ")
        return rep
    return rep


def huntBush(rep):
    print(" ")
    answer = input("The deer is a bush away. Do you quickly charge it or slowly creep up? (Type 'charge' or 'creep')").lower()
    if answer == "charge":
        print("You crash and stab the dear before he runs away. Jon is pleased and helps you prepare it for dinner.")
        rep = rep + 1
        print("Reputation:", rep)
        print(" ")
        return rep
    elif answer == "creep":
        print(" ")
        print("You step on a branch and the deer runs. You missed your opportunity and Jon isn’t happy.")
        print("**you return to your barracks for the night**")
        rep = rep - 1
        print("Reputation:", rep)
        print(" ")
        return rep
    return rep


def assassin(rep):
    print(" ")
    print("** after a couple months of training Jon has one last mission. Before he deems you a knight. There has been a revolution stirring around and Jon asks you to secretly take out the one in charge**")
    print("You sneak into the man's house at night while he is sleeping. You are hovering over his body and are unsure how to kill him.")
    ans = question(["Use poison. Put some droplets into the glass of water on his night stand.","Take out a rag and suffocate him.","Stab him in the throat in honor of the King"])
    if ans == 1:
        print("The man did not take the poison bait. He roams the streets and is revolution is overthrowing the king. You were sentenced to death.")
        print(" ")
        rep = 0
        return rep
    elif ans == 2:
        print(" ")
        print("He wakes up and grabs you, you slit is arm with your knife and run. The man lives and Jon is not happy.")
        rep = rep - 2
        print("Reputation:", rep)
        print(" ")
        return rep
    elif ans == 3:
        print(" ")
        print("Jon is pleased with your performance. He will talk with the king about knighting you.")
        rep = rep + 2
        print("Reputation:", rep)
        print(" ")
        return rep
    return rep


def battleAxe():
    print(" ")
    print("Blacksmith: Excellent choice! You must be a brute. The battle axe is big, you will have to use it with both hands.")
    print("With this weapon you will need to be strong and aware of your surroundings. If not, you will be vulnerable.")
    print("**Theo takes you to the axe barracks where you will meet your new instructor.**")
    print("Donald: Welcome! Looking to become a ruthless brute I see. Good you have come to the right place. I will teach you how to use the battle axe and dominate the battlefield.")


def training(rep):
    print(" ")
    print("Donald: Our training will begin on learning how to use the axe and channel your strength with every swing. I will take you to the forest where you will learn how to cut the great trees.")
    print("** You follow Donald to the forest where he teaches you to cut down great oak trees.**")
    print("After watching Donald cut some down he points to a tree and tells you to chop it down. At first you do not hesitate but then you see a nest with baby birds in the top of the tree.")
    ans = question(["Spare the tree, saving the birds and disobeying Donald.","Show no mercy. After all you are a brute."])
    if ans == 1:
        print(" ")
        print("Donald isn’t happy and thinks he has to roughen you up. He beats you up and leaves.")
        rep = rep - 2
        print("Reputation:", rep)
        print(" ")
        return rep
    elif ans == 2:
        print(" ")
        print("you show no mercy and take down the tree regardless of the birds. Donald likes the ruthlessness within you and think you will make a great brute.")
        rep = rep + 1
        print("Reputation:", rep)
        print(" ")
        return rep
    return rep
def villageAttack(rep):
    print(" ")
    print("** You have been training for months with Donald. He wakes you up one morning and tells you to grab your axe there is an attack on a local village**")
    print("This is your first battle but you are ready. You see villagers being attacked by 3 goons in the middle of the village and charge them.")
    ans = question(["Charge and swing at the three goons with one swing.","Take the goons one by one.","Grab the locals and run."])
    if ans == 1:
        print(" ")
        print("You kill all three goons however you greatly injured a local in the process. They are grateful you saved them but the town is not happy with your choice.")
        print("Donald is pleased your performance and thinks you are ready for knighting. He leaves to meet with the king.")
        rep = rep + 1
        print("Reputation:", rep)
        print(" ")
        return rep
    elif ans == 2:
        print(" ")
        print("You crush the skull of 2 of the goons, the third one tries to run but you throw your axe at his leg then execute him. The villagers were saved.")
        print("Donald is also pleased your performance and thinks you are ready for knighting. He leaves to meet with the king.")
        rep = rep + 1
        print("Reputation:", rep)
        print(" ")
        return rep
    elif ans == 3:
        print(" ")
        print("As you flee with the villagers more goons show up. You take down a few but they overwhelmed you. The goons are ruthless and chop you to pieces.")
        print(" ")
        rep = 0
        return rep
    return rep


def swordAndShield():
    print(" ")
    print("'Blacksmith: Excellent choice! With this weapon you will have to be strong but also smart. You must learn when to block and when to swing.'")
    print("**Theo takes you to meet your new instructor.**")
    print("Matthew: 'Hello sir, I am Matt. I will train you to become a master with the sword and shield. It is a powerful combo when taught the right way.'")


def swordTraining(rep):
    print(" ")
    print("Matthew: We will go straight into dueling. It is the best way to learn how to use your sword.")
    print("**Matthew teaches you some mechanics then sets you up for a duel**")
    print("Your opponent lashes at you. There three things you can do.")
    ans = question(["Block then nudge opponent with shield.","Dodge to the side then lash at him with your sword.","Attack back and have a sword fight."])
    if ans == 1:
        shieldBash(rep)
    elif ans == 2:
        dodgeAttack(rep)
    elif ans == 3:
        swordFight(rep)
    print("**you and Matthew train a lot the next couple of months. He meets with the king to see if you have met his standards. **")
    return rep

def shieldBash(rep):
        print(" ")
        bash = input("Your shield bash was successful. Your opponent stumbled. Do you push him again or lunge at him with your sword?(type “push” or “lunge”)").lower()
        rep = rep + 1
        print("Reputation:", rep)
        print(" ")
        if bash == "push":
            print(" ")
            print("You push your opponent to the ground making him surrender. Matthew is pleased and compliments your shield bash.")
            rep = rep + 1
            print("Reputation:", rep)
            print(" ")
            return rep
        elif bash == "lunge":
            print(" ")
            print("you lunge to hard. Your opponent dodges and you fall on your face. Matthew is ashamed.")
            rep = rep - 2
            print("Reputation:", rep)
            print(" ")
            return rep
        return rep

def dodgeAttack(rep):
    print(" ")
    attack = input("Your dodge was successful. His right side is exposed or you can sweep his feet. What would you like to attack? (type 'right' or 'sweep')")
    rep = rep + 1
    print("Reputation:", rep)
    print(" ")
    if attack == "right":
        print(" ")
        print("you caught your opponent exposed and capitalized on it. Matthew is impressed and compliment your smooth tactic.")
        rep = rep + 1
        print("Reputation:", rep)
        print(" ")
        return rep
    elif attack == "sweep":
        print(" ")
        print("Your opponent catches on and bashes you with his shield. Matthew shakes his head in disappointment.")
        rep = rep - 2
        print("Reputation:", rep)
        print(" ")
        return rep
    return rep

def swordFight(rep):
    print(" ")
    counter = input("You had a loose grip and your opponent knocks your sword away. You block him with your shield then go for another swing. Swing left or right? (Type left or right)")
    rep = rep - 1
    print("Reputation:", rep)
    print(" ")
    if counter == "left":
        print(" ")
        print("You had no shot on his left side. Matthew is confused about your choice.")
        rep = rep - 1
        print("Reputation:", rep)
        print(" ")
        return rep
    elif counter == "right":
        print(" ")
        print("You stabbed him in a large gap. Matthew is pleased with your recovery.")
        rep = rep + 3
        print("Reputation:", rep)
        print(" ")
        return rep
    return rep


def knighting(rep):
    print(" ")
    print("**you meet with the king about being knighted**")
    if rep > 12:
        print(" ")
        print("King Louis:'During your training I have been keeping track of your reputation. It looks like you have done very well! You have required enough reputation to become a noble night. Congratulations!'")
        print(" ")
    elif rep < 11:
        print(" ")
        print("King Louis:'It looks like you have tried very hard during your training however you have made many mistakes along your journey. I am sorry but I am unable to knight you.'")
        print(" ")
    return rep



#this function will ask the question and print the choices from a given list.
def question(choices):
    print("What will you do?")
    i = 1
    for choice in choices:
        print(i, choice)
        i = i + 1
    return int(input("Enter your decision(number): "))

# reads rep and allows user to proceed to next part if rep is > 0
rep = -1
if intro():
    rep = 10
    if rep > 0:
        rep = part1(rep)
        if rep > 0:
            rep = part2(rep)
        if rep > 0:
            rep = part3(rep)
        if rep > 0:
            rep = part4(rep)


    def main():
        intro()
        conditioning1(rep)
        conditioning2(rep)
        conditioning3(rep)
        competitionGame1(rep)
        competitionGame2(rep)
        competitionGame3(rep)
        combat(rep)
        knighting(rep)
    
        main()


    # determines if game ends early or not
    if rep == -1:
        print("Thank you, come again.")
        print("Copyrighted by: Hunter Conway. hunter.conway1@marist.edu. https://www.linkedin.com/in/hunterco25/")
    elif rep == 0:
        again = input("Game over. Would you like to play again? (y/n)").lower()
        if again == "y":
            print(" ")
            rep = 10
            main()
        else:
            print(" ")
            print("Copyrighted by: Hunter Conway. hunter.conway1@marist.edu. https://www.linkedin.com/in/hunterco25/")
            input("Thank you for playing. Hit <enter> to exit")
    else:
        again = input("Thank you for playing. Would you like to play again? (y/n)").lower()
        if again == "y":
            print(" ")
            rep = 10
            main()
        else:
            print(" ")
            print("Copyrighted by: Hunter Conway. hunter.conway1@marist.edu. https://www.linkedin.com/in/hunterco25/")
            input("Hit <enter> to exit")
