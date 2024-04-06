import random

def opcion():
  opcion_PC = ('Piedra','Papel','Tijera')
  print('Elige Piedra, Papel o Tijera')
  user = input('Elige => ')
  user = user.capitalize()
  if user not in opcion_PC:
    print('esa opcion no es valida')
    return None, None
    # continue
  
  PC = random.choice(opcion_PC)
  print('name Eligio =>', user)
  print('PC elige =>', PC)
  
  
  
  return user, PC


def combate(PC,user,wins_user,wins_pc):
  if user == PC:
    print('Empate')
  elif user == 'Piedra':
    if PC == 'Tigera':
        print('Piedra Gana a Tijera')
        print('user Gana')
        wins_user += 1
    else:
        print('Papel Gana a Piedra')
        print('PC gana =>')
        wins_pc += 1
  elif user == 'Papel':
    if PC == 'Piedra':
        print('Papel Gana a Piedra')
        print('User gana')
        wins_user += 1
    else:
        print('Tigera le Gana a Papel')
        print('PC gana')
        wins_pc += 1
  elif user == 'Tijera':
    if PC == 'Papel':
        print('Tijera Gana a Papel')
        print('User Gana')
        wins_user += 1
    else:
        print('Piedra le Gana a Tijera')
        print('PC gana')
        wins_pc += 1   
  return wins_user, wins_pc

def run_game():
  wins_user = 0
  wins_pc = 0
  rounds = 1
  while True:

      print('*' * 10)
      print('ROUND', rounds)
      print('*' * 10)

      print('computer_wins', wins_pc)
      print('user_wins', wins_user)
      rounds += 1

      user, PC = opcion()
      wins_user,wins_pc = combate(PC,user,wins_user,wins_pc)

      if wins_pc == 3:
        print('El ganador es la computadora')
        break

      if wins_user == 3:
        print('El ganador es el usuario')
        break

run_game()
