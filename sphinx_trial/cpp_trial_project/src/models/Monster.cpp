#include "models/Monster.h"
#include "utils/Dice.h"
#include <iostream>

Monster::Monster(std::string name, int hp, int attackPower)
    : Character(name, hp, attackPower) {}

void Monster::attack(Character& target) {
    int damage = Dice::get(attackPower - 2, attackPower + 2);
    std::cout << name << " attacks " << target.getName() << "!" << std::endl;
    target.takeDamage(damage);
}

void Monster::performAction(Character& target) {
    // Simple AI: 20% chance to do a strong attack (if we had skills), otherwise normal attack
    // For now, just attack
    attack(target);
}
