
# Catalog Item Modifier List Info

References a text-based modifier or a list of non text-based modifiers applied to a `CatalogItem` instance
and specifies supported behaviors of the application.

## Structure

`Catalog Item Modifier List Info`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `modifier_list_id` | `str` | Required | The ID of the `CatalogModifierList` controlled by this `CatalogModifierListInfo`.<br>**Constraints**: *Minimum Length*: `1` |
| `modifier_overrides` | [`List Catalog Modifier Override`](../../doc/models/catalog-modifier-override.md) | Optional | A set of `CatalogModifierOverride` objects that override whether a given `CatalogModifier` is enabled by default. |
| `min_selected_modifiers` | `int` | Optional | If 0 or larger, the smallest number of `CatalogModifier`s that must be selected from this `CatalogModifierList`. |
| `max_selected_modifiers` | `int` | Optional | If 0 or larger, the largest number of `CatalogModifier`s that can be selected from this `CatalogModifierList`. |
| `enabled` | `bool` | Optional | If `true`, enable this `CatalogModifierList`. The default value is `true`. |
| `ordinal` | `int` | Optional | The position of this `CatalogItemModifierListInfo` object within the `modifier_list_info` list applied<br>to a `CatalogItem` instance. |

## Example (as JSON)

```json
{
  "modifier_list_id": "modifier_list_id6",
  "modifier_overrides": [
    {
      "modifier_id": "modifier_id8",
      "on_by_default": false
    },
    {
      "modifier_id": "modifier_id8",
      "on_by_default": false
    }
  ],
  "min_selected_modifiers": 170,
  "max_selected_modifiers": 66,
  "enabled": false,
  "ordinal": 204
}
```

