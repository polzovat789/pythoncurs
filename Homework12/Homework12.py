
class Bank:
    def __init__(self):
        self.clients = {}
        self.deposits = {}

    def register_client(self, client_id, name):
        """Регистрация нового клиента."""
        if client_id in self.clients:
            raise ValueError("Клиент с таким ID уже зарегистрирован.")
        self.clients[client_id] = name

    def open_deposit_account(self, client_id, start_balance, years):
        """Открытие вклада для клиента."""
        if client_id not in self.clients:
            raise ValueError("Клиент не зарегистрирован.")
        if client_id in self.deposits:
            raise ValueError("Вклад для этого клиента уже открыт.")
        self.deposits[client_id] = {
            'start_balance': start_balance,
            'years': years,
            'current_balance': start_balance
        }

    def calc_deposit_interest_rate(self, client_id):
        """Расчет итоговой суммы вклада с учетом ежемесячной капитализации."""
        if client_id not in self.deposits:
            raise ValueError("Вклад для этого клиента не открыт.")

        deposit = self.deposits[client_id]
        start_balance = deposit['start_balance']
        years = deposit['years']
        monthly_rate = 0.10 / 12  # Ежемесячная процентная ставка
        months = years * 12  # Общее количество месяцев

        # Формула для расчета сложных процентов с ежемесячной капитализацией
        final_balance = start_balance * (1 + monthly_rate) ** months
        deposit['current_balance'] = final_balance
        return round(final_balance, 2)

    def close_deposit(self, client_id):
        """Закрытие вклада и возврат итоговой суммы."""
        if client_id not in self.deposits:
            raise ValueError("Вклад для этого клиента не открыт.")

        final_balance = self.calc_deposit_interest_rate(client_id)
        del self.deposits[client_id]
        return final_balance


# Пример
client_id = "0000001"

bank = Bank()
bank.register_client(client_id=client_id, name="Siarhei")
bank.open_deposit_account(
    client_id=client_id, start_balance=1000, years=1)

# Проверка расчета процентов
assert bank.calc_deposit_interest_rate(client_id=client_id) == 1104.71, \
    "Ошибка в расчете процентов"

# Закрытие вклада и получение денег
final_amount = bank.close_deposit(client_id=client_id)
print(
    f"Итоговая сумма вклада: {final_amount} рублей"
)
