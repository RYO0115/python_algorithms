# Character Class

{cpp:class}`Character` クラスは、全てのキャラクター（ヒーロー、モンスター）の基底クラスです。

## 概要

*   **名前空間**: `models`
*   **ヘッダファイル**: `include/models/Character.h`
*   **ソースファイル**: `src/models/Character.cpp`

## 責務

*   共通ステータス（名前、HP、攻撃力）の保持
*   ダメージ処理の共通化
*   死亡判定

## メンバ変数

### `protected`

*   `std::string name`: キャラクターの名前
*   `int hp`: 現在のHP
*   `int maxHp`: 最大HP
*   `int attackPower`: 攻撃力

## メンバ関数

### `public`

#### {cpp:func}`Character::Character`
*   **説明**: コンストラクタ。ステータスを初期化します。

#### {cpp:func}`Character::attack`
*   **説明**: 純粋仮想関数。対象を攻撃します。派生クラスで実装する必要があります。

#### {cpp:func}`Character::takeDamage`
*   **説明**: ダメージを受けます。HPを減算し、0未満にならないようにします。

#### {cpp:func}`Character::isDead`
*   **説明**: キャラクターが死亡しているか（HP <= 0）を判定します。

#### {cpp:func}`Character::getName`
*   **説明**: 名前を取得します。

#### {cpp:func}`Character::getHp`
*   **説明**: 現在のHPを取得します。

#### {cpp:func}`Character::getMaxHp`
*   **説明**: 最大HPを取得します。

#### {cpp:func}`Character::getAttackPower`
*   **説明**: 攻撃力を取得します。
