# register() メソッドで、ユーザーが正しく登録されるか
# ユーザーを登録し、正しく登録されているかを assert で評価します。
# register() メソッドで、すでに存在するユーザー名で登録を試みた場合に、エラーメッセージが出力されるか
# 同じユーザーを登録し、例外が発生することを pytest.raises() で確認します。
# login() メソッドで、正しいユーザー名とパスワードでログインできるか
# ユーザーを登録し、ログインメッセージを assert で評価します。
# login() メソッドで、誤ったパスワードでエラーが出るか
# ユーザーを登録し、誤ったパスワードでログインして例外が発生することを pytest.raises() で確認します。


import pytest
from authenticator import Authenticator


def test_authenticator():
    auth = Authenticator()

    auth.register("a", "111")
    auth.register("b", "222")
    auth.register("c", "333")

    with pytest.raises(ValueError, match="エラー: ユーザーは既に存在します。"):
        auth.register("a", "444")

    r = auth.login("a", "111")
    assert r == "ログイン成功"
    r = auth.login("b", "222")
    assert r == "ログイン成功"

    with pytest.raises(ValueError, match="エラー: ユーザー名またはパスワードが正しくありません。"):
        auth.login("a", "000")
    with pytest.raises(ValueError, match="エラー: ユーザー名またはパスワードが正しくありません。"):
        auth.login("d", "000")
