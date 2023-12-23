import sys
import requests
import json

def main():
    if len(sys.argv) == 2:
        try:
            n = float(sys.argv[1])
        except ValueError:
            sys.exit("Command-line argument is not a number")
        else:
            url = "https://api.coindesk.com/v1/bpi/currentprice.json"
            cost = get_cost(n, url)
            print(f"${cost:,.4f}")
    else:
        sys.exit("Missing command-line argument")


def get_cost(n, url):
    try:
        res = requests.get(url)
        res.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print('Http Error:', e)
    except requests.RequestException as e:
        print("RequestException:", e)
    except:
        print("Error")
    else:
        try:
            data = (res.json())
        except requests.exceptions.JSONDecodeError:
            sys.exit("JSONDecodeError")
        # print(json.dumps(data, indent=2))
        cost = data["bpi"]["USD"]["rate_float"] * n
        return cost



if __name__ == "__main__":
    main()




# {
#   "time": {
#     "updated": "Dec 23, 2023 13:07:00 UTC",
#     "updatedISO": "2023-12-23T13:07:00+00:00",
#     "updateduk": "Dec 23, 2023 at 13:07 GMT"
#   },
#   "disclaimer": "This data was produced from the CoinDesk Bitcoin Price Index (USD). Non-USD currency data converted using hourly conversion rate from openexchangerates.org",
#   "chartName": "Bitcoin",
#   "bpi": {
#     "USD": {
#       "code": "USD",
#       "symbol": "&#36;",
#       "rate": "43,752.8579",
#       "description": "United States Dollar",
#       "rate_float": 43752.8579
#     },
#     "GBP": {
#       "code": "GBP",
#       "symbol": "&pound;",
#       "rate": "36,559.5381",
#       "description": "British Pound Sterling",
#       "rate_float": 36559.5381
#     },
#     "EUR": {
#       "code": "EUR",
#       "symbol": "&euro;",
#       "rate": "42,621.6715",
#       "description": "Euro",
#       "rate_float": 42621.6715
#     }
#   }
# }



"""
{
  "time": {
    "updated": "Dec 23, 2023 13:07:00 UTC",
    "updatedISO": "2023-12-23T13:07:00+00:00",
    "updateduk": "Dec 23, 2023 at 13:07 GMT"
  },
  "disclaimer": "This data was produced from the CoinDesk Bitcoin Price Index (USD). Non-USD currency data converted using hourly conversion rate from openexchangerates.org",
  "chartName": "Bitcoin",
  "bpi": {
    "USD": {
      "code": "USD",
      "symbol": "&#36;",
      "rate": "43,752.8579",
      "description": "United States Dollar",
      "rate_float": 43752.8579
    },
    "GBP": {
      "code": "GBP",
      "symbol": "&pound;",
      "rate": "36,559.5381",
      "description": "British Pound Sterling",
      "rate_float": 36559.5381
    },
    "EUR": {
      "code": "EUR",
      "symbol": "&euro;",
      "rate": "42,621.6715",
      "description": "Euro",
      "rate_float": 42621.6715
    }
  }
}
"""