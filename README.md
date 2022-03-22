### django_https0227がベース
- ↑カスタムユーザーでなくOne to Oneのみ
- ↑ユーザーのimport-exportが不可
- ↑そのためカスタムユーザーにして、One to Oneをやめた

### しかし
- ユーザー追加しても、PWがハッシュにならずログイン不可となる

### ひとまずの回避策
- import-exportを無効にしてユーザー登録をする（importやexportしたいときに有効にしてする）