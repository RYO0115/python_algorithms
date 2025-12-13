#include "core/GameManager.h"
#include "utils/Dice.h"
#include <iostream>
#include <limits>

GameManager::GameManager() {
    Dice::init();
}

void GameManager::start() {
    std::cout << "Welcome to the RPG Battle Simulator!" << std::endl;
    std::string name;
    std::cout << "Enter Hero's name: ";
    std::cin >> name;

    hero = std::make_unique<Hero>(name, 100, 20, 30);
    hero->addSkill(Skill("Fireball", 10, 30, SkillType::ATTACK));
    hero->addSkill(Skill("Heal", 8, 40, SkillType::HEAL));

    monster = std::make_unique<Monster>("Goblin", 80, 15);

    std::cout << "A wild " << monster->getName() << " appeared!" << std::endl;
    battle();
}

void GameManager::battle() {
    int turn = 1;
    while (!hero->isDead() && !monster->isDead()) {
        std::cout << "\n--- Turn " << turn << " ---" << std::endl;
        showStatus();

        heroTurn();
        if (monster->isDead()) break;

        monsterTurn();
        if (hero->isDead()) break;

        turn++;
    }

    if (hero->isDead()) {
        std::cout << "\n" << hero->getName() << " was defeated... Game Over." << std::endl;
    } else {
        std::cout << "\n" << monster->getName() << " was defeated! You Win!" << std::endl;
    }
}

void GameManager::showStatus() {
    std::cout << hero->getName() << " - HP: " << hero->getHp() << "/" << hero->getMaxHp() 
              << " MP: " << hero->getMp() << "/" << hero->getMaxMp() << std::endl;
    std::cout << monster->getName() << " - HP: " << monster->getHp() << "/" << monster->getMaxHp() << std::endl;
}

void GameManager::heroTurn() {
    std::cout << "Choose action: 1. Attack  2. Skill" << std::endl;
    int choice;
    while (true) {
        std::cout << "> ";
        std::cin >> choice;
        if (std::cin.fail()) {
            std::cin.clear();
            std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
            continue;
        }

        if (choice == 1) {
            hero->attack(*monster);
            break;
        } else if (choice == 2) {
            const auto& skills = hero->getSkills();
            std::cout << "Choose skill:" << std::endl;
            for (size_t i = 0; i < skills.size(); ++i) {
                std::cout << i + 1 << ". " << skills[i].getName() 
                          << " (MP: " << skills[i].getMpCost() << ")" << std::endl;
            }
            std::cout << "0. Back" << std::endl;

            int skillChoice;
            std::cout << "> ";
            std::cin >> skillChoice;

            if (skillChoice > 0 && skillChoice <= (int)skills.size()) {
                const auto& skill = skills[skillChoice - 1];
                if (hero->payMp(skill.getMpCost())) {
                    hero->useSkill(skill, *monster);
                    break;
                } else {
                    std::cout << "Not enough MP!" << std::endl;
                }
            }
        }
    }
}

void GameManager::monsterTurn() {
    monster->performAction(*hero);
}
