ALCHEMISER_CHARGES_PER_ITEM = 6
DISASSEMBLER_CHARGES_PER_ITEM = 3.8
CORRUPTED_MAGIC_LOGS_ID = 40338
DIVINE_CHARGE_ID = 36390
EMPTY_DIVINE_CHARGE_ID = 41073
ITEMS = ['magic logs', 'corrupted magic logs', 'soapstone']
ITEMS_DISASSEMBLED_PER_HOUR = 60
ITEMS_ALCHEMISED_PER_HOUR = 25
MAGIC_LOGS_ID = 1513
NATURE_RUNE_ID = 561
SOAPSTONE_ID = 49458
VALID_CHARS = 'abcdefghijklmnopqrstuvwxyz1234567890!&()/-+. '
VALID_NUMS = '0123456789'
API_ITEMS_QUERY = 'https://services.runescape.com/m=itemdb_rs/api/catalogue/items.json?category={x}&alpha={y}&page={z}'
WIKI_API_QUERY = 'https://api.weirdgloop.org/exchange/history/rs/latest?id={}'
LOGS_COMPS = {
    'simple parts': 0.99,
    'junk': 0.034
}
SOAPSTONE_COMPS = {
    'special': {
        'historic': 0.16,
        'classic': 0.4
        },
    'normal': {
        'simple parts': 1.0,
        'junk': 27.2
    }
}