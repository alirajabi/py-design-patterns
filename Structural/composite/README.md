Intent: Treat Individual objects and multiple, recursively composed objects uniformly.

Where:
  - Recursive hierarchies
  - no distinction between individual and composed elements
  - objects in structure can be treated uniformly

uniformity: Treat components similarly. (Iterate the same, etc.)
so no type tags etc.
new Components subclasses work easily
classes hold data that they actually need

complex hierarchy
unnecessary methods

Do we need parent references?

same interface between leaf & composites

notes:
* don't allocate storage for children in composites
* who is responsible for deleting chilren?
