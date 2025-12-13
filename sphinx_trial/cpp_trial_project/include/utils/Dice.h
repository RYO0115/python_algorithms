#ifndef DICE_H
#define DICE_H

#include <random>

class Dice {
public:
    // Initialize the random number generator
    static void init();

    // Get a random integer between min and max (inclusive)
    static int get(int min, int max);

private:
    static std::mt19937 mt;
};

#endif // DICE_H
