 **Periodic Table Element Information Retrieval**

This Python script allows users to retrieve detailed information about elements from the periodic table by inputting their atomic number. It utilizes the `periodictable` module to access and display various properties of the specified element.

**Step-by-Step Explanation:**

1. **Importing the `periodictable` Module**:
   ```python
   import periodictable
   ```
   This line imports the `periodictable` module, which provides a comprehensive library for working with elements and their properties.

2. **User Input**:
   ```python
   Atomic_no = int(input("Enter element Atomic no. :-"))
   ```
   The script prompts the user to enter the atomic number of the element they want to retrieve information about. The `input()` function captures the user's input as a string, and the `int()` function converts it into an integer.

3. **Accessing Element Information**:
   ```python
   element = periodictable.elements[Atomic_no]
   ```
   Using the atomic number provided by the user, the script accesses the corresponding element object from the `periodictable` module's `elements` dictionary. This element object contains detailed information about the specified element.

4. **Displaying Element Properties**:
   The script then proceeds to display various properties of the selected element:
   - **Atomic Number**:
     ```python
     print('Atomic no: ', element.number)
     ```
   - **Symbol**:
     ```python
     print('Symbol: ', element.symbol)
     ```
   - **Name**:
     ```python
     print('Name: ', element.name)
     ```
   - **Atomic Mass**:
     ```python
     print('Atomic mass: ', element.mass)
     ```
   - **Density**:
     ```python
     print('Density: ', element.density)
     ```

**Code Snippets:**

- Importing the `periodictable` module:
  ```python
  import periodictable
  ```

- Accessing element information:
  ```python
  element = periodictable.elements[Atomic_no]
  ```

- Displaying element properties:
  ```python
  print('Atomic no: ', element.number)
  print('Symbol: ', element.symbol)
  print('Name: ', element.name)
  print('Atomic mass

