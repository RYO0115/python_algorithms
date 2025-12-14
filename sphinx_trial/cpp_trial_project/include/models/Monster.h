#ifndef MONSTER_H
#define MONSTER_H

#include "models/Character.h"

/**
 * @brief Represents an enemy character (Monster).
 *
 * Inherits from Character and includes AI logic for battle actions.
 */
class Monster : public Character {
public:
    /**
     * @brief Constructor for Monster.
     *
     * @param name The name of the monster.
     * @param hp The initial HP.
     * @param attackPower The base attack power.
     */
    Monster(std::string name, int hp, int attackPower);

    /**
     * @brief Attacks a target character.
     *
     * @param target The character to attack.
     */
    void attack(Character& target) override;

    /**
     * @brief Performs an action during the monster's turn.
     *
     * Decides whether to attack or perform other actions based on AI logic.
     *
     * @param target The target of the action (usually the Hero).
     */
    void performAction(Character& target);
};

#endif // MONSTER_H
