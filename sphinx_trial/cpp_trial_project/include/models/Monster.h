#ifndef MONSTER_H
#define MONSTER_H

#include "models/Character.h"

class Monster : public Character {
public:
    Monster(std::string name, int hp, int attackPower);

    void attack(Character& target) override;
    void performAction(Character& target); // AI logic
};

#endif // MONSTER_H
