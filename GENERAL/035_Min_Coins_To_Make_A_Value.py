"""

"""

class Solution :
    def get_coins(self,
                  number: int,
                  coins_available: list[int]) -> None :
        coins_available.sort(reverse=True)

        coin_index = 0
        coins = {}

        while coin_index < len(coins_available) and number > 0 :
            if coin_index < number :
                coins[coins_available[coin_index]] = number//coins_available[coin_index]
                number -= coins[coins_available[coin_index]]*coins_available[coin_index]
            coin_index += 1

        return coins
