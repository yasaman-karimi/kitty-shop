from django.test.client import Client

from apps.user.models import User


def test_full_name(db):
    b = User(
        username="poopoopy", first_name="pooya", last_name="loop", password="123678990"
    )
    b.save()

    assert b.full_name() == "pooya loop"


def test_full_name_with_no_first_name(db):
    b = User(username="poopoopy", last_name="loop", password="123678990")
    b.save()

    assert b.full_name() == "Ms/Mr loop"


def test_full_name_with_no_last_name(db):
    b = User(username="poopoopy", first_name="pooya", password="123678990")
    b.save()

    assert b.full_name() == "pooya"


def test_full_name_with_no_names(db):
    b = User(username="poopoopy", password="123678990")
    b.save()

    assert b.full_name() == "Kitty"


def test_login_view_get(db, client: Client):
    resp = client.get("/login/")

    assert resp.status_code == 200
    assert "Login to your account" in str(resp.content)


def test_login_view_post(db, client: Client, user1):
    client.force_login(user1)
    resp = client.post(
        "/login/",
        content_type="application/x-www-form-urlencoded",
        data={"username": "poopoopy", "password": "123678990"},
    )

    assert resp.status_code == 200
    assert "Please enter a correct username and password" in str(resp.content)
