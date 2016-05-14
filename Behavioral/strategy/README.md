# Strategy

decoupling interface from implementations
different behaviors whose interfaces can be changed transparently when it's being used by clients

has: family of behaviors
make different implementations of a behavior

* context

good: changing strategies on the fly
problem: multiple strategies getting in-compatible
context: not everything can be put in a common interface (hashmap)

use when:
difference only in behavior
algorithms: different space-time complexities
a lot of conditional behaviors in an entity

context: pass itself to strategy
sometimes has CreateConcreteStrategy: clients will only interact with context

favor composition over inheritance

