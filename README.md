# PyTime

Small class used to provide time with "with" statement.

---
### Usage

```python
var = Chronos()
with var:
	#Do_something
	mySuperFunction(lot,"of",arguments)
elapsed_time=var.get()

# elapsed_time is a list of two elements
#   containing all elapsed time, time.sleep()
#   included, and processing time.```
