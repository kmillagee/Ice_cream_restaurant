import pytest

from src.models.restaurant import Restaurant


@pytest.fixture
def restaurante():
    return Restaurant("Pizza Hut", "pizza")


# Teste se o nome e o tipo de cozinha do restaurante são atribuídos corretamente
def test_describe_restaurant(restaurante):
    response = restaurante.describe_restaurant()
    assert response == "Esse restaturante se chama Pizza Hut, servimos pizza e estamos servindo 0 consumidores desde que está aberto."


def test_open_restaurant(restaurante):
    response = restaurante.open_restaurant()
    assert response == f"Pizza Hut agora está aberto!"


def test_open_now_restaurant(restaurante):
    restaurante.open_restaurant()
    response = restaurante.open_restaurant()
    assert response == "Pizza Hut já está aberto!"


def test_closed_restaurant(restaurante):
    restaurante.open_restaurant()
    response = restaurante.close_restaurant()
    assert response == "Pizza Hut agora está fechado!"


def test_closed_now_restaurant(restaurante):
    restaurante.open_restaurant()
    restaurante.close_restaurant()
    response = restaurante.close_restaurant()
    assert response == "Pizza Hut já está fechado!"


def test_set_number_served_open_restaurant(restaurante):
    restaurante.open_restaurant()
    response = restaurante.set_number_served(10)
    assert response == 10


def test_set_number_served_closed_restaurant(restaurante):
    response = restaurante.set_number_served(0)
    assert response == "Pizza Hut está fechado!"


def test_increment_number_served_open_restaurant(restaurante):
    restaurante.open_restaurant()
    restaurante.set_number_served(0)
    response = restaurante.increment_number_served(1)
    assert response == 1


def test_increment_number_served_closed_restaurant(restaurante):
    restaurante.close_restaurant()
    response = restaurante.increment_number_served(0)
    assert response == "Pizza Hut está fechado!"
