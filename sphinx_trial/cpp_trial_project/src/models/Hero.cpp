#include "models/Hero.h"
#include "utils/Dice.h"
#include <iostream>

Hero::Hero(std::string name, int hp, int attackPower, int mp)
    : Character(name, hp, attackPower), mp(mp), maxMp(mp) {}

void Hero::attack(Character& target) {
    int damage = Dice::get(attackPower - 2, attackPower + 2);
    std::cout << name << " attacks " << target.getName() << "!" << std::endl;
    target.takeDamage(damage);
}

void Hero::useSkill(const Skill& skill, Character& target) {
    std::cout << name << " uses " << skill.getName() << "!" << std::endl;
    if (skill.getType() == SkillType::ATTACK) {
        int damage = skill.getPower(); // Fixed damage for simplicity, or could use Dice
        target.takeDamage(damage);
    } else if (skill.getType() == SkillType::HEAL) {
        heal(skill.getPower());
    }
}

void Hero::heal(int amount) {
    hp += amount;
    if (hp > maxHp) hp = maxHp;
    std::cout << name << " recovered " << amount << " HP!" << std::endl;
}

void Hero::recoverMp(int amount) {
    mp += amount;
    if (mp > maxMp) mp = maxMp;
}

bool Hero::payMp(int amount) {
    if (mp >= amount) {
        mp -= amount;
        return true;
    }
    return false;
}

int Hero::getMp() const {
    return mp;
}

int Hero::getMaxMp() const {
    return maxMp;
}

const std::vector<Skill>& Hero::getSkills() const {
    return skills;
}

void Hero::addSkill(const Skill& skill) {
    skills.push_back(skill);
}
