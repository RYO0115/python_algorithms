# Hero Class

`Hero` クラスは、プレイヤーが操作するキャラクターを表すクラスです。`Character` クラスを継承しています。

## 概要

*   **名前空間**: `models`
*   **ヘッダファイル**: `include/models/Hero.h`
*   **ソースファイル**: `src/models/Hero.cpp`

## 責務

*   MP（マジックポイント）の管理
*   スキルの保持と使用
*   回復処理

## メンバ変数

### `private`

*   `int mp`: 現在のMP
*   `int maxMp`: 最大MP
*   `std::vector<Skill> skills`: 習得しているスキルのリスト

## メンバ関数

### `public`

#### `Hero(std::string name, int hp, int attackPower, int mp)`
*   **説明**: コンストラクタ。

#### `void attack(Character& target) override`
*   **説明**: 通常攻撃を行います。`Dice`を使用してダメージを計算します。

#### `void useSkill(const Skill& skill, Character& target)`
*   **説明**: スキルを使用します。攻撃スキルの場合はダメージを与え、回復スキルの場合は自身を回復します。

#### `void heal(int amount)`
*   **説明**: HPを回復します。最大HPを超えないようにします。

#### `void recoverMp(int amount)`
*   **説明**: MPを回復します。

#### `bool payMp(int amount)`
*   **説明**: MPを消費します。足りない場合は `false` を返します。

#### `int getMp() const`
*   **説明**: 現在のMPを取得します。

#### `int getMaxMp() const`
*   **説明**: 最大MPを取得します。

#### `const std::vector<Skill>& getSkills() const`
*   **説明**: スキルリストを取得します。

#### `void addSkill(const Skill& skill)`
*   **説明**: スキルを習得します。
