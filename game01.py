from sys import exit

def start():
	print("you are in hell and thre is a battle!")
	print("it is between dream and morning star")
	print("u have to pick a side")
	pick=input(">")
	if pick=="dream":
		sandman()
	elif pick=="morning star":
		morning_star()
    else:
        print("good job now you are dead")

				
def sandman():
	print("you have the following powers")
	print(" bird of prey\n a life naturing planet\n hope)
	print("pick your move")
	
	move=input('>')
	if move=="1":
		print("you have picked to be a bird of prey ")
		print("but morning star picks to be a life eating bacteria so you have to pick another move")
		start()
	elif move=="2":
		print("you have picked to be a life naturing planet")
		print("but morning star is a nova the destroyer of planets")
	elif move=="3":
		print("you are hope and nothing can kill hope")
		exit(0)
	else:
		start()
		
	
def morning_star():
	print("you have the following powers")
	print("a serpent\n a life eating bacteria\n a nova")
	print("select a power")
	power=input(">")
	if power=="1":
		print("you are a sepernt but dream is a bird of prey")
	    start()
	elif power=="2":
		print("You are a life eating bacteria  but dream is a life naturing planet")
		start()
	elif power=="3":
		print("u are a nova the destroyer")
		exit(0)
	else:
		start()
	
	
start()
		
	
	