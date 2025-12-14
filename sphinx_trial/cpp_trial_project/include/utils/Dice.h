#ifndef DICE_H
#define DICE_H

#include <random>

/**
 * @brief Utility class for random number generation.
 *
 * Uses the Mersenne Twister engine for high-quality random numbers.
 */
class Dice {
public:
    /**
     * @brief Initializes the random number generator.
     *
     * Should be called once at the beginning of the program.
     */
    static void init();

    /**
     * @brief Generates a random integer within a specified range.
     *
     * @param min The minimum value (inclusive).
     * @param max The maximum value (inclusive).
     * @return A random integer between min and max.
     */
    static int get(int min, int max);

private:
    static std::mt19937 mt; ///< Mersenne Twister random number generator.
};

#endif // DICE_H
