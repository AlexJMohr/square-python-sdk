# -*- coding: utf-8 -*-

from square.api_helper import APIHelper
from square.http.api_response import ApiResponse
from square.api.base_api import BaseApi
from apimatic_core.request_builder import RequestBuilder
from apimatic_core.response_handler import ResponseHandler
from apimatic_core.types.parameter import Parameter
from square.http.http_method_enum import HttpMethodEnum
from apimatic_core.authentication.multiple.single_auth import Single


class MerchantsApi(BaseApi):

    """A Controller to access Endpoints in the square API."""
    def __init__(self, config):
        super(MerchantsApi, self).__init__(config)

    def list_merchants(self,
                       cursor=None):
        """Does a GET request to /v2/merchants.

        Provides details about the merchant associated with a given access
        token.
        The access token used to connect your application to a Square seller
        is associated
        with a single merchant. That means that `ListMerchants` returns a
        list
        with a single `Merchant` object. You can specify your personal access
        token
        to get your own merchant information or specify an OAuth token to get
        the
        information for the merchant that granted your application access.
        If you know the merchant ID, you can also use the
        [RetrieveMerchant]($e/Merchants/RetrieveMerchant)
        endpoint to retrieve the merchant information.

        Args:
            cursor (int, optional): The cursor generated by the previous
                response.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server('default')
            .path('/v2/merchants')
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                         .key('cursor')
                         .value(cursor))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .is_api_response(True)
            .convertor(ApiResponse.create)
        ).execute()

    def retrieve_merchant(self,
                          merchant_id):
        """Does a GET request to /v2/merchants/{merchant_id}.

        Retrieves the `Merchant` object for the given `merchant_id`.

        Args:
            merchant_id (str): The ID of the merchant to retrieve. If the
                string "me" is supplied as the ID, then retrieve the merchant
                that is currently accessible to this call.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server('default')
            .path('/v2/merchants/{merchant_id}')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('merchant_id')
                            .value(merchant_id)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .is_api_response(True)
            .convertor(ApiResponse.create)
        ).execute()
