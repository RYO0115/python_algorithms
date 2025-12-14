#ifndef CHARACTER_H
#define CHARACTER_H

#include <string>
#include <iostream>

/**
 * @brief Abstract base class for all characters in the game.
 *
 * Defines common attributes like name, HP, and attack power,
 * as well as common behaviors like taking damage.
 */
class Character {
public:
    /**
     * @brief Constructor for Character.
     *
     * @param name The name of the character.
     * @param hp The initial (and maximum) hit points.
     * @param attackPower The base attack power.
     */
    Character(std::string name, int hp, int attackPower);

    /**
     * @brief Virtual destructor.
     */
    virtual ~Character() = default;

    /**
     * @brief Pure virtual function for attacking a target.
     *
     * @param target The character to attack.
     */
    virtual void attack(Character& target) = 0;

    /**
     * @brief Inflicts damage on the character.
     *
     * Reduces HP by the specified amount. HP will not drop below 0.
     *
     * @param damage The amount of damage to take.
     */
    virtual void takeDamage(int damage);

    /**
     * @brief Checks if the character is dead.
     *
     * @return true if HP is 0 or less, false otherwise.
     */
    bool isDead() const;

    /**
     * @brief Gets the character's name.
     * @return The name of the character.
     */
    std::string getName() const;

    /**
     * @brief Gets the current HP.
     * @return The current hit points.
     */
    int getHp() const;

    /**
     * @brief Gets the maximum HP.
     * @return The maximum hit points.
     */
    int getMaxHp() const;

    /**
     * @brief Gets the attack power.
     * @return The attack power.
     */
    int getAttackPower() const;

protected:
    std::string name; ///< The name of the character.
    int hp;           ///< Current hit points.
    int maxHp;        ///< Maximum hit points.
    int attackPower;  ///< Base attack power.
};

#endif // CHARACTER_H
