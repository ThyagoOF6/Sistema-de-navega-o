class TestNavigation:
    @staticmethod
    def run(browser, commands):
        """Testa a navegação no objeto Browser dado um conjunto de comandos."""
        for command in commands:
            if command.startswith("access"):
                _, url = command.split(maxsplit=1)
                browser.access(url)
            elif command == "back":
                try:
                    browser.back()
                except Exception as e:
                    print(e)
            elif command == "forward":
                try:
                    browser.forward()
                except Exception as e:
                    print(e)
            elif command == "get-current":
                print(browser.get_current_page())

# Exemplo de uso:
browser = Browser()
commands = [
    "get-current",         # Deve imprimir "home"
    "access page1",        # Acessa "page1"
    "get-current",         # Deve imprimir "page1"
    "access page2",        # Acessa "page2"
    "get-current",         # Deve imprimir "page2"
    "back",                # Volta para "page1"
    "get-current",         # Deve imprimir "page1"
    "forward",             # Avança para "page2"
    "get-current",         # Deve imprimir "page2"
    "back",                # Volta para "page1"
    "back",                # Volta para "home"
    "get-current",         # Deve imprimir "home"
    "forward",             # Avança para "page1"
    "get-current",         # Deve imprimir "page1"
    "access page3",        # Acessa "page3" (limpa histórico futuro)
    "get-current",         # Deve imprimir "page3"
    "forward",             # Deve lançar erro "Forward error"
]

TestNavigation.run(browser, commands)
