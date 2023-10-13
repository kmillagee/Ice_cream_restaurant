from src.models.restaurant import Restaurant


class IceCreamStand(Restaurant):
    """Um tipo especializado de restaurante."""

    def __init__(self, restaurant_name, cuisine_type):
        """
        Inicialize os atributos da classe pai.
        Em seguida, inicialize os atributos específicos de uma sorveteria.
        """
        super().__init__(restaurant_name, cuisine_type)
        #Ajuste -> Flavors é iniciada como uma lista vazia, assim já sendo considerada como um tipo primitivo no construtor da classe
        self.flavors = []

    def add_flavor(self, flavor):
        #Ajuste -> Remoção do print para colocar o return como padrão de retorno da função
        #BUG -> o sistema não consegue validar se já existe um sabor na nossa lista de sabores, foi criado um laço e uma validação para verificar se sabor já existe.
        #Melhoria -> Remoção de "elses" desnecessários
        """Add o sabor informado ao estoque."""
        #Melhoria -> validação se o valor passado é valido
        if flavor is None:
            return "Valor inválido"
        #Melhoria -> split para formatação da lista de sabores
        sabor = flavor.split(", ")
        for item in sabor:
            if item in self.flavors:
                return "Sabor já cadastrado"
        #Melhoria -> Utilizei um laço e também o extends, em vez do append, pois desta forma podemos incluir mais de um sabor dentro da lista sem precisar reinicia-la em uma segunda chamada do metodo add.
        self.flavors.extend(sabor)
        return f"{self.flavors} adicionado ao estoque!"

    def flavors_available(self):
        """Percorra a lista de sabores disponíveis e imprima."""
        #Ajuste -> Remoção do print para colocar o return como padrão de retorno da função
        #BUG -> O retorno do metodo estava apenas retornando a primeira letra da lista(f"\t-{flavor}") , foi realizado o ajuste removendo o trecho de código que acontecia o Bug
        #Melhoria -> Remoção de "elses" desnecessários
        if self.flavors:
            return f"No momento temos os seguintes sabores de sorvete disponíveis: {self.flavors}"
        return "Estamos sem estoque atualmente!"

    def find_flavor(self, flavor):
        """Verifica se o sabor informado está disponível."""
        # Ajuste -> Remoção do print para colocar o return como padrão de retorno da função
        # Melhoria -> validação se o valor passado é valido
        if flavor is None:
            return "Valor invalido"
        if self.flavors:
            if flavor in self.flavors:
                return f"Temos no momento {self.flavors}!"
            # BUG -> o sistema está retornando todos os sabores existentes, mesmo que o sabor do usuário não seja encontrado quando o ideal seria retornar apenas aquele sabor que o usuário desejava, informando que
            # o sabor não está disponivel. foi realizada a troca pelo flavor único da lista
            else:
                return f"Não temos no momento {flavor}!"
        return "Estamos sem estoque atualmente!"

    def clear_flavors(self):
        #Melhoria -> Criação de uma função para reinicar a lista de estoque, caso necessário
        self.flavors = []
        return self.flavors

