print('''
*******************************************************************************
        .-.__.-.__.-.__.-._.-.
       (  How The Hell Do I  )
        "-"(    Play This  )"
            "-"(  GAME?   )
                '-..-"-..-'
                       O          _____________________
                ,_    o         _(  Hey, Dad, Are You  )_
          ____   \"\___,-'7    (        Winning?  )
  ____..-"_.-"|   )     (/      """""""((""""""""""""""""
 |   |====    |   a_ /@  E              \\
 |## |====    | =: T ::= )      __       ))
 |## |====    |   \/\   <,     {__\      Y
 |___|====____|    7"\_// \       \\  |\__,-7
     _/____\_     /( (@)   \      )) _}; .  {
    '.,____,.'-.,( \_____ ) \    //   \^ = _/
     ._ _        | (((__ ~   ) _//    /&~~")     ,
       Y       = |      '-,_    / T-cc_  // }   ((
       | __,..--"'          "-,/_ | |  cc7_(     ))
                                 "+-,_ |  |"|_,,;/
                                      "-, | |--"  

*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# https://rb.gy/5nxowf

# Write your code below this line 👇

direction = input("\nYou're part of the working class. Where do you want to go? Type \"left\" or \"right\".\n").lower()

if direction == "right":
    print("\nGo back to school. Marx is disappointed with you... Game Over!")

elif direction == "left":
    decision = input(
        "\nYou came to a restaurant. There are two options in the menu. Type \"mito\" to have a pile of hay. Type "
        "\"lulala\" to have a nice baloney sandwich.\n").lower()

    if decision == "mito":
        print("\nThe Agro is Pop and the hey is poisoned. Game Over!")

    elif decision == "lulala":
        door = input(
            "\nYou arrive at the Planalto Palace. There are some doors you need to open. One green, one yellow and "
            "one red. Which color do you choose?\n").lower()

        if door == "green":
            print("\nOh no! You got into a room full of patriots with CBF jerseys. Game Over!")

        elif door == "yellow":
            print("\nOh no! The door is loocked. Call the locksmith. Game Over!")

        elif door == "red":
            print("\nDo the L! We won!!!")

        else:
            print("\nGame Over!")

    else:
        print("\nGame Over!")

else:
    print("\nOh no! Another exempted Ciro Gomes' fan. Game Over!")

