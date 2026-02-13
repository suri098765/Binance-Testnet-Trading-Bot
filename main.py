import argparse
import os
from bot_logic import BinanceBot
from dotenv import load_dotenv

load_dotenv()

def main():
    parser = argparse.ArgumentParser(description="Binance Futures Testnet Bot")
    parser.add_argument("--symbol", required=True, help="e.g. BTCUSDT")
    parser.add_argument("--side", required=True, choices=["BUY", "SELL"])
    parser.add_argument("--type", required=True, choices=["MARKET", "LIMIT"])
    parser.add_argument("--quantity", required=True, type=float)
    parser.add_argument("--price", type=str, help="Required for LIMIT orders")

    args = parser.parse_args()

    # Get credentials from environment variables for safety
    api_key = os.getenv("BINANCE_API_KEY")
    api_secret = os.getenv("BINANCE_API_SECRET")

    if not api_key or not api_secret:
        print("Error: Please set BINANCE_API_KEY and BINANCE_API_SECRET in your .env file")
        return

    bot = BinanceBot(api_key, api_secret)
    result = bot.place_order(args.symbol, args.side, args.type, args.quantity, args.price)
    
    print("\n--- Order Result ---")
    print(result)

if __name__ == "__main__":
    main()
