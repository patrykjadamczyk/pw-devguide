### 6.1 - CQS & CQRS
CQS - Command Query Separation - this is way of writing code. 
In this way you separating writes (side effects) from reads. 
Query in this model can take data from somewhere for example database or some kind of object. 
And give you back data. Query can only read, can't write, can't make side effects of use. 
Command on the other hand can only do some stuff having side effects and write somewhere.
Can't return anything.

CQRS - Command Query Responsibility Segregation - This is model based CQS.
In this model role of Command change in some way. Because Command is clean data.
Logic behind Command is hidden behind Command Handler.
This is function which is associated with exactly one type of Command. 

Below are some examples of implementation. 
