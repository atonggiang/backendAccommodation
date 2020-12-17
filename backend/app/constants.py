HOUSE = 'H'
STUDIO = 'S'
APARTMENT = 'A'
MINIROOM = 'M'
ROOM_TYPE = [
    (HOUSE, 'House'),
    (STUDIO, 'Studio'),
    (APARTMENT, 'Apartment'),
    (MINIROOM, 'Miniroom'),
]
SHARED = 'S'
PRIVATE = 'P'
NOKITCHEN = 'N'
BATHROOM_TYPE = [
    (SHARED, 'Shared'),
    (PRIVATE, 'Private'),
]
KITCHEN_TYPE = [
    (SHARED, 'Shared'),
    (PRIVATE, 'Private'),
    (NOKITCHEN, 'No Kitchen'),
]
WEEK = 'W'
MONTH = 'M'
QUATER = 'Q'
YEAR = 'Y'
DISPLAY_DURATION_TYPE = [
    (WEEK, 'A Week'),
    (MONTH, 'A Month'),
    (QUATER, 'A Quater'),
    (YEAR, 'A Year'),
]
PENDING = 'P'
APPROVED = 'A'
DECLINED = 'D'
VERIFY_STATUS = [
    (PENDING, 'Pending'),
    (APPROVED, 'Approved'),
    (DECLINED, 'Declined'),
]
WEEK_PRICE = 12.99
MONTH_PRICE = 9.99
QUATER_PRICE = 5.99
YEAR_PRICE = 2.99