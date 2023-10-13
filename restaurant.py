class Restaurant:
    """Model de restaurante simples."""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0
        self.open = False

    def describe_restaurant(self):
        """Imprima uma descrição simples da instância do restaurante."""
        #BUG -> O sistema estava retornando o nome do produto comercializado e não o nome do restaurante cadastrado.
        # Ajuste -> Remoção do print para colocar o return como padrão de retorno da função além da concatenação do texto anterior
        return f"Esse restaturante se chama {self.restaurant_name}, servimos {self.cuisine_type} e estamos servindo {self.number_served} consumidores desde que está aberto."

    def open_restaurant(self):
        """Imprima uma mensagem indicando que o restaurante está aberto para negócios."""
        #BUG -> o atributo self.open estava com o valor False, quando deveria ser True para sinalizar que o restaurante esta aberto
        # Melhoria -> Remoção de "elses" desnecessários
        #BUG -> número de consumidores estava setado com um valor negativo de clientes no momento da abertura do restaurante
        #Melhoria -> realizei a chamada da função "set_number_serverd, para indicar a quantidade de concumidores iniciais no reaturante
        # Ajuste -> Remoção do print para colocar o return como padrão de retorno da função
        if not self.open:
            self.open = True
            self.set_number_served(0)
            return f"{self.restaurant_name} agora está aberto!"
        return f"{self.restaurant_name} já está aberto!"

    def close_restaurant(self):
        """Imprima uma mensagem indicando que o restaurante está fechado para negócios."""
        # Melhoria -> Remoção de "elses" desnecessários
        # Melhoria -> realizei a chamada da função "Set_number_serverd, para indicar a quantidade de concumidores finais no reaturante
        # Ajuste -> Remoção do print para colocar o return como padrão de retorno da função
        if self.open:
            self.open = False
            self.set_number_served(0)
            return f"{self.restaurant_name} agora está fechado!"
        return f"{self.restaurant_name} já está fechado!"

    def set_number_served(self, total_customers):
        """Defina o número total de pessoas atendidas por este restaurante até o momento."""
        # Melhoria -> Remoção de "elses" desnecessários
        # Ajuste -> Remoção do print para colocar o return como padrão de retorno da função
        if self.open:
            self.number_served = total_customers
            return self.number_served
        return f"{self.restaurant_name} está fechado!"

    def increment_number_served(self, more_customers):
        """Aumenta número total de clientes atendidos por este restaurante."""
        # Melhoria -> Remoção de "elses" desnecessários
        # Ajuste -> Remoção do print para colocar o return como padrão de retorno da função
        # BUG -> o número de clientes não estava sendo incrementado, apenas estava sendo substituido pelo valor informado no parametro "more_customers", foi acrescentada a soma
        if self.open:
            self.number_served = self.number_served + more_customers
            return self.number_served
        return f"{self.restaurant_name} está fechado!"
