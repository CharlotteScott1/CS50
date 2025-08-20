# Analysis

## Layer 8, Head 11
This mask specifically focuses on the key relationships in the sentence such as who is making the action, what the action is doing and where it is occuring leaving most other nodes dim.

With the first example below the brightest pixles are [the -> man],[rode -> [MASK]],[a -> [MASK]] and [through -> town]
With the second example [the -> penguin], [happly -> waddled], [along -> ice] and [mask -> ice]

Example Sentences:
- The man rode a [MASK] through town -> horse, wagon, carriage
- The penguin waddled happily along the [MASK] ice -> frozen, wet, broken

## Layer 6, Head 10

This layer focuses on the connection between a word and the word that follows it with the exception of the verb which ignores the "a" and instead focuses on the noun that follows. The action also focuses equally on the adjective and the following description/noun.

In the first example below the word "rode" maps to the mask with a dimmer focus on the word "a"
In the second example the word "waddled" maps equally to "happily" and "along"

Example Sentences:
- The man rode a [MASK] through town -> horse, wagon, carriage
- The penguin waddled happily along the [MASK] ice -> frozen, wet, broken

