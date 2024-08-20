kolory = ["X", "O"]
ostatnie = [[],[]]
tura = 0
gameGoing = True

board = ["-","-","-",
         "-","-","-",
         "-","-","-"]

def showCurrentBoard():
    print(
        board[0], "|", board[1], "|", board[2], "\n"+
        board[3], "|", board[4], "|", board[5], "\n"+
        board[6], "|", board[7], "|", board[8], "\n"
        )

def checkLast(kolor):
    if(len(ostatnie[kolor]) > 3):
        board[ostatnie[kolor][0]] = "-"
        del ostatnie[kolor][0]

def umiesc(kolor, pos):
    if(board[pos] == "-"):
        board[pos] = kolory[kolor]
        ostatnie[kolor].append(pos)
        return 0
    else:
        print("Pole jest już zajęte")
        return -1

def sprawdzWygrana(kolor):
    ''' sprawdzanie 
    1|2|3
    4|5|6
    7|8|9

    7 ^ ^> >
    8 ^
    9 <^ ^
    4 >
    1 >
    ale wszystko -1 bo index = 0
    '''
    wygrana = False
    if(board[6] == kolory[kolor]):
        if(board[7] == kolory[kolor] and board[8] == kolory[kolor]): #7 >
            wygrana = True
        elif(board[4] == kolory[kolor] and board[2] == kolory[kolor]): #7 ^>
            wygrana = True
        elif(board[3] == kolory[kolor] and board[0] == kolory[kolor]): #7 ^
            wygrana = True
    if(board[7] == kolory[kolor] and wygrana == False):
        if(board[4] == kolory[kolor] and board[1] == kolory[kolor]): #8 ^
            wygrana = True
    if(board[8] == kolory[kolor] and wygrana == False):
        if(board[4] == kolory[kolor] and board[0] == kolory[kolor]): #9 <^
            wygrana = True
        if(board[5] == kolory[kolor] and board[2] == kolory[kolor]): #9 ^
            wygrana = True
    if(board[3] == kolory[kolor] and wygrana == False):
        if(board[4] == kolory[kolor] and board[5] == kolory[kolor]): #4 >
            wygrana = True
    if(board[0] == kolory[kolor] and wygrana == False):
        if(board[1] == kolory[kolor] and board[2] == kolory[kolor]): #1 >
            wygrana = True
    if(wygrana):
        print("---------------")
        print("Wygrał", kolory[kolor])
        return 1
    return 0



while gameGoing:
    showCurrentBoard()
    print("Tura", kolory[tura])
    pole = int(input("Wybierz pole od 1 do 9: ")) 
    pole -= 1
    if(pole > 9 or pole < 0):
        print("Niepoprawny wybor")
        continue
    czySieUdalo = umiesc(tura, pole)
    if(czySieUdalo == -1):
        continue
    checkLast(tura)
    koniec = sprawdzWygrana(tura)
    if(koniec == 1):
        gameGoing = False
        showCurrentBoard()
    tura = int(not bool(tura)) #zamien na to drugie. lol
    