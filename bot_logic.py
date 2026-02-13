import logging
from binance.client import Client
from binance.exceptions import BinanceAPIException

# Configure Logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler("bot.log"), logging.StreamHandler()]
)

class BinanceBot:
    def __init__(self, api_key, api_secret):
        # Initialize client for Testnet
        self.client = Client(api_key, api_secret, testnet=True)
        
    def place_order(self, symbol, side, order_type, quantity, price=None):
        try:
            logging.info(f"Attempting {order_type} {side} order for {symbol}")
            
            params = {
                'symbol': symbol.upper(),
                'side': side.upper(),
                'type': order_type.upper(),
                'quantity': quantity
            }
            
            if order_type.upper() == 'LIMIT':
                if not price:
                    raise ValueError("Price is required for LIMIT orders")
                params['price'] = price
                params['timeInForce'] = 'GTC' # Good Till Cancelled

            # Placing the Futures Order (USDT-M)
            response = self.client.futures_create_order(**params)
            
            logging.info(f"Order Successful! ID: {response.get('orderId')}")
            return response

        except BinanceAPIException as e:
            logging.error(f"Binance API Error: {e.message}")
            return {"error": e.message}
        except Exception as e:
            logging.error(f"Unexpected Error: {str(e)}")
            return {"error": str(e)}
