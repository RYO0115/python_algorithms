# Skill Class

{cpp:class}`Skill` クラスは、キャラクターが使用する魔法や技を表すクラスです。

## 概要

*   **名前空間**: `models`
*   **ヘッダファイル**: `include/models/Skill.h`
*   **ソースファイル**: `src/models/Skill.cpp`

## 列挙型

### {cpp:enum}`SkillType`
*   `ATTACK`: 攻撃スキル
*   `HEAL`: 回復スキル

## メンバ変数

### `private`

*   `std::string name`: スキル名
*   `int mpCost`: 消費MP
*   `int power`: 威力（ダメージまたは回復量）
*   `SkillType type`: スキルの種類

## メンバ関数

### `public`

#### {cpp:func}`Skill::Skill`
*   **説明**: コンストラクタ。

#### {cpp:func}`Skill::getName`
*   **説明**: スキル名を取得します。

#### {cpp:func}`Skill::getMpCost`
*   **説明**: 消費MPを取得します。

#### {cpp:func}`Skill::getPower`
*   **説明**: 威力を取得します。

#### {cpp:func}`Skill::getType`
*   **説明**: スキルの種類を取得します。
