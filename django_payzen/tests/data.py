import collections
import random


def get_vads_trans_id():
    vads_trans_id = ""
    for i in range(0, 6):
        vads_trans_id += str(random.randint(0, 9))
    return vads_trans_id

cards = [
    {
        'type': 'CB',
        'card_number': '4970100000000000',
        'behaviour': '3D-Secure',
        'result': 'accepted'
    },
    {
        'type': 'MasterCard',
        'card_number': '5970100300000000',
        'behaviour': '3D-Secure',
        'result': 'accepted'
    },
    {
        'type': 'Maestro',
        'card_number': '5000550000000000',
        'behaviour': '3D-Secure',
        'result': 'accepted'
    },
    {
        'type': 'CB',
        'card_number': '4970100000000009',
        'behaviour': '3D-Secure interactive',
        'result': 'accepted'
    },
    {
        'type': 'MasterCard',
        'card_number': '5970100300000009',
        'behaviour': '3D-Secure interactive',
        'result': 'accepted'
    },
    {
        'type': 'Maestro',
        'card_number': '5000550000000009',
        'behaviour': '3D-Secure interactive',
        'result': 'accepted'
    },
    {
        'type': 'CB',
        'card_number': '4970100000000003',
        'behaviour': 'Merchant without 3D-secure',
        'result': 'accepted'
    },
    {
        'type': 'MasterCard',
        'card_number': '5970100300000003',
        'behaviour': 'Merchant without 3D-secure',
        'result': 'accepted'
    },
    {
        'type': 'Maestro',
        'card_number': '5000550000000003',
        'behaviour': 'Merchant without 3D-secure',
        'result': 'accepted'
    },
    {
        'type': 'CB',
        'card_number': '4970100000000001',
        'behaviour': 'Buyer without 3D-secure',
        'result': 'accepted'
    },
    {
        'type': 'MasterCard',
        'card_number': '5970100300000001',
        'behaviour': 'Buyer without 3D-secure',
        'result': 'accepted'
    },
    {
        'type': 'Maestro',
        'card_number': '5000550000000001',
        'behaviour': 'Buyer without 3D-secure',
        'result': 'accepted'
    },
    {
        'type': 'CB',
        'card_number': '4970100000000002',
        'behaviour': 'Transaction to force',
        'result': 'rejected'
    },
    {
        'type': 'MasterCard',
        'card_number': '5970100300000002',
        'behaviour': 'Transaction to force',
        'result': 'rejected'
    },
    {
        'type': 'Maestro',
        'card_number': '5000550000000002',
        'behaviour': 'Transaction to force',
        'result': 'rejected'
    },
    {
        'type': 'CB',
        'card_number': '4970100000000007',
        'behaviour': 'Warranty = NO',
        'result': 'accepted'
    },
    {
        'type': 'MasterCard',
        'card_number': '5970100300023006',
        'behaviour': 'Warranty = NO',
        'result': 'accepted'
    },
    {
        'type': 'Maestro',
        'card_number': '5000550000023006',
        'behaviour': 'Warranty = NO',
        'result': 'accepted'
    },
    {
        'type': 'CB',
        'card_number': '4970100000000097',
        'behaviour': '3-D Secure authentication failed',
        'result': 'rejected'
    },
    {
        'type': 'MasterCard',
        'card_number': '5970100300000097',
        'behaviour': '3-D Secure authentication failed',
        'result': 'rejected'
    },
    {
        'type': 'Maestro',
        'card_number': '5000550000000097',
        'behaviour': '3-D Secure authentication failed',
        'result': 'rejected'
    },
    {
        'type': 'CB',
        'card_number': '4970100000000098',
        'behaviour': 'Card payment limit exceeded',
        'result': 'rejected'
    },
    {
        'type': 'MasterCard',
        'card_number': '5970100300000098',
        'behaviour': 'Card payment limit exceeded',
        'result': 'rejected'
    },
    {
        'type': 'Maestro',
        'card_number': '5000550000000098',
        'behaviour': 'Card payment limit exceeded',
        'result': 'rejected'
    },
    {
        'type': 'CB',
        'card_number': '4970100000000099',
        'behaviour': 'Wrong cryptogram',
        'result': 'rejected'
    },
    {
        'type': 'MasterCard',
        'card_number': '5970100300000099',
        'behaviour': 'Wrong cryptogram',
        'result': 'rejected'
    },
    {
        'type': 'Maestro',
        'card_number': '5000550000000099',
        'behaviour': 'Wrong cryptogram',
        'result': 'rejected'
    },
]

base_url = "http://www.if-then-else.fr/"

theme_args = collections.OrderedDict([
    ("success_footer_msg_return", "Success footer msg test"),
    ("cancel_footer_msg_return", "Cancel footer msg test"),
    ("secure_message", "Secure message test"),
    ("secure_message_register", "Secure message register test"),
    ("site_id_label", "Site ID label test"),
    ("css_for_payment", base_url+"payment.css"),
    ("css_for_payment_mobile", base_url+"mobile_payment.css"),
    ("header_for_mail", base_url+"mail_header.html"),
    ("footer_for_mail", base_url+"footer_mail.html"),
    ("shop_logo", base_url+"logo.png"),
])

payment_config_args = {
    "first": 5000,
    "count": 2,
    "period": 5
}

basic_payment_args = {
    "vads_trans_id": get_vads_trans_id(),
    "vads_amount": "1000",
}

customized_payment_args = {
    # Base fields
    "vads_amount": "10000",
    "vads_capture_delay": "2",
    "vads_payment_cards": "CB;Visa",
    "vads_return_mode": "POST",
    "vads_validation_mode": "1",
    "vads_url_success": base_url+"success/",
    "vads_url_referral": base_url+"referral/",
    "vads_url_refused": base_url+"refused/",
    "vads_url_cancel": base_url+"cancel/",
    "vads_url_error": base_url+"error/",
    "vads_url_return": base_url+"return/",
    "vads_trans_id": get_vads_trans_id(),
    "vads_user_info": "Abbath Doom Occulta",
    "vads_shop_name": "Immortal",
    "vads_redirect_success_timeout": "5",
    "vads_redirect_success_message": "Tragedies Blows At Horizon",
    "vads_redirect_error_timeout": "5",
    "vads_redirect_error_message": "At The Heart Of Winter",
    # customer fields
    "vads_cust_address": "Oeschstr.",
    "vads_cust_address_number": "9",
    "vads_cust_country": "GE",
    "vads_cust_email": "test@nuclearblast.de",
    "vads_cust_id": "1",
    "vads_cust_name": "NUCLEAR BLAST",
    "vads_cust_cell_phone": "+49 7162 9280-0",
    "vads_cust_phone": "+49 7162 9280 26",
    "vads_cust_title": "Guitarist",
    "vads_cust_city": "Donzdorf",
    "vads_cust_state": "Donzdorf",
    "vads_cust_zip": "73072",
    "vads_language": "fr",
    # order fields
    "vads_order_id": "1234567890",
    "vads_order_info": "Order test info 1",
    "vads_order_info2": "Order test info 2",
    "vads_order_info3": "Order test info 3",
    # shipping fields
    "vads_ship_to_name": "NUCLEAR BLAST",
    "vads_ship_to_street_number": "9",
    "vads_ship_to_street": "Oeschstr. 9",
    "vads_ship_to_street2": "...",
    "vads_ship_to_zip": "73072",
    "vads_ship_to_city": "Donzdorf",
    "vads_ship_to_country": "GE",
    "vads_ship_to_phone_num": "+49 7162 9280-0",
    "vads_ship_to_state": "Donzdorf"
}
