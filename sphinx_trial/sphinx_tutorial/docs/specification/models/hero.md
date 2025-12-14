# Hero Class

{cpp:class}`Hero` クラスは、プレイヤーが操作するキャラクターを表すクラスです。{cpp:class}`Character` クラスを継承しています。

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

#### {cpp:func}`Hero::Hero`
*   **説明**: コンストラクタ。

#### {cpp:func}`Hero::attack`
*   **説明**: 通常攻撃を行います。`Dice`を使用してダメージを計算します。

#### {cpp:func}`Hero::useSkill`
*   **説明**: スキルを使用します。攻撃スキルの場合はダメージを与え、回復スキルの場合は自身を回復します。

#### {cpp:func}`Hero::heal`
*   **説明**: HPを回復します。最大HPを超えないようにします。

#### {cpp:func}`Hero::recoverMp`
*   **説明**: MPを回復します。

#### {cpp:func}`Hero::payMp`
*   **説明**: MPを消費します。足りない場合は `false` を返します。

#### {cpp:func}`Hero::getMp`
*   **説明**: 現在のMPを取得します。

#### {cpp:func}`Hero::getMaxMp`
*   **説明**: 最大MPを取得します。

#### {cpp:func}`Hero::getSkills`
*   **説明**: スキルリストを取得します。

#### {cpp:func}`Hero::addSkill`
*   **説明**: スキルを習得します。
