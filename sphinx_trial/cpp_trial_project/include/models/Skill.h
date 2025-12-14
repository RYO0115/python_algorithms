#ifndef SKILL_H
#define SKILL_H

#include <string>

/**
 * @brief Enumeration of skill types.
 */
enum class SkillType {
    ATTACK, ///< Offensive skill that deals damage.
    HEAL    ///< Support skill that restores HP.
};

/**
 * @brief Represents a skill or ability.
 *
 * A skill has a name, MP cost, power (damage or heal amount), and a type.
 */
class Skill {
public:
    /**
     * @brief Constructor for Skill.
     *
     * @param name The name of the skill.
     * @param mpCost The MP cost to use the skill.
     * @param power The power of the skill (damage or healing amount).
     * @param type The type of the skill (ATTACK or HEAL).
     */
    Skill(std::string name, int mpCost, int power, SkillType type);

    /**
     * @brief Gets the name of the skill.
     * @return The skill name.
     */
    std::string getName() const;

    /**
     * @brief Gets the MP cost of the skill.
     * @return The MP cost.
     */
    int getMpCost() const;

    /**
     * @brief Gets the power of the skill.
     * @return The power value.
     */
    int getPower() const;

    /**
     * @brief Gets the type of the skill.
     * @return The skill type.
     */
    SkillType getType() const;

private:
    std::string name; ///< The name of the skill.
    int mpCost;       ///< The MP cost required to use the skill.
    int power;        ///< The power of the skill.
    SkillType type;   ///< The type of the skill.
};

#endif // SKILL_H
