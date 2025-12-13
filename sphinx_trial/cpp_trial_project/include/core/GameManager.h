#ifndef GAMEMANAGER_H
#define GAMEMANAGER_H

#include "models/Hero.h"
#include "models/Monster.h"
#include <memory>

class GameManager {
public:
    GameManager();
    void start();

private:
    void battle();
    void heroTurn();
    void monsterTurn();
    void showStatus();

    std::unique_ptr<Hero> hero;
    std::unique_ptr<Monster> monster;
};

#endif // GAMEMANAGER_H
