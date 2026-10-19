> ## Documentation Index
> Fetch the complete documentation index at: https://docs.blinkops.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Array Utilities

> Utility actions for manipulating, filtering, and transforming array data in Blink workflows.

## Append To Array

Append an element to an array.

<div className="integrations-table">
  | Parameter | Description |
  | - | - |
  | Array | The source array to append the element to. |
  | Element To Append | The element to append to the array. |
</div>

<Frame>
  <img src="https://mintcdn.com/blinkops-2/5S6z5MxgBLy6FDIP/img/Utilities/array_utilities_append_to_list.png?fit=max&auto=format&n=5S6z5MxgBLy6FDIP&q=85&s=5d97ea7b7fb869c065568be9b0002f1f" width="2380" height="840" data-path="img/Utilities/array_utilities_append_to_list.png" />
</Frame>

## Append To JSON List

Append an object to a list within a JSON object. The object will be added even if it already exists within the list.

<div className="integrations-table">
  | Parameter | Description |
  | - | - |
  | Existing JSON List Or Object | The JSON list or object to which the new object will be appended. Note that nested keys are only applicable to JSON objects, not lists. If the existing JSON is a list, direct appending to the end of the list is used. Also, ensure that the nested key provided points to an existing JSON list inside the JSON object. |
  | JSON Object To Append | The object data to append. |
  | Nested Object Key | The nested object key to append the data to. This parameter can only be used when the existing JSON is an object. |
</div>

<Frame>
  <img src="https://mintcdn.com/blinkops-2/rI4Qa3pv_haSGbfd/img/Utilities/array_utilities-appendjson.png?fit=max&auto=format&n=rI4Qa3pv_haSGbfd&q=85&s=524c8925b709ba63619b01f2fd22bbe5" width="1994" height="882" data-path="img/Utilities/array_utilities-appendjson.png" />
</Frame>

## Append To List (Deprecated)

<Warning>
  This utility has been deprecated and will no longer be available in new workflows. You can use `Append To Array` instead.
</Warning>

Append an item to the end of a list. If the variable does not exist, the action will create a new list automatically.

<div className="integrations-table">
  | Parameter | Description |
  | - | - |
  | Variable Name | The name of the variable. |
  | Item | Item to add to list. |
</div>

<Frame>
  <img src="https://mintcdn.com/blinkops-2/rI4Qa3pv_haSGbfd/img/Utilities/array_utilities-append.png?fit=max&auto=format&n=rI4Qa3pv_haSGbfd&q=85&s=ba17e10eb0a1b4e9a611a5bde7de2c29" width="1990" height="880" data-path="img/Utilities/array_utilities-append.png" />
</Frame>

## Compare Arrays

Compare two arrays and determine if they are equal.

<div className="integrations-table">
  | Parameter | Description |
  | - | - |
  | First Array | The first array to compare with the `Second Array`. Value must be a valid array or a comma-separated list. |
  | Second Array | The second array to compare with the `First Array`. Value must be a valid array or a comma-separated list. |
  | Ignore Order | When checked, arrays will be considered equal even if elements appear in a different order. |
  | Loose Typing | When checked, enables type coercion during comparison (e.g., number `12` equals string `"12"`, boolean `true` equals string `"true"`). |
</div>

<Frame>
  <img src="https://mintcdn.com/blinkops-2/rI4Qa3pv_haSGbfd/img/Utilities/array_utilities-compare.png?fit=max&auto=format&n=rI4Qa3pv_haSGbfd&q=85&s=57bf7f6387c3f8911f11d11c5d0467f2" width="1992" height="880" data-path="img/Utilities/array_utilities-compare.png" />
</Frame>

## Concat Arrays

Combine two arrays into a single array containing all elements from both.

<div className="integrations-table">
  | Parameter | Description |
  | - | - |
  | First Array | The initial array whose elements will appear at the beginning of the result. Value must be a valid array or a comma separated list. |
  | Second Array | The array whose elements will be appended after the first array. Value must be a valid array or a comma separated list. |
  | Remove Duplicates | When checked, repeated values in the final combined array are removed. |
</div>

<Frame>
  <img src="https://mintcdn.com/blinkops-2/rI4Qa3pv_haSGbfd/img/Utilities/array_utilities-concat.png?fit=max&auto=format&n=rI4Qa3pv_haSGbfd&q=85&s=59510d4113e7d1c255601e0ac12507ac" width="1992" height="880" data-path="img/Utilities/array_utilities-concat.png" />
</Frame>

## Extract Field From Array

Extract a specific field from each item in an array and get the values as a new array.

<div className="integrations-table">
  | Parameter | Description |
  | - | - |
  | Array | The array from which to extract the specified field.<br /><br />Value must be a valid array or a comma-separated list. |
  | Field Path | The name or path of the field to extract from each array item.<ul><li>For top-level properties, simply use the property name (e.g., `id`).</li><li>For nested properties, use dot notation (e.g., `details.id`).</li></ul>For example, given this array:<br /><br />`[{"userId": "user123","details": {"id": "id123"}},{"userId": "user789","details": {"id": "id789"}}]`<ul><li>Using `userId` would extract: <code>\["user123", "user789"]</code></li><li>Using `details.id` would extract: <code>\["id123", "id789"]</code></li></ul> |
  | Skip Missing | When checked, records with missing fields will be excluded from the result.<br /><br />When unchecked, records with missing fields will be included with `null` values. |
  | Remove Duplicates | When checked, repeated values in the final array are removed. |
</div>

<Frame>
  <img src="https://mintcdn.com/blinkops-2/rI4Qa3pv_haSGbfd/img/Utilities/array_utilities-extractfield.png?fit=max&auto=format&n=rI4Qa3pv_haSGbfd&q=85&s=8df9c573147aa66547b33f254e244b45" width="1988" height="878" data-path="img/Utilities/array_utilities-extractfield.png" />
</Frame>

## Extend List

The **Extend List** utility action allows you to **append an item** to the end of your list or **append a second list** onto the end of your original list.
You can choose the **list** you want to **append** to by clicking on the dynamic dropdown menu and selecting your preferred **list**.

<div className="integrations-table">
  | Parameter | Description |
  | - | - |
  | Variable name | The name of the original list variable |
  | List to append | The name of second list to append. |
  | Value | Name of the item to append to the list |
</div>

The **Extend List** utility action enables you to:

1. Append a variable to the end of an original list

<Frame>
  <img src="https://mintcdn.com/blinkops-2/ZUtie3exEe7_7B_M/img/Actions/Extend.png?fit=max&auto=format&n=ZUtie3exEe7_7B_M&q=85&s=6c96141e1fdc5948018e5680718d067e" width="2401" height="1662" data-path="img/Actions/Extend.png" />
</Frame>

2. Append a second list to the end of an original list

<Frame>
  <img src="https://mintcdn.com/blinkops-2/ZUtie3exEe7_7B_M/img/Actions/Extend-2.png?fit=max&auto=format&n=ZUtie3exEe7_7B_M&q=85&s=22cf0678e49af674ef16dbf5c3470018" width="2408" height="1680" data-path="img/Actions/Extend-2.png" />
</Frame>

3. Append both a variable and a second list to the end of the original list

<Frame>
  <img src="https://mintcdn.com/blinkops-2/ZUtie3exEe7_7B_M/img/Actions/Extend-3.png?fit=max&auto=format&n=ZUtie3exEe7_7B_M&q=85&s=4bbd4093539801366cf9b7d58a54aff8" width="2390" height="1684" data-path="img/Actions/Extend-3.png" />
</Frame>

## Filter Array

Filter array elements using a `Filter Function`.

<div className="integrations-table">
  | Parameter | Description |
  | - | - |
  | Array | The array to be filtered.<br /><br />Value must be a valid array or a comma-separated list. |
  | Filter Function | A Python function that determines which elements to keep in the array.<br /><br />The `Filter Function` is executed **individually for each element** in the input `Array`. For every element, the function should:<br /><ul><li>Return `True` if you want to include that element in the resulting filtered array.</li><li>Return `False` if you want to exclude that element.</li></ul><br />For example:<br /><code>def even(n):  return n % 2 == 0</code> |
</div>

<Frame>
  <img src="https://mintcdn.com/blinkops-2/rI4Qa3pv_haSGbfd/img/Utilities/array_utilities-filter.png?fit=max&auto=format&n=rI4Qa3pv_haSGbfd&q=85&s=ff6890c81687f05b91ed827d1bb30ad4" width="1990" height="876" data-path="img/Utilities/array_utilities-filter.png" />
</Frame>

## Get Array Length

Get the number of elements in a specified array.

<div className="integrations-table">
  | Parameter | Description |
  | - | - |
  | Array | The array to get the length of.<br /><br />Value must be a valid array or a comma-separated list. |
</div>

<Frame>
  <img src="https://mintcdn.com/blinkops-2/aSwCm9AAnnCD7gkQ/img/Utilities/array_utilities-getlength.png?fit=max&auto=format&n=aSwCm9AAnnCD7gkQ&q=85&s=7704672dd7d5ecfea2ab6bd54d29be63" width="2584" height="878" data-path="img/Utilities/array_utilities-getlength.png" />
</Frame>

## Get Item From Array

Get a single item from an array at the specified index position.

<div className="integrations-table">
  | Parameter | Description |
  | - | - |
  | Array | The array from which to retrieve an element.<br /><br />Value must be a valid array or a comma-separated list. |
  | Index | The position of the item to get. The first item has an index of `0`. |
</div>

<Frame>
  <img src="https://mintcdn.com/blinkops-2/rI4Qa3pv_haSGbfd/img/Utilities/array_utilities-getitem.png?fit=max&auto=format&n=rI4Qa3pv_haSGbfd&q=85&s=d0ab83e2dc7635af79c3db732e997ac4" width="1994" height="882" data-path="img/Utilities/array_utilities-getitem.png" />
</Frame>

## Get Random Item From Array

Get a random item from a specified array.

<div className="integrations-table">
  | Parameter | Description |
  | - | - |
  | Array | The array from which to select a random item.<br /><br />Value must be a valid array or a comma-separated list. |
</div>

<Frame>
  <img src="https://mintcdn.com/blinkops-2/aSwCm9AAnnCD7gkQ/img/Utilities/array_utilities-getrandomitem.png?fit=max&auto=format&n=aSwCm9AAnnCD7gkQ&q=85&s=2b2e7a20516211888ad858e0cac28619" width="2582" height="876" data-path="img/Utilities/array_utilities-getrandomitem.png" />
</Frame>

## Remove Duplicates From List

Removes duplicate elements from a list.

<div className="integrations-table">
  | Parameter | Description |
  | - | - |
  | List | The JSON list to remove duplicates from. <br /> <br /> For example: The input list `[1,2,2,1]` will result in the output list `[2,1]`. |
</div>

<Frame>
  <img src="https://mintcdn.com/blinkops-2/rI4Qa3pv_haSGbfd/img/Utilities/array_utilities-removeduplicates.png?fit=max&auto=format&n=rI4Qa3pv_haSGbfd&q=85&s=a1864c24e195c836125bb44e08197a87" width="1990" height="878" data-path="img/Utilities/array_utilities-removeduplicates.png" />
</Frame>

## Remove From JSON List

Remove an object from a list within a JSON object. All instances of the object will be removed from the list.

<div className="integrations-table">
  | Parameter | Description |
  | - | - |
  | Existing JSON List Or Object | The JSON list or object from which the object will be removed. Note that nested keys are only applicable to JSON objects, not lists. Also, ensure that the nested key provided points to an existing JSON list inside the JSON object. |
  | JSON Object To Remove | The concrete object to remove. Ensure that the provided object is equal to the desired object to remove. |
  | Nested Object Key | The nested object key to remove the data from. This parameter can only be used when the existing JSON is an object. |
</div>

<Frame>
  <img src="https://mintcdn.com/blinkops-2/rI4Qa3pv_haSGbfd/img/Utilities/array_utilities-removefromjsonlist.png?fit=max&auto=format&n=rI4Qa3pv_haSGbfd&q=85&s=47041b05f17d0a0669e17268df30da05" width="1990" height="878" data-path="img/Utilities/array_utilities-removefromjsonlist.png" />
</Frame>

## Reverse List

Reverses the order of elements in a list.

For example: The list `[8,12,2,6]` will result in the output list: `[6,2,12,8]`.

<div className="integrations-table">
  | Parameter | Description |
  | - | - |
  | List | The JSON list to reverse. <br /> <br />  For example: The input list `[1,2,3]` will result in the output list `[3,2,1]`. |
</div>

<Frame>
  <img src="https://mintcdn.com/blinkops-2/rI4Qa3pv_haSGbfd/img/Utilities/array_utilities-reverse.png?fit=max&auto=format&n=rI4Qa3pv_haSGbfd&q=85&s=7e66c3981cd3401dab3fb1aa80d5ed8f" width="1992" height="874" data-path="img/Utilities/array_utilities-reverse.png" />
</Frame>

## Slice Array

Slice elements from an array between `Start Index` and `End Index`.

The new array will contain elements from the source array beginning at `Start Index` (inclusive) up to but not including `End Index` (exclusive).

<div className="integrations-table">
  | Parameter | Description |
  | - | - |
  | Array | The array to slice elements from.<br /><br />Value must be a valid array or a comma-separated list. |
  | Start Index | The index of the first element to include in the slice.<br /><br /><ul><li>The first element of the array has an index of `0`.</li><li>Defaults to `0` if not specified, effectively starting from the beginning of the array.</li></ul> |
  | End Index | The index of the element *after* the last element to include in the slice.<br /><br /><ul><li>The slice includes elements up to, but not including, this index.</li><li>If not provided, the slice will go to the end of the array.</li></ul> |
</div>

<Frame>
  <img src="https://mintcdn.com/blinkops-2/rI4Qa3pv_haSGbfd/img/Utilities/array_utilities-slice.png?fit=max&auto=format&n=rI4Qa3pv_haSGbfd&q=85&s=c3a6490c37ca7a361817c5c18930b43d" width="1990" height="878" data-path="img/Utilities/array_utilities-slice.png" />
</Frame>

## Sort Array

Sort array elements of the same type in ascending or descending order.

<div className="integrations-table">
  | Parameter | Description |
  | - | - |
  | Array | The array to be sorted.<br /><br />Value must be a valid array or a comma-separated list. |
  | Order | Select the sorting direction for the array. |
  | Comparison Function | A Python function used to extract a comparison key from each element. Used for sorting complex or mixed-type arrays.<br /><br />This function must return a comparable value.<br />For example:<br /><code>def myFunc(item):  return item\['property']</code> |
</div>

<Frame>
  <img src="https://mintcdn.com/blinkops-2/rI4Qa3pv_haSGbfd/img/Utilities/array_utilities-sort.png?fit=max&auto=format&n=rI4Qa3pv_haSGbfd&q=85&s=42f8073f003596704165b5a815d8e5da" width="1990" height="880" data-path="img/Utilities/array_utilities-sort.png" />
</Frame>

## Split Array

Split a single array into multiple smaller arrays (chunks) of a specified size.

<div className="integrations-table">
  | Parameter | Description |
  | - | - |
  | Array | The array to be sorted.<br /><br />Value must be a valid array or a comma-separated list. |
  | Chunk Size | The maximum size of the chunks that will be created. |
  | Get Response As JSON Object | Select to get the result as JSON object instead of a nested array. |
</div>

<Frame>
  <img src="https://mintcdn.com/blinkops-2/rI4Qa3pv_haSGbfd/img/Utilities/array_utilities-split.png?fit=max&auto=format&n=rI4Qa3pv_haSGbfd&q=85&s=992a7847e00481efc08dce89e44b6e93" width="1988" height="878" data-path="img/Utilities/array_utilities-split.png" />
</Frame>


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.