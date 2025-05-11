class bank:
    bank_name = "Meezan Bank"

    @classmethod
    def change_bnk_name(cls, bnk_name):
        cls.bank_name = bnk_name

B1 = bank()
B2 = bank()

print(B1.bank_name)

bank.change_bnk_name("HBL")
print(B2.bank_name)