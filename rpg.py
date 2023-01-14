import random
class  Player:
    def __init__(self,name,hp,damage):
        self.name=name
        self.hp=hp
        self.damage=damage
        self.lvl=1
        self.exp=0
    def create_hero(name,species,prof):
        name=name
        hp=0
        damage=0
        if species==species_list[0]:
            hp+=100
            damage+=50
        elif species==species_list[1]:
            hp+=50
            damage+=100
        if prof==prof_list[0]:
            hp+=100
            damage+=50
        elif prof==prof_list[1]:
            hp+=50
            damage+=100
        else:
            print('i dont know who you are')
        return Player(name,hp,damage)
    def attack(self,enemy):
        max_exp=self.lvl*100
        enemy.hp-=self.damage
        if enemy.hp<=0:
            print('yay u beat',enemy.name,'!')
            print('You got 20 XP')
            self.exp+=20
            if self.exp>=max_exp:
                self.lvlup(max_exp)
            thing=random.randint(0,3)
            if thing==1:
                wpn=self.create_weapon()
                print(f'you got a weapon. {wpn[0]}{wpn[1]}')
            elif thing==2:
                armor=self.create_armor()
                print('you got armor. {armor[0]}{armor[1]}')
            else:
                print('you didnt get anything.')
            return False
        else:
            print('name of enemy:',enemy.name,'remaining health of enemy: ',enemy.hp)
            return True
    def lvlup(self,max_exp):
        self.exp-=max_exp
        self.lvl+=1
        self.damage+=self.lvl*5
        self.hp+=self.lvl*10
        print('You leveled up!')
        print('Your level is now',self.lvl,'!')
    def create_weapon(self):
        wpn_type=weapon_type_list[random.randint(0,2)]
        wpn_rare = random.choice(list(weapon_rare_dict.keys()))
        if wpn_type == weapon_type_list[0]:
            self.damage +=4*rnd_wpn_rare
        elif wpn_type==weapon_type_list[1]:
            self.damage +=5*rnd_wpn_rare
        elif wpn_type == weapon_type_list[2]:
            self.damage +=6*rnd_wpn_rare
        return wpn_type,weapon_rare_dict[wpn_rare]
    def create_armor(self):
        armor_type=armor_type_list[ramdom.randint(0,2)]
        armor_rarity=random.choice(list(armor_rarity_dict.keys()))
        if armor_type==armor_type_list[0]:
            self.hp+=4*rnd_armor_rare
        elif armor_type==armor_type_list[1]:
            self.hp+=5*rnd_armor_rare
        elif armor_type==armor_type_list[2]:
            self.hp+=6*rnd_armor_rare
        return armor_type,armor_rarity_dict[rnd_armor_rarity]
class Enemy:
    def __init__(self,name,hp,damage):
        self.name=name
        self.hp=hp
        self.damage=damage
    def create_enemy():
        rnd_name=random.choice(enemy_name_list)
        rnd_hp=random.randint(50,200)
        rnd_damage=random.randint(30,70)
        return Enemy(rnd_name,rnd_hp,rnd_damage)
    def attack(self,victim):
        victim.hp-=self.damage
        if victim.hp<=0:
            print('you lost to',self.name,'.') 
            return True
        else: 
            print('remaining health:',victim.hp)
            return False
def fight_choice():
    answer=input(f'Ready to fight{enemy.name}?(answer "yes" or "no")').lower()
    if  answer=='yes':
        result=hero.attack(enemy)
        if result==True     :
            enemy.attack(hero)
            fight_choice()
    elif answer=='no':
        event=random.randint(1,2)
        if event==1:
            print('you ran from',enemy.name,'!')
        elif event==2:
            print('You failed to run from',enemy.name,'!')
            enemy.attack(hero)
            fight_choice()
    else:
        print('i do not understand what you said.')
        fight_choice()
my_name=input("type a name: ")
prof_list=['archer','warrior']
enemy_name_list=[' Minotaur',' Draugr',' Gorgon',' Demogorgon']
species_list=['elf','gnome']
weapon_type_list=['sword','bow','spear']
weapon_rarity_dict={1:'common', 2:'rare', 3:'epic',}
armor_type_list=['helmet','barrier','shield']
armor_rarity_dict={1:'common',2:'rare',3:'epic'}
print(species_list)
my_species=input("choose a species: ")
print(prof_list)
my_prof=input('choose a job: ')
hero=Player.create_hero(my_name,my_species,my_prof)
print(hero.name,hero.hp,hero.damage,hero.lvl,hero.exp)
enemy=Enemy.create_enemy()
while 2>1:
    event=random.randint(1,2)
    if event==1:
        print("You did not find a monster")
        print('You search again')
    elif event==2:
        enemy=Enemy.create_enemy()
        print('You found',enemy.name)
        fight_choice()
        answer=input(f'Do you want to quit?').lower()
        if answer=='yes':
            print('Shutting down...')
            break
