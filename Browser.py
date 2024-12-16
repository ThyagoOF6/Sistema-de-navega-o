class Browser:
    def __init__(self):
        # Página inicial
        self.current_page = "home"
        self.history_back = []  # Histórico para voltar
        self.history_forward = []  # Histórico para avançar

    def access(self, url):
        """Acessa uma nova página e limpa o histórico de páginas futuras."""
        if self.current_page:
            self.history_back.append(self.current_page)
        self.current_page = url
        self.history_forward.clear()  # Invalida o histórico de páginas futuras

    def back(self):
        """Volta para a página anterior."""
        if not self.history_back:
            raise Exception("Back error")
        self.history_forward.append(self.current_page)
        self.current_page = self.history_back.pop()

    def forward(self):
        """Avança para a próxima página no histórico."""
        if not self.history_forward:
            raise Exception("Forward error")
        self.history_back.append(self.current_page)
        self.current_page = self.history_forward.pop()

    def get_current_page(self):
        """Retorna a página atual."""
        return self.current_page

