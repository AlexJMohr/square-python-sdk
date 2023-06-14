
# Update Location Custom Attribute Definition Response

Represents an [UpdateLocationCustomAttributeDefinition](../../doc/api/location-custom-attributes.md#update-location-custom-attribute-definition) response.
Either `custom_attribute_definition` or `errors` is present in the response.

## Structure

`Update Location Custom Attribute Definition Response`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `custom_attribute_definition` | [`Custom Attribute Definition`](../../doc/models/custom-attribute-definition.md) | Optional | Represents a definition for custom attribute values. A custom attribute definition<br>specifies the key, visibility, schema, and other properties for a custom attribute. |
| `errors` | [`List of Error`](../../doc/models/error.md) | Optional | Any errors that occurred during the request. |

## Example (as JSON)

```json
{
  "custom_attribute_definition": {
    "created_at": "2022-12-02T19:06:36.559Z",
    "description": "Update the description as desired.",
    "key": "bestseller",
    "name": "Bestseller",
    "schema": {
      "key1": "val1",
      "key2": "val2"
    },
    "updated_at": "2022-12-02T19:34:10.181Z",
    "version": 2,
    "visibility": "VISIBILITY_READ_ONLY"
  },
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
  ]
}
```
