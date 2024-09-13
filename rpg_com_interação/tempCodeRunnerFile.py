  if choice == "1":
            enemy.hp -= player.attack
            print(f"{player.name} attacks {enemy.name}!")
            time.sleep(1)
            print(f"{enemy.name} HP: {enemy.hp}\n")
        elif choice == "2":
            print("You ran away successfully!")
            return False
        
        # Enemy's turn
        player.hp -= enemy.attack
        print(f"{enemy.name} attacks {player.name}!")
        time.sleep(1)
        print(f"{player.name} HP: {player.hp}\n")
    
    if player.is_alive():
        print(f"{enemy.name} was defeated!")
        return True
    else:
        print(f"{player.name} was defeated...")
        return False

def main():
    print("Welcome to the Adventure RPG!\n")
    player_name = input("Enter your name: ")
    player = Player(player_name, 100, 10)
    enemies = [Enemy("Goblin", 50, 5), Enemy("Orc", 80, 8), Enemy("Dragon", 150, 15)]

    print("\nLet's start your adventure!\n")
    for enemy in enemies:
        if battle(player, enemy):
            print("You continue your journey...\n")
        else:
            print("Game Over")
            break
    else:
        print("Congratulations! You defeated all the enemies and completed your adventure!")

if __name__ == "__main__":
    main()
