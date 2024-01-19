Did you discuss this assignment with any students? Please list their cs logins.
no
How many late days are you using on this assignment?
too many (thank you for your patience)

Suppose that you were sorting records (i.e., instances of a dataclass with multiple fields, only one of which is the
key to be sorted over), rather than just integer keys. What issues might arise in your random testing approach?
Dataclasses won’t let you use different subsets of fields for == and <
the field declaration excludes the name field from these comparisons. As a result, Records will be ordered entirely
by their age field.