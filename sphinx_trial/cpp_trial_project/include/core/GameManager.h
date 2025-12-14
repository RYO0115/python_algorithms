#ifndef GAMEMANAGER_H
#define GAMEMANAGER_H

#include "models/Hero.h"
#include "models/Monster.h"
#include <memory>

/**
 * @brief Manages the game flow and battle logic.
 *
 * This class handles the initialization of the game, the battle loop,
 * and the interaction between the Hero and the Monster.
 */
class GameManager {
public:
    /**
     * @brief Constructor for GameManager.
     *
     * Initializes the random number generator.
     */
    GameManager();

    /**
     * @brief Starts the game.
     *
     * Sets up the characters and begins the battle loop.
     */
    void start();

private:
    /**
     * @brief Executes the main battle loop.
     *
     * Continues until either the Hero or the Monster is defeated.
     */
    void battle();

    /**
     * @brief Executes the Hero's turn.
     *
     * Handles player input for attacking or using skills.
     */
    void heroTurn();

    /**
     * @brief Executes the Monster's turn.
     *
     * Handles the monster's AI logic.
     */
    void monsterTurn();

    /**
     * @brief Displays the current status of the characters.
     */
    void showStatus();

    std::unique_ptr<Hero> hero;       ///< Pointer to the player's Hero.
    std::unique_ptr<Monster> monster; ///< Pointer to the enemy Monster.
};

#endif // GAMEMANAGER_H
