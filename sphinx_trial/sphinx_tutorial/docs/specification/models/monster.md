# Monster Class

{cpp:class}`Monster` クラスは、敵キャラクターを表すクラスです。{cpp:class}`Character` クラスを継承しています。

## 概要

*   **名前空間**: `models`
*   **ヘッダファイル**: `include/models/Monster.h`
*   **ソースファイル**: `src/models/Monster.cpp`

## 責務

*   AIロジックによる行動決定

## メンバ関数

### `public`

#### {cpp:func}`Monster::Monster`
*   **説明**: コンストラクタ。

#### {cpp:func}`Monster::attack`
*   **説明**: 通常攻撃を行います。

#### {cpp:func}`Monster::performAction`
*   **説明**: 行動を決定し実行します。現在は単純な攻撃のみを行いますが、将来的にランダム行動などを実装可能です。
