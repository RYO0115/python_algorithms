#include "models/Skill.h"

Skill::Skill(std::string name, int mpCost, int power, SkillType type)
    : name(name), mpCost(mpCost), power(power), type(type) {}

std::string Skill::getName() const {
    return name;
}

int Skill::getMpCost() const {
    return mpCost;
}

int Skill::getPower() const {
    return power;
}

SkillType Skill::getType() const {
    return type;
}
