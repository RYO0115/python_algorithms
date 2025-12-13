#ifndef SKILL_H
#define SKILL_H

#include <string>

enum class SkillType {
    ATTACK,
    HEAL
};

class Skill {
public:
    Skill(std::string name, int mpCost, int power, SkillType type);

    std::string getName() const;
    int getMpCost() const;
    int getPower() const;
    SkillType getType() const;

private:
    std::string name;
    int mpCost;
    int power;
    SkillType type;
};

#endif // SKILL_H
