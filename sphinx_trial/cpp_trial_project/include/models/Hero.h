#ifndef HERO_H
#define HERO_H

#include "models/Character.h"
#include "models/Skill.h"
#include <vector>

class Hero : public Character {
public:
    Hero(std::string name, int hp, int attackPower, int mp);

    void attack(Character& target) override;
    void useSkill(const Skill& skill, Character& target);
    void heal(int amount);
    void recoverMp(int amount);
    bool payMp(int amount);

    int getMp() const;
    int getMaxMp() const;
    const std::vector<Skill>& getSkills() const;
    void addSkill(const Skill& skill);

private:
    int mp;
    int maxMp;
    std::vector<Skill> skills;
};

#endif // HERO_H
