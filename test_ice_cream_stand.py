from src.models.ice_cream_stand import IceCreamStand


class TestIceCreamStand:

    def test_add_flavor(self):
        ice_cream = IceCreamStand("CopaCabana", "Brasileira")
        response = ice_cream.add_flavor("Flocos, Baunilha")
        assert response == "['Flocos', 'Baunilha'] adicionado ao estoque!"

    def test_add_flavor_exist(self):
        ice_cream = IceCreamStand("CopaCabana", "Brasileira")
        ice_cream.add_flavor("Flocos, Baunilha")
        response = ice_cream.add_flavor("Baunilha")
        assert response == "Sabor já cadastrado"

    def test_flavors_available(self):
        ice_cream = IceCreamStand("CopaCabana", "Brasileira")
        ice_cream.add_flavor("Flocos, Baunilha")
        response = ice_cream.flavors_available()
        assert response == "No momento temos os seguintes sabores de sorvete disponíveis: ['Flocos', 'Baunilha']"

    def test_flavors_not_available(self):
        ice_cream = IceCreamStand("CopaCabana", "Brasileira")
        ice_cream.add_flavor(None)
        assert ice_cream.flavors_available() == "Estamos sem estoque atualmente!"

    def test_find_flavor_successful(self):
        ice_cream = IceCreamStand("CopaCabana", "Brasileira")
        ice_cream.add_flavor("Flocos, Baunilha")
        assert ice_cream.find_flavor("Flocos") == "Temos no momento ['Flocos', 'Baunilha']!"

    def test_find_flavor_none(self):
        ice_cream = IceCreamStand("CopaCabana", "Brasileira")
        ice_cream.add_flavor("Flocos, Baunilha")
        assert ice_cream.find_flavor(None) == "Valor invalido"

    def test_find_flavor_itemnotfound(self):
        ice_cream = IceCreamStand("CopaCabana", "Brasileira")
        ice_cream.add_flavor("Flocos, Baunilha")
        assert ice_cream.find_flavor("Abacaxi") == "Não temos no momento Abacaxi!"

    def test_find_flavor_checkiventory(self):
        ice_cream = IceCreamStand("CopaCabana", "Brasileira")
        ice_cream.add_flavor("Flocos, Baunilha")
        ice_cream.clear_flavors()
        assert ice_cream.find_flavor("Abacaxi") == "Estamos sem estoque atualmente!"

    def test_clear_successful(self):
        ice_cream = IceCreamStand("CopaCabana", "Brasileira")
        ice_cream.add_flavor("Flocos, Baunilha")
        response = ice_cream.clear_flavors()
        assert response == []


