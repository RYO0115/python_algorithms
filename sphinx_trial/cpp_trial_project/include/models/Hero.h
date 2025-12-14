#ifndef HERO_H
#define HERO_H

#include "models/Character.h"
#include "models/Skill.h"
#include <vector>

/**
 * @brief Represents the player's character (Hero).
 *
 * Inherits from Character and adds mana points (MP) and skill capabilities.
 */
class Hero : public Character {
public:
    /**
     * @brief Constructor for Hero.
     *
     * @param name The name of the hero.
     * @param hp The initial HP.
     * @param attackPower The base attack power.
     * @param mp The initial MP.
     */
    Hero(std::string name, int hp, int attackPower, int mp);

    /**
     * @brief Attacks a target character.
     *
     * Overrides the base attack method to include critical hit logic or other hero-specific mechanics.
     *
     * @param target The character to attack.
     */
    void attack(Character& target) override;

    /**
     * @brief Uses a skill on a target.
     *
     * @param skill The skill to use.
     * @param target The target of the skill.
     */
    void useSkill(const Skill& skill, Character& target);

    /**
     * @brief Heals the hero by a specified amount.
     *
     * @param amount The amount of HP to recover.
     */
    void heal(int amount);

    /**
     * @brief Recovers MP by a specified amount.
     *
     * @param amount The amount of MP to recover.
     */
    void recoverMp(int amount);

    /**
     * @brief Attempts to pay a specified amount of MP.
     *
     * @param amount The amount of MP to spend.
     * @return true if MP was sufficient and spent, false otherwise.
     */
    bool payMp(int amount);

    /**
     * @brief Gets the current MP.
     * @return The current MP.
     */
    int getMp() const;

    /**
     * @brief Gets the maximum MP.
     * @return The maximum MP.
     */
    int getMaxMp() const;

    /**
     * @brief Gets the list of skills learned by the hero.
     * @return A constant reference to the vector of skills.
     */
    const std::vector<Skill>& getSkills() const;

    /**
     * @brief Adds a skill to the hero's repertoire.
     *
     * @param skill The skill to learn.
     */
    void addSkill(const Skill& skill);

private:
    int mp;    ///< Current Magic Points.
    int maxMp; ///< Maximum Magic Points.
    std::vector<Skill> skills; ///< List of learned skills.
};

#endif // HERO_H
