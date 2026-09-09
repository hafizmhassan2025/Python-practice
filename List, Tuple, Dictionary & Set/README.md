# Python Collections: List, Tuple, Dictionary & Set

Python provides several built-in data types for storing multiple values.

The four important collection types are:

* **List** → Ordered and changeable collection
* **Tuple** → Ordered and unchangeable collection
* **Dictionary** → Key-value pairs
* **Set** → Unordered collection of unique values

---

## 1. Quick Comparison

| Feature                | List                | Tuple            | Dictionary     | Set          |
| ---------------------- | ------------------- | ---------------- | -------------- | ------------ |
| Syntax                 | `[]`                | `()`             | `{key: value}` | `{}`         |
| Ordered                | Yes                 | Yes              | Yes*           | No indexing  |
| Changeable             | Yes                 | No               | Yes            | Yes          |
| Allows duplicates      | Yes                 | Yes              | Keys: No       | No           |
| Indexing               | Yes                 | Yes              | No             | No           |
| Stores key-value pairs | No                  | No               | Yes            | No           |
| Main use               | Collection of items | Fixed collection | Key-value data | Unique items |

> **Note:** Dictionaries preserve insertion order in modern Python, but they are accessed using **keys**, not numeric indexes.

---

# 2. List

A **list** is used when you want to store multiple values and may need to change them later.

### Example

```python
fruits = ["apple", "banana", "mango"]

print(fruits)
```

### Lists are changeable

```python
fruits[1] = "orange"

print(fruits)
```

Output:

```text
["apple", "orange", "mango"]
```

### Lists allow duplicates

```python
numbers = [10, 20, 20, 30, 30]
```

---

## Useful List Methods

### `append()`

Adds one item at the end.

```python
numbers = [1, 2, 3]

numbers.append(4)

print(numbers)
```

Output:

```text
[1, 2, 3, 4]
```

---

### `insert()`

Adds an item at a specific position.

```python
numbers.insert(1, 10)
```

---

### `remove()`

Removes a specific value.

```python
numbers.remove(10)
```

---

### `pop()`

Removes an item using its index.

```python
numbers.pop(1)
```

If no index is provided, it removes the last item.

```python
numbers.pop()
```

---

### `sort()`

Sorts the list.

```python
numbers.sort()
```

---

### `reverse()`

Reverses the list.

```python
numbers.reverse()
```

---

### `count()`

Counts how many times a value appears.

```python
numbers.count(20)
```

---

### `index()`

Returns the index of a value.

```python
numbers.index(20)
```

---

# 3. Tuple

A **tuple** is similar to a list, but it **cannot be changed after creation**.

### Example

```python
coordinates = (10, 20, 30)
```

You can access values using indexes:

```python
print(coordinates[0])
```

Output:

```text
10
```

But you cannot change an item:

```python
coordinates[0] = 50
```

This gives an error because tuples are **immutable**.

---

## Why Use a Tuple?

Use a tuple when your data should remain fixed.

For example:

```python
student_info = ("Hassan", 20, "AI")
```

If the information should not be changed, a tuple can be useful.

---

## Useful Tuple Methods

Tuples have fewer methods because they cannot be changed.

### `count()`

Counts how many times a value appears.

```python
numbers = (10, 20, 20, 30)

print(numbers.count(20))
```

Output:

```text
2
```

---

### `index()`

Returns the index of a value.

```python
print(numbers.index(20))
```

Output:

```text
1
```

---

# 4. Dictionary

A **dictionary** stores data in **key-value pairs**.

### Example

```python
student = {
    "name": "Hassan",
    "age": 20,
    "field": "AI"
}
```

Here:

```text
"name"  → key
"Hassan" → value

"age"   → key
20      → value
```

You access values using their keys:

```python
print(student["name"])
```

Output:

```text
Hassan
```

---

## Dictionaries Are Changeable

You can change a value:

```python
student["age"] = 21
```

You can also add a new key-value pair:

```python
student["city"] = "Islamabad"
```

---

## Dictionary Keys Must Be Unique

This is not recommended:

```python
student = {
    "name": "Hassan",
    "name": "Ali"
}
```

The second `"name"` replaces the first one.

---

## Useful Dictionary Methods

### `get()`

Gets the value of a key.

```python
print(student.get("name"))
```

A major advantage of `get()` is that it can avoid an error if the key doesn't exist.

```python
print(student.get("email"))
```

---

### `keys()`

Returns all keys.

```python
print(student.keys())
```

---

### `values()`

Returns all values.

```python
print(student.values())
```

---

### `items()`

Returns key-value pairs.

```python
print(student.items())
```

---

### `update()`

Adds or updates dictionary data.

```python
student.update({"age": 21})
```

---

### `pop()`

Removes a key-value pair.

```python
student.pop("age")
```

---

### `clear()`

Removes everything from the dictionary.

```python
student.clear()
```

---

# 5. Set

A **set** is a collection that stores **unique values**.

### Example

```python
numbers = {1, 2, 3, 4}
```

Sets automatically remove duplicates:

```python
numbers = {1, 2, 2, 3, 3, 4}

print(numbers)
```

The result contains only:

```text
{1, 2, 3, 4}
```

---

## Sets Do Not Use Indexes

You cannot do:

```python
numbers[0]
```

because sets do not support indexing.

---

## Useful Set Methods

### `add()`

Adds one item.

```python
numbers.add(5)
```

---

### `remove()`

Removes an item.

```python
numbers.remove(5)
```

If the item doesn't exist, `remove()` gives an error.

---

### `discard()`

Removes an item if it exists.

```python
numbers.discard(5)
```

Unlike `remove()`, `discard()` does not give an error if the item is missing.

---

### `union()`

Combines two sets.

```python
a = {1, 2, 3}
b = {3, 4, 5}

print(a.union(b))
```

Result:

```text
{1, 2, 3, 4, 5}
```

---

### `intersection()`

Returns common values.

```python
print(a.intersection(b))
```

Result:

```text
{3}
```

---

### `difference()`

Returns values that exist in the first set but not the second.

```python
print(a.difference(b))
```

Result:

```text
{1, 2}
```

---

### `clear()`

Removes all items.

```python
numbers.clear()
```

---

# 6. Methods Commonly Used with These Collections

Some useful functions work with **all or most** of these data types.

### `len()`

Returns the number of items.

```python
len([1, 2, 3])
```

```python
len((1, 2, 3))
```

```python
len({"a": 1, "b": 2})
```

```python
len({1, 2, 3})
```

---

### `in`

Checks whether an item exists.

```python
2 in [1, 2, 3]
```

Result:

```text
True
```

For dictionaries, `in` checks **keys**:

```python
"name" in student
```

---

### `not in`

Checks whether an item does not exist.

```python
5 not in [1, 2, 3]
```

Result:

```text
True
```

---

### `for` Loop

You can loop through collections.

#### List

```python
for item in fruits:
    print(item)
```

#### Tuple

```python
for item in coordinates:
    print(item)
```

#### Dictionary

```python
for key, value in student.items():
    print(key, value)
```

#### Set

```python
for item in numbers:
    print(item)
```

---

# 7. When Should You Use Each One?

### Use a List when:

You need an **ordered collection that you can change**.

```python
shopping_list = ["milk", "bread", "eggs"]
```

---

### Use a Tuple when:

You need an **ordered collection that should not change**.

```python
coordinates = (10, 20)
```

---

### Use a Dictionary when:

You need to store **information using names/keys**.

```python
student = {
    "name": "Hassan",
    "age": 20
}
```

---

### Use a Set when:

You need **unique values** and don't need indexes.

```python
unique_numbers = {1, 2, 3, 4}
```

---

# 8. Easy Way to Remember

Think about them like this:

```text
LIST
↓
Ordered + Changeable + Duplicates allowed

TUPLE
↓
Ordered + NOT changeable + Duplicates allowed

DICTIONARY
↓
Key → Value

SET
↓
Unique values + No indexing
```

### One-line summary

> **List = Changeable collection**
> **Tuple = Fixed collection**
> **Dictionary = Key-value collection**
> **Set = Unique collection**

---

# 9. Quick Example

```python
# List
fruits = ["apple", "banana", "apple"]

# Tuple
coordinates = (10, 20)

# Dictionary
student = {
    "name": "Hassan",
    "age": 20
}

# Set
numbers = {1, 2, 2, 3}

print(fruits)
print(coordinates)
print(student)
print(numbers)
```

The set will automatically remove the duplicate `2`.

---

## Important Terms

| Term      | Meaning                                 |
| --------- | --------------------------------------- |
| Mutable   | Can be changed after creation           |
| Immutable | Cannot be changed after creation        |
| Ordered   | Items have a predictable position/order |
| Duplicate | Same value appears more than once       |
| Key       | Name used to access a dictionary value  |
| Value     | Data stored in a dictionary             |
| Index     | Position of an item, starting from `0`  |

---

## Final Comparison

```text
              LIST       TUPLE       DICTIONARY       SET

Ordered       Yes        Yes         Yes              No indexing
Mutable       Yes        No          Yes              Yes
Duplicates    Yes        Yes         Keys: No         No
Indexing      Yes        Yes         No               No
Key-Value     No         No          Yes              No
```

These four data types are some of the **most important Python collections**. Understanding when and why to use each one will make it much easier to write Python programs.
