import text_alert
import gas_check


if __name__ == '__main__':
    zack = 15216
    jen = 15203

    best = gas_check.get_results(jen)
    store = None
    price = None
    for key, val in best.items():
        store = key
        price = f'${val}'
    text_alert.send_alert(store, price)
