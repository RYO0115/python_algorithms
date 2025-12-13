# Monster Class

`Monster` クラスは、敵キャラクターを表すクラスです。`Character` クラスを継承しています。

## 概要

*   **名前空間**: `models`
*   **ヘッダファイル**: `include/models/Monster.h`
*   **ソースファイル**: `src/models/Monster.cpp`

## 責務

*   AIロジックによる行動決定

## メンバ関数

### `public`

#### `Monster(std::string name, int hp, int attackPower)`
*   **説明**: コンストラクタ。

#### `void attack(Character& target) override`
*   **説明**: 通常攻撃を行います。

#### `void performAction(Character& target)`
*   **説明**: 行動を決定し実行します。現在は単純な攻撃のみを行いますが、将来的にランダム行動などを実装可能です。
