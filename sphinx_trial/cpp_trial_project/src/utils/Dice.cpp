#include "utils/Dice.h"
#include <ctime>

std::mt19937 Dice::mt;

void Dice::init() {
    std::random_device rd;
    mt.seed(rd());
}

int Dice::get(int min, int max) {
    std::uniform_int_distribution<int> dist(min, max);
    return dist(mt);
}
