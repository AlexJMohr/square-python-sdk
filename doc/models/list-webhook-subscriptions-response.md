
# List Webhook Subscriptions Response

Defines the fields that are included in the response body of
a request to the [ListWebhookSubscriptions](../../doc/api/webhook-subscriptions.md#list-webhook-subscriptions) endpoint.

Note: if there are errors processing the request, the subscriptions field will not be
present.

## Structure

`List Webhook Subscriptions Response`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `errors` | [`List of Error`](../../doc/models/error.md) | Optional | Information on errors encountered during the request. |
| `subscriptions` | [`List of Webhook Subscription`](../../doc/models/webhook-subscription.md) | Optional | The requested list of [Subscription](entity:WebhookSubscription)s. |
| `cursor` | `string` | Optional | The pagination cursor to be used in a subsequent request. If empty,<br>this is the final response.<br><br>For more information, see [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination). |

## Example (as JSON)

```json
{
  "subscriptions": [
    {
      "api_version": "2021-12-15",
      "created_at": "2022-01-10 23:29:48 +0000 UTC",
      "enabled": true,
      "event_types": [
        "payment.created",
        "payment.updated"
      ],
      "id": "wbhk_b35f6b3145074cf9ad513610786c19d5",
      "name": "Example Webhook Subscription",
      "notification_url": "https://example-webhook-url.com",
      "updated_at": "2022-01-10 23:29:48 +0000 UTC"
    }
  ],
  "errors": [
    {
      "category": "AUTHENTICATION_ERROR",
      "code": "REFUND_ALREADY_PENDING",
      "detail": "detail1",
      "field": "field9"
    },
    {
      "category": "INVALID_REQUEST_ERROR",
      "code": "PAYMENT_NOT_REFUNDABLE",
      "detail": "detail2",
      "field": "field0"
    },
    {
      "category": "RATE_LIMIT_ERROR",
      "code": "REFUND_DECLINED",
      "detail": "detail3",
      "field": "field1"
    }
  ],
  "cursor": "cursor6"
}
```
