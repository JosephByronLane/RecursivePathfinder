labyrinth = [
    ['X','X','X','X','X','X','X','X','X','X','X','X','X'],
    ['X','-','-','X','-','-','-','-','-','X','X','-','X'],
    ['X','-','X','X','-','X','-','X','-','X','X','-','X'],
    ['X','-','-','-','-','X','-','X','-','-','X','-','X'],
    ['X','-','X','X','X','X','X','X','X','-','-','-','X'],
    ['O','-','-','-','-','-','-','-','-','-','X','-','X'],
    ['X','-','X','X','X','X','-','X','X','X','X','-','X'],
    ['X','-','-','-','X','X','-','-','-','-','-','X','X'],
    ['X','-','X','-','X','X','-','X','-','X','-','X','X'],
    ['X','-','X','-','-','-','-','X','-','X','-','-','X'],
    ['X','-','X','X','X','X','-','X','-','X','X','-','X'],
    ['X','-','-','-','-','X','-','X','-','X','X','-','-'],
    ['X','X','X','X','X','X','X','X','X','X','X','X','X'],
]

HP = 10

def return_health(labyrinth,col,row):
    if labyrinth[col][row].startswith('K-'):
        tempstring = labyrinth[col][row]
        tempstring2 = ''
        for i in range(2, len(labyrinth[col][row])):
            tempstring2 += tempstring[i]
        return int(tempstring2)




def find_damage_tiles(labyrinth,damagetiles):
    temparr = []
    amount_healed_list = []

    for i in range(len(labyrinth)):
        for a in range(len(labyrinth[i])):
            if labyrinth[i][a].startswith("K-"):
                tempstring = labyrinth[i][a]
                tempstring2 = ''
                for b in range(2, len(labyrinth[i][a])):
                    tempstring2 += tempstring[b]
                temparr.append(i)
                temparr.append(a)
                damagetiles.append(temparr)
                amount_healed_list.append(int(tempstring2))
                temparr = []
    return damagetiles, amount_healed_list


def find_health_tiles(labyrinth, healhtiles):
    temparr = []
    amount_healed_list=[]

    for i in range(len(labyrinth)):
        for a in range(len(labyrinth[i])):
            if labyrinth[i][a].startswith("K+"):
                tempstring = labyrinth[i][a]
                tempstring2 = ''
                for b in range(2, len(labyrinth[i][a])):
                    tempstring2 += tempstring[b]
                temparr.append(i)
                temparr.append(a)
                healhtiles.append(temparr)
                amount_healed_list.append(int(tempstring2))
                temparr = []
    return healhtiles, amount_healed_list


def return_hp_heal(labyrinth,col,row,lchp):
    if labyrinth[col][row].startswith('K+'):
        tempstring = labyrinth[col][row]
        tempstring2 = ''
        for i in range(2, len(labyrinth[col][row])):
            tempstring2 += tempstring[i]
        return lchp-int(tempstring2)
    else:
        return lchp
def return_hp_damage(labyrinth,col,row,lchp):
    if labyrinth[col][row].startswith('K-'):
        tempstring = labyrinth[col][row]
        tempstring2 = ''
        for i in range(2, len(labyrinth[col][row])):
            tempstring2 += tempstring[i]
            return lchp + int(tempstring2)
    else:
            return lchp


def replace_poison(labyrinth,col,row):
    labyrinth[col][row]="V"


def redo_health_tiles(labyrinth,col,row,movabletiles):
    currentcoords = [col, row]
    for i in range(len(movabletiles[0])):
        if currentcoords == movabletiles[0][i]:
            tempstring = movabletiles[1][i]
            labyrinth[col][row]="K+"+f"{tempstring}"
    for i in range(len(movabletiles[2])):
        if currentcoords == movabletiles[2][i]:
            tempstring = movabletiles[3][i]
            labyrinth[col][row]="K+"+f"{tempstring}"

def redo_traps(lab, col, row, triggertraptiles, walltraptiles):
    currentcoords = [col, row]
    for i in range(len(triggertraptiles)):
        if currentcoords == triggertraptiles[i]:
            lab[walltraptiles[i][0]][walltraptiles[i][1]] = f"T{i + 1}"


def replace_traps(lab, triggertraptiles, walltraptiles, col, row):
    currentcoords = [col, row]
    for i in range(len(triggertraptiles)):
        if currentcoords == triggertraptiles[i]:
            lab[col][row] = f"S{i + 1}"
    for i in range(len(walltraptiles)):
        if currentcoords == walltraptiles[i]:
            lab[col][row] = f"T{i + 1}"
    return lab

def omg_why_you_do_this(labyrinth, col, row):
    if labyrinth[col][row].startswith('K+') or labyrinth[col][row].startswith('K-'):
        return True
    else:
        return False


def find_predetermined_start(labyrinth, startingcell):
    for i in range(len(labyrinth)):
        for a in range(len(labyrinth[i])):
            if labyrinth[i][a] in startingcell:
                return i, a


def healthcheck(labyrinth, col, row):
    if labyrinth[col][row].startswith('K+'):
        tempstring = labyrinth[col][row]
        tempstring2 = ''
        for i in range(2, len(labyrinth[col][row])):
            tempstring2 += tempstring[i]
        return True, int(tempstring2)
    else:
        return False, 0


def findpoison(labyrinth, col, row, movabletiles):
    if labyrinth[col][row] in movabletiles[3]:
        return True


def printlab(labyrinth):
    for i in range(len(labyrinth)):
        print(labyrinth[i])


def characterdeath(labyrinth):
    printlab(labyrinth)
    print("No se pudo resolver el laberinto")

    print("El personaje se murio")
    exit()


def appendtiles(movabletiles):
    temparr = []
    for i in range(len(movabletiles) - 2):
        temparr.append(movabletiles[i])
    for i in range(len(movabletiles)):
        for a in range(len(movabletiles[i])):
            temparr.append(movabletiles[i][a])
    return temparr


def damage_check(labyrinth, col, row):
    if labyrinth[col][row].startswith('K-'):
        tempstring = labyrinth[col][row]
        tempstring2 = ''
        for i in range(2, len(labyrinth[col][row])):
            tempstring2 += tempstring[i]
        return True, int(tempstring2)
    else:
        return False, 0



def find_trap_triggers(labyrinth, triggertraptiles):
    aretheretrapsleft = True
    valuefoundaux = False
    temparr = []
    c = 0
    colcounter = 0

    while (aretheretrapsleft) == True:
        valuefoundaux = False
        c += 1
        colcounter += 1

        for i in range(len(labyrinth)):
            if valuefoundaux:
                break
            for a in range(len(labyrinth[i])):
                if labyrinth[i][a] == ('S' + f'{c}'):
                    temparr.append(i)
                    temparr.append(a)
                    triggertraptiles.append(temparr)
                    temparr = []
                    aretheretrapsleft = True
                    valuefoundaux = True
                    break
            if valuefoundaux == False:
                aretheretrapsleft = False
    return triggertraptiles, c


def find_trap_walls(labyrinth, walltraptiles):
    aretheretrapsleft = True
    valuefoundaux = False
    temparr = []
    c = 0
    colcounter = 0

    while aretheretrapsleft == True:
        valuefoundaux = False
        c += 1
        colcounter += 1

        for i in range(len(labyrinth)):
            if valuefoundaux:
                break
            for a in range(len(labyrinth[i])):
                if labyrinth[i][a] == ('T' + f'{c}'):
                    temparr.append(i)
                    temparr.append(a)
                    walltraptiles.append(temparr)
                    temparr = []
                    aretheretrapsleft = True
                    valuefoundaux = True
                    break
            if valuefoundaux == False:
                aretheretrapsleft = False
    return walltraptiles, c


def answer_check(labyrinth, col, row):
    # # R
    # if labyrinth[col][row + 1] == 'E':
    #     return True
    # # D
    # if labyrinth[col + 1][row] == 'E':
    #     return True
    # # L
    # if labyrinth[col][row - 1] == 'E':
    #     return True
    # # U
    # if labyrinth[col - 1][row] == 'E':
    #     return True

    # R
    if row + 1 > len(labyrinth[0]) - 1:
        return True
        # D
    if col + 1 > len(labyrinth) - 1:
        return True
        # L
    if row - 1 < 0:
        return True
        # U
    if col - 1 < 0:
        return True


def trap_checker(labyrinth, col, row, movabletiles):
    if labyrinth[col][row] in movabletiles[2]:
        return True
    else:
        return False


def place_checker(labyrinth, col, row, triggertraptiles, walltraptiles, pchp, movabletiles, startcol, startrow, poison, poisoncounter):
    if row + 1 < len(labyrinth[col]):
        # R
        if labyrinth[col][row + 1] in movabletiles or omg_why_you_do_this(labyrinth, col, row + 1):
            did_move, poison, pchp = lab_checker(labyrinth, col, row + 1, triggertraptiles, walltraptiles, pchp, movabletiles, startcol, startrow, poison, poisoncounter)
            if did_move:
                return True, poison, pchp

    if col + 1 < len(labyrinth):
        # D
        if labyrinth[col + 1][row] in movabletiles or omg_why_you_do_this(labyrinth, col + 1, row):
            did_move, poison, pchp = lab_checker(labyrinth, col + 1, row, triggertraptiles, walltraptiles, pchp, movabletiles, startcol, startrow, poison, poisoncounter)
            if did_move:
                return True, poison, pchp

    if row - 1 >= 0:
        # L
        if labyrinth[col][row - 1] in movabletiles or omg_why_you_do_this(labyrinth, col, row - 1):
            did_move, poison, pchp = lab_checker(labyrinth, col, row - 1, triggertraptiles, walltraptiles, pchp, movabletiles, startcol, startrow, poison, poisoncounter)
            if did_move:
                return True, poison, pchp

    if col - 1 >= 0:
        # U
        if labyrinth[col - 1][row] in movabletiles or omg_why_you_do_this(labyrinth, col - 1, row):
            did_move, poison, pchp = lab_checker(labyrinth, col - 1, row, triggertraptiles, walltraptiles, pchp, movabletiles, startcol, startrow, poison, poisoncounter)
            if did_move:
                return True, poison, pchp

            else:

                return False, poison, pchp
        else:

            return False, poison, pchp
    else:
        return False, poison, pchp


def lab_checker(labyrinth, col, row, triggertraptiles, walltraptiles, lchp, movabletiles, startcol, startrow, poison, poisoncounter):
    poisontile=False
    if trap_checker(labyrinth, col, row, movabletiles):
        for i in range(len(movabletiles[2])):
            if labyrinth[col][row] == ("S" + f'{i + 1}'):
                labyrinth[walltraptiles[i][0]][walltraptiles[i][1]] = "X"

    if findpoison(labyrinth, col, row, movabletiles):
        poison = True
        poisontile=True
        poisoncounter = 2
    did_hurt, how_much_did_it_hurt = damage_check(labyrinth, col, row)
    if did_hurt:
        lchp -= how_much_did_it_hurt

    # if damage_check(labyrinth, col, row, movabletiles):
    #     lchp -= 1
    # if healthcheck(labyrinth, col, row, movabletiles):
    #     lchp += 1
    did_heal, how_much_did_it_heal = healthcheck(labyrinth, col, row)
    if did_heal:
        lchp += how_much_did_it_heal

    if lchp <= 0  and poison==False:
        comebacktolife = return_health(labyrinth,col,row)
        return False, poison, lchp+comebacktolife

    if lchp <=0 and poison == True:
        lchp+=1
        return False, poison, lchp

    labyrinth[col][row] = '⬛'

    if col != startcol or row != startrow:
        if answer_check(labyrinth, col, row):
            return True, poison, lchp

    if poison:
        poisoncounter -= 1
        if poisoncounter < 0:
            lchp -= 1
            poisoncounter = 2
            if lchp == 0:
                labyrinth[col][row] = '-'
                return False, poison, lchp


    did_move, poison, lchp = place_checker(labyrinth, col, row, triggertraptiles, walltraptiles, lchp, movabletiles, startcol, startrow, poison, poisoncounter)



    if did_move:
        return True, poison, lchp
    else:
        labyrinth[col][row] = '-'
        replace_traps(labyrinth, triggertraptiles, walltraptiles, col, row)
        if poison==True:
            poisoncounter+=2
        redo_traps(labyrinth, col, row, triggertraptiles, walltraptiles)
        if poisontile:
            replace_poison(labyrinth, col, row)
        if poisoncounter>3:
            lchp +=1
            poisoncounter=0
        redo_health_tiles(labyrinth,col,row,movabletiles)
        lchp = return_hp_heal(labyrinth,col,row,lchp)
        lchp = return_hp_damage(labyrinth,col,row,lchp)
        return False, poison, lchp


def lab_start(labyrinth, col, row,hp):
    startingcell = [
        'O'
    ]
    predetermined_start = True
    if predetermined_start:
        col, row = find_predetermined_start(labyrinth, startingcell)

    startcol = col
    startrow = row
    poison = False
    poisoncounter = 2

    triggertraptiles = [

    ]
    walltraptiles = [

    ]

    triggertraptiles, triggerc = find_trap_triggers(labyrinth, triggertraptiles)

    walltraptiles, triggerw = find_trap_walls(labyrinth, walltraptiles)

    traptiles = [

    ]
    for i in range(triggerc):
        traptiles.append('S' + f'{i}')

    damagetiles = [

    ]

    healthtiles = [

    ]


    damagetiles,amount_damaged_list=find_damage_tiles(labyrinth,damagetiles)
    healthtiles,amount_healed_list=find_health_tiles(labyrinth,healthtiles)
    poisontiles = [
        'V'
    ]



    trapwalltiles = [

    ]
    for i in range(triggerw):
        trapwalltiles.append("T" + f'{i}')

    movabletiles = [
        healthtiles,amount_healed_list ,damagetiles,amount_damaged_list, traptiles, poisontiles, trapwalltiles, '-', ''
    ]

    movabletiles = appendtiles(movabletiles)

    did_finish, poison, fhp = lab_checker(labyrinth, col, row, triggertraptiles, walltraptiles, hp, movabletiles, startcol, startrow, poison,
                                          poisoncounter)

    if did_finish:
        return labyrinth, True, fhp
    else:
        return labyrinth, False, fhp


ystart = 1
xstart = 0

labyrinth, is_solved, hp = lab_start(labyrinth, ystart, xstart, HP)

printlab(labyrinth)

if is_solved:
    print(f"Si se pudo resolver el laberinto")
    print(f"Con {hp} de vida restante")
else:
    print("No se pudo resolver el laberinto")
    print("No hay salida")
