#include "models/Character.h"

Character::Character(std::string name, int hp, int attackPower)
    : name(name), hp(hp), maxHp(hp), attackPower(attackPower) {}

void Character::takeDamage(int damage) {
    hp -= damage;
    if (hp < 0) hp = 0;
    std::cout << name << " took " << damage << " damage!" << std::endl;
}

bool Character::isDead() const {
    return hp <= 0;
}

std::string Character::getName() const {
    return name;
}

int Character::getHp() const {
    return hp;
}

int Character::getMaxHp() const {
    return maxHp;
}

int Character::getAttackPower() const {
    return attackPower;
}
