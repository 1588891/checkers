
symbol = '='
list1 = ['O','O','O','O','O','O','O','O','O','O','O','O',' ',' ',' ',' ',' ',' ',' ',' ','X','X','X','X','X','X','X','X','X','X','X','X']
board =  f'||{symbol * 38}||\n||   || {list1[0]} ||   || {list1[1]} ||   || {list1[2]} ||   || {list1[3]} ||\n||{symbol * 38}||\n|| {list1[4]} ||   || {list1[5]} ||   || {list1[6]} ||   || {list1[7]} ||   ||\n||{symbol * 38}||\n||   || {list1[8]} ||   || {list1[9]} ||   || {list1[10]} ||   || {list1[11]} ||\n||{symbol * 38}||\n|| {list1[12]} ||   || {list1[13]} ||   || {list1[14]} ||   || {list1[15]} ||   ||\n||{symbol * 38}||\n||   || {list1[16]} ||   || {list1[17]} ||   || {list1[18]} ||   || {list1[19]} ||\n||{symbol * 38}||\n|| {list1[20]} ||   || {list1[21]} ||   || {list1[22]} ||   || {list1[23]} ||   ||\n||{symbol * 38}||\n||   || {list1[24]} ||   || {list1[25]} ||   || {list1[26]} ||   || {list1[27]} ||\n||{symbol * 38}||\n|| {list1[28]} ||   || {list1[29]} ||   || {list1[30]} ||   || {list1[31]} ||   ||\n||{symbol * 38}||'
grid = f'||{symbol * 38}||\n||   || 0 ||   || 1 ||   || 2 ||   || 3 ||\n||{symbol * 38}||\n|| 4 ||   || 5 ||   || 6 ||   || 7 ||   ||\n||{symbol * 38}||\n||   || 8 ||   || 9 ||   ||10 ||   ||11 ||\n||{symbol * 38}||\n||12 ||   ||13 ||   ||14 ||   ||15 ||   ||\n||{symbol * 38}||\n||   ||16 ||   ||17 ||   ||18 ||   ||19 ||\n||{symbol * 38}||\n||20 ||   ||21 ||   ||22 ||   ||23 ||   ||\n||{symbol * 38}||\n||   ||24 ||   ||25 ||   ||26 ||   ||27 ||\n||{symbol * 38}||\n||28 ||   ||29 ||   ||30 ||   ||31 ||   ||\n||{symbol * 38}||'

def checker_moves(current_place, destination):
    destination = int(destination)
    current_place = int(current_place)
    
    
    
    if list1[destination] != list1[current_place] and destination - current_place <= 5 and list1[current_place] == 'O' and destination - current_place >= 4 and list1[destination] != 'X':
        list1[destination] = list1[current_place]
        list1[current_place] = ' '
        board =  f'||{symbol * 38}||\n||   || {list1[0]} ||   || {list1[1]} ||   || {list1[2]} ||   || {list1[3]} ||\n||{symbol * 38}||\n|| {list1[4]} ||   || {list1[5]} ||   || {list1[6]} ||   || {list1[7]} ||   ||\n||{symbol * 38}||\n||   || {list1[8]} ||   || {list1[9]} ||   || {list1[10]} ||   || {list1[11]} ||\n||{symbol * 38}||\n|| {list1[12]} ||   || {list1[13]} ||   || {list1[14]} ||   || {list1[15]} ||   ||\n||{symbol * 38}||\n||   || {list1[16]} ||   || {list1[17]} ||   || {list1[18]} ||   || {list1[19]} ||\n||{symbol * 38}||\n|| {list1[20]} ||   || {list1[21]} ||   || {list1[22]} ||   || {list1[23]} ||   ||\n||{symbol * 38}||\n||   || {list1[24]} ||   || {list1[25]} ||   || {list1[26]} ||   || {list1[27]} ||\n||{symbol * 38}||\n|| {list1[28]} ||   || {list1[29]} ||   || {list1[30]} ||   || {list1[31]} ||   ||\n||{symbol * 38}||'
        return board
    
    
    
    
    
    elif list1[destination] != list1[current_place] and current_place - destination <= 5 and list1[current_place] == 'X' and current_place - destination >= 3:
        list1[destination] = list1[current_place]
        list1[current_place] = ' '
        board =  f'||{symbol * 38}||\n||   || {list1[0]} ||   || {list1[1]} ||   || {list1[2]} ||   || {list1[3]} ||\n||{symbol * 38}||\n|| {list1[4]} ||   || {list1[5]} ||   || {list1[6]} ||   || {list1[7]} ||   ||\n||{symbol * 38}||\n||   || {list1[8]} ||   || {list1[9]} ||   || {list1[10]} ||   || {list1[11]} ||\n||{symbol * 38}||\n|| {list1[12]} ||   || {list1[13]} ||   || {list1[14]} ||   || {list1[15]} ||   ||\n||{symbol * 38}||\n||   || {list1[16]} ||   || {list1[17]} ||   || {list1[18]} ||   || {list1[19]} ||\n||{symbol * 38}||\n|| {list1[20]} ||   || {list1[21]} ||   || {list1[22]} ||   || {list1[23]} ||   ||\n||{symbol * 38}||\n||   || {list1[24]} ||   || {list1[25]} ||   || {list1[26]} ||   || {list1[27]} ||\n||{symbol * 38}||\n|| {list1[28]} ||   || {list1[29]} ||   || {list1[30]} ||   || {list1[31]} ||   ||\n||{symbol * 38}||'
        return board
    
    
    
    
    
    
    elif list1[current_place] == 'O' and list1[destination] == 'X':
        if destination - current_place == 4 and current_place == 4 or current_place == 5 or current_place == 6 or current_place == 12 or current_place == 13 or current_place == 14 or current_place == 20 or current_place == 21 or current_place == 22:
            num1 = destination - current_place 
            num1 += 1
            num1 += destination
            if list1[num1] != 'O' and list1[num1] != 'X':
                list1[num1] = list1[current_place]
                list1[current_place] = ' '
                list1[destination] = ' '
                board =  f'||{symbol * 38}||\n||   || {list1[0]} ||   || {list1[1]} ||   || {list1[2]} ||   || {list1[3]} ||\n||{symbol * 38}||\n|| {list1[4]} ||   || {list1[5]} ||   || {list1[6]} ||   || {list1[7]} ||   ||\n||{symbol * 38}||\n||   || {list1[8]} ||   || {list1[9]} ||   || {list1[10]} ||   || {list1[11]} ||\n||{symbol * 38}||\n|| {list1[12]} ||   || {list1[13]} ||   || {list1[14]} ||   || {list1[15]} ||   ||\n||{symbol * 38}||\n||   || {list1[16]} ||   || {list1[17]} ||   || {list1[18]} ||   || {list1[19]} ||\n||{symbol * 38}||\n|| {list1[20]} ||   || {list1[21]} ||   || {list1[22]} ||   || {list1[23]} ||   ||\n||{symbol * 38}||\n||   || {list1[24]} ||   || {list1[25]} ||   || {list1[26]} ||   || {list1[27]} ||\n||{symbol * 38}||\n|| {list1[28]} ||   || {list1[29]} ||   || {list1[30]} ||   || {list1[31]} ||   ||\n||{symbol * 38}||'
                return board
            else:
                print('Invalid Move!')
                board =  f'||{symbol * 38}||\n||   || {list1[0]} ||   || {list1[1]} ||   || {list1[2]} ||   || {list1[3]} ||\n||{symbol * 38}||\n|| {list1[4]} ||   || {list1[5]} ||   || {list1[6]} ||   || {list1[7]} ||   ||\n||{symbol * 38}||\n||   || {list1[8]} ||   || {list1[9]} ||   || {list1[10]} ||   || {list1[11]} ||\n||{symbol * 38}||\n|| {list1[12]} ||   || {list1[13]} ||   || {list1[14]} ||   || {list1[15]} ||   ||\n||{symbol * 38}||\n||   || {list1[16]} ||   || {list1[17]} ||   || {list1[18]} ||   || {list1[19]} ||\n||{symbol * 38}||\n|| {list1[20]} ||   || {list1[21]} ||   || {list1[22]} ||   || {list1[23]} ||   ||\n||{symbol * 38}||\n||   || {list1[24]} ||   || {list1[25]} ||   || {list1[26]} ||   || {list1[27]} ||\n||{symbol * 38}||\n|| {list1[28]} ||   || {list1[29]} ||   || {list1[30]} ||   || {list1[31]} ||   ||\n||{symbol * 38}||'
                return board
        elif destination - current_place == 5 and current_place == 0 or current_place == 1 or current_place == 2 or current_place == 8 or current_place == 9 or current_place == 10 or current_place == 16 or current_place == 17 or current_place == 18:
            num2 = destination - current_place
            num2 -= 1
            num2 += destination
            if list1[num2] != 'O' and list1[num2] != 'X':
                list1[num2] = list1[current_place]
                list1[current_place] = ' '
                list1[destination] = ' '
                board =  f'||{symbol * 38}||\n||   || {list1[0]} ||   || {list1[1]} ||   || {list1[2]} ||   || {list1[3]} ||\n||{symbol * 38}||\n|| {list1[4]} ||   || {list1[5]} ||   || {list1[6]} ||   || {list1[7]} ||   ||\n||{symbol * 38}||\n||   || {list1[8]} ||   || {list1[9]} ||   || {list1[10]} ||   || {list1[11]} ||\n||{symbol * 38}||\n|| {list1[12]} ||   || {list1[13]} ||   || {list1[14]} ||   || {list1[15]} ||   ||\n||{symbol * 38}||\n||   || {list1[16]} ||   || {list1[17]} ||   || {list1[18]} ||   || {list1[19]} ||\n||{symbol * 38}||\n|| {list1[20]} ||   || {list1[21]} ||   || {list1[22]} ||   || {list1[23]} ||   ||\n||{symbol * 38}||\n||   || {list1[24]} ||   || {list1[25]} ||   || {list1[26]} ||   || {list1[27]} ||\n||{symbol * 38}||\n|| {list1[28]} ||   || {list1[29]} ||   || {list1[30]} ||   || {list1[31]} ||   ||\n||{symbol * 38}||'
                return board
            else:
                print('Invalid Move!')
                board =  f'||{symbol * 38}||\n||   || {list1[0]} ||   || {list1[1]} ||   || {list1[2]} ||   || {list1[3]} ||\n||{symbol * 38}||\n|| {list1[4]} ||   || {list1[5]} ||   || {list1[6]} ||   || {list1[7]} ||   ||\n||{symbol * 38}||\n||   || {list1[8]} ||   || {list1[9]} ||   || {list1[10]} ||   || {list1[11]} ||\n||{symbol * 38}||\n|| {list1[12]} ||   || {list1[13]} ||   || {list1[14]} ||   || {list1[15]} ||   ||\n||{symbol * 38}||\n||   || {list1[16]} ||   || {list1[17]} ||   || {list1[18]} ||   || {list1[19]} ||\n||{symbol * 38}||\n|| {list1[20]} ||   || {list1[21]} ||   || {list1[22]} ||   || {list1[23]} ||   ||\n||{symbol * 38}||\n||   || {list1[24]} ||   || {list1[25]} ||   || {list1[26]} ||   || {list1[27]} ||\n||{symbol * 38}||\n|| {list1[28]} ||   || {list1[29]} ||   || {list1[30]} ||   || {list1[31]} ||   ||\n||{symbol * 38}||'
                return board
        elif destination - current_place == 3 and current_place == 5 or current_place == 6 or current_place == 7 or current_place == 13 or current_place == 14 or current_place == 15 or current_place == 21 or current_place == 22 or current_place == 23:
            num3 = destination - current_place
            num3 += 1
            num3 += destination
            if list1[num3] != 'O' and list1[num3] != 'X':
                list1[num3] = list1[current_place]
                list1[current_place] = ' '
                list1[destination] = ' '
                board =  f'||{symbol * 38}||\n||   || {list1[0]} ||   || {list1[1]} ||   || {list1[2]} ||   || {list1[3]} ||\n||{symbol * 38}||\n|| {list1[4]} ||   || {list1[5]} ||   || {list1[6]} ||   || {list1[7]} ||   ||\n||{symbol * 38}||\n||   || {list1[8]} ||   || {list1[9]} ||   || {list1[10]} ||   || {list1[11]} ||\n||{symbol * 38}||\n|| {list1[12]} ||   || {list1[13]} ||   || {list1[14]} ||   || {list1[15]} ||   ||\n||{symbol * 38}||\n||   || {list1[16]} ||   || {list1[17]} ||   || {list1[18]} ||   || {list1[19]} ||\n||{symbol * 38}||\n|| {list1[20]} ||   || {list1[21]} ||   || {list1[22]} ||   || {list1[23]} ||   ||\n||{symbol * 38}||\n||   || {list1[24]} ||   || {list1[25]} ||   || {list1[26]} ||   || {list1[27]} ||\n||{symbol * 38}||\n|| {list1[28]} ||   || {list1[29]} ||   || {list1[30]} ||   || {list1[31]} ||   ||\n||{symbol * 38}||'
                return board
            else:
                print('Invalid Move!')
                board =  f'||{symbol * 38}||\n||   || {list1[0]} ||   || {list1[1]} ||   || {list1[2]} ||   || {list1[3]} ||\n||{symbol * 38}||\n|| {list1[4]} ||   || {list1[5]} ||   || {list1[6]} ||   || {list1[7]} ||   ||\n||{symbol * 38}||\n||   || {list1[8]} ||   || {list1[9]} ||   || {list1[10]} ||   || {list1[11]} ||\n||{symbol * 38}||\n|| {list1[12]} ||   || {list1[13]} ||   || {list1[14]} ||   || {list1[15]} ||   ||\n||{symbol * 38}||\n||   || {list1[16]} ||   || {list1[17]} ||   || {list1[18]} ||   || {list1[19]} ||\n||{symbol * 38}||\n|| {list1[20]} ||   || {list1[21]} ||   || {list1[22]} ||   || {list1[23]} ||   ||\n||{symbol * 38}||\n||   || {list1[24]} ||   || {list1[25]} ||   || {list1[26]} ||   || {list1[27]} ||\n||{symbol * 38}||\n|| {list1[28]} ||   || {list1[29]} ||   || {list1[30]} ||   || {list1[31]} ||   ||\n||{symbol * 38}||'
                return board
        elif destination - current_place == 4 and current_place == 1 or current_place == 2 or current_place == 3 or current_place == 9 or current_place == 10 or current_place == 11 or current_place == 17 or current_place == 18 or current_place == 19:
            num4 = 0
            num4 += destination - current_place
            num4 -= 1
            num4 += destination
            print(num4)
            if list1[num4] != 'O' and list1[num4] != 'X':
                list1[num4] = list1[current_place]
                list1[current_place] = ' '
                list1[destination] = ' '
                board =  f'||{symbol * 38}||\n||   || {list1[0]} ||   || {list1[1]} ||   || {list1[2]} ||   || {list1[3]} ||\n||{symbol * 38}||\n|| {list1[4]} ||   || {list1[5]} ||   || {list1[6]} ||   || {list1[7]} ||   ||\n||{symbol * 38}||\n||   || {list1[8]} ||   || {list1[9]} ||   || {list1[10]} ||   || {list1[11]} ||\n||{symbol * 38}||\n|| {list1[12]} ||   || {list1[13]} ||   || {list1[14]} ||   || {list1[15]} ||   ||\n||{symbol * 38}||\n||   || {list1[16]} ||   || {list1[17]} ||   || {list1[18]} ||   || {list1[19]} ||\n||{symbol * 38}||\n|| {list1[20]} ||   || {list1[21]} ||   || {list1[22]} ||   || {list1[23]} ||   ||\n||{symbol * 38}||\n||   || {list1[24]} ||   || {list1[25]} ||   || {list1[26]} ||   || {list1[27]} ||\n||{symbol * 38}||\n|| {list1[28]} ||   || {list1[29]} ||   || {list1[30]} ||   || {list1[31]} ||   ||\n||{symbol * 38}||'
                return board
            else:
                print('Invalid Move!')
                board =  f'||{symbol * 38}||\n||   || {list1[0]} ||   || {list1[1]} ||   || {list1[2]} ||   || {list1[3]} ||\n||{symbol * 38}||\n|| {list1[4]} ||   || {list1[5]} ||   || {list1[6]} ||   || {list1[7]} ||   ||\n||{symbol * 38}||\n||   || {list1[8]} ||   || {list1[9]} ||   || {list1[10]} ||   || {list1[11]} ||\n||{symbol * 38}||\n|| {list1[12]} ||   || {list1[13]} ||   || {list1[14]} ||   || {list1[15]} ||   ||\n||{symbol * 38}||\n||   || {list1[16]} ||   || {list1[17]} ||   || {list1[18]} ||   || {list1[19]} ||\n||{symbol * 38}||\n|| {list1[20]} ||   || {list1[21]} ||   || {list1[22]} ||   || {list1[23]} ||   ||\n||{symbol * 38}||\n||   || {list1[24]} ||   || {list1[25]} ||   || {list1[26]} ||   || {list1[27]} ||\n||{symbol * 38}||\n|| {list1[28]} ||   || {list1[29]} ||   || {list1[30]} ||   || {list1[31]} ||   ||\n||{symbol * 38}||'
                return board


        
        # board =  f'||{symbol * 38}||\n||   || {list1[0]} ||   || {list1[1]} ||   || {list1[2]} ||   || {list1[3]} ||\n||{symbol * 38}||\n|| {list1[4]} ||   || {list1[5]} ||   || {list1[6]} ||   || {list1[7]} ||   ||\n||{symbol * 38}||\n||   || {list1[8]} ||   || {list1[9]} ||   || {list1[10]} ||   || {list1[11]} ||\n||{symbol * 38}||\n|| {list1[12]} ||   || {list1[13]} ||   || {list1[14]} ||   || {list1[15]} ||   ||\n||{symbol * 38}||\n||   || {list1[16]} ||   || {list1[17]} ||   || {list1[18]} ||   || {list1[19]} ||\n||{symbol * 38}||\n|| {list1[20]} ||   || {list1[21]} ||   || {list1[22]} ||   || {list1[23]} ||   ||\n||{symbol * 38}||\n||   || {list1[24]} ||   || {list1[25]} ||   || {list1[26]} ||   || {list1[27]} ||\n||{symbol * 38}||\n|| {list1[28]} ||   || {list1[29]} ||   || {list1[30]} ||   || {list1[31]} ||   ||\n||{symbol * 38}||'
        # return board
    else:
        print('Invalid Move!')
        board =  f'||{symbol * 38}||\n||   || {list1[0]} ||   || {list1[1]} ||   || {list1[2]} ||   || {list1[3]} ||\n||{symbol * 38}||\n|| {list1[4]} ||   || {list1[5]} ||   || {list1[6]} ||   || {list1[7]} ||   ||\n||{symbol * 38}||\n||   || {list1[8]} ||   || {list1[9]} ||   || {list1[10]} ||   || {list1[11]} ||\n||{symbol * 38}||\n|| {list1[12]} ||   || {list1[13]} ||   || {list1[14]} ||   || {list1[15]} ||   ||\n||{symbol * 38}||\n||   || {list1[16]} ||   || {list1[17]} ||   || {list1[18]} ||   || {list1[19]} ||\n||{symbol * 38}||\n|| {list1[20]} ||   || {list1[21]} ||   || {list1[22]} ||   || {list1[23]} ||   ||\n||{symbol * 38}||\n||   || {list1[24]} ||   || {list1[25]} ||   || {list1[26]} ||   || {list1[27]} ||\n||{symbol * 38}||\n|| {list1[28]} ||   || {list1[29]} ||   || {list1[30]} ||   || {list1[31]} ||   ||\n||{symbol * 38}||'
        return board 
    

print(board)

while True:

    print('\n')
    print(grid)
    user_input1 = input('Type a Number from the Diagram to select a piece to Move:\n--->')
    user_input2 = input('Type a Number to choose where you want your selected piece to go or piece you want to jump:\n--->')

    print(checker_moves(user_input1, user_input2))
    print('\n\n')











 #list1[current_place] == 'O' and destination - current_place >= 7 and destination - current_place <= 9 and destination - current_place != 8: