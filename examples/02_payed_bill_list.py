# coding=utf-8
from __future__ import unicode_literals
from pod_base import APIException, PodException
from examples.config import *
from pod_tools import PodTools

try:
    pod_tools = PodTools(api_token=API_TOKEN, sc_api_key=SC_API_KEY)

    params = {
        # "id": 0,  # شناسه
        # "fromDate": "1398/12/01",  # حد پایین تاریخ - به صورت شمسی و فرمت yyyy/mm/dd
        # "toDate": "1398/12/29",  # حد بالای تاریخ - به صورت شمسی و فرمت yyyy/mm/dd
        # "billId": "5006002508016"  # شناسه قبض
        # "paymentId": "10884247",  # شناسه پرداخت
        # "referenceNumber": "828590"  # کد رهگیری (ارجاع)
        "page": 1,
        "size": 50
    }

    print(pod_tools.payed_bill_list(**params))
    # OUTPUT
    # [
    #   {
    #     "id": 82859,
    #     "billId": "500××××××××16",
    #     "paymentId": "10××××47",
    #     "price": 108000,
    #     "utilityCompanyName": "آب",
    #     "subUtilityCompanyName": "آبفا مشهد080",
    #     "requestDate": 1583218721659,
    #     "referenceNumber": 8××××0,
    #     "status": "SERVICE_BILL_ACCEPTED",
    #     "invoiceId": 9×××××3,
    #     "settlementRequestId": 0,
    #     "userSrv": {
    #       "id": 2841073,
    #       "name": "شرکت رضا زارع",
    #       "ssoId": "11963175",
    #       "ssoIssuerCode": 1,
    #       "profileImage": "https://core.pod.ir:443/nzh/image/?imageId=..."
    #     },
    #     "cancelDate": 0
    #   }
    # ]

except APIException as e:
    print("API Exception\nError {}\nError Code : {}\nReference Number : {}".format(e.message, e.error_code,
                                                                                   e.reference_number))
except PodException as e:
    print("Pod Exception: ", e.message)
