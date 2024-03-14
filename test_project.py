import project
import pytest

def test_create_and_shuffle_cards():
    cards1 = project.create_and_shuffle_cards()
    cards2 = project.create_and_shuffle_cards()

    assert len(cards1) == len(cards2)
    assert cards1 != cards2

def test_deal_cards():
    cards = [ ("Pikachu", "50pts & 35hp"), ("Charmander", "65pts & 39hp"), ("Bulbasaur", "45pts & 45hp"), ("Squirtle", "60pts & 44hp"),
        ("Jigglypuff", "55pts & 115hp"), ("Meowth", "40pts & 40hp"), ("Psyduck", "52pts & 50hp"), ("Abra", "48pts & 25hp"),
        ("Gastly", "47pts & 30hp"), ("Magikarp", "30pts & 20hp"), ("Eevee", "58pts & 55hp"), ("Snorlax", "80pts & 160hp"),
        ("Mewtwo", "90pts & 106hp"), ("Mew", "85pts & 100hp"), ("Cyndaquil", "62pts & 39hp"), ("Totodile", "59pts & 50hp"),
        ("Chikorita", "54pts & 45hp"), ("Marill", "49pts & 70hp"), ("Hoothoot", "46pts & 60hp"), ("Togepi", "51pts & 35hp")]


