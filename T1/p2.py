"""
Solución a problema 2:
Dados dos enteros m y n, donde m es la cantidad de empresas productoras y n es la cantidad de
empresas consumidoras, una cantidad m de líneas, donde la i-ésima línea contiene dos enteros p_i y
s_i, indicando el precio unitario de venta y el día en que comienza a operar la empresa i-ésima, y
una cantidad n de líneas, donde la j-ésima línea contiene dos enteros q_j y e_j, indicando el máximo
precio por unidad que puede comprar cada producto la empresa j-ésima, y el última día en que la
la empresa j-ésima opera.

Se pide encontrar un entero correspondiente a la máxima ganancia que se puede obtener.
"""
import math

if __name__ == "__main__":

    # --------------------------------------------------------------------------
    # O(1)
    # Se leen los datos de entrada
    m, n = map(int, input().split())

    # Data structures
    sellers = {}
    best_sellers = {}
    buyers = {}
    best_buyers = {}

    # Useful info
    min_start = math.inf
    # max_start = 0
    # min_end = math.inf
    max_end = 0
    min_sell_price = math.inf
    # max_sell_price = 0
    # min_buy_price = math.inf
    max_buy_price = 0

    # --------------------------------------------------------------------------
    # O(m + n)
    for i in range(m):
        p, s = map(int, input().split())
        val = sellers.get(s)
        if val is None or val > p:
            sellers[s] = p
            if s < min_start:
                min_start = s
            # if s > max_start:
            #     max_start = s
            if p < min_sell_price:
                min_sell_price = p
            # if p > max_sell_price:
            #     max_sell_price = p
    for j in range(n):
        q, e = map(int, input().split())
        val = buyers.get(e)
        if (val is None or val < q) and e >= min_start:
            buyers[e] = q
            if e > max_end:
                max_end = e
            # if e < min_end:
            #     min_end = e
            if q > max_buy_price:
                max_buy_price = q
            # if q < min_buy_price:
            #     min_buy_price = q

    # --------------------------------------------------------------------------
    # O(m)
    for s in list(sellers.keys()):
        if s > max_end:
            del sellers[s]

    # --------------------------------------------------------------------------
    # O(mlog(m))
    # Remove unoptimal sellers
    if sellers:
        # Sorting is O(mlog(m))
        ordered_sellers_indices = sorted(sellers.keys())
        current_tracked_price = sellers[ordered_sellers_indices[0]]
        best_sellers[ordered_sellers_indices[0]] = current_tracked_price
        # O(m)
        for s in ordered_sellers_indices[1:]:
            current_price = sellers[s]
            if current_price < current_tracked_price:
                current_tracked_price = current_price
                best_sellers[s] = current_tracked_price

    # --------------------------------------------------------------------------
    # O(nlog(n))
    # Remove unoptimal buyers
    if buyers:
        # Sorting is O(nlog(n))
        ordered_buyers_indices = sorted(buyers.keys(), reverse=True)
        current_tracked_price = buyers[ordered_buyers_indices[0]]
        best_buyers[ordered_buyers_indices[0]] = current_tracked_price
        # O(n)
        for e in ordered_buyers_indices[1:]:
            current_price = buyers[e]
            if current_price > current_tracked_price:
                current_tracked_price = current_price
                best_buyers[e] = current_tracked_price

    # --------------------------------------------------------------------------
    # O(n*m) ????
    # Calcular la ganancia
    best_profit = 0
    for e in best_buyers:
        buy_price = best_buyers[e]
        for s in best_sellers:
            sell_price = best_sellers[s]
            trade_window = e - s + 1
            if (trade_window > 0):
                res = trade_window * (buy_price - sell_price)
                if res > best_profit:
                    best_profit = res

    print(best_profit)

    # 1 - 9966347413977789
    # 2 - 9976615254630354
    # 3 - 9981135029457732
