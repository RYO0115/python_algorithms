#ifndef CHARACTER_H
#define CHARACTER_H

#include <string>
#include <iostream>

class Character {
public:
    Character(std::string name, int hp, int attackPower);
    virtual ~Character() = default;

    virtual void attack(Character& target) = 0;
    virtual void takeDamage(int damage);
    bool isDead() const;

    std::string getName() const;
    int getHp() const;
    int getMaxHp() const;
    int getAttackPower() const;

protected:
    std::string name;
    int hp;
    int maxHp;
    int attackPower;
};

#endif // CHARACTER_H
