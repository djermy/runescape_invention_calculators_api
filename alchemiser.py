from api_fetcher import get_item_cost
from scraper import scrape_alch_value
from user_input import get_user_input
from database_handler import id_grabber
from calculator_utils import cost_of_charge
import constants

# main functions
def alchemiser_calculator():
    '''
    Calculates profit/loss to alchemise the chosen item,
    and provides several outputs. 
    '''

    # get user input and process it into components needed
    item_name = get_user_input()

    item_id = id_grabber(item_name)
    if item_id == None:
        print('Error item not found!')
        print('Perhaps you mispelled it?')
        return alchemiser_calculator()

    item_cost = get_item_cost(item_id)
    alch_value = scrape_alch_value(item_name)

    # check alch_value was properly obtained
    if type(alch_value) == str:
        print(alch_value)
        print('Please try again')
        return alchemiser_calculator()

    # calculate the cost of machine fuels to process 1 item
    cost_of_charges = constants.ALCHEMISER_CHARGES_PER_ITEM * cost_of_charge()
    cost_of_nature_rune = get_item_cost(constants.NATURE_RUNE_ID)
    cost_per_item = round(cost_of_charges + cost_of_nature_rune, 2)

    # total cost to process 1 item
    total_cost_per_item = item_cost + cost_per_item

    # total profit/loss per item
    profit_or_loss = alch_value - total_cost_per_item
    hourly = (alch_value - total_cost_per_item) * constants.ITEMS_ALCHEMISED_PER_HOUR
    daily = hourly * 24

    # for testing purposes
    # render output
    print(f'The profit/loss to alchemise this item is: {round(profit_or_loss, 2)}')
    print(f'The hourly profit/loss to alchemise this item is: {round(hourly, 2)}')
    print(f'The daily profit/loss to alchemise this item is: {round(daily, 2)}')

alchemiser_calculator()